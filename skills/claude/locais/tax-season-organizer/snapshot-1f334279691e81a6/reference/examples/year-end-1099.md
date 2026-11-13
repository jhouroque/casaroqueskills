# Exemplo: Fechamento anual + DEFIS + checagem MEI

> O nome do arquivo é mantido por compatibilidade. O conteúdo é um exemplo de
> **fechamento anual** da Casa Roque para a Contabilizei (DEFIS + limites + RPA).
> Não existe "1099" no Brasil — o equivalente são os recibos/RPA das costureiras.

**Cenário:** o JhEY diz: "a Contabilizei pediu o fechamento do ano e os recibos.
Monta pra mim."

---

## Passo 1: Compilar o faturamento do ano (Bling)

Faturamento 2025 da Casa Roque, mês a mês (exemplo ilustrativo):

| Mês | Faturamento | Canal predominante |
|---|---|---|
| jan | R$ 68.200,00 | ML / site |
| fev | R$ 71.500,00 | ML / Shopee |
| mar | R$ 74.900,00 | ML / Shopee |
| abr | R$ 72.100,00 | ML |
| mai | R$ 78.000,00 | ML / site (Dia das Mães) |
| jun | R$ 70.300,00 | ML |
| jul | R$ 73.400,00 | Shopee / site |
| ago | R$ 75.100,00 | ML / Shopee |
| set | R$ 76.800,00 | ML |
| out | R$ 79.200,00 | ML / site |
| nov | R$ 92.500,00 | ML / Shopee (Black Friday) |
| dez | R$ 88.000,00 | ML / site (Natal) |
| **Total** | **R$ 920.000,00** | — |

RBT12 de dezembro: **R$ 920.000,00** → **4ª faixa** do Anexo I.

---

## Passo 2: Conferir limites

- **Teto do Simples (R$ 4,8 mi):** faturamento de R$ 920 mil → folga grande
  (~19% do teto). Sem risco de desenquadramento do Simples este ano.
- **MEI — Casa Weber (teto R$ 81 mil/ano):** ⚠️ a meta interna da Casa Weber é
  R$ 87 mil/**mês**. Se a operação se aproximar disso, **estoura o teto MEI no
  primeiro mês**. Alerta de **risco de desenquadramento** — decisão de migrar de
  regime a tomar com a Contabilizei. (Não afirmar irregularidade; é alerta.)

---

## Passo 3: Recibos das costureiras (RPA)

Pagamentos 2025 (exemplo):

| Pessoa | Total pago no ano | Recibos na mão? | Observação |
|---|---|---|---|
| Cleusa (costureira geral) | R$ 14.400,00 | ⚠️ Faltam 2 meses | Trocadores, ninhos, kits |
| Vanda (lençóis) | R$ 6.240,00 | ✅ Completo | R$ 2,00/lençol |

Recibos a regularizar: **Cleusa — meses de set e out**. Pedir/emitir RPA antes de
entregar à Contabilizei.

---

## Passo 4: Saída entregue ao JhEY

```
## Fechamento anual 2025 — apoio à Contabilizei
Preparado em 10/01/2026 · Para conferência e DEFIS pela Contabilizei · Não é declaração final

### Resumo
- Faturamento total 2025: R$ 920.000,00
- RBT12 (dez/2025): R$ 920.000,00 → 4ª faixa (Anexo I)
- Meses com NF emitida: 12
- Status Simples: folga vs teto R$ 4,8 mi (sem risco de desenquadramento)

### Faturamento mês a mês
[tabela do Passo 1]

### Checagem de limites
- Simples (R$ 4,8 mi/ano): R$ 920 mil — confortável
- MEI Casa Weber (R$ 81 mil/ano): ⚠️ meta de R$ 87 mil/mês incompatível com MEI —
  risco de desenquadramento. Avaliar mudança de regime com a Contabilizei.

### Recibos das costureiras (RPA)
| Pessoa | Total ano | Recibos | Ação |
|---|---|---|---|
| Cleusa | R$ 14.400,00 | Faltam set/out | Regularizar RPA antes de entregar |
| Vanda | R$ 6.240,00 | Completo | — |

### Reforma CBS/IBS (2026, ano-teste)
NF-e já trazem CBS 0,9% + IBS 0,1% (informativo/compensável). Confirmar com a
Contabilizei o impacto para o Simples e o cronograma dos campos.

### Próximos passos para a Contabilizei
- [ ] Transmitir a DEFIS 2025
- [ ] Confirmar enquadramento Simples (Anexo I) e MEI (Casa Weber)
- [ ] Validar recibos/RPA (regularizar Cleusa set/out)
- [ ] Conferir impacto da reforma CBS/IBS para o Simples
```

---

## Por que este exemplo funciona

- Compila o ano inteiro com RBT12 e faixa corretos (Anexo I)
- Aplica os limites reais: **Simples R$ 4,8 mi** e **MEI R$ 81 mil** (Casa Weber)
- Sinaliza o **risco de desenquadramento MEI** sem afirmar irregularidade
- Trata as costureiras como **RPA/recibo**, nunca "1099"
- Deixa a **DEFIS e a validação final com a Contabilizei** — a skill só prepara
