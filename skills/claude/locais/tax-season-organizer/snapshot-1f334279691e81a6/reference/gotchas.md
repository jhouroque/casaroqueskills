# Pegadinhas (fiscal Casa Roque · Simples Nacional)

Erros comuns e como evitá-los. Padrão Errado / Certo.

---

## Apurar o DAS sobre o RBT12 errado

**Por que importa:** a alíquota efetiva depende do **RBT12** (receita bruta dos 12
meses anteriores). Usar o faturamento do mês como se fosse o RBT12, ou o RBT12
desatualizado, joga a empresa na faixa errada e erra o DAS.

**ERRADO:** aplicar a alíquota cheia da faixa direto sobre o faturamento do mês.
```
Faturamento de maio: R$ 78.000,00 × 10,70% = R$ 8.346,00  ← errado (ignora a PD)
```

**CERTO:** calcular a **efetiva** com a fórmula e o RBT12 correto.
```
Efetiva = (RBT12 × 10,70% − 22.500) / RBT12 = 8,20% (com RBT12 = 900 mil)
DAS = 78.000 × 8,20% = R$ 6.396,00  (provisão)
```
Recalcule a efetiva todo mês com o RBT12 atualizado. A Contabilizei fecha no PGDAS-D.

---

## Confundir alíquota nominal com efetiva

**ERRADO:** "Você está na 4ª faixa, então paga 10,70%."

**CERTO:** "Faixa 4ª, nominal 10,70%, mas a **efetiva** (depois da parcela a
deduzir) fica ~8–10% conforme o RBT12. O número do mês é provisão — a Contabilizei
confirma no PGDAS-D."

---

## Esquecer o sublimite de ICMS (R$ 3,6 mi)

**Por que importa:** acima de R$ 3,6 mi de RBT12 o ICMS sai do DAS e passa a ser
recolhido à parte (regra estadual). A Casa Roque está bem abaixo, mas no
crescimento do grupo isso muda a conta.

**ERRADO:** assumir que o DAS sempre engloba o ICMS, independente do faturamento.

**CERTO:** registrar que, **se** o RBT12 ultrapassar R$ 3,6 mi, o ICMS sai do DAS
e é recolhido separadamente — ponto a confirmar com a Contabilizei antes de a
empresa chegar lá.

---

## Tratar MEI como se nunca desenquadrasse

**Por que importa:** a Casa Weber é MEI (teto R$ 81 mil/ano) com meta interna de
R$ 87 mil/**mês**. É incompatível.

**ERRADO:** "A Casa Weber é MEI, então é só pagar o DAS-MEI de ~R$ 76,90/mês."

**CERTO:** "A meta da Casa Weber estoura o teto MEI (R$ 81 mil/ano) já no primeiro
mês. **Risco de desenquadramento** — avaliar mudança de regime com a Contabilizei.
Excesso até 20% (R$ 97.200) desenquadra no ano seguinte; acima, retroage." Alertar,
**sem afirmar irregularidade**.

---

## Chamar pagamento de costureira de "1099"

**Por que importa:** "1099-NEC", "W-9", "1099-K" são formulários dos EUA. **Não
existem no Brasil.**

**ERRADO:** "Gere um 1099 para a Cleusa e a Vanda."

**CERTO:** "Cleusa e Vanda são terceirizadas pagas por **recibo/RPA**. Reúna os
recibos do ano e informe à Contabilizei — é o que substitui qualquer
'comprovante de pagamento a autônomo'."

---

## Afirmar valores de recolhimento da reforma CBS/IBS

**Por que importa:** 2026 é ano-teste; CBS 0,9% + IBS 0,1% nas NF-e são
informativos/compensáveis, sem aumento de carga. O impacto definitivo para o
Simples depende de regra ainda em implantação.

**ERRADO:** "Você vai pagar 1% a mais de CBS/IBS este ano."

**CERTO:** "As NF-e já trazem CBS 0,9% + IBS 0,1% (informativo/compensável em
2026). **Confirmar com a Contabilizei** o impacto para empresa do Simples e o
cronograma dos campos — não afirmar valor de recolhimento."

---

## Dar conselho fiscal no lugar da Contabilizei

**Por que importa:** a skill prepara material; quem decide/declara é a Contabilizei.

**ERRADO:** "Migre a Casa Weber para Simples já que vale mais a pena."

**CERTO:** "A Contabilizei pode avaliar migrar a Casa Weber de MEI para Simples
dado o faturamento projetado — isso muda a carga e as obrigações. Trago os números;
a decisão e a declaração são com o contador."

A skill levanta as opções; a Contabilizei aconselha e transmite.

---

## Pagar o DAS sem validar

**ERRADO:** "Seu DAS é R$ 6.396,00, pode pagar."

**CERTO:** "Provisão do DAS ≈ R$ 6.396,00 (vence 22/06). É estimativa — **valide
com a Contabilizei** (PGDAS-D) antes de pagar; o valor oficial sai da apuração
dela."
