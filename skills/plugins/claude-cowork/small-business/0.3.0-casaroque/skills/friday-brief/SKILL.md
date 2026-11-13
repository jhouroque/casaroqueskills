---
name: friday-brief
description: Delivers the Friday end-of-week pulse — revenue vs prior week, top sellers, wins and watches. Accepts optional lookback window of 7 or 14 days.
allowed-tools: Read, WebFetch, Bash
---

Run the Friday wins-and-watches briefing. Pull the numbers, surface what matters, and give the owner a clean end-of-week picture.

Parse arguments:
- `--lookback` (default: `7d`) — `7d` for one week or `14d` for a two-week rolling comparison

## Step 1 — Revenue pulse

Using the `business-pulse` skill workflow:

1. Pull PayPal transactions for the lookback period.
2. Pull any HubSpot deal closes for the same window.
3. Calculate week-over-week revenue delta.
4. Surface top 3 revenue sources (product / customer / channel) ranked by contribution.

## Step 2 — Sales breakdown

1. List the top 5 selling products/services by volume and revenue.
2. List the bottom 3 (anything that moved less than expected vs. prior period).
3. Flag any items with a sudden spike or drop (>20% change).

## Step 3 — Wins and watches summary

Format the output as:

```
Friday Brief — {date}

WINS
• {win 1}
• {win 2}
• {win 3}

WATCHES
• {watch 1} — {recommended action}
• {watch 2} — {recommended action}

Revenue this week: ${amount} ({+/-}X% vs last week)
```

## Connector failures

Run with whatever is connected — this command degrades gracefully. If PayPal is missing, skip transaction data and note "PayPal not connected — revenue data from HubSpot deals only." If HubSpot is missing, skip deal closes and note it. If neither is connected, stop and tell the owner: "No revenue sources connected. Connect PayPal or HubSpot to run the Friday brief."

## Approval gates

- **Never send or post this brief automatically.** Always display it for the owner to review first.
- **Never auto-cancel or modify anything.** Surface the data and recommendations only.

## Output

End with the formatted brief and ask the owner: "Want me to post this to Slack, email it to yourself, or save it?"

---

## 🇧🇷 Casa Roque — customização (ler antes de executar)

Plugin customizado para a **Casa Roque** (e-commerce de enxoval/bebê + Roque Gestão & Engenharia/SST, Limeira/SP). Premissas obrigatórias:

- **Moeda BRL (R$)**, vírgula decimal, datas dd/mm/aaaa, fuso America/Sao_Paulo. **NÃO usar premissas dos EUA** (QuickBooks/PayPal/1099/IRS/sales tax).
- **Impostos:** Simples Nacional 10% sobre faturamento (DAS via Contabilizei).
- **Marketplaces:** comissão 16% (Mercado Livre e Shopee); site NuvemShop 0%. Pagamentos: NuvemPago (3x), Pix, boleto.
- **Precificação:** markup padrão **2,70x** sobre custo total; meta margem líquida >30%.
- **Dados:** Bling/NuvemShop/ML/Shopee **não têm MCP** → usar export CSV do Bling ou números informados pelo JhEY. Conectados: Google (Gmail/Agenda/Drive) e Canva.
- **Idioma:** responder sempre em **pt-BR**; aceitar gatilhos em pt-BR além do inglês.
- **OFF-LIMITS sem ok explícito:** Bling, ML admin, Shopee admin, TikTok Shop. Compras > R$500 exigem aprovação do JhEY.

> Contexto completo: `CASA_ROQUE_CONTEXT.md` (raiz do plugin) e bloco `## Business context` da memória.
