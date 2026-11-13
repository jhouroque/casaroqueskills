# Guia de relatórios a pedir (Bling / Contabilizei)

Não há conector de Bling nem de Contabilizei. Este guia diz **quais relatórios
pedir ao JhEY** (ou onde buscar) para cada modo.

---

## Modo apuração mensal / DAS

### Faturamento do mês (Bling)

Peça o relatório de **vendas / notas fiscais emitidas** do Bling, filtrado pelo
**mês de apuração** (primeiro ao último dia).

Capturar:
- `faturamento_bruto_mes` — soma das NFs autorizadas no mês
- Quebra por canal (ML, Shopee, site) — útil para a Contabilizei, opcional p/ o DAS
- Devoluções no mês (CFOP de retorno) — reduzem a receita bruta tributável

> O DAS incide sobre a **receita bruta** do mês. Confirme com a Contabilizei o
> tratamento de devoluções/cancelamentos na base.

### RBT12 (receita bruta dos 12 meses)

Precisa do **RBT12** = soma da receita bruta dos **12 meses anteriores** ao mês de
apuração. Duas formas:
1. Pedir o número fechado à Contabilizei (extrato do PGDAS-D traz o RBT12), ou
2. Pedir ao JhEY os **faturamentos mensais dos últimos 12 meses** (Bling) e somar.

Se o RBT12 não estiver disponível, **não invente** — peça. É o insumo que define a
faixa e a alíquota efetiva.

---

## Modo fechamento anual (DEFIS)

### Faturamento mês a mês do ano (Bling)

Peça o relatório **anual** de vendas/NFs do Bling, do ano-calendário inteiro.

Capturar:
- Faturamento por mês (12 linhas)
- Total do ano e RBT12 de dezembro
- Quebra por canal e por empresa (Casa Roque, Casa Lima, Casa Weber) se aplicável

### Pagamentos a costureiras / contratados (RPA)

Peça ao JhEY:
- Total pago no ano a **Cleusa** e **Vanda** (e demais terceirizados), com datas
- Os **recibos/RPA** correspondentes (arquivo/PDF)

Marque recibos faltantes como pendência. **Não existe "1099" no Brasil** — o que a
Contabilizei precisa são os recibos/RPA.

### Dados da Contabilizei

Quando houver, peça ao JhEY:
- Extrato do **PGDAS-D** do ano (alíquotas efetivas mês a mês, RBT12)
- DAS pagos no ano (para conferir provisão x pago)
- Enquadramento atual (Simples — Anexo I; e MEI da Casa Weber)

---

## Fallback (sempre, pois não há conector)

Como Bling e Contabilizei não têm MCP, o fluxo **sempre** depende de exportações.
Peça de forma objetiva:

1. **Bling** → Relatórios → Vendas/Notas Fiscais → exportar CSV do período.
2. **Contabilizei** → extrato do PGDAS-D / DAS do período (PDF), se disponível.
3. **Recibos** das costureiras (PDF/foto) para o modo anual.

Ao ler CSVs, procure as colunas (nomes variam): `data_emissao`/`data`, `valor_total`/
`valor`, `canal`, `status_nf`, `cfop`. Se as colunas não baterem, peça ao JhEY para
identificar a coluna de valor e a de data.

> Em dúvida sobre RBT12, faixa ou base de cálculo: **pergunte ou marque
> `[confirmar]`** e valide com a Contabilizei. Nunca preencher número estimado como
> se fosse oficial.
