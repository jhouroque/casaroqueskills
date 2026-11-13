<!-- C:\Users\Jhonatas\AppData\Roaming\Claude\local-agent-mode-sessions\c5e8a475-a351-48d2-8db3-3f0857ad643d\1d524d29-2570-4e4b-8d1f-844a61e14635\local_f6e23d68-ce2b-4eec-b343-aeec8fb24add\outputs\cr-plugin\small-business\skills\content-strategy\SKILL.md -->
---
name: content-strategy
description: >
  Analisa os dados de venda da Casa Roque (Bling, Mercado Livre, Shopee, site
  NuvemShop) para achar os campeões de venda e os itens parados, cruza com a
  sazonalidade do segmento (bebê/enxoval/decoração) e entrega um plano de
  conteúdo priorizado de 30 dias: o que empurrar no Instagram (@casaroque.design)
  e no blog NuvemShop, qual oferta rodar, o que segurar. Saída estratégica —
  não gera calendário nem artes. Use quando o JhEY perguntar "o que eu posto
  esse mês", pedir um plano de conteúdo, perguntar "o que tá vendendo" ou
  "o que promover".
compatibility: "Sem conector de Bling/ML/Shopee — trabalha com relatórios/CSV exportados de venda. Conectores ativos só de apoio: Gmail, Google Agenda, Google Drive, Canva. A execução (calendário, artes, legendas) fica na skill canva-creator."
---

# Estratégia de conteúdo (content-strategy)

> **Status:** rascunho MVP
> **Dono:** JhEY
> **Categoria:** Marketing & Vendas

## Início rápido

Quando o JhEY pergunta "o que eu posto esse mês?" ou "qual meu plano de conteúdo?", esta skill:

1. **Lê os dados de venda** dos relatórios/CSV do Bling, Mercado Livre, Shopee e site NuvemShop (vendas por produto/SKU, por data, por canal).
2. **Acha os padrões** — campeões de venda, itens parados, tendências de alta/baixa.
3. **Cruza com sazonalidade** — calendário do segmento (Dia das Mães, Black Friday, Natal, Dia das Crianças, volta às aulas) e o histórico da loja.
4. **Entrega um plano de 30 dias** — o que empurrar, o que segurar, qual oferta rodar, com foco em Instagram (@casaroque.design) e blog NuvemShop (1 post/semana).
5. **Pega o ok do JhEY** antes de o plano virar execução na skill `canva-creator`.

A saída é **só estratégica** — sem calendário de postagem detalhado, sem artes. Quem executa é a `canva-creator`.

---

## Fluxo de trabalho

### Passo 1 — Identificar a fonte de dados de venda

A Casa Roque **não tem conector** de Bling, Mercado Livre, Shopee ou NuvemShop. A fonte é **relatório/CSV exportado**. Veja `reference/square-integration.md` para o passo a passo de cada export. Se nada foi anexado, peça de forma objetiva:

> "Me manda o relatório de **vendas por produto** dos últimos 90 dias — do Bling (consolidado) ou, separado, do Mercado Livre, da Shopee e do site (NuvemShop). CSV serve."

Anote quais canais entraram na análise — isso muda a leitura (o site tem ticket maior e margem cheia; o ML/Shopee têm volume mas pagam 16% de comissão).

### Passo 2 — Combinar a métrica de "campeão"

Pergunte ao JhEY como ele quer medir os campeões:

- **"Como eu mido 'mais vendido'?"**
  - Por faturamento total (R$)?
  - Por margem (lembrando o markup 2,70x e a comissão de 16% no marketplace)?
  - Por giro (quantas unidades saem por semana)?
  - Combinação?

Padrão útil pra Casa Roque: ranquear por **faturamento** e cruzar com **giro**, porque a meta é subir o ticket médio (de R$ 71,63 para R$ 200,00) — itens de ticket alto que giram bem (kits/ninhos, berços, espumas) valem mais que volume de item barato.

### Passo 3 — Puxar e analisar as vendas

Janela: **últimos 90 dias** (ou todo o histórico disponível, se < 90 dias). Extraia: nome do produto/SKU, data da venda, canal, faturamento, quantidade.

Notas por canal:

- **Bling** — relatório consolidado de vendas por produto (já agrega ML + Shopee + site, se o JhEY integrou tudo). É a fonte preferida quando existe.
- **Mercado Livre** — export de vendas/anúncios (volume alto, ticket menor, comissão 16%).
- **Shopee** — relatório de pedidos/produtos (volume, comissão 16%).
- **Site (NuvemShop)** — relatório de pedidos (ticket maior, margem cheia, Pix com desconto e 3x no NuvemPago).

Se vier ambíguo, mostre o cabeçalho do CSV e confirme o mapeamento antes de calcular (ver `reference/gotchas.md`).

Identifique:
- **Top 3–5 campeões** (pela métrica escolhida).
- **3–5 parados** (candidatos a segurar, encartar ou girar com oferta — ex.: espuma de densidade que encalhou).
- **Em alta** (ganhando tração nos últimos 30 dias).
- **Em queda** (perdendo tração).

**Fallback:** com menos de 3 meses de dados, use a sazonalidade do segmento (abaixo) como referência e sinalize que a leitura está com base curta.

### Passo 4 — Cruzar com a sazonalidade

A linha da Casa Roque (trocadores, berços, kits/ninhos, espumas D23/D28/D33/D44, lençóis, plumante) responde a datas claras:

- **Dia das Mães** (maio) — pico de enxoval e itens de bebê/presente; empurrar trocadores, kits e ninhos.
- **Volta às aulas** (jan–fev e jul) — menos central, mas movimenta decoração de quarto e organização.
- **Dia das Crianças** (outubro) — kits, ninhos, decoração de quarto infantil.
- **Black Friday** (novembro) — pico de volume; preparar oferta com antecedência (estoque + arte).
- **Natal** (dezembro) — presente; kits e itens de ticket maior.

Sinalize o que deve **subir ou descer** nos próximos 30 dias conforme a data que está chegando. Quando o JhEY já tiver leitura própria de sazonalidade, ela manda — pergunte "isso bate com o que você vê na loja?".

### Passo 5 — Montar o plano de 30 dias

Estrutura:
- **Resumo** (1–2 frases: "Seus campeões são X e Y. A virada pro Dia das Mães começa agora.").
- **Empurrar forte** (top 2–3 produtos + ângulo de conteúdo: post de antes/depois do quarto, reels mostrando densidade da espuma, depoimento de cliente).
- **Manter** (intermediários; manter visibilidade sem esforço pesado).
- **Encartar ou pausar** (parados; oferta, kit/combo, ou segurar até a próxima data).
- **Oportunidade sazonal** (a data que vem aí e o que posicionar desde já).
- **Ofertas sugeridas** (combo, desconto no Pix do site, frete grátis SP acima de R$ 199 — alavancas reais da Casa Roque).
- **Blog NuvemShop** (1 tema da semana, dos já mapeados: enxoval, trocador tradicional x americano, densidade de espuma, decoração de quarto de bebê, plumante).

Tamanho: **200–400 palavras** (curto e acionável, não redação).

### Passo 6 — Aprovação e iteração

Apresente o plano ao JhEY. Pergunte:
- "Bate com sua leitura?"
- "Algo pra ajustar?"
- "Mando isso pra `canva-creator` montar o calendário e as artes?"

Itere se preciso; aprovado, devolva o plano final estruturado (pronto pra `canva-creator`). Se for útil, ofereça também um **rascunho no Gmail** com o plano e um **bloco pra colar no WhatsApp** (alinhar com Thomas a parte de tráfego). Nada é executado/postado aqui — isso é da `canva-creator`, com aprovação.

---

## Pegadinhas

Veja [`reference/gotchas.md`](reference/gotchas.md) para os erros mais comuns (ticket baixo, dependência de marketplace, sazonalidade de bebê).

---

## Arquivos de referência

| Arquivo | Carregar quando |
|---|---|
| `reference/square-integration.md` | Para o passo a passo de exportar os relatórios de venda do Bling/ML/Shopee/NuvemShop |
| `reference/gotchas.md` | Para as pegadinhas de leitura (correlação x causa, margem x volume, sazonalidade, estoque) |
| `reference/examples/retail-boutique-example.md` | Para um exemplo completo (empurrar trocadores no Dia das Mães; girar espuma parada) |
