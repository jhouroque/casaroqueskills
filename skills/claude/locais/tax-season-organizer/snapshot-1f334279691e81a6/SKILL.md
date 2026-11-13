---
name: tax-season-organizer
description: >
  Organiza obrigações fiscais da Casa Roque (Simples Nacional) — sempre como
  material de apoio para a Contabilizei, não como aconselhamento contábil. Dois
  modos: (1) apuração mensal / DAS — estima a alíquota efetiva do Simples (Anexo
  I) sobre o RBT12, calcula a provisão do DAS e lembra do vencimento dia 20 e do
  PGDAS-D; (2) fechamento anual — DEFIS, conferência de limites (Simples R$ 4,8
  mi; MEI R$ 81 mil para a Casa Weber), recibos das costureiras (RPA) e
  acompanhamento da reforma CBS/IBS. Monta o pacote de entrega para a Contabilizei.

  Dispare quando o JhEY mencionar: DAS, imposto do mês, quanto provisionar de
  imposto, alíquota do Simples, PGDAS-D, RBT12, DEFIS, fechamento anual, MEI,
  limite do Simples, recibo de costureira, ou "o contador pediu". Dispare também
  quando ele perguntar por faturamento/lucro num contexto de preocupação com o
  imposto.
---

# Organizador fiscal (Casa Roque · Simples Nacional)

> **Enquadramento:** esta skill produz material de apoio para a **Contabilizei**,
> não aconselhamento contábil. Diga isso cedo e declare cada premissa para o
> contador ajustar. Todo valor de DAS/imposto é **provisão** — "validar com a
> Contabilizei antes de pagar/declarar".

> A Casa Roque não tem conector de Bling nem de Contabilizei. Os dados de
> faturamento e RBT12 vêm de relatórios que o JhEY exporta do Bling ou de
> extratos/declarações da Contabilizei. Quando faltar, peça o relatório.

## Início rápido

Identifique o modo, peça/puxe os dados, calcule ou compile, e entregue um
documento estruturado que a Contabilizei usa direto.

```
JhEY: "quanto vou pagar de DAS esse mês?"
→ Pedir o faturamento do mês (Bling) e o RBT12 (soma dos últimos 12 meses)
→ Calcular a alíquota efetiva (Anexo I) e a provisão do DAS
→ Mostrar o valor estimado, o vencimento (dia 20) e as premissas
→ Saída: "DAS de maio (vence 22/06) ≈ R$ X — provisão, confirmar com a Contabilizei"

JhEY: "o contador pediu o fechamento anual / DEFIS"
→ Compilar faturamento mês a mês do ano + RBT12 acumulado
→ Conferir limites (Simples R$ 4,8 mi; MEI R$ 81 mil p/ Casa Weber)
→ Reunir recibos das costureiras (RPA) e acompanhamento CBS/IBS
→ Saída: pacote de entrega para a Contabilizei (DEFIS + checagens)
```

## Determinar o modo

Leia a mensagem e o contexto para escolher o caminho:

- **Apuração mensal / DAS** — palavras-chave: DAS, imposto do mês, quanto
  provisionar, alíquota efetiva, RBT12, PGDAS-D, vencimento dia 20.
- **Fechamento anual** — palavras-chave: DEFIS, fechamento anual, declaração
  anual, limite do Simples, desenquadramento, MEI (Casa Weber), recibos do ano,
  "o contador pediu".

Se a intenção estiver ambígua, pergunte: "É a apuração do DAS deste mês, ou o
fechamento anual (DEFIS + limites) que a Contabilizei pediu?"

---

## Modo 1: Apuração mensal / DAS

### 1. Reunir o faturamento e o RBT12

Peça (ou puxe do relatório do Bling):
- **Faturamento do mês de apuração** (receita bruta do mês — soma das NFs)
- **RBT12** = receita bruta acumulada dos **últimos 12 meses** (anteriores ao mês
  de apuração). Se o JhEY não tiver o número fechado, peça os faturamentos
  mensais dos últimos 12 meses e some.

> A Casa Roque fatura ~R$ 900 mil/ano → cai na **4ª faixa** do Anexo I, alíquota
> efetiva **~10%** (bate com o registro). Ver premissas e fórmula em
> [reference/calculation-assumptions.md](reference/calculation-assumptions.md).

### 2. Calcular a alíquota efetiva e a provisão do DAS

Anexo I (comércio). **Alíquota efetiva = (RBT12 × alíquota nominal − PD) / RBT12**,
onde PD é a parcela a deduzir da faixa. Depois: **DAS do mês ≈ faturamento do mês
× alíquota efetiva**.

A tabela de faixas, alíquotas nominais e parcelas a deduzir está em
[reference/calculation-assumptions.md](reference/calculation-assumptions.md).

Passos:
1. Localize a faixa pelo RBT12.
2. Calcule a alíquota efetiva com a fórmula.
3. Multiplique pelo faturamento do mês → provisão do DAS.
4. **Sublimite ICMS/ISS (R$ 3,6 mi):** a Casa Roque está bem abaixo, mas registre
   que acima do sublimite o ICMS sai do DAS e é recolhido à parte (ponto de
   atenção para o crescimento; confirmar com a Contabilizei).

### 3. Declarar premissas e entregar

Estruture a saída como documento, nesta ordem:

1. **Cabeçalho** — H2 "Apuração do DAS" + mês e ano. Sublinha: data de preparo,
   "Para conferência da Contabilizei. Provisão — não pagar antes de validar."

2. **Base do mês** — faturamento do mês de apuração e RBT12 usado (com o período
   dos 12 meses).

3. **Faixa e alíquota** — faixa do Anexo I, alíquota nominal, parcela a deduzir e
   a **alíquota efetiva calculada** (mostre a conta).

4. **Provisão do DAS** — faturamento do mês × alíquota efetiva = valor estimado.

5. **Vencimento** — **dia 20** do mês seguinte (se cair em fim de semana/feriado,
   próximo dia útil). Cite a data concreta. Apuração no **PGDAS-D**.

6. **Provisão recomendada** — sugira separar o valor do DAS assim que o
   faturamento entra, para não faltar caixa no dia 20.

7. **Premissas** — Anexo I (comércio); RBT12 informado pelo JhEY/Bling; reforma
   CBS/IBS em 2026 é informativa/compensável (ver abaixo); valor é provisão, a
   Contabilizei fecha no PGDAS-D.

> ⚠️ **Reforma tributária 2026 (ano-teste):** as NF-e já trazem **CBS 0,9% + IBS
> 0,1%** (campos vCBS, vIBS etc.). Em 2026 é informativo/compensável, sem aumento
> de carga. **Confirmar com a Contabilizei** o impacto específico para empresa do
> Simples — não afirmar valor de recolhimento.

---

## Modo 2: Fechamento anual (DEFIS + limites + RPA)

### 1. Compilar o faturamento do ano

Peça (ou puxe do Bling) o **faturamento mês a mês do ano-calendário** e o RBT12
acumulado. Some por canal (ML, Shopee, site) se útil para a Contabilizei.

Se o Bling não estiver à mão, peça ao JhEY o relatório anual de faturamento ou
os extratos que a Contabilizei já tenha.

### 2. Conferir os limites

- **Teto do Simples: R$ 4,8 mi/ano.** A Casa Roque (~R$ 900 mil) está confortável;
  registre a folga. Sinalize se a projeção do grupo se aproximar do teto.
- **MEI (Casa Weber): teto R$ 81 mil/ano (R$ 6.750/mês).** ⚠️ A meta interna da
  Casa Weber é R$ 87 mil/**mês**, **incompatível com MEI**. Sinalize o **risco de
  desenquadramento** — sem afirmar irregularidade; é alerta para o JhEY decidir
  migrar de regime com a Contabilizei. Excesso até 20% (R$ 97.200) desenquadra no
  ano seguinte; acima disso, retroage.

### 3. Recibos das costureiras (RPA) e contratados

- **Cleusa** (costureira geral) e **Vanda** (lençóis, R$ 2,00/lençol) são
  **terceirizadas, pagas por recibo/RPA**. **Não existe "1099" no Brasil** — o
  correto é manter os **recibos/RPA do ano** e informar à Contabilizei.
- Compile a lista de pagamentos do ano às costureiras (valor total por pessoa,
  datas). Marque recibos faltantes como pendência a regularizar antes do
  fechamento.
- Demais contratados/serviços do ano: reúna NFs de tomador e recibos.

### 4. Acompanhamento da reforma CBS/IBS

Registre, sem afirmar valores: em 2026 as NF-e trazem CBS 0,9% + IBS 0,1%
(informativo/compensável). Liste como item a **confirmar com a Contabilizei** no
fechamento: impacto para o Simples e cronograma de obrigatoriedade dos campos.

### 5. Entregar o pacote para a Contabilizei

Estruture a saída como documento:

1. **Cabeçalho** — H2 "Fechamento anual [ano] — apoio à Contabilizei". Sublinha:
   data de preparo, "Para conferência e DEFIS pela Contabilizei. Não é
   declaração final."

2. **Resumo** — faturamento total do ano, RBT12 de dezembro, faixa do Anexo I,
   número de meses com NF emitida, total de DAS provisionado vs pago (se houver).

3. **Faturamento mês a mês** — tabela: mês, faturamento, canal (se útil), DAS
   provisionado.

4. **Checagem de limites** — Simples (R$ 4,8 mi: folga atual) e MEI Casa Weber
   (R$ 81 mil: status e alerta de desenquadramento, se aplicável).

5. **Recibos das costureiras (RPA)** — tabela: pessoa, total pago no ano, recibos
   na mão (sim/falta), observação. Lista de recibos a regularizar.

6. **Reforma CBS/IBS** — item de acompanhamento a confirmar com a Contabilizei.

7. **Próximos passos para a Contabilizei** — entregar/transmitir DEFIS, confirmar
   enquadramento (Simples e MEI), validar recibos, conferir impacto CBS/IBS.

---

## Guard-rails

- **Não é aconselhamento contábil.** Abra todo entregável com: "Material de apoio
  para a Contabilizei — não é aconselhamento contábil." No cabeçalho, não só no chat.
- **Todo valor de DAS/imposto é provisão.** "Validar com a Contabilizei antes de
  pagar/declarar." A Contabilizei fecha no PGDAS-D / DEFIS.
- **Declare cada premissa.** RBT12 usado, faixa, alíquota efetiva — dê as alavancas
  para o contador ajustar.
- **MEI Casa Weber:** alerte risco de desenquadramento; **não afirme
  irregularidade**.
- **Costureiras = RPA/recibo**, nunca "1099" (não existe no Brasil).
- **Não transmita nada.** PGDAS-D e DEFIS são feitos/validados pela Contabilizei.

## Arquivos de referência

- [reference/calculation-assumptions.md](reference/calculation-assumptions.md) —
  premissas verificadas: Anexo I (faixas, alíquotas, PD), fórmula da efetiva, DAS
  dia 20, MEI, FGTS — com a ressalva de validar com a Contabilizei
- [reference/connector-queries.md](reference/connector-queries.md) — quais
  relatórios pedir do Bling/Contabilizei (faturamento mensal, RBT12, NFs)
- [reference/gotchas.md](reference/gotchas.md) — pegadinhas BR (RBT12, sublimite
  ICMS, MEI desenquadramento, reforma 2026)
- [reference/examples/quarterly-estimate.md](reference/examples/quarterly-estimate.md)
  — exemplo de apuração mensal do DAS da Casa Roque
- [reference/examples/year-end-1099.md](reference/examples/year-end-1099.md) —
  exemplo de fechamento anual + DEFIS + checagem MEI
