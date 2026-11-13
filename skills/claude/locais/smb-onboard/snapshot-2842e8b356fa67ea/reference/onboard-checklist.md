# Checklist de configuração — Casa Roque

> O `CONTEXTO_CASA_ROQUE.md` **já existe**. Este checklist é de **confirmação e conexão**, não de entrevista do zero.

## Passo A — Confirmar o contexto (não re-entrevistar)

Leia o `CONTEXTO_CASA_ROQUE.md` e confirme com o JhEY só o que muda com frequência. Uma pergunta de cada vez:

1. **Equipe/folha.** "Mudou algo na folha? (Keila R$ 1.400/mês, Emerson R$ 1.400/mês, costureiras Cleusa e Vanda por demanda, dissídio de 6% pendente)"
2. **Metas.** "As metas seguem as mesmas? (faturamento grupo R$ 83,3 mil/mês, ticket R$ 71,63 → R$ 200, ROI > 3x, CPC < R$ 2,00)"
3. **Ferramentas.** "Continua tudo no Bling + marketplaces + site NuvemShop? Já decidiu qual assinatura eletrônica usa (Gov.br/Clicksign/D4Sign/ZapSign)?" `[confirmar]`
4. **Datas-chave.** "Calendário segue o mesmo? (NFs ao Contabilizei dia 5, salário Emerson dia 10, DAS dia 20)"

Atualize **só** os campos que mudaram. Mostre atual vs proposto antes de gravar.

---

## Passo B — Conectores do plugin (Google + Canva)

Os **únicos conectores deste plugin**. Conecte um de cada vez.

| Função | Conector | O que destrava (uma frase) |
|---|---|---|
| Inbox | **Gmail** | Lê threads de SAC/fornecedor e prepara rascunhos pra você enviar. |
| Agenda | **Google Agenda** | Puxa a reunião de segunda com o Thomas, o batimento de sexta e os prazos de folha/DAS. |
| Arquivos | **Google Drive** | Salva briefings, projeções e pacotes de fechamento. |
| Design | **Canva** | Gera os posts das campanhas a partir de um brief aprovado (casaroque.design). |

**Não há conector de Bling, ML, Shopee, NuvemShop, NuvemPago nem Contabilizei.** Não tente conectar — esses dados vêm de relatórios exportados (Passo C).

---

## Passo C — Exportações do Bling/marketplace (substituem o conector de ERP/pagamentos)

Ensine o JhEY a tirar cada relatório e diga qual skill precisa dele. As skills leem CSV/PDF/print.

| Relatório (de onde) | Formato | Skills que usam |
|---|---|---|
| **Vendas do período** (Bling ou ML/Shopee) | CSV/print | `business-pulse`, `sales-brief`, `friday-brief`, `margin-analyzer`, `quarterly-review` |
| **Contas a receber / a pagar** (Bling) | CSV/PDF | `cash-flow-snapshot`, `plan-payroll`, `invoice-chase`, `month-end-prep` |
| **Repasses / liberações** (Mercado Livre/Mercado Pago, Shopee) | CSV | `cash-flow-snapshot`, `plan-payroll`, `month-end-prep` |
| **Parcelas a receber** (NuvemPago, vendas 3x do site) | CSV | `cash-flow-snapshot`, `month-end-prep` |
| **Faturamento / NFs do mês** (Bling) | CSV/PDF | `tax-prep`, `month-end-prep` |
| **Relatório de tráfego** (Thomas, toda sexta) | print/PDF | `friday-brief`, `business-pulse` |
| **Perguntas / avaliações** (ML, Shopee) + WhatsApp | print/planilha | `lead-triage`, `call-list`, `customer-pulse-check` |

Frase-padrão quando faltar dado:
> "me manda o relatório de [X] do Bling (CSV) ou um print do ML/Shopee que eu fecho."

---

## Passo D — Provar valor com um relatório real

Assim que o JhEY anexar um relatório, rode a skill casada **na hora** (não espere a configuração toda):

1. Relatório de vendas → `business-pulse` ou `sales-brief`
2. Contas a receber/pagar → `cash-flow-snapshot`
3. Perguntas/avaliações → `lead-triage`
4. Só Agenda conectada → `business-pulse` (semana à frente)

É o momento "aha". Narre o que o Claude está fazendo e por quê.

---

## Passo E — Cadência semanal (ritmo da Casa Roque)

| Quando | Frase-gatilho | Skill |
|---|---|---|
| **Segunda, antes das 9h** (reunião Thomas) | "briefing de segunda" | `monday-brief` |
| **Sexta, após relatório do Thomas, antes das 15h** (batimento) | "pulso de sexta" | `friday-brief` |
| **Fim do mês** | "fecha o mês" | `month-end-prep` |
| **Dia 25** | "alerta do mês" | `month-heads-up` |

Se o JhEY preferir outra frase ou dia, registre no contexto.

---

## Onde gravar o que muda

Atualizações de contexto vão no **`CONTEXTO_CASA_ROQUE.md`** (fonte única de verdade do plugin). Atualize só os campos alterados; não toque no resto. Mostre atual vs proposto e espere aprovação antes de gravar.
