#!/usr/bin/env python3
"""Custo líquido de uma viagem aos EUA, comparado a comprar os aparelhos no Brasil.

Padrões: casal (2 pessoas), 8 dias / 7 noites em Newark, compra de 2 iPhone Pro.
Busca o dólar comercial do dia; use --usd para fixar uma cotação.

    python custo_viagem.py --passagem 2900
    python custo_viagem.py --passagem 2900 --usd 5.42 --noites 6
"""

import argparse
import json
import sys
import urllib.request

COTACAO_URL = "https://economia.awesomeapi.com.br/last/USD-BRL"
NJ_SALES_TAX = 0.06625
IOF = 0.011
COTA_ISENCAO_USD = 1000.0   # por pessoa, entrada aerea no Brasil
ALIQUOTA_EXCEDENTE = 0.50   # sobre o que passa da cota

CENARIOS = [
    ("2x 17 Pro recondicionado", 780.0),
    ("2x 17 Pro novo em liquidacao", 899.0),
    ("2x 18 Pro novo", 1299.0),
]


def dolar_do_dia(fixo=None):
    if fixo:
        return fixo, "fixado pelo usuario"
    try:
        with urllib.request.urlopen(COTACAO_URL, timeout=10) as r:
            d = json.load(r)["USDBRL"]
        return float(d["bid"]), f"AwesomeAPI, {d['create_date']}"
    except Exception as e:
        print(f"AVISO: nao consegui buscar a cotacao ({e}). Passe --usd.", file=sys.stderr)
        sys.exit(1)


def imposto_importacao(preco_unit, pessoas, aparelhos):
    """Imposto de 50% sobre o que exceder a cota de US$ 1.000 por pessoa."""
    total = preco_unit * aparelhos
    cota = COTA_ISENCAO_USD * pessoas
    excedente = max(0.0, total - cota)
    return excedente * ALIQUOTA_EXCEDENTE


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--passagem", type=float, required=True,
                   help="R$ por pessoa, ida e volta")
    p.add_argument("--usd", type=float, help="cotacao BRL/USD (default: do dia)")
    p.add_argument("--pessoas", type=int, default=2)
    p.add_argument("--noites", type=int, default=7)
    p.add_argument("--dias", type=int, default=8)
    p.add_argument("--bagagem", type=float, default=0.0,
                   help="R$ por pessoa, ida e volta, se cobrada a parte")
    p.add_argument("--hotel-noite", type=float, default=90.0, help="US$/noite, total")
    p.add_argument("--comida-dia", type=float, default=55.0, help="US$/dia/pessoa")
    p.add_argument("--transporte", type=float, default=180.0, help="US$ total")
    p.add_argument("--passeios", type=float, default=150.0, help="US$ total")
    p.add_argument("--seguro", type=float, default=500.0, help="R$ total")
    p.add_argument("--apple-brasil", type=float, default=27200.0,
                   help="R$ por 2x iPhone 18 Pro na Apple Brasil")
    a = p.parse_args()

    usd, fonte = dolar_do_dia(a.usd)
    aparelhos = a.pessoas

    # Custos em reais, fixos entre cenarios
    passagens = a.passagem * a.pessoas
    bagagem = a.bagagem * a.pessoas

    # Custos em dolar, fixos entre cenarios (sofrem IOF)
    hotel = a.hotel_noite * a.noites
    comida = a.comida_dia * a.dias * a.pessoas
    base_usd = hotel + comida + a.transporte + a.passeios

    print(f"Dolar comercial: R$ {usd:.4f}  ({fonte})")
    print(f"Passagem: R$ {a.passagem:,.0f}/pessoa x {a.pessoas} = R$ {passagens:,.0f}")
    print(f"Estadia {a.noites} noites / {a.dias} dias, {a.pessoas} pessoas\n")

    linhas = []
    for nome, preco_unit in CENARIOS:
        subtotal_aparelhos = preco_unit * aparelhos
        tax = subtotal_aparelhos * NJ_SALES_TAX
        gasto_usd = base_usd + subtotal_aparelhos + tax
        gasto_brl = gasto_usd * usd * (1 + IOF)
        imposto = imposto_importacao(preco_unit, a.pessoas, aparelhos) * usd
        total = passagens + bagagem + a.seguro + gasto_brl + imposto
        diferenca = a.apple_brasil - total
        linhas.append((nome, preco_unit, tax, imposto, total, diferenca))

    w = max(len(n) for n, *_ in linhas)
    print(f"{'Cenario':<{w}}  {'US$/un':>8}  {'NJ tax':>9}  {'Imp.imp.':>10}  "
          f"{'TOTAL R$':>11}  {'vs Apple BR':>12}")
    print("-" * (w + 60))
    for nome, unit, tax, imposto, total, dif in linhas:
        sinal = "economiza" if dif > 0 else "perde"
        print(f"{nome:<{w}}  {unit:>8,.0f}  {tax:>9,.0f}  {imposto:>10,.0f}  "
              f"{total:>11,.0f}  {sinal} {abs(dif):>7,.0f}")

    print(f"\nReferencia Apple Brasil (2x 18 Pro): R$ {a.apple_brasil:,.0f}")
    print("Nota: 'vs Apple BR' compara a VIAGEM INTEIRA contra so comprar os "
          "aparelhos no Brasil.\nQuando negativo, a diferenca e o custo real de "
          "fazer a viagem — e ela entrega\nmuito mais que dois telefones.")


if __name__ == "__main__":
    main()
