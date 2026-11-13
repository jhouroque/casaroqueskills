---
name: month-end-prep
description: >
  Conduz o fechamento mensal da Casa Roque: concilia o Bling (NFs e pedidos
  emitidos) contra os repasses de Mercado Livre, Shopee e NuvemPago, identifica
  divergências, comissões (16%), taxas, devoluções/estornos e a dívida do ML
  descontada no repasse, confere NFs sem pendência e monta um DRE simplificado
  (faturamento − comissões − Simples − CMV − folha − Ads − frete). Use quando o
  JhEY disser "fechar o mês", "fechamento", "conciliar repasses", "o que ficou
  pendente", "DRE", "bateu o caixa?" ou perguntar por que faturamento ou margem
  mudaram no mês.
---

# Fechamento mensal (Casa Roque)

## Início rápido

A Casa Roque não tem conector de Bling, Mercado Livre, Shopee nem NuvemPago.
Para fechar o mês, o JhEY exporta os relatórios e manda os CSVs/PDFs. Peça
explicitamente o que falta — nunca pule uma etapa em silêncio:

> "Pra fechar [mês], me manda: (1) relatório de **vendas/NFs do Bling** (CSV),
> (2) **repasses do Mercado Livre/Mercado Pago** (extrato/liberações), (3)
> **repasses da Shopee**, (4) **repasses NuvemPago** do site. Se tiver
> devoluções/estornos no período, manda também."

Conduza o JhEY passo a passo. Pare em cada gate antes de avançar.

> **Calendário (ver CONTEXTO §6):** o fechamento roda no **último dia útil** do
> mês. O envio das **NFs ao Contabilizei vence dia 5** do mês seguinte — sinalize
> isso já no começo se a data estiver perto.

## Fluxo

Trabalhe as etapas em ordem. Cada etapa tem um estado de conclusão; não avance
até a etapa atual estar resolvida.

### Passo 1 — Acordar o mês de referência

Pergunte qual mês fechar. Default: o mês civil anterior. Confirme antes de pedir
qualquer dado.

### Passo 2 — Puxar o faturamento do Bling (NFs e pedidos)

Do relatório do Bling, extraia para o mês:
- **Faturamento bruto** (soma das NFs emitidas)
- **Pedidos por canal** (Mercado Livre, Shopee, site/NuvemShop)
- **Lista de NFs**: número, canal, data, valor, status

Sinalize na hora:
- **Pedidos sem NF emitida** — todo pedido precisa de NF (POP 1, Keila). Liste-os
  para o JhEY resolver antes de avançar (lembre: prazos Shopee 11h, site 12h).
- **NFs canceladas/denegadas** no período.

Apresente a contagem ("8 pedidos ainda sem NF") e a lista. Não avance com pedidos
sem NF a menos que o JhEY diga "deixa pra depois".

Veja [reference/quickbooks-reconcile.md](reference/quickbooks-reconcile.md) para
os campos do relatório do Bling e problemas comuns de dados.

### Passo 3 — Conciliar com os repasses dos marketplaces

Para cada canal, pegue o extrato de repasses (ML/Mercado Pago, Shopee, NuvemPago)
do mesmo mês e concilie contra o faturamento do Bling.

Atenção ao conceito central: **o que cai na conta NÃO é o valor da venda.** O
marketplace desconta comissão (~16%), taxas, frete e — no caso do ML — a parcela
da **dívida** (Casa Roque ~R$ 80 mil, Casa Weber ~R$ 75 mil). O repasse líquido é
sempre menor que o bruto faturado.

Para cada repasse:
- **Bate** — valor bruto da venda confere com o pedido do Bling (data ±2 dias) →
  marcar como conciliado; registrar comissão e taxas como deduções esperadas.
- **Diferença < R$ 1,00** — arredondamento/centavos; anote, não sinalize.
- **Diferença ≥ R$ 1,00** (além de comissão/taxa/frete já explicados) → sinalize
  com o valor da diferença e a provável causa.
- **Repasse sem pedido no Bling** → sinalize como "venda sem NF no Bling".
- **Pedido no Bling sem repasse** → ainda **a liberar** (ML/Shopee seguram o
  valor; site NuvemPago libera conforme o parcelamento). Anote como pendente do
  próximo mês, não como erro.

Separe e some por categoria: **comissão (16%)**, **taxas**, **frete**, **dívida ML
descontada**, **antecipação** (se o JhEY antecipou recebíveis), **estornos/
devoluções**.

Veja [reference/paypal-settlements.md](reference/paypal-settlements.md) para a
estrutura dos repasses de ML, Shopee e NuvemPago.

### Passo 4 — Detectar lançamentos duplicados / suspeitos

Varra os relatórios procurando NFs ou repasses duplicados. Sinalize como suspeita
de duplicidade quando **os três** baterem:
- Mesmo valor (± R$ 0,01)
- Mesmo cliente/pedido ou mesmo canal
- Lançados em até 5 dias um do outro

Apresente os pares ao JhEY. Ele decide se é legítimo (ex.: dois pedidos iguais do
mesmo cliente) ou duplicidade real a corrigir.

Veja [reference/gotchas.md](reference/gotchas.md) para falsos positivos comuns.

### Passo 5 — Devoluções, estornos e dívida ML

Concilie as devoluções/trocas do período (fluxo do POP: SAC → etiqueta de retorno
→ Emerson confere → restock/descarte → reembolso/reenvio).

Para cada estorno/reembolso:
- Deve casar com a NF de devolução / pedido original. **Não** trate um estorno
  como repasse faltante.
- Some o total devolvido no mês — entra como dedução do faturamento líquido.

Confirme o valor de **dívida do ML descontada no mês** (lido do extrato de
repasses). Ele reduz o que entrou em caixa, mas é abatimento de passivo, não
despesa do mês — registre separado para não distorcer o DRE.

### Passo 6 — Gate de aprovação do JhEY

Apresente o resumo antes de seguir:

```
Pedidos sem NF:               X de X resolvidos
Divergências de repasse:      X sinalizadas, X resolvidas
Duplicidades suspeitas:       X sinalizadas, X liberadas
Devoluções/estornos no mês:   R$ X
Dívida ML descontada no mês:  R$ X
```

Pergunte: "Pronto pra montar o DRE e exportar o pacote de fechamento?"

**Não avance para os Passos 7–8 sem confirmação explícita.**

### Passo 7 — Montar o DRE simplificado + narrativa

Estrutura do DRE simplificado do mês:

```
(+) Faturamento bruto (Bling)
(−) Devoluções/estornos
(=) Faturamento líquido
(−) Comissões marketplace (~16% ML/Shopee; site 0%)
(−) Simples Nacional (DAS ~10% efetivo — ver CONTEXTO §10)
(−) CMV (custo das mercadorias vendidas)
(−) Folha (Keila, Emerson, Cleusa, Vanda + encargos FGTS 8%)
(−) Ads (Google Ads, Performance Max)
(−) Frete (parcela paga pela empresa)
(=) Resultado do mês
```

> ⚠️ A alíquota efetiva do Simples depende do RBT12 (fórmula em CONTEXTO §10). Use
> ~10% como referência da 4ª faixa, mas **o valor do DAS quem fecha é a
> Contabilizei** — registre como provisão e marque "validar com a Contabilizei".
> A dívida do ML aparece em nota, não como linha de despesa do DRE.

Depois escreva uma **narrativa curta em pt-BR** (150–250 palavras), do jeito que o
JhEY explicaria pra um sócio — direto, técnico, sem jargão vazio:

1. **Manchete** — uma frase: "Maio fechou em R$ X de resultado, +/−Y% vs abril."
2. **Faturamento** — o que puxou o número; cite canais (ML/Shopee/site) e SKUs
   se houver concentração (trocadores, ninhos, espumas D23/D28, lençóis).
3. **Margem** — se segurou, subiu ou comprimiu, e por quê (comissão, frete, CMV).
4. **Despesas-chave** — qualquer linha que mexeu >10% vs mês anterior; uma frase.
5. **Resultado** — vs mês anterior e vs **meta de R$ 83,3 mil/mês** (grupo).
6. **Watch list** — 1 a 3 pontos pra acompanhar (ex.: dívida ML, ROI Ads, devoluções).

Veja [reference/examples/pl-narrative.md](reference/examples/pl-narrative.md) para
um exemplo pronto.

### Passo 8 — Exportar o pacote de fechamento

Gere dois arquivos:

**`fechamento-[AAAA-MM].xlsx`** — três abas:
- `DRE` — o DRE simplificado, formatado, com coluna de comparação vs mês anterior
- `Conciliacao` — pedidos/NFs do Bling x repasses, lado a lado
- `Pendencias` — qualquer item em aberto (pedido sem NF, divergência, etc.)

**`fechamento-[AAAA-MM]-resumo.pdf`** — uma página:
- Mês e empresa no topo
- Números-chave (faturamento líquido, margem %, resultado)
- A narrativa do Passo 7
- Contagem de pendências, se houver

Salve no Google Drive (ou no caminho que o JhEY indicar). Confirme os locais dos
arquivos.

Veja [reference/close-packet-format.md](reference/close-packet-format.md) para
specs de colunas e layout do PDF.

## Gates de aprovação

- **Nunca rode o fechamento de um mês já entregue ao contador.** Confirme que o
  mês ainda está aberto antes de puxar dados.
- **Nunca altere NF ou pedido direto no Bling.** Você só sinaliza; o JhEY/Keila
  ajustam no Bling.
- **Sempre pare no Passo 6** antes de gerar os arquivos. Pendências precisam ser
  resolvidas ou explicitamente adiadas.
- **Imposto/folha:** qualquer número de DAS, Simples ou folha é **provisão** —
  "validar com a Contabilizei antes de pagar/declarar".

## Degradação graciosa (sem conector)

| Falta | Alternativa |
|---|---|
| Bling | Pedir CSV de vendas/NFs do mês (faturamento + detalhe por pedido) |
| Repasse ML/Mercado Pago | Pedir o extrato de liberações/repasses do período |
| Repasse Shopee | Pedir o relatório de repasses da Shopee |
| Repasse NuvemPago (site) | Pedir o extrato de recebimentos do NuvemPago |
| Devoluções | Pedir ao JhEY a lista de devoluções/estornos do mês |

## Arquivos de referência

- [reference/quickbooks-reconcile.md](reference/quickbooks-reconcile.md) — campos
  do relatório do Bling, paginação de exportações, problemas comuns de dados
- [reference/paypal-settlements.md](reference/paypal-settlements.md) — estrutura
  dos repasses de Mercado Livre, Shopee e NuvemPago (liberação, comissão, taxas,
  antecipação)
- [reference/close-packet-format.md](reference/close-packet-format.md) — specs das
  colunas do xlsx, layout do PDF, padrão de nome de arquivo
- [reference/gotchas.md](reference/gotchas.md) — pegadinhas BR (comissão x repasse
  líquido, devoluções, dívida ML, regime de caixa x competência)
- [reference/examples/pl-narrative.md](reference/examples/pl-narrative.md) —
  exemplo de DRE/narrativa da Casa Roque
