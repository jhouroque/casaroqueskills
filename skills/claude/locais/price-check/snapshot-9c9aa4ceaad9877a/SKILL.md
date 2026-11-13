<!-- C:\Users\Jhonatas\AppData\Roaming\Claude\local-agent-mode-sessions\c5e8a475-a351-48d2-8db3-3f0857ad643d\1d524d29-2570-4e4b-8d1f-844a61e14635\local_f6e23d68-ce2b-4eec-b343-aeec8fb24add\outputs\cr-plugin\small-business\skills\price-check\SKILL.md -->
---
name: price-check
description: >
  Calcula a margem por produto da Casa Roque e mostra 3 cenários de preço, para o
  JhEY ver o quadro financeiro antes de decidir quanto cobrar. Usa o markup padrão
  2,70x, comissão de marketplace 16%, Simples efetivo ~10%, custo de espuma
  R$ 653,33/m³, frete grátis SP acima de R$ 199,00 e o ticket médio R$ 71,63 (meta
  R$ 200,00). Use quando o JhEY disser "qual a margem do trocador?", "quanto cobrar
  no berço?", "tá valendo a pena esse preço?", "subir o preço da espuma?" ou pedir
  análise de preço. Aceita o nome do produto como argumento opcional.
allowed-tools: Read, Bash
---

Roda a análise de preço. Levante custo e receita, monte a tabela de margem e modele
três cenários — pro JhEY ver os números claros antes de decidir o preço. **Não
recomende um preço; apresente dados.**

Parâmetros:
- `NOME_PRODUTO` (opcional) — produto específico (ex.: "trocador", "berço",
  "espuma D28", "kit", "ninho"); se omitido, analise os principais produtos ativos.

## Constantes da Casa Roque (CONTEXTO §5 — não inventar)

| Constante | Valor |
|---|---|
| Markup padrão | **2,70x** sobre o custo total |
| Comissão marketplace (ML/Shopee) | **16%** (site próprio: 0%) |
| Simples Nacional (alíquota efetiva) | **~10%** sobre o faturamento |
| Custo da espuma D23/D28 | **R$ 653,33/m³** |
| Frete grátis (site) | pedidos **SP acima de R$ 199,00** |
| Ticket médio atual / meta | **R$ 71,63** / **R$ 200,00** |
| Margem líquida (meta do grupo) | **> 30%** |

> A reforma tributária 2026 (ano-teste) já traz CBS 0,9% + IBS 0,1% nas NF-e, mas é
> informativo/compensável com PIS-Cofins, **sem aumento de carga** em 2026. Não somar
> isso à margem como custo novo — é acompanhamento. **Confirmar o impacto com a
> Contabilizei.**

## Passo 1 — Margem atual (baseline)

Sem conector de Bling/marketplace — peça/leia os relatórios:
1. **Custo do produto**: ficha do produto no **Bling** (custo de matéria-prima:
   espuma, tecido, aviamentos) + mão de obra (costureira: Cleusa por demanda, Vanda
   R$ 2,00/lençol) + embalagem. Se o JhEY não tiver a ficha, peça os itens de custo.
2. **Receita por produto**: relatório de vendas dos últimos 90 dias (Bling/ML/Shopee).
3. **Canal**: separar venda de **marketplace** (comissão 16% + Simples ~10%) de
   venda de **site** (0% comissão + Simples ~10%) — a margem líquida muda bastante.

Cálculo da margem (por unidade, num canal):
```
preço_sugerido      = custo_total × 2,70
receita_líquida_mkt = preço − (preço × 16%) − (preço × 10%)      [marketplace]
receita_líquida_site= preço − (preço × 10%)                       [site, sem comissão]
margem_R$           = receita_líquida − custo_total
margem_%            = margem_R$ ÷ preço
```

Monte a tabela de margem:

```
Produto        | Custo total | Preço (2,70x) | Canal      | Rec. líquida | Margem R$  | Margem %
{produto}      | R$ {valor}  | R$ {valor}    | Marketplace | R$ {valor}   | R$ {valor} | {X}%
{produto}      | R$ {valor}  | R$ {valor}    | Site        | R$ {valor}   | R$ {valor} | {X}%
```

Sinalize qualquer produto com margem líquida **abaixo de 30%** (meta do grupo) como
ponto de atenção — e abaixo de 20% como risco.

## Passo 2 — Três cenários de preço

Para cada produto (ou o produto pedido), modele três cenários. **NÃO recomende um
preço — só dados.**

**Cenário A — Manter o preço atual**
- Receita projetada = preço atual × volume atual
- Margem com o custo atual

**Cenário B — Aumento de preço (+10% a +20%, o JhEY define o %)**
- Receita projetada assumindo perda de volume de 0%, 5% e 10% no novo preço
- Volume de equilíbrio (break-even) pra manter o lucro atual
- Verifique o efeito no **frete grátis SP > R$ 199,00** (subir o preço pode cruzar o
  limite e ativar o frete grátis — muda a conta) e no **ticket médio** (meta R$ 200,00)

**Cenário C — Redução de preço (−10%, pra girar volume)**
- Receita projetada assumindo aumento de volume de 10%, 20% e 30%
- Volume necessário pra igualar o lucro atual
- Atenção: com comissão 16% + Simples ~10%, a margem é sensível — mostre quanto de
  volume extra paga o desconto

Apresente cada cenário como tabela de dados, não como recomendação.

## Passo 3 — Texto pro cliente (só em cenário de aumento)

Se for cenário de aumento, produza um texto curto que o JhEY pode usar pra comunicar:
- Um parágrafo explicando o reajuste (ex.: alta no custo da espuma/tecido)
- Três opções de mensagem (direta, focada em valor, empática)
- Sugestão de timing e canal (descrição do anúncio no ML/Shopee, post no
  @casaroque.design, ou bloco pra WhatsApp no atacado)

## Falhas de fonte de dados

Sem conector: se faltar a ficha de custo do Bling, a análise de margem trava —
peça os itens de custo do produto (espuma em m³, tecido, mão de obra, embalagem). Se
faltar o relatório de vendas, rode a margem unitária só com o custo e avise que não
dá pra projetar volume.

## Portões de aprovação

- **Nunca recomende um preço específico.** Só apresente os dados — a decisão de preço
  é do JhEY.
- **Sinalize se o custo estiver incompleto** (ficha do Bling sem mão de obra ou
  embalagem, por ex.) e aponte a lacuna.
- **Nunca altere preço no Bling, ML, Shopee, NuvemShop ou qualquer sistema.**
- Onde o cálculo toca imposto (Simples, reforma tributária): **validar com a
  Contabilizei** antes de decidir.

## Saída

Apresente a tabela de margem, depois as três tabelas de cenário lado a lado. Se um
aumento estiver em análise, anexe o texto pro cliente. Encerre com: "Qual cenário
você quer explorar a fundo?"

---

## Exemplo rápido (trocador, venda em marketplace)

Dados de custo (ficha Bling, ilustrativos — confirmar os reais):
- Espuma D28: 0,012 m³ × R$ 653,33/m³ = R$ 7,84
- Tecido + plumante + aviamentos = R$ 9,50
- Mão de obra (Cleusa, por demanda) = R$ 6,00
- Embalagem = R$ 2,00
- **Custo total = R$ 25,34**

| Item | Conta | Valor |
|---|---|---|
| Preço sugerido (2,70x) | 25,34 × 2,70 | **R$ 68,42** |
| Comissão marketplace (16%) | 68,42 × 0,16 | − R$ 10,95 |
| Simples (~10%) | 68,42 × 0,10 | − R$ 6,84 |
| Receita líquida | 68,42 − 10,95 − 6,84 | R$ 50,63 |
| Custo total | — | − R$ 25,34 |
| **Margem líquida** | 50,63 − 25,34 | **R$ 25,29 (37,0% do preço)** |

No **site** (sem os 16% de comissão): receita líquida R$ 61,58, margem R$ 36,24
(53,0%). Por isso empurrar venda pro site (e pro frete grátis SP > R$ 199,00 no
pedido combinado) melhora muito a margem. Ticket de R$ 68,42 ainda está perto do
ticket médio atual (R$ 71,63) e longe da meta (R$ 200,00) — kit/combo ajuda a subir.
