<!-- C:\Users\Jhonatas\AppData\Roaming\Claude\local-agent-mode-sessions\c5e8a475-a351-48d2-8db3-3f0857ad643d\1d524d29-2570-4e4b-8d1f-844a61e14635\local_f6e23d68-ce2b-4eec-b343-aeec8fb24add\outputs\cr-plugin\small-business\skills\cash-flow-snapshot\reference\examples\worked-example.md -->
# Exemplo prático — projeção de caixa (Casa Roque)

**Cenário:** Casa Roque, operação de e-commerce (enxoval/bebê + espumas).
Sem conector — o JhEY mandou o CSV de contas a receber/pagar do Bling, o
relatório de repasses do Mercado Livre e da Shopee, e o de parcelas a receber
do NuvemPago. **Data-base: 01/07/2026** (fuso America/Sao_Paulo).

> Janelas: W1 = 01/07 → 31/07 · W2 = 01/08 → 30/08 · W3 = 31/08 → 29/09.

---

## Dados de entrada (relatórios/CSV enviados)

**Repasses a liberar — Mercado Livre / Mercado Pago (já líquidos da comissão 16% e do desconto automático da dívida ML):**

| Origem | Valor líquido | Data da venda | Liberação prevista |
|---|---|---|---|
| Vendas ML (lote A) | R$ 21.200,00 | fim de junho | 09/07 |
| Vendas ML (lote B) | R$ 19.800,00 | início de julho | 18/07 |
| Vendas ML (lote C) | R$ 20.500,00 | fim de julho | 04/08 |

**Repasses a liberar — Shopee:**

| Origem | Valor líquido | Data da venda | Liberação prevista |
|---|---|---|---|
| Vendas Shopee (lote A) | R$ 8.900,00 | fim de junho | 04/07 |
| Vendas Shopee (lote B) | R$ 9.200,00 | início de julho | 21/07 |

**Parcelas a receber — NuvemPago (site, vendas 3x):**

| Parcela | Valor | Crédito previsto |
|---|---|---|
| Julho | R$ 2.300,00 | 28/07 |
| Agosto | R$ 2.300,00 | 28/08 |
| Setembro | R$ 2.300,00 | 28/09 |

**Pix/boleto (site/atacado):**
- Pix do dia (entrada imediata): R$ 1.200,00 — 02/07.
- Boleto atacado em aberto: R$ 3.400,00 — vencimento 10/07.

**Contas a pagar e custos fixos (CSV Bling + calendário §6):**
- Fornecedor de espuma D23/D28: R$ 14.000,00 — vence 05/07.
- Fornecedor de tecidos/plumante: R$ 5.200,00 — vence 28/07.
- Folha julho: Keila R$ 840,00 (saldo, ~07/07, 5º dia útil) + Emerson R$ 1.400,00 (10/07) + Keila R$ 560,00 (adiantamento, 20/07) + VT Keila R$ 250,00 e VT Emerson R$ 250,00 (20/07) + VA Keila e Emerson (10/07) [confirmar valor do VA] + costureiras Cleusa e Vanda (10/07, por demanda) [confirmar valor].
- DAS Simples Nacional (apuração junho): R$ 7.600,00 — vence 20/07.
- FGTS 8% sobre folha CLT (Keila + Emerson): ~R$ 224,00 — depósito mensal.

> Os repasses ML já chegam **abatidos** do desconto automático da dívida do grupo
> no Mercado Livre — por isso não entram como saída separada (ver `reference/gotchas.md`).

---

## Saída do Passo 3 — prazos históricos de liberação

| Canal | Prazo médio | Desvio-padrão | Repasses no histórico |
|---|---|---|---|
| Mercado Livre | 14 dias | 5 dias | 12 |
| Shopee | 12 dias | 4 dias | 9 |
| NuvemPago (parcelas) | fixo do parcelamento (30/60/90) | ~1 dia | n/a |
| Pix | 0–1 dia | ~0 | banda fixa 5% |

---

## Saída do Passo 4 — projeção 30/60/90 dias

Cálculo da banda de confiança (ponderada por valor entre ML e Shopee):
- Desvio-padrão médio ponderado: 4,7 dias
- Prazo médio ponderado: 13,4 dias
- banda_pct = 4,7 / 13,4 = **35,1%**

**Entradas W1 (01/07–31/07):** ML 09/07 R$ 21.200 + ML 18/07 R$ 19.800 + Shopee 04/07 R$ 8.900 + Shopee 21/07 R$ 9.200 + NuvemPago 28/07 R$ 2.300 + Pix 02/07 R$ 1.200 + boleto 10/07 R$ 3.400 = **R$ 66.000,00**.

**Saídas W1 (01/07–31/07):** espuma R$ 14.000 + tecidos R$ 5.200 + Emerson R$ 1.400 + Keila saldo R$ 840 + Keila adiant. R$ 560 + VTs R$ 500 + DAS R$ 7.600 + FGTS R$ 224 = **R$ 30.324,00** (fora deste total: VA e costureiras, [confirmar]).

| Janela | Entradas previstas | Saídas previstas | Líquido | Baixo (−35,1%) | Alto (+35,1%) |
|---|---|---|---|---|---|
| 0–30 dias (W1) | R$ 66.000,00 | R$ 30.324,00 | +R$ 35.676,00 | +R$ 23.153,72 | +R$ 48.198,28 |
| 31–60 dias (W2) | R$ 22.800,00 | R$ 11.124,00 | +R$ 11.676,00 | +R$ 7.577,72 | +R$ 15.774,28 |
| 61–90 dias (W3) | R$ 20.300,00 | R$ 11.124,00 | +R$ 9.176,00 | +R$ 5.955,22 | +R$ 12.396,78 |

(W2/W3 com folha + DAS recorrentes ~R$ 11.124; entradas = repasses do período + parcela NuvemPago.)

---

## Saída do Passo 5 — riscos sinalizados

1. **Concentração de saídas entre 05 e 20/07:** espuma (R$ 14.000, 05/07), folha
   (Keila R$ 840 ~07/07; Emerson R$ 1.400 + Keila adiant. R$ 560 + VTs R$ 500) e DAS
   (R$ 7.600, 20/07) somam **R$ 24.900,00** numa mesma quinzena. As entradas grandes
   (ML 09 e 18/07, Shopee 04 e 21/07) chegam ao longo do mês, então o líquido fecha
   positivo — mas qualquer atraso de liberação aperta o dia 20. *Recomendo: confirmar
   as datas de liberação do ML/Shopee antes de 05/07.*

2. **Liberação atrasada de repasse:** o lote ML de R$ 19.800 (liberação 18/07) cai
   **dois dias antes** do dia 20 (DAS + adiantamento + VTs). Se escorregar, o dia 20
   fica sem esse reforço.

3. **Validar folha e DAS:** os valores de VA e das costureiras estão [confirmar]. Os
   números de DAS e encargos precisam ser validados com a Contabilizei antes do pagamento.

---

## Saída do Passo 6 — resumo no chat

```
Projeção de caixa — 01/07 → 29/09/2026 (fuso America/Sao_Paulo)
Fontes: CSV Bling (a receber/a pagar), repasses ML + Shopee, parcelas NuvemPago

              Esperado       Baixo          Alto
30 dias:      +R$ 35.676,00  +R$ 23.153,72  +R$ 48.198,28
60 dias:      +R$ 11.676,00  +R$  7.577,72  +R$ 15.774,28
90 dias:      +R$  9.176,00  +R$  5.955,22  +R$ 12.396,78

⚠ 3 riscos sinalizados:
  • Saídas concentradas 05–20/07 (espuma R$14k + folha + DAS R$7,6k ≈ R$24.900).
    As entradas chegam ao longo do mês, mas atraso de liberação aperta o dia 20.
  • Lote ML de R$19,8k libera 18/07 — dois dias antes do dia 20 (DAS + VTs + adiant.).
  • VA e costureiras [confirmar]; DAS e encargos: validar com a Contabilizei.

Banda de confiança: ±35,1% (variância de liberação ML + Shopee).

Esta projeção usa CSV do Bling e relatórios de repasse. Não substitui o contador —
valide folha, DAS e encargos com a Contabilizei antes de pagar/declarar.
```

**XLSX:** `projecao-caixa-2026-07-01.xlsx` — abas Resumo / Detalhe / Riscos.

Opcional (com aprovação): bloco pra colar no WhatsApp avisando que a folha de
julho está coberta, e rascunho no Gmail com a planilha anexada.
