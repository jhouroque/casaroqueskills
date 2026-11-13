#!/usr/bin/env python3
"""Análise de um item de cotação. Somente stdlib; nunca autoriza assinatura."""
from __future__ import annotations

import argparse
import copy
import json
import sys
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation, ROUND_CEILING, ROUND_HALF_UP, localcontext
from pathlib import Path

VERSAO = "1.0.0"
D = Decimal
CENTAVO = D("0.01")
FIXOS = ("embalagem", "carga", "descarga", "outros")
TRECHOS = {"direto": {"fornecedor_orgao"},
           "via_empresa": {"fornecedor_empresa", "empresa_orgao"}}


def texto(valor):
    return isinstance(valor, str) and bool(valor.strip())


def numero_texto(valor):
    return format(valor, "f") if isinstance(valor, D) else valor


def moeda(valor):
    return format(valor.quantize(CENTAVO, rounding=ROUND_HALF_UP), ".2f")


class Conferencia:
    def __init__(self):
        self.erros, self.pendencias, self.estimativas = [], [], []

    def erro(self, campo, motivo):
        self.erros.append({"campo": campo, "motivo": motivo})

    def pendente(self, campo, motivo):
        self.pendencias.append({"campo": campo, "motivo": motivo})

    def numero(self, valor, campo, positivo=False, inteiro=False):
        if valor is None:
            self.pendente(campo, "Valor obrigatório desconhecido; não substituído por zero.")
            return None
        if isinstance(valor, bool) or not isinstance(valor, (str, int, float, D)):
            self.erro(campo, "Esperado número decimal, sem booleanos ou estruturas.")
            return None
        try:
            n = D(str(valor))
        except (InvalidOperation, ValueError):
            self.erro(campo, "Número inválido.")
            return None
        if not n.is_finite():
            self.erro(campo, "O número deve ser finito.")
            return None
        if n < 0 or (positivo and n == 0):
            self.erro(campo, "Exigido valor positivo." if positivo else "Não pode ser negativo.")
            return None
        if inteiro and n != n.to_integral_value():
            self.erro(campo, "Exigida quantidade inteira de embalagens.")
            return None
        # Evita estouro/consumo excessivo com expoentes ou números impraticáveis.
        if abs(n.adjusted()) > 100 or len(n.as_tuple().digits) > 100:
            self.erro(campo, "Precisão fora do limite de análise: 100 dígitos/expoente.")
            return None
        return D(0) if n == 0 else n

    def valor(self, dado, campo, percentual=False):
        if dado is None:
            self.pendente(campo, "Informar valor, natureza e justificativa; desconhecido não é zero.")
            return None
        if not isinstance(dado, dict):
            self.erro(campo, "Esperado objeto com valor, natureza e justificativa.")
            return None
        n = self.numero(dado.get("valor"), campo + ".valor")
        natureza = dado.get("natureza")
        if natureza is None:
            self.pendente(campo + ".natureza", "Indicar confirmado ou estimado.")
        elif natureza not in ("confirmado", "estimado"):
            self.erro(campo + ".natureza", "Use confirmado ou estimado.")
        elif natureza == "estimado":
            self.estimativas.append(campo)
        if not texto(dado.get("justificativa")):
            self.pendente(campo + ".justificativa", "Informar origem/evidência; zero também exige justificativa.")
        if percentual and n is not None and n >= 1:
            self.erro(campo + ".valor", "Percentual deve ser fração menor que 1, por exemplo 0.04.")
        return n


def logistica(dados, c, prefixo):
    modo = dados.get("modo_logistico")
    if modo is None:
        c.pendente(prefixo + "modo_logistico", "Indicar direto ou via_empresa.")
    elif not isinstance(modo, str) or modo not in TRECHOS:
        c.erro(prefixo + "modo_logistico", "Use direto ou via_empresa.")
    rotas = dados.get("fretes")
    if rotas is None:
        c.pendente(prefixo + "fretes", "Informar rotas, inclusive gratuidades comprovadas.")
        return None
    if not isinstance(rotas, list):
        c.erro(prefixo + "fretes", "Esperada lista de rotas.")
        return None
    ids, trechos, pares, valores = set(), set(), set(), []
    for i, r in enumerate(rotas):
        campo = f"{prefixo}fretes[{i}]"
        if not isinstance(r, dict):
            c.erro(campo, "Esperado objeto de rota.")
            continue
        ident, trecho = r.get("id"), r.get("trecho")
        if not texto(ident):
            c.pendente(campo + ".id", "Identificar a rota.")
        elif ident in ids:
            c.erro(campo + ".id", "Rota duplicada.")
        else:
            ids.add(ident)
        if not texto(trecho):
            c.pendente(campo + ".trecho", "Identificar o trecho logístico.")
        elif trecho in trechos:
            c.erro(campo + ".trecho", "Trecho duplicado: agregar subtaxas/coleta em uma rota justificada.")
        else:
            trechos.add(trecho)
        for k in ("origem", "destino"):
            if not texto(r.get(k)):
                c.pendente(campo + "." + k, "Identificar local/parte responsável; não inventar endereço.")
        if texto(r.get("origem")) and texto(r.get("destino")):
            par = (r["origem"].strip().casefold(), r["destino"].strip().casefold())
            if par in pares:
                c.erro(campo, "Par origem/destino duplicado.")
            pares.add(par)
        n = c.valor(r, campo)
        valores.append(n)
    if isinstance(modo, str) and modo in TRECHOS:
        esperados = TRECHOS[modo]
        for falta in sorted(esperados - trechos):
            c.pendente(prefixo + "fretes", "Falta trecho obrigatório: " + falta)
        if trechos - esperados:
            c.erro(prefixo + "fretes", "Trecho incompatível com a rota escolhida. Não somar frete direto e via empresa.")
        # Conferência de continuidade dos locais declarados, sem geocodificação.
        mapa = {r["trecho"]: r for r in rotas
                if isinstance(r, dict) and texto(r.get("trecho"))}
        if modo == "via_empresa" and esperados <= trechos:
            a, b = mapa["fornecedor_empresa"], mapa["empresa_orgao"]
            if texto(a.get("destino")) and texto(b.get("origem")):
                if a["destino"].strip().casefold() != b["origem"].strip().casefold():
                    c.erro(prefixo + "fretes", "Destino da entrada difere da origem da saída; conciliar a rota.")
    if not rotas or any(n is None for n in valores):
        return None
    return sum((n.quantize(CENTAVO, rounding=ROUND_HALF_UP) for n in valores), D(0))


def fixos(dados, c, prefixo):
    itens = dados.get("custos_fixos")
    if itens is None:
        c.pendente(prefixo + "custos_fixos", "Informar embalagem, carga, descarga e outros, inclusive zeros justificados.")
        return None
    if not isinstance(itens, dict):
        c.erro(prefixo + "custos_fixos", "Esperado objeto com custos nomeados.")
        return None
    valores = []
    for chave in sorted(set(FIXOS) | set(itens)):
        n = c.valor(itens.get(chave), prefixo + "custos_fixos." + chave)
        valores.append(n)
    if any(n is None for n in valores):
        return None
    return sum((n.quantize(CENTAVO, rounding=ROUND_HALF_UP) for n in valores), D(0))


def compra(qtd, conteudo, preco, moq, multiplo):
    if any(v is None for v in (qtd, conteudo, preco, moq, multiplo)):
        return None
    embalagens = (max(qtd / conteudo, moq) / multiplo).to_integral_value(rounding=ROUND_CEILING) * multiplo
    quantidade = embalagens * conteudo
    desembolso = (embalagens * preco).quantize(CENTAVO, rounding=ROUND_HALF_UP)
    consumido = desembolso * qtd / quantidade
    return {"embalagens": embalagens, "quantidade_comprada": quantidade,
            "quantidade_entrega": qtd, "sobra": quantidade - qtd,
            "desembolso_produtos": desembolso, "consumido_exato": consumido}


def compra_publica(x):
    if x is None:
        return None
    entregue_arredondado = x["consumido_exato"].quantize(CENTAVO, rounding=ROUND_HALF_UP)
    return {"embalagens_comprar": int(x["embalagens"]),
            "quantidade_comprada": numero_texto(x["quantidade_comprada"]),
            "quantidade_entrega": numero_texto(x["quantidade_entrega"]),
            "sobra_fisica": numero_texto(x["sobra"]),
            "desembolso_produtos": moeda(x["desembolso_produtos"]),
            "custo_produto_consumido": moeda(entregue_arredondado),
            "custo_produto_consumido_nao_arredondado": numero_texto(x["consumido_exato"]),
            "estoque_excedente_custo": moeda(x["desembolso_produtos"] - entregue_arredondado)}


def precificar(x, fretes, outros, taxa, margem):
    consumido = x["consumido_exato"] + fretes + outros
    caixa = x["desembolso_produtos"] + fretes + outros
    resultado = {"fretes": moeda(fretes), "custos_fixos": moeda(outros),
                 "custo_direto_consumido": moeda(consumido), "desembolso_integral": moeda(caixa),
                 "encargos_sobre_venda": numero_texto(taxa), "margem_alvo": numero_texto(margem),
                 "cenarios": {}}
    for nome, base in (("consumo", consumido), ("recuperacao_integral_desembolso", caixa)):
        receita_minima = base / (1 - taxa - margem)
        unitario = (receita_minima / x["quantidade_entrega"]).quantize(CENTAVO, rounding=ROUND_CEILING)
        receita = (unitario * x["quantidade_entrega"]).quantize(CENTAVO, rounding=ROUND_HALF_UP)
        ajuste = receita < receita_minima
        if ajuste:  # Quantidades fracionadas podem perder centavos no total da linha.
            piso_total = receita_minima.quantize(CENTAVO, rounding=ROUND_CEILING)
            unitario = (piso_total / x["quantidade_entrega"]).quantize(CENTAVO, rounding=ROUND_CEILING)
            receita = (unitario * x["quantidade_entrega"]).quantize(CENTAVO, rounding=ROUND_HALF_UP)
        encargos = receita * taxa
        contribuicao = receita - encargos - consumido
        caixa_apos_venda = receita - encargos - caixa
        resultado["cenarios"][nome] = {
            "preco_unitario_analise": moeda(unitario), "receita": moeda(receita),
            "base_do_criterio": moeda(base), "encargos_estimados_pela_aliquota_informada": moeda(encargos),
            "contribuicao_apos_custo_consumido": moeda(contribuicao),
            "margem_contribuicao_sobre_consumido": numero_texto(contribuicao / receita) if receita else None,
            "margem_pelo_criterio_de_preco": numero_texto((receita - encargos - base) / receita) if receita else None,
            "resultado_caixa_apos_venda": moeda(caixa_apos_venda),
            "ajuste_por_arredondamento_total": ajuste,
            "nota": ("A sobra permanece em estoque; o caixa pode ser negativo apesar da margem de contribuição."
                     if nome == "consumo" else "Recupera todo o desembolso na venda. O excedente continua estoque; recuperação de caixa não é custo consumido nem lucro líquido.")}
    return resultado


def avaliar(entrada):
    c = Conferencia()
    saida = {"ferramenta": "avaliar_custo", "versao": VERSAO,
             "aprovado_para_assinatura": False, "preco_final_liberado": False,
             "principal": None, "parcial": {"status": "NAO_AVALIADA"},
             "erros": c.erros, "pendencias": c.pendencias, "estimativas": c.estimativas,
             "avisos": ["Análise aritmética: não calcula enquadramento tributário, não verifica estoque, prazo ou equivalência técnica e nunca autoriza assinatura.",
                        "Percentuais são frações da receita. Excedente físico e caixa são separados de margem de contribuição; nenhum resultado é lucro líquido.",
                        "Fretes e fixos são custos totais deste item no contexto informado. Não há rateio automático nem confirmação independente da evidência declarada."]}
    if not isinstance(entrada, dict):
        c.erro("entrada", "Esperado objeto JSON.")
        saida["status"] = "INVALIDO"
        return saida
    try:
        with localcontext() as ctx:
            ctx.prec = 160
            qtd = c.numero(entrada.get("quantidade_entrega"), "quantidade_entrega", positivo=True)
            if not texto(entrada.get("unidade_entrega")):
                c.pendente("unidade_entrega", "Definir unidade; conteúdo da embalagem deve usar a mesma unidade.")
            conteudo = c.numero(entrada.get("conteudo_embalagem"), "conteudo_embalagem", positivo=True)
            preco = c.valor(entrada.get("preco_embalagem"), "preco_embalagem")
            moq = c.numero(entrada.get("moq_embalagens"), "moq_embalagens", positivo=True, inteiro=True)
            multiplo = c.numero(entrada.get("multiplo_embalagens"), "multiplo_embalagens", positivo=True, inteiro=True)
            if entrada.get("multiplo_confirmado") is not True:
                c.pendente("multiplo_confirmado", "Exigida confirmação explícita do múltiplo; não inferir da caixa master ou quantidade pré-preenchida.")
            taxa = c.valor(entrada.get("aliquota_efetiva"), "aliquota_efetiva", percentual=True)
            adicionais = entrada.get("taxas_percentuais")
            taxas = []
            if adicionais is None:
                c.pendente("taxas_percentuais", "Informar lista, inclusive lista vazia justificada.")
            elif not isinstance(adicionais, list):
                c.erro("taxas_percentuais", "Esperada lista.")
            else:
                nomes = set()
                if not adicionais and not texto(entrada.get("justificativa_sem_taxas")):
                    c.pendente("justificativa_sem_taxas", "Explicar ausência de taxas percentuais adicionais.")
                for i, item in enumerate(adicionais):
                    campo = f"taxas_percentuais[{i}]"
                    if not isinstance(item, dict):
                        c.erro(campo, "Esperado objeto com nome, valor, natureza e justificativa.")
                        continue
                    nome = item.get("nome")
                    if not texto(nome):
                        c.pendente(campo + ".nome", "Nomear a taxa.")
                    elif nome.strip().casefold() in nomes:
                        c.erro(campo + ".nome", "Taxa repetida; verificar dupla contagem.")
                    else:
                        nomes.add(nome.strip().casefold())
                    taxas.append(c.valor(item, campo, percentual=True))
            total_taxas = None if taxa is None or any(t is None for t in taxas) else taxa + sum(taxas, D(0))
            margem = c.numero(entrada.get("margem_alvo"), "margem_alvo")
            if margem is not None and margem >= 1:
                c.erro("margem_alvo", "Margem deve ser fração menor que 1.")
            if total_taxas is not None and margem is not None and total_taxas + margem >= 1:
                c.erro("aliquota_efetiva + taxas_percentuais + margem_alvo", "A soma deve ser menor que 1.")
            frete, outros = logistica(entrada, c, ""), fixos(entrada, c, "")
            x = compra(qtd, conteudo, preco, moq, multiplo)
            unidade = entrada.get("unidade_entrega")
            saida["principal"] = {"unidade": unidade if texto(unidade) else None,
                                  "compra": compra_publica(x), "precos": None}
            parcial_flag = entrada.get("avaliar_parcial")
            parcial_x = parcial_frete = parcial_outros = None
            if not isinstance(parcial_flag, bool):
                c.pendente("avaliar_parcial", "Informar true ou false; não presumir viabilidade de adjudicação parcial.")
            elif parcial_flag:
                parcial = entrada.get("parcial")
                saida["parcial"] = {"status": "PENDENTE", "compra": None, "precos": None}
                if not isinstance(parcial, dict):
                    c.pendente("parcial", "Informar quantidade, logística e custos fixos exclusivos da adjudicação parcial.")
                else:
                    pq = c.numero(parcial.get("quantidade_entrega"), "parcial.quantidade_entrega", positivo=True)
                    if pq is not None and qtd is not None and pq > qtd:
                        c.erro("parcial.quantidade_entrega", "Quantidade parcial não pode exceder a principal.")
                    if parcial.get("custos_exclusivos_confirmados") is not True:
                        c.pendente("parcial.custos_exclusivos_confirmados", "Confirmar que os valores exclusivos não dependem de vencer outros itens.")
                    if parcial.get("condicoes_compra_mantidas") is not True:
                        c.pendente("parcial.condicoes_compra_mantidas", "Confirmar preço, embalagem, MOQ, múltiplo e encargos aplicáveis na parcial; se mudarem, executar nova análise com as condições atualizadas.")
                    parcial_frete = logistica(parcial, c, "parcial.")
                    parcial_outros = fixos(parcial, c, "parcial.")
                    parcial_x = compra(pq, conteudo, preco, moq, multiplo)
                    saida["parcial"]["compra"] = compra_publica(parcial_x)
            if not c.erros and not c.pendencias:
                saida["principal"]["precos"] = precificar(x, frete, outros, total_taxas, margem)
                if parcial_flag:
                    saida["parcial"]["precos"] = precificar(parcial_x, parcial_frete, parcial_outros, total_taxas, margem)
                    saida["parcial"]["status"] = "SIMULACAO" if c.estimativas else "CALCULO_COMPLETO"
    except (InvalidOperation, OverflowError, ZeroDivisionError) as exc:
        c.erro("calculo", "Operação decimal fora dos limites de análise: " + type(exc).__name__)
        if saida["principal"]:
            saida["principal"]["precos"] = None
        if "precos" in saida["parcial"]:
            saida["parcial"]["precos"] = None
    saida["status"] = "INVALIDO" if c.erros else "PENDENTE" if c.pendencias else "SIMULACAO" if c.estimativas else "CALCULO_COMPLETO"
    return saida


def caso_base():
    def valor(n, justificativa="Dado sintético de teste; não é cotação real."):
        return {"valor": n, "natureza": "confirmado", "justificativa": justificativa}
    return {"quantidade_entrega": "1", "unidade_entrega": "unidade", "conteudo_embalagem": "1",
            "preco_embalagem": valor("100"), "moq_embalagens": 1, "multiplo_embalagens": 1,
            "multiplo_confirmado": True, "modo_logistico": "direto",
            "fretes": [dict(valor("0", "Gratuidade documentada somente neste teste sintético."),
                            id="direto", trecho="fornecedor_orgao", origem="Fornecedor", destino="Órgão")],
            "custos_fixos": {k: valor("0", "Não aplicável neste teste sintético.") for k in FIXOS},
            "aliquota_efetiva": valor("0"), "taxas_percentuais": [],
            "justificativa_sem_taxas": "Ausência de taxas neste teste sintético.",
            "margem_alvo": "0.30", "avaliar_parcial": False}


def self_tests():
    resultados = []
    def teste(nome, editar, verificar):
        dado = caso_base()
        editar(dado)
        resposta = avaliar(dado)
        try:
            verificar(resposta)
            resultados.append({"teste": nome, "passou": True})
        except (AssertionError, KeyError, TypeError) as exc:
            resultados.append({"teste": nome, "passou": False, "falha": str(exc), "resposta": resposta})
    def exigir(condicao, mensagem="Resultado diferente do esperado."):
        if not condicao:
            raise AssertionError(mensagem)
    def preco(r):
        return r["principal"]["precos"]["cenarios"]["consumo"]["preco_unitario_analise"]
    teste("100_com_margem30_resulta142_86", lambda d: None, lambda r: exigir(preco(r) == "142.86"))
    teste("frete_null_bloqueia", lambda d: d["fretes"][0].update(valor=None),
          lambda r: exigir(r["status"] == "PENDENTE" and r["principal"]["precos"] is None))
    teste("zero_sem_justificativa_bloqueia", lambda d: d["custos_fixos"]["carga"].update(justificativa=""),
          lambda r: exigir(r["status"] == "PENDENTE"))
    def moq(d):
        d.update(quantidade_entrega="5", conteudo_embalagem="2", moq_embalagens=18)
        d["preco_embalagem"]["valor"] = "0.69"
    teste("moq18_packs2_demanda5_sobra31", moq,
          lambda r: exigir(r["principal"]["compra"]["embalagens_comprar"] == 18 and r["principal"]["compra"]["sobra_fisica"] == "31" and r["principal"]["compra"]["desembolso_produtos"] == "12.42"))
    teste("margem_consumo_nao_garante_caixa", moq,
          lambda r: exigir(D(r["principal"]["precos"]["cenarios"]["consumo"]["resultado_caixa_apos_venda"]) < 0 and D(r["principal"]["precos"]["cenarios"]["recuperacao_integral_desembolso"]["resultado_caixa_apos_venda"]) > 0))
    teste("estoque_arredondado_concilia_desembolso", moq,
          lambda r: exigir(D(r["principal"]["compra"]["custo_produto_consumido"]) + D(r["principal"]["compra"]["estoque_excedente_custo"]) == D("12.42")))
    teste("margem30_apos_tributos10", lambda d: d["aliquota_efetiva"].update(valor="0.10"),
          lambda r: exigir(preco(r) == "166.67" and D(r["principal"]["precos"]["cenarios"]["consumo"]["margem_contribuicao_sobre_consumido"]) >= D("0.30")))
    teste("taxa_adicional_entra_denominador", lambda d: d.update(taxas_percentuais=[dict(d["aliquota_efetiva"], nome="comissão", valor="0.05")]),
          lambda r: exigir(preco(r) == "153.85"))
    teste("arredondar_compra_para_multiplo", lambda d: d.update(quantidade_entrega="10", conteudo_embalagem="3", moq_embalagens=2, multiplo_embalagens=3),
          lambda r: exigir(r["principal"]["compra"]["embalagens_comprar"] == 6 and r["principal"]["compra"]["sobra_fisica"] == "8"))
    teste("multiplo_nao_confirmado_bloqueia", lambda d: d.update(multiplo_confirmado=False), lambda r: exigir(r["status"] == "PENDENTE"))
    teste("estimativa_somente_simulacao", lambda d: d["preco_embalagem"].update(natureza="estimado"),
          lambda r: exigir(r["status"] == "SIMULACAO" and not r["aprovado_para_assinatura"] and not r["preco_final_liberado"]))
    teste("soma_taxa_margem_invalida", lambda d: d["aliquota_efetiva"].update(valor="0.70"), lambda r: exigir(r["status"] == "INVALIDO"))
    teste("quantidade_zero_invalida", lambda d: d.update(quantidade_entrega="0"), lambda r: exigir(r["status"] == "INVALIDO"))
    teste("preco_negativo_invalido", lambda d: d["preco_embalagem"].update(valor="-1"), lambda r: exigir(r["status"] == "INVALIDO"))
    teste("nao_finito_invalido", lambda d: d["preco_embalagem"].update(valor="Infinity"), lambda r: exigir(r["status"] == "INVALIDO"))
    teste("moq_fracionario_invalido", lambda d: d.update(moq_embalagens="1.5"), lambda r: exigir(r["status"] == "INVALIDO"))
    teste("frete_duplicado_rejeitado", lambda d: d["fretes"].append(copy.deepcopy(d["fretes"][0])), lambda r: exigir(r["status"] == "INVALIDO"))
    teste("direto_e_via_empresa_nao_somados", lambda d: d["fretes"].append(dict(d["fretes"][0], id="entrada", trecho="fornecedor_empresa", destino="Empresa")), lambda r: exigir(r["status"] == "INVALIDO"))
    teste("parcial_sem_custos_exclusivos_bloqueia", lambda d: d.update(avaliar_parcial=True),
          lambda r: exigir(r["status"] == "PENDENTE" and r["principal"]["precos"] is None))
    def parcial(d):
        d["fretes"][0]["valor"] = "5"
        a = dict(d["fretes"][0], id="entrada_exclusiva", trecho="fornecedor_empresa", destino="Empresa", valor="30")
        b = dict(d["fretes"][0], id="saida_exclusiva", trecho="empresa_orgao", origem="Empresa", valor="30")
        d.update(avaliar_parcial=True, parcial={"quantidade_entrega": "1", "custos_exclusivos_confirmados": True,
                 "condicoes_compra_mantidas": True,
                 "modo_logistico": "via_empresa", "fretes": [a, b], "custos_fixos": copy.deepcopy(d["custos_fixos"])})
    teste("parcial_recalcula_frete_exclusivo", parcial,
          lambda r: exigir(preco(r) == "150.00" and r["parcial"]["precos"]["cenarios"]["consumo"]["preco_unitario_analise"] == "228.58"))
    def parcial_sem_desconto(d):
        parcial(d)
        d["parcial"]["condicoes_compra_mantidas"] = False
    teste("parcial_nao_presume_desconto_do_lote", parcial_sem_desconto,
          lambda r: exigir(r["status"] == "PENDENTE" and r["parcial"]["precos"] is None))
    def fracionado(d):
        d.update(quantidade_entrega="0.03", conteudo_embalagem="0.03")
        d["preco_embalagem"]["valor"] = "0.01"
    teste("quantidade_fracionada_total_preserva_margem", fracionado,
          lambda r: exigir(D(r["principal"]["precos"]["cenarios"]["consumo"]["margem_contribuicao_sobre_consumido"]) >= D("0.30")))
    teste("completo_tambem_nao_autoriza_assinatura", lambda d: None,
          lambda r: exigir(r["status"] == "CALCULO_COMPLETO" and not r["aprovado_para_assinatura"]))
    teste("modo_logistico_malformado_nao_crasha", lambda d: d.update(modo_logistico=[]),
          lambda r: exigir(r["status"] == "INVALIDO"))
    teste("trecho_malformado_nao_crasha", lambda d: d["fretes"][0].update(trecho=[]),
          lambda r: exigir(r["status"] == "PENDENTE" and r["principal"]["precos"] is None))
    teste("zero_expoente_extremo_rejeitado", lambda d: d.update(margem_alvo="0e-10000"),
          lambda r: exigir(r["status"] == "INVALIDO"))
    teste("zero_normalizado", lambda d: d["aliquota_efetiva"].update(valor="0e-50"),
          lambda r: exigir(r["principal"]["precos"]["encargos_sobre_venda"] == "0"))
    teste("unidade_numerica_nao_quebra_json", lambda d: d.update(unidade_entrega=D(20)),
          lambda r: exigir(r["status"] == "PENDENTE" and r["principal"]["unidade"] is None and bool(json.dumps(r))))
    return {"ferramenta": "avaliar_custo", "versao": VERSAO,
            "executado_utc": datetime.now(timezone.utc).isoformat(),
            "dados": "Todos os casos são sintéticos; não são cotações reais.",
            "total": len(resultados), "passaram": sum(t["passou"] for t in resultados),
            "sucesso": all(t["passou"] for t in resultados), "testes": resultados}


def pares_sem_duplicatas(pares):
    resultado = {}
    for k, v in pares:
        if k in resultado:
            raise ValueError("Chave JSON duplicada: " + k)
        resultado[k] = v
    return resultado


def carregar(texto_json):
    def rejeitar(constante):
        raise ValueError("Constante JSON não finita: " + constante)
    return json.loads(texto_json, parse_float=D, parse_int=D,
                      parse_constant=rejeitar, object_pairs_hook=pares_sem_duplicatas)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("entrada", nargs="?", default="-", help="Arquivo JSON; '-' lê stdin.")
    parser.add_argument("--saida", help="Gravar resultado JSON neste arquivo; padrão stdout.")
    parser.add_argument("--self-test", action="store_true", help="Executar testes internos sintéticos.")
    args = parser.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    try:
        resultado = self_tests() if args.self_test else avaliar(carregar(
            sys.stdin.read() if args.entrada == "-" else Path(args.entrada).read_text(encoding="utf-8-sig")))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        resultado = {"status": "INVALIDO", "aprovado_para_assinatura": False,
                     "preco_final_liberado": False, "erros": [{"campo": "arquivo", "motivo": str(exc)}]}
    conteudo = json.dumps(resultado, ensure_ascii=False, indent=2) + "\n"
    if args.saida:
        Path(args.saida).write_text(conteudo, encoding="utf-8")
    else:
        sys.stdout.write(conteudo)
    return 0 if resultado.get("sucesso") or resultado.get("status") in ("CALCULO_COMPLETO", "SIMULACAO") else 2


if __name__ == "__main__":
    raise SystemExit(main())
