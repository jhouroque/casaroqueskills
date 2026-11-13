---
name: tax-prep
description: Prepara material fiscal da Casa Roque — apuração mensal do DAS (Simples Nacional) ou fechamento anual (DEFIS) — e monta o pacote de entrega para a Contabilizei. Gatilhos: "imposto", "DAS", "o contador pediu", "DEFIS". Aceita argumentos opcionais de modo e ano.
allowed-tools: Read, WebFetch, Bash
---

Roda o fluxo fiscal usando a skill `tax-season-organizer`. Aja imediatamente — o
JhEY digitou /tax-prep, então pule a fase de descoberta.

Argumentos:
- `--modo` (default: inferir pela data — nos primeiros dias do mês até o dia 20,
  default `das`; em janeiro, default `anual`) — `das` para apuração mensal do DAS,
  `anual` para fechamento anual + DEFIS
- `--ano` (default: ano atual)

**Enquadramento:** abra todo entregável com "Material de apoio para a Contabilizei
— não é aconselhamento contábil." Todo valor de imposto é **provisão** — "validar
com a Contabilizei antes de pagar/declarar".

> Sem conector de Bling/Contabilizei: peça os relatórios (faturamento do mês,
> RBT12, NFs) ao JhEY.

## Passo 1 — Determinar o modo

Se `--modo` não foi passado:
1. Veja a data. Em janeiro, default `anual`. Caso contrário, default `das`.
2. Confirme com o JhEY: "Pela época do ano, vou preparar a [apuração do DAS /
   fechamento anual]. Quer outra coisa?"

## Passo 2 — Apuração mensal do DAS (se modo inclui `das`)

1. Peça o **faturamento do mês** (Bling) e o **RBT12** (12 meses anteriores). Se o
   RBT12 não estiver fechado, peça os faturamentos mensais e some — não invente.
2. Localize a faixa do **Anexo I** pelo RBT12 e calcule a **alíquota efetiva**:
   `(RBT12 × nominal − PD) / RBT12`.
3. Provisão do DAS = faturamento do mês × efetiva.
4. Informe o **vencimento (dia 20** do mês seguinte; próximo dia útil se cair em
   fim de semana/feriado) e a apuração no **PGDAS-D**.
5. Declare as premissas (RBT12 usado, faixa, efetiva) e marque como **provisão**.

## Passo 3 — Fechamento anual (se modo inclui `anual`)

1. Compile o **faturamento mês a mês** do ano (Bling) e o RBT12 de dezembro.
2. Confira limites: **Simples R$ 4,8 mi/ano**; **MEI R$ 81 mil/ano** (Casa Weber —
   alerte risco de desenquadramento, sem afirmar irregularidade).
3. Reúna os **recibos/RPA** das costureiras (Cleusa, Vanda) do ano; marque
   faltantes. **Não existe "1099" no Brasil.**
4. Registre o acompanhamento da **reforma CBS/IBS** (informativo/compensável em
   2026; confirmar impacto com a Contabilizei).
5. Monte o pacote de entrega para a Contabilizei (DEFIS + checagens).

## Gates de aprovação

- **Não é aconselhamento contábil.** Diga isso no cabeçalho de toda saída.
- **Todo valor é provisão.** Validar com a Contabilizei antes de pagar/declarar.
- **Declare cada premissa.** RBT12, faixa, efetiva — dê as alavancas ao contador.
- **MEI Casa Weber:** alerte risco; não afirme irregularidade.
- **Costureiras = RPA/recibo**, nunca "1099".
- **Não transmita nada.** PGDAS-D e DEFIS são feitos/validados pela Contabilizei.

## Saída

Encerre com um checklist de próximos passos para a Contabilizei: relatórios a
enviar (até dia 5), DAS a validar (vence dia 20), recibos a regularizar, DEFIS a
transmitir, impacto CBS/IBS a confirmar.
