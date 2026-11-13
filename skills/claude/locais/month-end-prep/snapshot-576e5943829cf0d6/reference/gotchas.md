# Pegadinhas (fechamento Casa Roque)

Erros comuns e casos de borda no fechamento mensal. Cada item tem o padrão, por
que importa, e um exemplo Errado / Certo.

---

## Pegadinha: comparar valor bruto do Bling com repasse líquido

**Por que importa:** o Bling mostra o **bruto** da venda; o extrato do marketplace
mostra o **líquido** (já menos comissão ~16%, taxas, frete e dívida ML). Comparar
bruto com líquido sempre acusa "diferença" igual às deduções — e não é erro.

### ✗ Errado

> Divergência: venda no Bling R$ 199,00, repasse R$ 160,16 — diferença R$ 38,84.
> Sinalizado como erro de conciliação.

Os R$ 38,84 são a comissão de 16% + taxa. É esperado e correto.

### ✓ Certo

Compare contra o **líquido esperado**: `bruto − 16% − frete − dívida ML`. Se o
líquido do extrato bater nessa conta (diferença < R$ 1,00), marque CONCILIADO.
Registre comissão/taxas como deduções esperadas, não como divergência.

---

## Pegadinha: tratar devolução/estorno como repasse faltante

**Por que importa:** uma devolução aparece como valor negativo no extrato. Se você
a tratar como saída não casada, sinaliza uma devolução legítima como problema.

### ✗ Errado

> Sinalizado: saída de −R$ 89,00 no ML em 18/05 sem pedido correspondente.
> Possível lançamento faltante.

Os −R$ 89,00 são um reembolso ao cliente. Deve casar com a NF de devolução /
pedido original, não com uma venda nova.

### ✓ Certo

Separe entradas (positivas) de saídas (negativas) antes de conciliar. Case
negativos contra NFs de devolução / pedidos originais. Só sinalize um negativo
não casado se não existir pedido original no Bling.

---

## Pegadinha: contar a dívida do ML como despesa do mês

**Por que importa:** o ML desconta a parcela da dívida (Casa Roque ~R$ 80 mil,
Casa Weber ~R$ 75 mil) automaticamente no repasse. É **abatimento de passivo**,
não despesa operacional. Jogar isso como despesa no DRE afunda o resultado e
distorce a margem.

### ✗ Errado

> DRE: (−) Dívida ML R$ 6.800,00 lançado junto com folha e Ads como despesa.
> Resultado do mês caiu para perto de zero.

### ✓ Certo

A dívida descontada reduz o que **entrou em caixa**, mas no DRE ela fica em
**nota** (abatimento de passivo). O resultado operacional do mês não muda por
causa dela. Mostre o caixa real separadamente se o JhEY quiser ver a liberação
líquida.

---

## Pegadinha: misturar regime de caixa com competência

**Por que importa:** a venda 3x do site (NuvemPago) e o valor "a liberar" do ML/
Shopee criam descasamento entre **quando a venda aconteceu** (competência) e
**quando o dinheiro caiu** (caixa). Tratar tudo como caixa subestima o faturamento
do mês; tratar tudo como competência infla o caixa.

### ✗ Errado

> Faturamento de maio = só o que caiu na conta em maio (R$ 61 mil). Ignora as
> vendas de maio que liberam em junho.

### ✓ Certo

Para o **DRE/faturamento**, use a competência: vendas com NF emitida no mês (Bling),
independente de quando o repasse libera. Para **fluxo de caixa**, use as
liberações efetivas. Diga ao JhEY qual visão está sendo mostrada. O fechamento
oficial é por competência (data da NF); o caixa é visão complementar.

---

## Pegadinha: sinalizar kit/combo como duplicidade

**Por que importa:** um kit (ninho + trocador + lençol) pode sair como várias
linhas com mesmo pedido e data, valores diferentes. Sinalizar como duplicado
manda o JhEY caçar fantasma.

### ✗ Errado

> Duplicado: pedido #4471 R$ 120,00 e pedido #4471 R$ 85,00 em 12/05 — mesmo
> pedido, mesma data.

As duas linhas têm o mesmo `numero_pedido` — são itens do mesmo kit de R$ 205,00.

### ✓ Certo

Antes de sinalizar duplicados, agrupe por `numero_pedido`. Só compare pedidos com
IDs distintos. Itens do mesmo pedido nunca são duplicidade.

---

## Pegadinha: fechar com pedido sem NF em aberto

**Por que importa:** todo pedido precisa de NF (POP 1). Fechar o mês e enviar ao
Contabilizei com pedido sem NF deixa furo fiscal e atrasa o envio do dia 5.

### ✗ Errado

> O JhEY não respondeu sobre os 8 pedidos sem NF. Gerando o pacote de fechamento
> assim mesmo pra ele ter algo.

### ✓ Certo

Segure no gate do Passo 6 até o JhEY resolver cada pedido sem NF — ou emitindo a
NF no Bling, ou marcando "deixa pra depois" de forma explícita. Pedidos sem NF
adiados devem aparecer na aba Pendencias, nunca sumir em silêncio. Lembre que o
**envio ao Contabilizei vence dia 5** e o **DAS vence dia 20**.
