---
name: close-month
description: Fecha o mês da Casa Roque — concilia Bling x repasses (ML/Shopee/NuvemPago), sinaliza pendências, escreve a narrativa do DRE e exporta o pacote de fechamento. Lembra o DAS (dia 20) e o envio ao Contabilizei (dia 5). Aceita argumentos opcionais de mês e destino.
allowed-tools: Read, WebFetch, Bash
---

Roda o fluxo de fechamento mensal. Concilia, sinaliza pendências, narra o DRE e
exporta o pacote para os registros do JhEY (e para a Contabilizei).

Argumentos:
- `--mes` (default: mês civil anterior) — formato `AAAA-MM`
- `--salvar-em` (default `drive`) — `drive` (Google Drive), `desktop` (local) ou `ambos`

> A Casa Roque não tem conector de Bling/marketplace. Este comando **orquestra**
> a skill `month-end-prep`, que pede os relatórios/CSVs ao JhEY.

## Passo 1 — Conciliar (via month-end-prep)

Dispare o fluxo da skill `month-end-prep`:

1. Peça o relatório de **vendas/NFs do Bling** do mês.
2. Peça os **repasses** de cada canal: Mercado Livre/Mercado Pago, Shopee e
   NuvemPago (site).
3. Case as NFs/pedidos do Bling contra os repasses por valor + data (±2 dias),
   lembrando que o repasse é **líquido** (menos comissão ~16%, taxas, frete e
   dívida ML).
4. Aponte as categorias de pendência:
   - **Repasse sem NF no Bling** — caiu dinheiro de venda que não tem NF emitida
   - **Pedido no Bling sem repasse** — ainda **a liberar** (ML/Shopee seguram;
     site libera por parcela) — pendente, não erro
   - **Divergências de valor** — além de comissão/taxa/frete/dívida já explicadas

## Passo 2 — Sinalizar suspeitas

No mesmo relatório:
- **Pedidos sem NF** — todo pedido precisa de NF (POP 1, Keila)
- **Duplicidades suspeitas** — mesmo valor, mesmo pedido/canal, em até 3 dias
- **Devoluções/estornos** — somar o total e casar com pedido original
- **Dívida ML descontada** — registrar em nota (abatimento de passivo)

Para cada item, recomende uma ação: emitir NF, conferir duplicidade, conciliar
devolução. **Espere o JhEY resolver as pendências antes de gerar a narrativa.**
Não emita NF nem altere nada no Bling automaticamente.

## Passo 3 — Narrativa do DRE

Após o triage, monte o DRE simplificado e a narrativa em pt-BR:

```
{Mês AAAA} fechou com R$ {fat. líquido} de faturamento líquido ({+/-}{X}% vs mês anterior).
Resultado do mês: R$ {resultado} · margem {X}% ({+/-}Y pts vs anterior).
Driver principal: {canal/SKU}. Maior variação: {linha} {direção} R$ {valor}
porque {motivo inferido dos lançamentos}.

Três pontos de atenção:
1. ...
2. ...
3. ...
```

DRE = faturamento bruto − devoluções − comissões (16%) − Simples (DAS, provisão
~10%) − CMV − folha (+ FGTS 8%) − Ads − frete. Os números vêm do Bling/repasses;
o *porquê* vem de cruzar top SKUs, canais e variação vs mês anterior. Compare
contra a **meta de R$ 83,3 mil/mês** e **margem >30%** do grupo.

## Passo 4 — Exportar o pacote de fechamento

Gere dois arquivos:

1. **`fechamento-{AAAA-MM}.xlsx`** — abas:
   - `Conciliacao` — Bling ↔ repasses, com pendências destacadas
   - `Pendencias` — pedidos sem NF / duplicidades / devoluções
   - `DRE` — DRE simplificado com coluna de variação vs mês anterior
2. **`fechamento-{AAAA-MM}-resumo.pdf`** — uma página: narrativa do DRE +
   números-chave + contagem de pendências

Salve no destino `--salvar-em`. Nome: `fechamento-2026-05.xlsx` etc.

## Lembretes de calendário (CONTEXTO §6 e §10)

Ao concluir, sempre lembre o JhEY dos prazos do mês seguinte:
- **Dia 5 / 5º dia útil:** enviar as **NFs do mês à Contabilizei** (prazo fixo).
- **Dia 20:** vencimento do **DAS Simples Nacional** (se cair em fim de semana/
  feriado, próximo dia útil). Apuração no PGDAS-D.
- O valor do DAS é **provisão** — "validar com a Contabilizei antes de pagar".

## Falhas de conector

Não há conector de Bling/marketplace: o fluxo depende dos relatórios que o JhEY
manda. Se faltar o relatório do **Bling**, pare — a conciliação precisa dele como
fonte de verdade. Se faltar um **repasse** (ML, Shopee ou NuvemPago), rode com os
que houver e anote "repasse [canal] não enviado — pulado da conciliação". Se
faltarem todos os repasses, rode só com o Bling e sinalize.

## Gates de aprovação

- **Nunca corrija pendências automaticamente.** Mostre a pendência, recomende a
  ação, espere o JhEY.
- **Nunca emita/cancele NF nem altere o Bling sem confirmação.** Mostre os
  registros lado a lado.
- **Imposto/folha são provisão** — sempre "validar com a Contabilizei antes de
  pagar/declarar".
- **Salvar o pacote é automático** — vai pro Drive do JhEY.

## Saída

Encerre com um parágrafo de recap: faturamento líquido, margem, pendências
restantes (se houver), caminhos dos arquivos salvos, e os prazos do dia 5
(Contabilizei) e dia 20 (DAS). Se sobraram pendências, liste-as.
