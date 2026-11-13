---
name: monday-brief
description: Gera o briefing de segunda-feira da Casa Roque em uma página — caixa, vendas dos últimos 7 dias, perguntas/leads, semana à frente e as 3 prioridades. Roda na segunda, antes da reunião das 9h com o Thomas. Aceita destino de envio e local para salvar. Gatilho quando o JhEY pede "briefing de segunda", "o que tem na semana", "começo de semana" ou "me prepara pra reunião do Thomas".
allowed-tools: Read, WebFetch, Bash
---

Rode o Briefing de Segunda-Feira. Puxe de toda fonte disponível, degrade com elegância quando faltar uma, e entregue um brief de uma página que o JhEY lê em menos de dois minutos — pronto **antes da reunião das 9h com o Thomas**.

> **Sem conector de venda.** A Casa Roque não tem MCP de Bling, Mercado Livre, Shopee ou NuvemShop. Caixa e vendas vêm de **relatórios/CSV exportados, prints ou extrato bancário** que o JhEY anexa. Gmail e Google Agenda **têm** conector. Quando faltar uma fonte, degrade aquela seção e marque "n/d" — nunca invente número.

Interprete os argumentos:
- `--post` (padrão `none`) — envia o resumo do brief para `gmail` (rascunho), `whatsapp` (bloco pronto pra colar) ou `none`
- `--save-to` (padrão `drive`) — `drive` (Google Drive), `desktop` (local) ou `both`

## Passo 1 — Rodar a business-pulse

Dispare o fluxo da skill `business-pulse`. Ela puxa nesta ordem, degradando pro que estiver conectado:

1. **Caixa** — saldo (Bling / extrato bancário) + faturamento do mês vs meta + contas a receber/pagar com vencimento próximo (folha dias 5/10/20, DAS dia 20).
2. **Vendas** — total dos últimos 7 dias vs os 7 anteriores (ML / Shopee / site), variação %, top produto.
3. **Perguntas/leads** ("pipeline" da casa) — perguntas de pré-venda em aberto no ML/Shopee, mensagens de WhatsApp e contatos do site sem resposta. Não há CRM.
4. **Compromissos da semana** (Google Agenda) — reuniões e prazos dos próximos 7 dias.
5. **Watch-list** (Gmail + SAC marketplace + estoque) — threads urgentes, SAC com resposta pendente > 2h (POP 4), itens com estoque < 5 unidades (alerta do Emerson, POP 2).
6. **As 3 prioridades** — as três ações de maior alavancagem para a semana, ranqueadas.

Se uma fonte faltar, anote no brief ("Sem relatório do Bling — caixa marcado n/d") em vez de travar.

## Passo 2 — Montar o brief de uma página

Layout (markdown, cabe numa tela):

```
# Briefing de Segunda — {dd/mm/aaaa}

## Caixa
{Saldo R$ X · faturamento do mês R$ Y de R$ 83,3 mil (meta grupo) · próximos vencimentos}

## Vendas (últimos 7d vs 7d anteriores)
{R$ X total · {▲/▼}Z% · top produto: {nome} (R$)}

## Perguntas & leads
{N perguntas em aberto (ML/Shopee) · M mensagens WhatsApp · K contatos do site}

## Semana à frente
- Seg 09h — Reunião com o Thomas (operações + tráfego)
- Sex 15h — Batimento NFs x estoque (Keila + Emerson, POP 3)
- Dia 5 / 5º dia útil — Enviar NFs ao Contabilizei · saldo Keila R$ 840,00
- Dia 10 — Salário Emerson R$ 1.400,00 + Cleusa + Vanda + VA
- Dia 20 — DAS Simples · adiantamento Keila R$ 560,00 + VTs
- {outros eventos da Agenda}

## Três coisas que precisam de você esta semana
1. {Ação de maior alavancagem com o porquê numa linha}
2. {...}
3. {...}
```

Inclua só os prazos do calendário financeiro que caem nos próximos 7 dias — não liste todos sempre. Se a data já passou no mês, omita.

## Passo 3 — Salvar e (opcional) enviar

1. Salve o brief no destino do `--save-to`:
   - `drive` — raiz do Google Drive, nome `briefing-segunda-AAAA-MM-DD.md`
   - `desktop` — `~/Desktop/briefing-segunda-AAAA-MM-DD.md`
   - `both` — os dois locais
2. Se `--post gmail`, gere um **rascunho no Gmail** com o brief completo (rascunho só — não envie). Se `--post whatsapp`, gere um **bloco curto pra colar no WhatsApp** com a seção "Três coisas" (a equipe usa WhatsApp, não Slack — o JhEY cola).
3. **Mostre o brief completo no chat sempre**, independente do destino de salvamento.

## Portões de aprovação

- **Salvar o arquivo é automático.** Sem aprovação — é o Drive do próprio JhEY.
- **Enviar (Gmail/WhatsApp) exige confirmação.** Mostre o rascunho/bloco e espere "manda" antes de enviar.
- **Nunca poste número ruim sem avisar.** Se o brief traz queda de vendas, caixa apertado ou meta longe, sinalize ao JhEY antes de gerar bloco de WhatsApp — o grupo pode ter gente além da liderança.

## Nota de cadência

Este comando roda toda **segunda de manhã, antes da reunião das 9h com o Thomas**. O JhEY pode agendá-lo no agendador de tarefas do Cowork — rodando segunda às 7h, a saída vai direto pro Drive e (se configurado) vira rascunho no Gmail.
