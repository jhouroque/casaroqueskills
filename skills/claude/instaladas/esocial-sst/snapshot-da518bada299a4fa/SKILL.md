---
name: esocial-sst
description: >
  Cria eventos S-2240 (Condicoes Ambientais do Trabalho) para o eSocial a partir de dados
  do PGR/LTCAT. Use SEMPRE que o usuario mencionar: eSocial, S-2240, evento SST, condicoes
  ambientais do trabalho, agente nocivo, codigo eSocial, fator de risco eSocial, enviar SST,
  leiaute eSocial, XML eSocial, tabela 23 eSocial, lotacao tributaria, ou qualquer referencia
  ao envio de dados de seguranca do trabalho ao governo. Ative tambem quando um PGR for
  finalizado e o proximo passo for gerar os eventos S-2240.
---

# eSocial SST — Eventos S-2240

Voce gera planilhas e XMLs do evento S-2240 (Condicoes Ambientais do Trabalho) do eSocial
a partir dos dados do PGR/LTCAT.

## O que e o S-2240

Evento periodico que informa as condicoes do ambiente de trabalho de cada trabalhador:
- Agentes nocivos a que esta exposto
- Intensidade/concentracao da exposicao
- Uso de EPC e EPI
- Responsavel tecnico pela medicao

## Dados de entrada (extraidos do PGR)

Para cada funcionario:
- CPF
- Matricula / NIS
- Data inicio da condicao
- Setor/ambiente (conforme inventario por ambiente do PGR)
- Cargo
- GES (Grupo de Exposicao Similar)
- Riscos identificados no inventario

## Tabela 23 — Codigos de agentes nocivos

| Codigo | Agente nocivo | Uso comum |
|---|---|---|
| 01.18.001 | Ruido continuo ou intermitente | Medicao com decibelimetro |
| 02.01.014 | Poeiras minerais (silica, amianto) | Industria |
| 09.01.001 | Ausencia de agentes nocivos | Administrativo/escritorio |

Regras:
- Se NENHUM risco: usar 09.01.001
- Se ruido ≤ 85 dB(A): risco EXISTE mas NAO gera insalubridade → informar
- Se ruido > 85 dB(A): agente nocivo com insalubridade
- Iluminancia fora da NBR 5413: risco ergonomico, NAO gera insalubridade

## Estrutura do S-2240

```xml
<eSocial xmlns="http://www.esocial.gov.br/schema/evt/evtExpRisco/v_S_01_02_00">
  <evtExpRisco Id="ID1...">
    <ideEvento>
      <indRetif>1</indRetif>
      <tpAmb>1</tpAmb> <!-- 1=producao, 2=homologacao -->
      <procEmi>1</procEmi>
    </ideEvento>
    <ideEmpregador>
      <tpInsc>1</tpInsc>
      <nrInsc>[CNPJ 8 digitos]</nrInsc>
    </ideEmpregador>
    <ideVinculo>
      <cpfTrab>[CPF]</cpfTrab>
      <matricula>[MATRICULA]</matricula>
    </ideVinculo>
    <infoExpRisco>
      <dtIniCondicao>[AAAA-MM-DD]</dtIniCondicao>
      <infoAmb>
        <localAmb>1</localAmb> <!-- 1=proprio -->
        <dscSetor>[SETOR]</dscSetor>
        <tpInsc>1</tpInsc>
        <nrInsc>[CNPJ completo]</nrInsc>
      </infoAmb>
      <infoAtiv>
        <dscAtivDes>[DESCRICAO ATIVIDADE]</dscAtivDes>
      </infoAtiv>
      <agNoc>
        <codAgNoc>[CODIGO TAB 23]</codAgNoc>
        <dscAgNoc>[DESCRICAO]</dscAgNoc>
        <tpAval>1</tpAval> <!-- 1=qualitativa, 2=quantitativa -->
        <intConc>[VALOR SE QUANTITATIVA]</intConc>
        <limTol>[LIMITE TOLERANCIA]</limTol>
        <unMed>[UNIDADE]</unMed>
        <tecMedicao>[TECNICA USADA]</tecMedicao>
        <epcEpi>
          <utilizEPC>0</utilizEPC> <!-- 0=nao, 1=nao implementa, 2=implementa -->
          <utilizEPI>0</utilizEPI>
        </epcEpi>
      </agNoc>
      <respReg>
        <cpfResp>[CPF ENGENHEIRO]</cpfResp>
        <ideOC>1</ideOC> <!-- 1=CREA -->
        <nrOC>[CREA-SP]</nrOC>
      </respReg>
    </infoExpRisco>
  </evtExpRisco>
</eSocial>
```

## Workflow

1. Ler PGR do cliente (inventario por ambiente, quadro de setores, riscos)
2. Montar planilha com 1 linha por funcionario
3. Para cada funcionario:
   - Identificar setor e cargo
   - Buscar riscos do setor no inventario
   - Mapear riscos para codigos Tabela 23
   - Determinar EPC/EPI
4. Gerar planilha .xlsx com todos os campos
5. Opcionalmente gerar XML para importacao direta

## Formato de saida (.xlsx)

Planilha com colunas:
CPF | Matricula | Nome | Setor | Cargo | Cod.Agente | Desc.Agente | Tipo.Aval |
Intensidade | Limite | Unidade | EPC | EPI | Data.Inicio | Resp.CPF | Resp.CREA

## Responsavel tecnico (fixo)

- CPF: 397.684.448-94
- Orgao de classe: CREA (codigo 1)
- Numero: 5071626112
