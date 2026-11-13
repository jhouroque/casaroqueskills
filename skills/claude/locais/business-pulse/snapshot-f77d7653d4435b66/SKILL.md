<!-- C:\Users\Jhonatas\AppData\Roaming\Claude\local-agent-mode-sessions\c5e8a475-a351-48d2-8db3-3f0857ad643d\1d524d29-2570-4e4b-8d1f-844a61e14635\local_f6e23d68-ce2b-4eec-b343-aeec8fb24add\outputs\cr-plugin\small-business\skills\business-pulse\SKILL.md -->
---
name: business-pulse
description: >
  Monta um snapshot de uma página da operação de e-commerce da Casa Roque —
  caixa (Bling / extrato bancário), vendas (Mercado Livre / Shopee / site, 7
  dias vs 7 dias), "pipeline" = perguntas e leads (ML, Shopee, WhatsApp),
  compromissos da semana (Google Agenda), watch-list de itens urgentes (Gmail,
  SAC dos marketplaces, estoque < 5 unidades) e a coisa nº 1 que precisa de
  atenção hoje. Tenta toda fonte disponível e degrada com elegância pro que
  estiver à mão — uma fonte dá um pulso parcial; o conjunto dá o quadro
  completo. Gatilho quando o JhEY pergunta como o negócio está, quer um
  snapshot, um resumo da semana, um brief de segunda, ou diz algo como "o que
  tô deixando passar" ou "me atualiza do negócio".
compatibility: "Sem conector de Bling/ML/Shopee/NuvemShop — caixa e vendas vêm de relatórios/CSV exportados, prints ou extrato. Conectores ativos: Gmail (watch-list), Google Agenda (compromissos), Google Drive, Canva. Degrada pro que estiver disponível."
---

# Pulso do Negócio (business-pulse)

Um pedido, uma página. Puxe o dado de toda fonte disponível, sintetize num único brief escaneável e aponte a coisa nº 1 pra agir hoje. Faça o trabalho — não peça pro JhEY ajudar a achar o dado.

> **Sem conector de venda.** A Casa Roque não tem MCP de Bling, Mercado Livre, Shopee ou NuvemShop. Caixa e vendas vêm de **relatórios/CSV exportados, prints ou extrato bancário** que o JhEY anexa. Gmail e Google Agenda **têm** conector. Quando faltar uma fonte, degrade aquela seção e diga "n/d" — nunca invente número (ver `reference/gotchas.md`).

## Passo 1 — Puxar dados em paralelo

**Dispare tudo que for conector num único lote paralelo** — veja `reference/data_sources.md` pro mapa exato fonte → métrica. Não puxe em série.

Fontes a tentar:

- **Caixa** (Bling / extrato) — saldo, faturamento do mês, contas a receber/pagar, vencimentos próximos. **Sem conector** → relatório/CSV do Bling ou extrato. Se não veio nada, marque "n/d" e siga.
- **Vendas** (ML / Shopee / site NuvemShop) — total dos últimos 7 dias vs os 7 anteriores, por canal. **Sem conector** → export/print. Se não veio nada, marque "n/d".
- **"Pipeline" = perguntas/leads** (ML, Shopee, WhatsApp) — perguntas de pré-venda em aberto, contatos do site. **Sem conector** → o JhEY/Keila informa ou manda print. É o equivalente de "pipeline" aqui (não há CRM).
- **Compromissos** (Google Agenda) — reuniões e prazos da semana e dos próximos 7 dias. **Conector ativo.**
- **Watch-list** (Gmail + SAC marketplace + estoque) — threads urgentes no Gmail, SAC dos marketplaces com resposta pendente (> 2h, POP 4), itens com estoque < 5 unidades (alerta do Emerson, POP 2). **Gmail tem conector**; SAC e estoque vêm de print/relatório.

Se uma fonte falhar ou vier vazia, anote internamente e siga. Nunca trave o pulso por uma integração ruim.

**Fallback de caixa/vendas:** sem conector de Bling/ML/Shopee, se nada foi anexado, marque a seção "n/d — sem relatório do Bling/marketplace" e ofereça: "me manda o relatório de vendas (7 dias) e o de contas a receber/pagar do Bling que eu fecho o pulso completo." Não fique pedindo de novo.

**Fallback de Gmail:** se o Gmail falhar (auth instável), pule a watch-list de e-mail em silêncio e anote "Gmail indisponível" no apêndice — não jogue erro no meio do pulso.

## Passo 2 — Calcular métricas

Leia `reference/thresholds.md` pros cortes 🟢/🟡/🔴. Calcule:

- **Vendas 7d vs 7d** — total dos últimos 7 dias vs os 7 anteriores, por canal e consolidado; delta %.
- **Faturamento do mês vs meta** — acumulado do mês vs a meta (grupo ~R$ 83,3 mil/mês; por empresa: Casa Lima R$ 137.250, Casa Weber R$ 87.000, Casa Roque R$ 25.750).
- **Contas a receber/pagar** — vencimentos próximos (folha dias 5/10/20, DAS dia 20).
- **Perguntas/leads em aberto** — quantas perguntas de pré-venda esperando resposta (ML/Shopee/WhatsApp).

Dê status 🟢/🟡/🔴 a cada seção. Se uma fonte não retornou nada, marque "n/d" e anote no apêndice.

## Passo 3 — Sinalizar riscos proativamente

Varra itens acionáveis. Todo risco nomeia um registro específico e um próximo passo — "algumas perguntas em aberto" não serve; "3 perguntas no ML sem resposta há 3h (POP 4 pede < 2h)" serve.

- **SAC** — perguntas/mensagens no ML, Shopee ou WhatsApp sem resposta > 2h (POP 4). Nomeie canal e quantidade.
- **Estoque** — itens com < 5 unidades (alerta do Emerson, POP 2). Nomeie o produto e a quantidade.
- **Caixa** — contas a pagar vencendo nos próximos dias sem caixa coberto; folha (dias 5/10/20) e DAS (dia 20) à vista.
- **Vendas** — queda relevante 7d vs 7d (ver thresholds); canal específico despencando.
- **Mídia** — se houver dado do Thomas: CPC > R$ 2,00 ou ROI < 3x (metas da casa).
- **Gmail** — threads com "reclamação", "cancelar", "reembolso", "urgente", reclamação de marketplace/Reclame Aqui.

## Passo 4 — Montar a saída

Use o modelo exato em `reference/output_template.md`. Inclua só seções com dado real — omita o cabeçalho de fonte que não veio. Adapte a profundidade: um "como a gente tá?" casual recebe um relatório mais completo; "snapshot rápido antes de uma reunião" recebe um mais enxuto.

A síntese cruzada é onde a skill ganha valor. Se uma mensagem de SAC se conecta a um item de estoque zerado, mostre esse elo na seção nº 1. Síntese é o que torna o pulso mais útil que olhar cada lugar separado.

Regras de escrita:
- Números na frente, palavras depois. Nunca "vendas saudáveis" — escreva "R$ 12.300 nos últimos 7 dias, ▲ 8% vs a semana anterior" e deixe o JhEY julgar.
- Todo número carrega um delta vs o período anterior quando houver. Snapshots absolutos (saldo) ainda mostram delta semana a semana.
- Nomes e reais, não adjetivos. "R$ 1.450,00 a pagar pro fornecedor de espuma dia 20" ganha de "alguns boletos a vencer".
- Sem encheção. Se uma seção não tem nada relevante, escreva "Sem mudança material" e siga.

## Passo 5 — Exportar e compartilhar (uma vez)

Depois de apresentar o pulso, ofereça uma vez:
- "Quer que eu salve isso num arquivo?" (Google Drive, se disponível)
- "Mando um bloco pra você colar no WhatsApp da equipe?" (a equipe usa WhatsApp, não Slack — gere o texto pronto; o JhEY cola)
- "Quer um rascunho no Gmail com o pulso?" (rascunho só; enviar só com aprovação)

Se sim, faça. Se não responder, siga — não pergunte de novo.

## Variações de escopo

O JhEY pode pedir um corte mais estreito:

- **"Só o caixa" / "como tá o dinheiro"** → só Caixa & Finanças + riscos de pagamento.
- **"Só vendas"** → só a seção de Vendas + queda relevante.
- **"O que tá pegando" / "tem algo urgente"** → só Watch-list + todos os riscos, sem seções de métrica.
- **"Snapshot rápido antes de uma reunião"** → TL;DR + nº 1 só, sem seções completas.

## O que não fazer

- **Não peça permissão antes de puxar dado.** Se a skill foi chamada, rode. Perguntar "posso ver seu Gmail?" mata o propósito.
- **Não invente nem estime número.** Sem conector de venda, se nada foi anexado, diga "n/d" explícito e ofereça pedir o relatório. Nunca preencha lacuna com chute.
- **Não pule o delta.** Número sem comparação é insight perdido. Sem base anterior, escreva "(sem base anterior)".
- **Não jogue erro de conector no meio do pulso.** Mande pro apêndice. O pulso lidera com o que foi entregue.
- **Não poste número ruim sem avisar.** Antes de gerar bloco de WhatsApp ou rascunho com número fraco (queda de vendas, prejuízo), sinalize ao JhEY (ver `reference/gotchas.md`).

## Arquivos de referência

- `reference/data_sources.md` — mapa exato fonte → métrica, com fallbacks (sem conector de venda)
- `reference/thresholds.md` — cortes 🟢/🟡/🔴 coerentes com as metas da Casa Roque
- `reference/output_template.md` — estrutura markdown exata em pt-BR; não desvie
- `reference/gotchas.md` — modos de falha conhecidos (degradar sem dado, não postar número ruim sem avisar)
