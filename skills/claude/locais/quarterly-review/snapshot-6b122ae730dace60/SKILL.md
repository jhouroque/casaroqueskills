---
name: quarterly-review
description: Gera a revisão trimestral da Casa Roque — faturamento vs meta (R$ 83,3 mil/mês), margem (>30%), dívida do ML, top SKUs, ROI do Google Ads (>3x) e desempenho por empresa (Lima/Weber/Roque) — num documento pronto para apresentação. Aceita argumentos opcionais de trimestre e destino.
allowed-tools: Read, WebFetch, Bash
---

Roda a revisão trimestral do grupo Casa Roque. Reúne dado financeiro, de vendas e
de mídia do trimestre, sintetiza numa narrativa e produz um documento pronto.

Argumentos:
- `--trimestre` (default: trimestre civil anterior) — formato `AAAA-TN` (ex.: `2026-T1`)
- `--salvar-em` (default: `drive`) — `drive` (Google Drive), `desktop` ou `ambos`

> Sem conector de Bling/marketplace/Ads: peça os relatórios do trimestre ao JhEY
> (faturamento do Bling, repasses ML/Shopee/NuvemPago, relatório do Google Ads —
> o Thomas reporta toda sexta).

## Passo 1 — Desempenho financeiro

Use o DRE do fechamento mensal (skill `month-end-prep`/`close-month`) dos 3 meses
do trimestre:

1. Faturamento bruto e líquido por mês (Bling); some o trimestre.
2. DRE: comissões (16%), Simples (~10%, provisão), CMV, folha (+ FGTS 8%), Ads,
   frete → resultado e **margem %**.
3. Compare com o trimestre anterior e, se houver, com o mesmo trimestre do ano
   passado.
4. Calcule: crescimento de faturamento %, variação de margem em pontos.

**Metas a confrontar (CONTEXTO §5):**
- Faturamento do grupo: **R$ 83,3 mil/mês (R$ 1 mi/ano)** até dez/2026 → ~R$ 250 mil
  no trimestre.
- **Margem líquida > 30%.**
- Ticket médio: meta R$ 200,00 (atual ~R$ 71,63). Pedidos/dia: meta 35.

## Passo 2 — Vendas, SKUs e canais

1. **Top SKUs** do trimestre (Bling): unidades e faturamento. Linha de produto:
   trocadores, berços, ninhos/kits, espumas (D23/D28/D33/D44), lençóis, plumante,
   decoração.
2. **Mix por canal** (ML, Shopee, site): lembre que o **site tem comissão 0%** e
   margem melhor — mais venda no site melhora o resultado.
3. **Dívida do ML** (Casa Roque ~R$ 80 mil, Casa Weber ~R$ 75 mil): quanto foi
   abatido no trimestre e saldo estimado. Ligar à **meta pessoal do JhEY de quitar
   ~R$ 375 mil até jan/2027**.
4. **Devoluções/estornos** do trimestre (meta de erros operacionais < 2%).

## Passo 3 — Mídia e ROI (Google Ads)

Do relatório do Google Ads (conta 568-607-6835, Performance Max R$ 35/dia):
1. Investimento no trimestre, receita atribuída, **ROI** (meta **> 3x**).
2. **CPC** (meta **< R$ 2,00**), conversão do site (meta 3%).
3. Sazonalidade do trimestre (Dia das Mães, Black Friday, Natal, Dia das Crianças,
   volta às aulas) e o que foi empurrado.

## Passo 4 — Desempenho por empresa

Confronte cada empresa com a meta (CONTEXTO §5):
- **Casa Lima:** meta R$ 137.250/mês — maior fatia do grupo.
- **Casa Weber:** meta R$ 87.000/mês — ⚠️ **incompatível com MEI** (teto R$ 81
  mil/**ano**). Sinalize o risco de desenquadramento e a decisão de regime com a
  Contabilizei (sem afirmar irregularidade).
- **Casa Roque:** meta R$ 25.750/mês — foco em espumas.

## Passo 5 — 3 oportunidades + 3 riscos

**Oportunidades** (específicas, do dado): ex.: migrar venda de espuma para o site
(0% comissão); SKU de margem alta para escalar; canal a reforçar.

**Riscos** (específicos): ex.: margem abaixo de 30% por comissão+frete;
concentração num SKU/canal; dívida ML pesando no caixa; Casa Weber estourando o
teto MEI; ROI de Ads abaixo de 3x.

## Passo 6 — Narrativa da revisão

Escreva 500–800 palavras em pt-BR, direto e técnico, com esta estrutura:
1. Manchete do trimestre (uma frase, com faturamento vs meta e margem)
2. História do faturamento (tendência + porquê, por canal/SKU)
3. História da margem (tendência + porquê: comissão, frete, CMV)
4. Dívida ML e caixa (abatimento no trimestre, saldo, meta de quitação)
5. Mídia (ROI, CPC, conversão vs metas)
6. Por empresa (Lima/Weber/Roque vs metas; alerta MEI Weber)
7. Três oportunidades
8. Três riscos
9. Um parágrafo de foco para o próximo trimestre

## Passo 7 — Exportar

Gere:
1. **`revisao-trimestral-{AAAA-TN}.pdf`** — narrativa + tabelas-chave (faturamento
   por mês, top SKUs, metas por empresa; tabelas ASCII se não houver gerador de
   gráfico)
2. Salve em `--salvar-em`.

## Falhas de conector

Sem conector: o fluxo depende dos relatórios do JhEY. Se faltar o faturamento do
**Bling**, pare — é a base. Se faltarem **repasses**, rode com o que houver e
anote a limitação. Se faltar o **relatório de Ads**, pule o Passo 3 e anote "Ads
não enviado — seção de mídia pulada".

## Gates de aprovação

- **Nunca publique nem envie a revisão automaticamente.** Mostre para o JhEY revisar.
- **Imposto/folha são provisão** — "validar com a Contabilizei".
- **Sinalize qualquer dado incompleto** — anote os furos na narrativa.

## Saída

Apresente a narrativa no chat, depois confirme a exportação. Encerre com um
parágrafo "foco do próximo trimestre" e, se útil, um bloco de texto pronto pra
colar no **WhatsApp** da equipe.
