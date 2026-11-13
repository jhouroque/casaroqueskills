# Exemplo: Apuração mensal do DAS

> O nome do arquivo é mantido por compatibilidade. O conteúdo é um exemplo de
> **apuração mensal do DAS** da Casa Roque (Simples Nacional, Anexo I).

**Cenário:** o JhEY pergunta: "quanto vou pagar de DAS de maio?"

---

## Passo 1: Reunir faturamento do mês e RBT12

Do relatório de NFs do Bling (maio/2026):
- Faturamento bruto de maio: **R$ 78.000,00**

RBT12 (soma dos 12 meses anteriores, jun/2025 a mai/2026, do Bling/Contabilizei):
- RBT12: **R$ 900.000,00**

---

## Passo 2: Localizar a faixa e calcular a efetiva

RBT12 de R$ 900.000,00 → **4ª faixa** do Anexo I (R$ 720.000,01 a R$ 1.800.000,00).
- Alíquota nominal: **10,70%**
- Parcela a deduzir (PD): **R$ 22.500,00**

```
Alíquota efetiva = (RBT12 × nominal − PD) / RBT12
                 = (900.000,00 × 0,107 − 22.500,00) / 900.000,00
                 = (96.300,00 − 22.500,00) / 900.000,00
                 = 73.800,00 / 900.000,00
                 = 8,20%

DAS de maio (provisão) = 78.000,00 × 0,0820 = R$ 6.396,00
```

---

## Passo 3: Vencimento

DAS de maio vence no **dia 20 de junho**. Em 2026, 20/06 é sábado → **vence no
próximo dia útil, 22/06/2026**. Apuração no PGDAS-D (Contabilizei).

---

## Passo 4: Saída entregue ao JhEY

```
## Apuração do DAS — maio/2026
Preparado em 31/05/2026 · Para conferência da Contabilizei · Provisão — não pagar antes de validar

**Faturamento de maio (Bling):** R$ 78.000,00
**RBT12 (jun/2025–mai/2026):** R$ 900.000,00
**Faixa (Anexo I, comércio):** 4ª faixa

### Alíquota efetiva
(900.000,00 × 10,70% − 22.500,00) / 900.000,00 = **8,20%**

### Provisão do DAS
R$ 78.000,00 × 8,20% = **R$ 6.396,00**

### Vencimento
Dia 20 do mês seguinte → 20/06/2026 cai no sábado → **vence 22/06/2026** (próximo dia útil).
Apuração no PGDAS-D.

### Recomendação
Separe R$ 6.396,00 do caixa assim que os repasses entrarem, para não faltar no dia 22/06.

### Premissas — conferir com a Contabilizei
- Anexo I (comércio); efetiva recalculada a cada mês com o RBT12 atualizado
- RBT12 informado pelo Bling/Contabilizei (não estimado)
- Devoluções/cancelamentos: confirmar tratamento na base com a Contabilizei
- Reforma CBS/IBS (2026, ano-teste): informativa/compensável — confirmar impacto p/ Simples
- Valor é **provisão** — a Contabilizei fecha no PGDAS-D
```

---

## Por que este exemplo funciona

- Usa a **fórmula oficial** da efetiva (Anexo I), não um número chutado
- Mostra a conta passo a passo (RBT12, nominal, PD)
- Acerta o **vencimento dia 20** e trata o caso de cair no fim de semana
- Marca tudo como **provisão a validar com a Contabilizei**
- Recomenda separar o caixa — útil pro fluxo do JhEY
