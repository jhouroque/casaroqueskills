# Fonte de dados de venda (relatórios/CSV — Bling, ML, Shopee, NuvemShop)

A Casa Roque **não tem conector** de Bling, Mercado Livre, Shopee ou NuvemShop. A estratégia de conteúdo se baseia em **relatórios/CSV exportados** desses sistemas. Este documento descreve de onde vem cada dado e como pedir o export.

## Situação atual

- Não existe MCP de venda ligado. A análise roda com arquivos que o JhEY anexa (CSV/Excel) ou cola.
- A fonte **preferida** é o **Bling**, porque ele integra Mercado Livre, Shopee e o site (NuvemShop) e gera um relatório de vendas por produto já consolidado.
- Quando o JhEY não tem o consolidado do Bling à mão, dá pra trabalhar com os exports separados de cada canal e somar.

## O que pedir (e onde está)

### 1. Bling — relatório de vendas por produto (preferido)

- Caminho típico: **Vendas → Relatórios → Vendas por produto** (ou "Curva ABC de produtos").
- Período: **últimos 90 dias**.
- Colunas úteis: produto/SKU, quantidade vendida, valor total, canal (se o Bling marcar a origem ML/Shopee/site).
- Formato: CSV ou Excel.

Pedido pronto:
> "Exporta do Bling o relatório de **vendas por produto** dos últimos 90 dias (CSV). Se der pra incluir a coluna de canal/origem, melhor."

### 2. Mercado Livre — vendas/anúncios

- Caminho: **Mercado Livre → Vendas** (ou central de vendedor → relatórios) → exportar.
- Útil quando não há o consolidado do Bling.
- Lembrar: ML cobra **16%** de comissão; o ticket aqui costuma ser menor e o volume maior.

### 3. Shopee — pedidos/produtos

- Caminho: **Seller Centre → Pedidos / Meus Produtos** → exportar relatório.
- Lembrar: Shopee também cobra **16%**.

### 4. Site — NuvemShop

- Caminho: **NuvemShop admin → Estatísticas / Pedidos** → exportar.
- Importante: o site tem **margem cheia** (0% de comissão), ticket maior, desconto no Pix e 3x sem juros no NuvemPago. Vendas do site pesam mais na meta de subir o ticket médio.

## Como ler os arquivos

1. **Confirme o cabeçalho antes de calcular.** Cada export nomeia as colunas de um jeito ("Valor total", "Total do pedido", "Receita"). Se houver ambiguidade, mostre as primeiras linhas e confirme o mapeamento com o JhEY (ver `gotchas.md`).
2. **Marque o canal de cada linha.** Mesmo produto vende em ritmos diferentes por canal. Manter a origem permite recomendar "empurrar X no site" x "X no ML".
3. **Some por produto/SKU**, não por anúncio — o mesmo trocador pode ter vários anúncios no ML/Shopee.
4. **Normalize nomes.** "Trocador americano", "Trocador de bebê americano" e "Kit trocador" podem ser o mesmo item ou itens diferentes — pergunte se não estiver claro.

## Quando faltar dado

- **Sem nenhum arquivo:** peça o relatório de vendas por produto do Bling (90 dias). É o de maior cobertura.
- **Só um canal:** rode com o que tiver e **anote no resultado** que a leitura cobre só aquele canal (ex.: "análise só com vendas do site — falta ML e Shopee").
- **Menos de 3 meses de histórico:** use a sazonalidade do segmento como referência e sinalize base curta.

## Por que não há integração automática

1. **Sem MCP de Bling/ML/Shopee/NuvemShop** no plugin hoje — só Canva, Gmail, Google Agenda e Google Drive estão ligados.
2. As contas de venda (Bling, ML admin, Shopee admin) são **off-limits** para operação automática sem autorização explícita (CONTEXTO §9).
3. Enquanto não houver conector, o fluxo por **relatório/CSV** é o caminho oficial — confiável e auditável, com o JhEY no controle do que é exportado.
