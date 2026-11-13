# Bling — referência de conciliação

> O nome do arquivo é mantido por compatibilidade. O conteúdo trata da
> conciliação no **Bling** (ERP/NF-e da Casa Roque) x **repasses dos
> marketplaces**. Não há conector de Bling — trabalhe com os relatórios/CSVs
> que o JhEY exporta.

## Relatórios a pedir do Bling

### Faturamento do mês (NFs emitidas)

Peça o relatório de **vendas / notas fiscais emitidas** do Bling, filtrado pelo
mês de referência (primeiro ao último dia).

Campos usados adiante:
| Campo | Observações |
|---|---|
| `numero_nf` | Número da NF-e |
| `data_emissao` | Data de emissão (não a de pedido) |
| `canal` | Mercado Livre, Shopee, NuvemShop (site) |
| `valor_total` | Valor bruto da venda (antes de comissão/taxas) |
| `cliente` | Nome do cliente / comprador |
| `status_nf` | Autorizada, Cancelada, Denegada |
| `cfop` | Útil para separar venda de devolução |

### Pedidos do mês (incluindo sem NF)

Peça também o relatório de **pedidos** do período — é o detalhe linha a linha
usado para achar pedido sem NF e para casar com os repasses.

Campos:
| Campo | Observações |
|---|---|
| `numero_pedido` | ID do pedido no marketplace/site |
| `data_pedido` | Data do pedido |
| `canal` | ML / Shopee / site |
| `valor_pedido` | Valor bruto |
| `situacao` | Em aberto, Faturado, Cancelado, Devolvido |
| `tem_nf` | Indica se já saiu NF (vincula ao POP 1 da Keila) |

## Identificando pedidos sem NF

Sinalize um pedido como pendente de NF quando `situacao` indicar faturado/enviado
mas `tem_nf` estiver vazio, ou quando o pedido aparecer no repasse do marketplace
e não houver NF correspondente no Bling. Lembre os prazos do POP 1: **Shopee 11h,
site 12h, ML variável**.

## Exportações grandes (paginação)

Exportações de CSV do Bling podem vir paginadas ou divididas por canal. Se o
JhEY mandar vários arquivos (um por marketplace), una-os pela coluna `canal`
antes de conciliar. Confira se o período de cada arquivo é o mesmo mês.

## Problemas comuns de dados

**Pedidos divididos / kits** — um kit (ex.: ninho + trocador + lençol) pode
aparecer como várias linhas com mesmo pedido e data, valores diferentes. **Não**
são duplicidade. Antes de sinalizar duplicados, agrupe por `numero_pedido` —
linhas com o mesmo pedido são itens do mesmo lançamento.

**Bruto x líquido** — o relatório do Bling mostra o **valor bruto** da venda. O
extrato do marketplace mostra o **repasse líquido** (já menos comissão ~16%,
taxas, frete e dívida ML). Comparar bruto com líquido sempre dá diferença igual
às deduções — é esperado, não é erro (ver gotchas.md).

**Site x marketplace** — vendas do site (NuvemShop) têm comissão 0%, mas a
NuvemPago retém taxa de cartão e o parcelamento 3x libera ao longo dos meses.
ML e Shopee descontam comissão 16% e seguram o valor até a entrega.

**Devoluções no período** — uma devolução gera NF de entrada/CFOP de retorno. Ela
não é venda; reduz o faturamento líquido. Sinalize devoluções grandes sem pedido
original correspondente para o JhEY conferir.
