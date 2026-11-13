---
name: margin-analyzer
description: >
  Analisa unit economics por produto/serviço da Casa Roque a partir de dados de
  custo e venda do Bling e dos repasses dos marketplaces. Aplica markup 2,70x,
  comissão 16% (ML/Shopee; site 0%), Simples efetivo ~10% e o custo de espuma
  (R$ 653,33/m³ para D23/D28), considera o frete grátis SP acima de R$ 199, e
  mostra três cenários de preço. Apresenta a análise — não recomenda preço. Use
  quando o JhEY perguntar sobre aumentar preço, precificação, margem, quanto
  cobrar, se o custo está comendo o lucro, ou como uma mudança de preço afeta o
  resultado. Dispare mesmo sem a palavra "margem" — "tô ganhando o suficiente?",
  "devo cobrar mais?" ou "meu custo subiu" pedem esta skill.
---

# Analisador de margem (Casa Roque)

> **Status:** rascunho MVP · **Dono:** JhEY · **Versão:** 1.1.0
> **Categoria:** Financeiro & Ops

## Início rápido

Quando o JhEY perguntar "devo aumentar o preço?" ou "minha margem tá ok?", esta
skill:

1. **Define o escopo** — quais produtos/serviços analisar
2. **Reúne os custos** do Bling (CMV, custo por item; espuma R$ 653,33/m³)
3. **Reúne as vendas** dos repasses (ML, Shopee, site) — valor líquido após
   comissão 16% e taxas
4. **Calcula unit economics** — receita, custo, comissão, Simples, margem por item
5. **Contextualiza** — inflação de insumo, mudança de custo, benchmarks do setor
6. **Monta três cenários de preço** — o que acontece com receita e margem a cada
   ajuste
7. **Apresenta a análise** — sem recomendar preço; a decisão é do JhEY

A saída dá ao JhEY os números reais para ele decidir o preço.

> Sem conector de Bling/marketplace: peça os CSVs (custos do Bling, repasses dos
> canais). Schema em [reference/csv-schema.md](reference/csv-schema.md).

---

## A conta da Casa Roque (base de toda análise)

Toda precificação parte do **markup 2,70x sobre o custo total**. Mas o markup não
é a margem — o marketplace come uma fatia grande. Decomposição de uma venda:

```
Preço de venda        = custo total × 2,70   (markup padrão)
(−) Comissão          = 16% do preço (ML/Shopee; site = 0%)
(−) Simples (DAS)     = ~10% efetivo do preço (provisão — ver tax-season-organizer)
(−) Frete             = parcela paga pela loja (frete grátis SP > R$ 199)
(−) CMV               = o custo total do item
(=) Margem de contribuição por item
```

> ⚠️ Markup 2,70x **não** significa margem de 170%. Depois de comissão + Simples +
> frete + custo, a margem líquida por item é bem menor. Ver
> [reference/gotchas.md](reference/gotchas.md).

**Custo de espuma (matéria-prima):** D23/D28 = **R$ 653,33/m³** (fornecedor SP).
Para itens de espuma, o custo por peça sai do volume (m³) × R$ 653,33 + corte/
encapamento + costura (Cleusa/Vanda). Confirme o volume da peça com o JhEY se não
estiver no Bling.

---

## Fluxo

### Passo 1: Pré-checagem

**Categoria:** confirme a linha de produto (trocadores, berços, ninhos/kits,
espumas D23/D28/D33/D44, lençóis, plumante, decoração) para puxar o benchmark
certo. Se não estiver claro, pergunte.

**Sem conector:** ofereça upload de CSV. A skill trabalha com exportações do Bling
(custos) e dos repasses (vendas líquidas). Schema em
[reference/csv-schema.md](reference/csv-schema.md).

### Passo 2: Definir escopo

Pergunte ao JhEY duas coisas:

1. **"Quais SKUs/produtos quer analisar?"** Todos, ou um subconjunto? Se "todos",
   confirme que há dado suficiente antes de puxar tudo.
2. **"Qual métrica importa mais?"** Margem de contribuição (após comissão +
   Simples + frete)? Margem bruta (só CMV)? Receita por unidade? A resposta molda
   a apresentação.

### Passo 3: Reunir custos (Bling)

Do relatório de custos/produtos do Bling, extraia por SKU:
- Custo total do item (CMV): matéria-prima + costura + embalagem
- Para espumas: volume (m³) × R$ 653,33 + custos de transformação
- Mudanças de custo conhecidas nos últimos 6–12 meses

Se o Bling não trouxer custo por item (só CMV total), **não use R$ 0,00 nem média
do negócio inteiro**. Diga ao JhEY:

> "O relatório do Bling tem o CMV total, mas não quebrado por SKU. Para calcular
> margem por produto, preciso do custo de cada item que você quer analisar —
> matéria-prima, costura, embalagem. Mesmo valor aproximado serve."

Sinalize a limitação na seção Notas de Qualidade dos Dados da saída.

### Passo 4: Reunir vendas (repasses)

Dos extratos de repasse (ML, Shopee, NuvemPago), extraia por SKU/período:
- Valor bruto da venda e **valor líquido** (após comissão 16% e taxas)
- Unidades vendidas, canal, data
- Frete (parcela da loja, quando houver)

Use o **valor de venda real** (com descontos/cupons aplicados), não o preço de
tabela. Se só um canal tiver dado, anote a limitação.

### Passo 5: Calcular unit economics

Para cada SKU no escopo, calcule:

| Métrica | Fórmula |
|---|---|
| **Preço de venda** | Valor real recebido por unidade (com desconto) |
| **Comissão** | 16% do preço (ML/Shopee); 0% no site |
| **Simples (DAS)** | ~10% efetivo do preço (provisão) |
| **Frete** | Parcela da loja (frete grátis SP > R$ 199) |
| **CMV** | Custo total do item (Bling) |
| **Margem de contribuição** | Preço − comissão − Simples − frete − CMV |
| **Margem %** | (Margem de contribuição ÷ Preço) × 100 |
| **Unidades** | Contagem de vendas |

Sinalize qualquer SKU com margem **abaixo de 30%** (meta do grupo) — não como
recomendação, mas como ponto de atenção.

### Passo 6: Contextualizar

- **Inflação de insumo:** ex.: "A espuma subiu ~X% no período e o preço ficou
  parado — isso comprimiu a margem em Y pontos."
- **Benchmarks:** use as faixas de e-commerce/enxoval BR de
  [reference/industry-benchmarks.md](reference/industry-benchmarks.md) — marcadas
  como **estimativa** quando não há fonte exata.
- **Comparação histórica:** se houver 12+ meses, compare a margem deste período
  com a do anterior.

Com pouco dado, seja honesto: se há menos de 6 meses de vendas, omita a parte de
elasticidade e diga: "Preciso de pelo menos 6 meses de histórico de preço para
estimar como o volume responde. Mostro os cenários com hipóteses de volume."

### Passo 7: Cenários de preço (três)

Para cada SKU, monte três cenários de ajuste — por padrão **+5%, +10%, +15%**
(ajuste se o JhEY pedir outros):

| Cenário | Novo preço | Receita projetada* | Margem de contribuição % |
|---|---|---|---|
| +5% | R$ X | R$ Y | Z% |
| +10% | R$ X | R$ Y | Z% |
| +15% | R$ X | R$ Y | Z% |

**Como projetar a receita:**
- **Com 6+ meses de histórico:** estime a resposta de volume pelo dado real. Se
  houve um ajuste de preço passado, calcule a elasticidade observada
  (`% variação volume ÷ % variação preço`) e aplique.
- **Sem histórico suficiente:** mostre três hipóteses de volume (−0%, −5%, −10%) e
  deixe o JhEY escolher a realista.

Nota: *"Projeções com base no dado disponível, não garantias. A resposta real
depende de concorrência, sazonalidade (Dia das Mães, Black Friday, Natal) e
sensibilidade do cliente."*

### Passo 8: Apresentar a análise

Estruture com H2 com a empresa e o período, e quatro seções: tabela de **Unit
Economics** (SKU, preço, comissão, Simples, frete, CMV, margem de contribuição,
margem %), **Contexto e Benchmark** (2–4 frases sobre inflação, custo, normas do
setor — marcando estimativas), **Cenários de Preço** (tabela por SKU, ou top 3–5
se muitos) e **Notas de Qualidade dos Dados** (limitações: dado parcial, CMV
ausente, histórico curto).

Mantenha factual. **Não diga** "você deveria aumentar o preço". O JhEY decide.

---

## Limite de escopo

**Esta skill mostra dado. Não recomenda preço.**

Se o JhEY perguntar "e aí, o que eu faço?" — responda: "Mostro o que o dado
sugere, mas a decisão de preço é sua. Quer que eu modele outros cenários?"

É intencional. Preço tem consequência real e depende de contexto que só o JhEY tem
(posicionamento, concorrência no ML/Shopee, necessidade de caixa). O papel da
skill é garantir que ele decida olhando número real.

---

## Conectores

**Sem conector de Bling/marketplace.** Trabalha com CSVs de custos (Bling) e de
repasses (ML, Shopee, NuvemPago) que o JhEY exporta.

---

## Arquivos de referência

- [reference/gotchas.md](reference/gotchas.md) — pegadinhas (comissão + frete +
  Simples comendo a margem; markup x margem)
- [reference/industry-benchmarks.md](reference/industry-benchmarks.md) — faixas de
  margem de e-commerce/enxoval BR (marcadas como estimativa)
- [reference/csv-schema.md](reference/csv-schema.md) — colunas esperadas do CSV de
  custos/vendas do Bling
- [reference/examples/](reference/examples/) — exemplos (Casa Roque produto; serviço)
