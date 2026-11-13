---
name: handle-complaint
description: Resolve uma reclamação de cliente da Casa Roque ponta a ponta — puxa o contexto (pedido no Bling, conversa do ML/Shopee/WhatsApp), rascunha a resposta no tom da Casa Roque e sugere uma correção operacional. Aceita um argumento opcional de ID/link da reclamação (e-mail, mediação do ML, conversa) ou o texto colado.
allowed-tools: Read, WebFetch, Bash
---

Rode o fluxo de resolução de reclamação encadeando duas skills. Leia a reclamação, reúna o contexto, rascunhe a resposta e sugira uma correção pra não acontecer de novo.

> **Sem conector de Bling/marketplace.** O status do pedido, a conversa do ML/Shopee e o histórico vêm de **print/relatório** anexado ou texto colado. Gmail tem conector. O SAC da Casa Roque é feito pela **Keila** (POP 4, resposta < 2h); o JhEY cobre o WhatsApp 13–17h. Reembolso/troca acontece **no marketplace de origem (ML/Shopee) ou via Pix** — nunca por outro meio. Datas dd/mm/aaaa, R$ com vírgula.

Interprete os argumentos:
- `EMAIL_OU_TICKET_ID` (opcional) — ID da thread no Gmail, link/ID da reclamação no marketplace, ou "última" pra pegar a reclamação aberta mais recente. Se faltar, peça ao JhEY/Keila pra colar o texto da reclamação (ou mandar o print).

## Passo 1 — Carregar a reclamação (ticket-deflector)

Usando o fluxo da skill `ticket-deflector`:

1. Se veio um ID/link: puxe a thread inteira do Gmail (ou peça o print da conversa do ML/Shopee/WhatsApp, que não têm conector).
2. Se for "última": peça o print da reclamação aberta mais recente (mediação do ML, disputa da Shopee, mensagem de WhatsApp ou thread do Gmail).
3. Se não veio nada: peça pro JhEY/Keila colar o texto da reclamação ou mandar o print.
4. Identifique: nome/apelido do cliente, dados do pedido (nº, produto), o que deixou ele insatisfeito e o que ele está pedindo.

## Passo 2 — Puxar contexto

1. Peça o print/relatório do pedido no **Bling**: status, produto, valor, data, situação de envio/rastreio. Sem conector → print. **Não invente status** — se não veio o print, trabalhe com o texto da reclamação e diga isso.
2. Veja o histórico do cliente na **planilha de contatos** (Google Sheets/Drive): é cliente novo ou recorrente, pedidos anteriores, reclamações passadas, se é atacado.
3. Se a reclamação é **mediação do ML** ou disputa da Shopee, destaque — afeta a reputação do vendedor e tem **prazo da plataforma** pra responder (ver `customer-pulse/reference/gotchas.md`).
4. Resuma: "Cliente {novo/recorrente}, {N} pedidos anteriores, {0/N} reclamações antes. O problema atual é {uma frase}. Canal: {ML/Shopee/WhatsApp/Gmail}. {Mediação aberta — prazo X, se for o caso}."

## Passo 3 — Rascunhar a resposta (ticket-deflector)

Usando o fluxo da skill `ticket-deflector` pra resposta no tom da Casa Roque:

1. Rascunhe a resposta ajustada à gravidade e ao histórico do cliente (tom da Keila: acolhedor, direto, resolutivo, em pt-BR):
   - Primeira reclamação, bom cliente → empático, generoso
   - Reclamante recorrente → profissional, firme, focado em solução
   - Tom agressivo → profissional, breve, pondo limite com educação
2. Inclua: reconhecimento, explicação (se sabida), solução oferecida, próximo passo. Quando couber, cite o **CDC** (direito de arrependimento de 7 dias em compra online) — sem prometer o que a transportadora não garante.
3. Se houver devolução/troca, siga o **POP de devolução/troca**: SAC verifica prazo/condição → etiqueta de retorno no marketplace → Emerson confere → restock/descarte → reembolso/reenvio.
4. Apresente o rascunho pro JhEY/Keila. **NÃO** envie.

## Passo 4 — Sugerir correção operacional (customer-pulse)

1. Veja se a reclamação bate com um tema conhecido (de rodadas anteriores de `/customer-pulse-check` ou reclamações parecidas).
2. Se é padrão: "Esta é a {Nª} reclamação sobre {assunto} este mês. Considere: {mudança operacional concreta — ex.: revisar a descrição da densidade da espuma no anúncio, antecipar aviso de prazo, ajustar o POP X}."
3. Se é isolada: "Parece um caso pontual. Sem padrão detectado."

## Falhas de conector

Se o Gmail não tem a thread e não veio print do marketplace, peça pro JhEY/Keila colar o texto — a skill funciona com entrada manual. Sem o print do pedido no Bling, pule o status do pedido e anote: "Sem print do Bling — status do pedido indisponível, trabalhando só com o texto da reclamação." Nunca invente nº de pedido, valor ou status de rastreio.

## Portões de aprovação

- **Nunca envie resposta sem aprovação explícita do JhEY/Keila.** Só rascunho.
- **Nunca emita reembolso nem autorize troca automaticamente.** Apresente a opção; o JhEY/Keila decide. Reembolso/troca sempre **pelo marketplace de origem (ML/Shopee) ou via Pix**, nunca por outro meio.
- **Nunca encerre uma mediação/disputa nem altere o pedido sem confirmação.** Essas contas são off-limits (ML admin, Shopee admin, Bling admin).

## Saída

Apresente o resumo do contexto do cliente, o rascunho da resposta e a sugestão operacional baseada em padrão (se houver). Pergunte: "Quer enviar essa resposta, editar, ou tratar de outro jeito? Se tiver reembolso/troca, eu sigo o POP e espero seu ok."
