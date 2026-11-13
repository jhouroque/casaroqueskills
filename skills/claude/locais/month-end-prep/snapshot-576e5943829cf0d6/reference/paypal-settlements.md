# Repasses de marketplace — referência

> O nome do arquivo é mantido por compatibilidade. O conteúdo trata dos
> **repasses de Mercado Livre/Mercado Pago, Shopee e NuvemPago** (liberação,
> comissão, taxas, antecipação). Não há conector — trabalhe com os extratos/
> relatórios que o JhEY exporta.

## Conteúdo

- [Mercado Livre / Mercado Pago](#mercado-livre--mercado-pago)
- [Shopee](#shopee)
- [NuvemPago (site)](#nuvempago-site)
- [Lógica de conciliação (todos os canais)](#lógica-de-conciliação-todos-os-canais)

---

## Mercado Livre / Mercado Pago

O extrato de repasses do ML (liberações no Mercado Pago) traz, por venda/pedido:

| Campo | Observações |
|---|---|
| `id_operacao` / `id_venda` | ID da venda no ML |
| `data` | Data da operação |
| `valor_bruto` | Valor da venda (entra positivo) |
| `comissao` | Tarifa de venda do ML (~**16%**) — sai como negativo |
| `tarifa_frete` / `custo_envio` | Parcela de frete (Mercado Envios) |
| `valor_liquido` | O que efetivamente cai (bruto − comissão − frete − dívida) |
| `status` | Liberado, A liberar, Em mediação |

**Liberação x venda:** o ML segura o valor até a entrega/prazo. Uma venda do dia
28/04 pode liberar só em 03/05. Concilie pela **data de liberação** contra o que
entrou em caixa, não pela data da venda.

**Dívida ML descontada:** a Casa Roque (~R$ 80 mil) e a Casa Weber (~R$ 75 mil)
têm dívida abatida automaticamente no repasse. Esse desconto reduz o líquido que
cai, mas é **abatimento de passivo**, não despesa do mês — registre separado (ver
SKILL Passo 5 e gotchas.md).

**Estornos/devoluções:** aparecem como valores negativos. Devem casar com a NF de
devolução / pedido original — não sinalize um estorno como repasse faltante a
menos que não exista pedido original correspondente.

**Antecipação:** se o JhEY antecipou recebíveis (receber antes da liberação
normal), há um custo de antecipação descontado. Registre como taxa, separado da
comissão.

**Em mediação / a liberar:** vendas nesses status ainda não caíram. Anote à parte
— entram no repasse do mês seguinte.

---

## Shopee

A Shopee chama de **repasse/liberação por pedido**. Campos típicos do relatório:

| Campo | Observações |
|---|---|
| `id_pedido` | ID do pedido na Shopee |
| `data_repasse` | Data em que o valor foi liberado |
| `valor_bruto` | Valor da venda |
| `comissao` + `taxa_servico` | Tarifas da Shopee (~**16%** no total de referência) |
| `taxa_frete` | Frete subsidiado/cobrado |
| `valor_liquido` | O que cai após tarifas e frete |
| `status` | Concluído (use só este para conciliar) |

**Tarifas antes do repasse:** a Shopee desconta comissão + taxa de serviço antes
de liberar, então `valor_liquido` já é líquido. Ao conciliar, compare contra o
que entrou em caixa, não contra o bruto do Bling.

**Campanhas/cupons Shopee:** descontos de campanha (Frete Grátis, cupom da loja)
reduzem o líquido. Some-os como dedução, separado da comissão.

---

## NuvemPago (site)

O NuvemPago processa os pagamentos do site (NuvemShop), com parcelamento **3x sem
juros** e desconto no Pix. Campos típicos:

| Campo | Observações |
|---|---|
| `id_transacao` | ID da transação |
| `data_liberacao` | Data prevista de liberação (varia com a parcela) |
| `valor_bruto` | Valor da venda |
| `taxa` | Taxa de processamento (cartão/Pix/boleto) |
| `parcelas` | Número de parcelas (3x libera ao longo dos meses) |
| `valor_liquido` | Líquido por liberação |
| `status` | Aprovado, Pago, Estornado |

**Comissão de marketplace = 0% no site.** A dedução aqui é a **taxa do NuvemPago**
e o efeito do **parcelamento** (uma venda 3x não cai inteira no mês — entram as
parcelas conforme liberação). Pix tem desconto na ponta e taxa menor; boleto cai
após compensação.

**Frete grátis SP > R$ 199:** quando o frete é por conta da loja, some-o como
custo de frete (não some como dedução do NuvemPago).

---

## Lógica de conciliação (todos os canais)

Use esta lógica para casar cada repasse contra o que entrou em caixa / o pedido
do Bling:

```
para cada repasse no mês de referência:
    achar o pedido no Bling onde:
        |valor_bruto_repasse − valor_bruto_bling| < R$ 1,00
        E |data_repasse − data_pedido| <= 2 dias

    se casou:
        marcar CONCILIADO
        registrar comissão/taxas/frete/dívida como deduções esperadas
    senão, se casou só o valor (data diferente):
        sinalizar DIVERGENCIA_DATA (geralmente timing de liberação — baixa prioridade)
    senão, se o repasse não casou com nenhum pedido:
        sinalizar VENDA_SEM_NF_NO_BLING
    senão, se o pedido do Bling não casou com nenhum repasse:
        sinalizar A_LIBERAR (ML/Shopee seguram; site libera por parcela — não é erro)
```

**Multicanal:** rode a lógica por canal (ML, Shopee, NuvemPago) e depois agregue
as deduções. Um pedido do Bling sem repasse no ML pode ter sido vendido na Shopee
— só sinalize depois de checar todos os canais.

**Conferência rápida do líquido esperado:** para uma venda de marketplace,
`líquido ≈ bruto − 16% comissão − frete − parcela dívida ML`. Se o líquido do
extrato bater nessa conta, está conciliado mesmo havendo "diferença" vs o bruto.
