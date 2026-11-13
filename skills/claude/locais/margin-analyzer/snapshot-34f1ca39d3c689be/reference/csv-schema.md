# Schema do CSV (custos e vendas — Bling)

Como a Casa Roque não tem conector de Bling/marketplace, o JhEY sobe os CSVs
exportados. Este documento especifica as colunas esperadas e como tratar
variações. Valores em R$ (vírgula decimal, ponto de milhar).

## CSV de vendas (repasses dos marketplaces)

Colunas esperadas (a ordem não importa; cabeçalhos sem distinção de maiúscula):

| Coluna | Obrigatória | Descrição |
|---|---|---|
| `data` | Sim | Data da venda (qualquer formato padrão: dd/mm/aaaa, aaaa-mm-dd) |
| `sku` ou `produto` ou `descricao` | Sim | O que foi vendido |
| `canal` | Recomendada | Mercado Livre, Shopee, Site (define comissão: 16% ou 0%) |
| `valor_bruto` ou `preco` ou `total` | Sim | Valor da venda (bruto, R$) |
| `valor_liquido` ou `repasse` | Recomendada | Líquido após comissão/taxas (R$) |
| `comissao` | Não | Tarifa do canal, se vier separada |
| `frete` | Não | Frete (parcela da loja) |
| `quantidade` ou `qtd` | Não | Unidades — se ausente, assuma 1 por linha |

**Exportações que costumam servir:**
- Bling: Relatórios → Vendas → exportar CSV
- Extrato de repasses do Mercado Livre / Mercado Pago
- Relatório de repasses da Shopee
- Extrato do NuvemPago (site)

Se vierem colunas extras, ignore. Se faltar coluna obrigatória, pergunte ao JhEY
qual coluna mapeia.

## CSV de custos (CMV / produtos — Bling)

Colunas esperadas:

| Coluna | Obrigatória | Descrição |
|---|---|---|
| `sku` ou `produto` ou `descricao` | Sim | A que o custo se refere |
| `custo_total` ou `cmv` ou `custo` | Sim | Custo do item (R$) |
| `materia_prima` | Não | Custo de matéria-prima (ex.: espuma) |
| `volume_m3` | Não | Para espumas: volume em m³ (× R$ 653,33 = custo de espuma) |
| `custo_costura` | Não | Costura (Cleusa/Vanda) |
| `embalagem` | Não | Embalagem/frete interno |
| `data` | Não | Data do custo (útil para tendência) |

**Exportações que costumam servir:**
- Bling: Cadastros → Produtos → exportar (com campo de custo)
- Bling: Relatórios → Custos / Margem

## Tratando CSVs bagunçados

Exportações reais são bagunçadas. Problemas comuns:

- **Linhas de cabeçalho extras:** pule linhas até achar a que parece nome de coluna
- **Símbolos de moeda:** remova `R$`, pontos de milhar e troque vírgula por ponto
  antes de converter número (ex.: `R$ 1.234,56` → `1234.56`)
- **Devoluções negativas:** inclua — reduzem a receita líquida
- **Bruto x líquido:** prefira o **líquido** (após comissão/taxa) para a receita;
  pergunte se não estiver claro
- **Espuma sem volume:** se o item é de espuma e não há `volume_m3`, pergunte o
  volume ao JhEY para aplicar R$ 653,33/m³ — não chute

## Depois de carregar

Confirme o formato com o JhEY antes de prosseguir:
- "Carreguei X vendas de [data] a [data] em Y SKUs, nos canais [ML/Shopee/site].
  Tá certo?"
- Se o período ou a contagem parecer estranha, peça pra ele revisar os filtros da
  exportação.
