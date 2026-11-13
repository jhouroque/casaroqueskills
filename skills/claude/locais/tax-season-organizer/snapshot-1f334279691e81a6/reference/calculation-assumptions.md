# Premissas de cálculo (Simples Nacional)

Documenta a matemática e as premissas usadas na apuração do DAS. Sempre exiba as
premissas na saída para a Contabilizei ajustar. **Todo valor é provisão — validar
com a Contabilizei antes de pagar/declarar.** Estes valores são de 2026 e mudam;
ver CONTEXTO §10.

---

## Simples Nacional — Anexo I (comércio)

A Casa Roque é optante do Simples Nacional, atividade de **comércio** (Anexo I).
O DAS unifica os tributos num único pagamento mensal, apurado no **PGDAS-D**.

### Tabela de faixas (Anexo I, 2026)

| Faixa | RBT12 (receita bruta 12 meses) | Alíquota nominal | Parcela a deduzir (PD) |
|---|---|---|---|
| 1ª | até R$ 180.000,00 | 4,00% | R$ 0,00 |
| 2ª | R$ 180.000,01 a R$ 360.000,00 | 7,30% | R$ 5.940,00 |
| 3ª | R$ 360.000,01 a R$ 720.000,00 | 9,50% | R$ 13.860,00 |
| 4ª | R$ 720.000,01 a R$ 1.800.000,00 | 10,70% | R$ 22.500,00 |
| 5ª | R$ 1.800.000,01 a R$ 3.600.000,00 | 14,30% | R$ 87.300,00 |
| 6ª | R$ 3.600.000,01 a R$ 4.800.000,00 | 19,00% | R$ 378.000,00 |

> A Casa Roque fatura ~R$ 900 mil/ano → **4ª faixa**. Alíquota nominal 10,70%,
> mas a **efetiva** fica ~10% por causa da parcela a deduzir (bate com o registro
> interno de ~10%).

### Fórmula da alíquota efetiva

```
Alíquota efetiva = (RBT12 × alíquota nominal − PD) / RBT12
DAS do mês       = faturamento do mês × alíquota efetiva
```

**Exemplo (4ª faixa):**
```
RBT12:               R$ 900.000,00
Alíquota nominal:    10,70%
Parcela a deduzir:   R$ 22.500,00

Efetiva = (900.000 × 0,107 − 22.500) / 900.000
        = (96.300 − 22.500) / 900.000
        = 73.800 / 900.000
        = 8,20%   ← efetiva (varia com o RBT12; ~8–11% na faixa)

Faturamento do mês:  R$ 78.000,00
DAS estimado:        78.000 × 0,0820 = R$ 6.396,00  (provisão)
```

> A efetiva sobe conforme o RBT12 cresce dentro da faixa. Recalcule a cada mês com
> o RBT12 atualizado. **A Contabilizei fecha o valor no PGDAS-D** — o cálculo aqui
> é provisão para o JhEY separar o caixa.

---

## Vencimento e apuração

| Item | Regra 2026 |
|---|---|
| **Vencimento do DAS** | **dia 20** do mês seguinte à apuração (se cair em fim de semana/feriado, próximo dia útil) |
| **Apuração** | **PGDAS-D** (feito/validado pela Contabilizei) |
| **Envio de NFs à Contabilizei** | até **dia 5** do mês seguinte |
| **DEFIS** | declaração anual do Simples (via Contabilizei) |
| **Teto do Simples** | R$ 4.800.000,00/ano |
| **Sublimite ICMS/ISS** | R$ 3.600.000,00 — acima, ICMS sai do DAS e é recolhido à parte |

---

## MEI (Casa Weber)

- **Teto:** R$ 81.000,00/ano (R$ 6.750,00/mês).
- **DAS-MEI comércio:** ≈ R$ 76,90/mês (R$ 75,90 INSS + R$ 1,00 ICMS) — valor fixo.
- **Excesso:** até 20% acima (R$ 97.200) → desenquadra no ano seguinte; acima
  disso → retroage ao início do ano.
- ⚠️ A meta interna da Casa Weber (R$ 87 mil/**mês**) é **incompatível com MEI**.
  Alerte risco de desenquadramento — **não afirme irregularidade**; é decisão de
  regime a tomar com a Contabilizei.

---

## Encargos de folha (referência — ver skill de folha)

Não fazem parte do DAS, mas entram no fechamento financeiro:
- **FGTS:** 8% sobre o salário bruto (depósito mensal) — Keila e Emerson (CLT).
- INSS, 13º (1ª parcela até 30/nov, 2ª até 20/dez), férias + 1/3.
- Costureiras (Cleusa, Vanda): **recibo/RPA**, não CLT, não MEI próprio aqui.

---

## Reforma tributária (2026 = ano-teste)

- NF-e já trazem **CBS 0,9% + IBS 0,1%** (campos vCBS, vIBS, pCBS, pIBS,
  cClassTrib, CST).
- Em 2026 é **informativo/compensável** com PIS/Cofins — sem aumento de carga.
- **Confirmar com a Contabilizei** o impacto específico para empresa do Simples e
  o cronograma de obrigatoriedade dos campos. **Não afirmar valores de
  recolhimento** — é acompanhamento.

---

## O que a provisão NÃO inclui

Liste sempre na saída:
- Eventual ICMS-ST/antecipação em compras (a depender do produto/fornecedor).
- Impacto definitivo da reforma CBS/IBS (a confirmar com a Contabilizei).
- Encargos de folha (FGTS, INSS, 13º, férias) — fora do DAS.
- Diferenças por exclusões/devoluções não lançadas ainda no Bling.

Estes itens podem mudar o número. Sinalize-os para a Contabilizei aplicar.

---

## Fontes (verificadas em jun/2026, CONTEXTO §10)

- Anexo I e DAS: Contabilizei, Receita Federal (Simples Nacional).
- MEI 2026: Contabilizei / Sebrae.
- Reforma CBS/IBS 2026: Receita Federal (orientações 2026), Câmara dos Deputados.

> Estes valores mudam. **Sempre validar com a Contabilizei** antes de pagar/declarar.
