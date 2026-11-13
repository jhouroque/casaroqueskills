---
name: sales-brief
description: Surfaces top and bottom sellers, identifies seasonality patterns, and produces a 2-week content brief to push winners and clear slow movers. Accepts optional lookback window of 30, 60, or 90 days.
allowed-tools: Read, WebFetch, Bash
---

Run the sales analysis and content brief. Pull what sold (and what didn't), explain why, and produce a ready-to-use content plan that acts on the data.

Parse arguments:
- `--lookback` (default: `30d`) — `30d`, `60d`, or `90d` lookback window

## Step 1 — Sales breakdown

Using the `content-strategy` skill workflow for sales analysis:

1. Pull PayPal transactions for the lookback period grouped by item/service/SKU.
2. Pull QuickBooks revenue by product/service category.
3. Rank products by: total revenue, unit volume, and margin (if available in QB).
4. Calculate each product's share of total revenue vs. prior equivalent period.

Top sellers: products that grew share or maintained top-3 rank.
Bottom sellers: products with declining volume or below 5% of revenue.

## Step 2 — Seasonality check

1. Compare current period to same period in prior year (if QB history available).
2. Flag any items with a seasonal pattern (e.g., spikes in Q4, slow summers).
3. Note any new products with insufficient history to detect seasonality.

## Step 3 — Why analysis

For each top and bottom seller, explain the likely driver:
- Price change, promo, new channel, seasonal demand, competitor move
- Cross-reference with HubSpot campaign activity for the period
- Note where attribution is inferred vs. confirmed

## Step 4 — 2-week content brief

Produce a ready-to-use content brief:

```
2-Week Content Brief — {date range}

PUSH THESE (winners)
• {product}: {suggested angle} — {channel: email|social|both}
• {product}: {suggested angle} — {channel}

CLEAR THESE (slow movers)
• {product}: {promo angle or bundle suggestion} — {channel}

CONTENT CALENDAR
Week 1:
  Mon: {post/email concept}
  Wed: {post/email concept}
  Fri: {post/email concept}
Week 2:
  Mon: {post/email concept}
  Wed: {post/email concept}
  Fri: {post/email concept}
```

## Connector failures

If both QuickBooks and PayPal are unreachable, stop — sales analysis requires at least one revenue source. If only one is connected, run from that source and note "QuickBooks not connected — revenue data from PayPal only" (or vice versa). If HubSpot is missing, skip campaign cross-reference in the "why analysis" and note it.

## Approval gates

- **Never auto-schedule or publish content.** The brief is for owner review only.
- **Never create Canva assets automatically** — offer to generate them after owner approves the brief.

## Output

Present the sales analysis, then the content brief. Ask the owner if they'd like to generate Canva assets for any of the planned posts.

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
