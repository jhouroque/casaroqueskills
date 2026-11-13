# Formato do pacote de fechamento

O pacote de fechamento são dois arquivos: uma planilha xlsx e um PDF de uma
página.

## Nome dos arquivos

```
fechamento-2026-05.xlsx
fechamento-2026-05-resumo.pdf
```

Use ano-mês no padrão `AAAA-MM` no nome. Local padrão de salvamento: **Google
Drive**; use o caminho que o JhEY indicar, se houver.

---

## Planilha xlsx — três abas

### Aba 1: DRE

Cópia formatada do DRE simplificado do mês. Layout em duas colunas: **Linha** e
**Valor** (R$).

Linhas obrigatórias (nesta ordem):
1. (+) Faturamento bruto (Bling)
2. (−) Devoluções/estornos
3. **(=) Faturamento líquido** (negrito)
4. (−) Comissões marketplace (~16% ML/Shopee; site 0%)
5. (−) Simples Nacional (DAS — provisão ~10% efetivo)
6. (−) CMV (custo das mercadorias vendidas)
7. (−) Folha (Keila, Emerson, Cleusa, Vanda + FGTS 8%)
8. (−) Ads (Google Ads)
9. (−) Frete (parcela da empresa)
10. **(=) Resultado do mês** (negrito)
11. **Margem %** (negrito, formato percentual)

Inclua coluna de comparação vs mês anterior se houver dado. Formate valores como
moeda (`R$ #.##0,00`). Negativos em vermelho.

> Nota fixa abaixo do DRE: "DAS e folha são **provisão** — validar com a
> Contabilizei antes de pagar/declarar. Dívida do ML descontada no mês: R$ X
> (abatimento de passivo, fora do DRE)."

### Aba 2: Conciliacao

Comparação lado a lado de pedidos/NFs do Bling x repasses dos marketplaces.

Colunas:
| Coluna | Origem |
|---|---|
| Data (Bling) | Data do pedido/NF |
| Canal | Mercado Livre / Shopee / Site |
| Valor bruto (Bling) | Valor da venda no Bling |
| Comissão | Tarifa (~16%) |
| Frete / taxas | Frete e taxas do canal |
| Dívida ML | Parcela da dívida descontada (se ML) |
| Valor líquido (repasse) | O que efetivamente caiu |
| Status | CONCILIADO / VENDA_SEM_NF_NO_BLING / A_LIBERAR / DIVERGENCIA_DATA |

Cores na coluna Status:
- CONCILIADO → verde
- DIVERGENCIA_DATA / A_LIBERAR → amarelo
- VENDA_SEM_NF_NO_BLING → vermelho

### Aba 3: Pendencias

Itens em aberto do checklist. Colunas:
| Coluna | Observações |
|---|---|
| Categoria | Pedido sem NF / Divergência de repasse / Duplicidade / Devolução |
| Data | Data do lançamento |
| Valor | Valor em R$ |
| Canal / Cliente | Identificação |
| Descrição | O que está errado e o que fazer |

Se não houver pendências, mostre uma linha: "Sem pendências — mês conciliado."

---

## PDF de resumo — uma página

Layout (de cima para baixo):

```
[Empresa]                          Fechamento — [Mês/Ano]
────────────────────────────────────────────────────────────

NÚMEROS-CHAVE
Faturamento líquido   R$ XX.XXX,XX
Margem                XX%
Resultado do mês      R$ XX.XXX,XX

RESUMO DO MÊS
[narrativa de 150–250 palavras do Passo 7]

PENDÊNCIAS
X pedidos sem NF · X divergências de repasse · X em aberto
[ou "Mês conciliado — sem pendências." se tudo certo]

────────────────────────────────────────────────────────────
Preparado em [data] · Provisões a validar com a Contabilizei
```

Use fonte sans-serif limpa (Helvetica ou equivalente). Logo opcional. Margens
≥ 1,9 cm em todos os lados para imprimir bem.

**Gerando o PDF:** use as libs Python `xlsxwriter` ou `reportlab` se rodar script,
ou peça ao Claude para renderizar o conteúdo e exportar como PDF. O JhEY também
pode imprimir o PDF a partir da aba DRE se não houver script disponível.
