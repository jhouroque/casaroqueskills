<!-- C:\Users\Jhonatas\AppData\Roaming\Claude\local-agent-mode-sessions\c5e8a475-a351-48d2-8db3-3f0857ad643d\1d524d29-2570-4e4b-8d1f-844a61e14635\local_f6e23d68-ce2b-4eec-b343-aeec8fb24add\outputs\cr-plugin\small-business\skills\sales-brief\SKILL.md -->
---
name: sales-brief
description: Mostra os mais e menos vendidos da Casa Roque, identifica padrões de sazonalidade e entrega um briefing de conteúdo de 2 semanas pra empurrar os campeões e girar os parados. Dados dos relatórios/CSV do Bling, Mercado Livre, Shopee e site (NuvemShop). Aceita janela opcional de 30, 60 ou 90 dias.
allowed-tools: Read, WebFetch, Bash
---

Rode a análise de vendas e o briefing de conteúdo. Mostre o que vendeu (e o que não), explique o porquê, e entregue um plano de conteúdo de 2 semanas pronto pra usar — em cima do dado.

Argumentos:
- `--janela` (padrão: `30d`) — `30d`, `60d` ou `90d`

## Passo 1 — Quebra de vendas

Usando o fluxo de análise da skill `content-strategy`:

1. Leia as vendas da janela agrupadas por produto/SKU. A Casa Roque **não tem conector** — a fonte é relatório/CSV exportado. Peça o que faltar: "me manda o relatório de vendas por produto do Bling (consolidado) ou, separado, do ML, da Shopee e do site (NuvemShop), CSV."
2. Some por produto (não por anúncio — o mesmo trocador tem vários anúncios no ML/Shopee). Marque o canal de cada linha.
3. Ranqueie por: faturamento total, volume de unidades, e margem quando der pra estimar (lembrar markup 2,70x e comissão 16% no marketplace; site tem margem cheia).
4. Calcule a participação de cada produto no faturamento vs. o período anterior equivalente.

Mais vendidos: produtos que ganharam participação ou se mantiveram no top-3.
Menos vendidos: produtos com volume em queda ou abaixo de 5% do faturamento.

## Passo 2 — Checagem de sazonalidade

1. Compare o período atual com o mesmo período do ano anterior (se houver histórico).
2. Sinalize itens com padrão sazonal da Casa Roque: pico no **Dia das Mães** (maio), Black Friday (novembro), Natal (dezembro), Dia das Crianças (outubro), volta às aulas (jan–fev e jul).
3. Anote produtos novos sem histórico suficiente pra detectar sazonalidade.

## Passo 3 — Análise do porquê

Pra cada mais e menos vendido, explique o provável motivo:
- Mudança de preço, oferta, canal novo, demanda sazonal, movimento de concorrente, ruptura de estoque (item zerou — POP 2, alerta < 5 un).
- Cruze com a atividade de mídia do período (Google Ads PMax na conta 568-607-6835; relatório de tráfego que o Thomas manda toda sexta) e o que foi postado no Instagram/site.
- Diga onde a atribuição é inferida vs. confirmada.

## Passo 4 — Briefing de conteúdo de 2 semanas

Produza um briefing pronto pra usar:

```
Briefing de conteúdo — 2 semanas — {período} (fuso America/Sao_Paulo)

EMPURRAR (campeões)
• {produto}: {ângulo sugerido} — {canal: Instagram | site/blog | ambos}
• {produto}: {ângulo sugerido} — {canal}

GIRAR (parados)
• {produto}: {ângulo de oferta ou combo} — {canal}

CALENDÁRIO
Semana 1:
  Seg: {ideia de post/e-mail}
  Qua: {ideia de post/e-mail}
  Sex: {ideia de post/e-mail}
Semana 2:
  Seg: {ideia de post/e-mail}
  Qua: {ideia de post/e-mail}
  Sex: {ideia + 1 tema pro blog NuvemShop}
```

Ofertas reais pra usar nos ângulos: Pix com desconto e 3x sem juros (site), frete grátis SP acima de R$ 199, combo pra subir o ticket (meta R$ 71,63 → R$ 200,00).

## Falta de dados

Se não veio nenhum relatório de venda, pare — a análise precisa de pelo menos uma fonte de venda. Peça o export do Bling (maior cobertura). Se só veio um canal, rode com ele e anote: "análise só com vendas do site (NuvemShop) — falta ML e Shopee" (ou equivalente). Sem relatório de tráfego do Thomas, pule o cruzamento de mídia no "porquê" e diga isso.

## Portões de aprovação

- **Nunca agende nem publique conteúdo sozinho.** O briefing é só pra revisão do JhEY.
- **Nunca crie artes no Canva automaticamente** — ofereça gerar depois que o JhEY aprovar o briefing (aí entra a `canva-creator`).

## Saída

Apresente a análise de vendas, depois o briefing. Se for útil, ofereça rascunho no Gmail e um bloco pra colar no WhatsApp (alinhar com o Thomas). Pergunte se o JhEY quer gerar as artes (via `canva-creator`) pra algum post planejado.
