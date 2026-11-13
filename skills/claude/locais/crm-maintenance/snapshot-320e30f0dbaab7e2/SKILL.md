<!-- C:\Users\Jhonatas\AppData\Roaming\Claude\local-agent-mode-sessions\c5e8a475-a351-48d2-8db3-3f0857ad643d\1d524d29-2570-4e4b-8d1f-844a61e14635\local_f6e23d68-ce2b-4eec-b343-aeec8fb24add\outputs\cr-plugin\small-business\skills\crm-maintenance\SKILL.md -->
---
name: crm-maintenance
description: >
  Mantém a base de contatos da Casa Roque em dia sem o JhEY precisar abrir a
  planilha: registra clientes (inclui atacado/B2B), pedidos e follow-ups,
  anota conversas (WhatsApp, e-mail, pergunta do Mercado Livre/Shopee) e marca
  contatos parados. A skill do "pare de digitar cadastro à mão". Gatilho
  quando o JhEY pede pra atualizar a base, registrar uma conversa, anotar um
  contato de atacado ou dar contexto a um pedido.
compatibility: "Não há CRM na Casa Roque. A base é uma PLANILHA no Google Sheets/Drive (conector ativo). Conversas vêm de WhatsApp, Gmail (conector ativo) e perguntas do ML/Shopee (sem conector → print/relatório). Pedidos vêm do Bling/marketplace (sem conector → print/relatório). Sem conector de Bling/ML/Shopee, peça o print/CSV."
---

# Manutenção da Base de Contatos (crm-maintenance)

> **Não há CRM.** A Casa Roque não usa HubSpot nem nenhuma ferramenta de CRM. A "base" é uma **planilha simples no Google Sheets/Drive** (uma aba "Contatos" e, quando útil, uma aba "Conversas"). O Google Drive **tem** conector. Bling, Mercado Livre e Shopee **não têm** — pedido e dado de cliente vêm de print/relatório (CSV/PDF) que o JhEY ou a Keila anexam. Atenção: o marketplace **oculta** nome/telefone/e-mail real do cliente (ver `reference/gotchas.md`).

## Início rápido

Puxe o contexto do e-mail, da conversa ou do print referenciado, ache a linha certa do contato na planilha, registre o que aconteceu e mostre o que mudou. Para uma faxina de pedido de atacado, confira o registro contra a conversa recente e proponha atualizações — nunca aplique sem aprovação.

```
JhEY: "registra essa conversa do WhatsApp da Marina"
→ Lê a conversa (print ou texto colado)
→ Acha a Marina na aba Contatos da planilha
→ Acrescenta uma linha na aba Conversas (data, canal, resumo)
→ Atualiza "última conversa" e "próximo follow-up" da Marina
→ Reporta: "Registrei a conversa da Marina (WhatsApp, 18/06). Próximo follow-up: 25/06."
```

## Fluxo de trabalho

1. **Identifique a intenção.** Decida qual dos três caminhos se aplica a partir da mensagem e do contexto:
   - **Caminho e-mail/pergunta** — "atualiza a base", "anota essa pergunta do ML", ou qualquer referência a um e-mail ou pergunta de marketplace
   - **Caminho conversa** — "registra essa conversa", "anota essa ligação", ou qualquer referência a uma conversa de WhatsApp/telefone
   - **Caminho faxina** — "confere o cadastro da fulana", "esse pedido de atacado tá atualizado?", ou qualquer pedido pra auditar um contato/negócio específico
   Se a intenção estiver ambígua (ex.: "atualiza a base" sem e-mail/conversa/contato referenciado), pergunte qual caminho antes de seguir.

2. **Reúna o contexto.**
   - Caminho e-mail/pergunta: leia a thread (assunto, participantes, últimas 1–3 mensagens) ou a pergunta do ML/Shopee (texto/print). Identifique o cliente. **Atenção:** no Gmail você tem o e-mail real; numa pergunta de marketplace, o que aparece é o **apelido/usuário** do comprador, não o nome civil nem o telefone.
   - Caminho conversa: leia a conversa (print do WhatsApp ou texto colado). Identifique o número/contato e o assunto. Se a conversa não foi indicada, use a mais recente que o JhEY mencionar e confirme antes de seguir.
   - Caminho faxina: puxe a linha do contato na planilha (canal, telefone/WhatsApp, último pedido, valor, status, próximo follow-up) e as conversas dos últimos 14 dias com esse contato (Gmail + prints de WhatsApp/marketplace que existirem).

3. **Ache o contato na planilha.** Para os caminhos e-mail/pergunta e conversa:
   - Busque na aba **Contatos** por telefone/WhatsApp, por e-mail ou por nome/apelido. Se o contato não existir, **crie a linha** com o que dá pra extrair (e-mail/assinatura, número do WhatsApp, apelido do marketplace) — **anuncie a criação no chat antes de gravar**.
   - Para os nomes de coluna e os valores aceitos em cada campo, leia [reference/hubspot-fields.md](reference/hubspot-fields.md) antes de gravar qualquer coisa na planilha.
   - Se o cliente é de **atacado/B2B**, marque `Tipo = Atacado` e registre o pedido como "negócio" (ver exemplo de faxina). Atacado tende a ter recompra — vale o follow-up agendado.
   - Se a deduplicação ou o pareamento de contato ficar ambíguo (mesmo número em dois nomes, dois apelidos de marketplace que parecem a mesma pessoa), confira [reference/gotchas.md](reference/gotchas.md) antes de seguir — cobre os erros mais comuns, inclusive LGPD.

4. **Execute a ação.**
   - Caminho e-mail/pergunta: acrescente uma linha na aba **Conversas** com a data, o canal (`E-mail` ou `Pergunta ML`/`Pergunta Shopee`), o contato e um resumo de 1–2 frases (não a thread inteira). Atualize "última conversa" e, se couber, "próximo follow-up" do contato. Para um exemplo completo, veja [reference/examples/log-email-happy-path.md](reference/examples/log-email-happy-path.md).
   - Caminho conversa: acrescente uma linha na aba **Conversas** com a data, o canal (`WhatsApp` ou `Telefone`), o contato e um resumo de 1–2 frases. Para um exemplo, incluindo o caso de contato que não existe ainda, veja [reference/examples/log-call-happy-path.md](reference/examples/log-call-happy-path.md).
   - Caminho faxina: percorra cada campo conforme [reference/cleanup-checklist.md](reference/cleanup-checklist.md) e monte uma lista de mudanças propostas. Mostre **atual → proposto** lado a lado. Grave só o que o JhEY aprovar. Para um exemplo completo (pedido de atacado), veja [reference/examples/cleanup-deal.md](reference/examples/cleanup-deal.md).

5. **Portão de aprovação — toda gravação visível.** Para criar contato e registrar conversa, anuncie antes de gravar e mostre o resultado depois. Para edições de faxina, não grave nada até o JhEY aprovar as mudanças específicas. **Nunca** envie mensagem ao cliente por aqui — esta skill só organiza a base; responder cliente é a `ticket-deflector`/`handle-complaint`.

6. **Reporte o que aconteceu.** Diga o que foi gravado e o que ficou pendente. Mantenha curto. Se o Drive tiver link da planilha, inclua.

## Portões de aprovação

- **Nunca apague linha.** Nem contato, nem conversa, nem pedido. Se o JhEY pedir, diga que a skill não apaga (histórico e LGPD) e oriente a marcar `Status = Inativo` ou arquivar na planilha.
- **Nunca dê um pedido/negócio de atacado por "ganho" ou "perdido" sem aprovação explícita.** Mesmo com indício forte. Sinalize e adie.
- **Nunca crie uma linha de pedido/negócio sem pedido.** Pergunte se o pedido certo não der pra identificar.
- **Anuncie a criação de contato antes de gravar.** Uma linha — deixa o JhEY pegar erro de digitação ou duplicado.
- **Diffs lado a lado na faxina.** Mostre valor atual e valor proposto; espere aprovação item a item.

## Referências

- [reference/hubspot-fields.md](reference/hubspot-fields.md) — os campos (colunas) da planilha de contatos e da aba de conversas usados nesta skill
- [reference/cleanup-checklist.md](reference/cleanup-checklist.md) — os campos checados numa faxina e a evidência exigida pra sinalizar cada um
- [reference/gotchas.md](reference/gotchas.md) — pares Certo/Errado pra pareamento de contato, resumo de conversa, dado oculto do marketplace, LGPD e duplicados
- [reference/examples/log-email-happy-path.md](reference/examples/log-email-happy-path.md) — exemplo: e-mail/pergunta de marketplace num contato existente
- [reference/examples/log-call-happy-path.md](reference/examples/log-call-happy-path.md) — exemplo: conversa de WhatsApp, contato que não existia
- [reference/examples/cleanup-deal.md](reference/examples/cleanup-deal.md) — exemplo: faxina de um pedido de atacado parado
