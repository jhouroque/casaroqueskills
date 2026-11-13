---
name: ticket-deflector
description: >
  Lê uma mensagem de cliente da Casa Roque (pergunta de ML/Shopee, WhatsApp ou
  e-mail), puxa o status do pedido (Bling/rastreio) e o histórico da planilha
  de contatos, rascunha uma resposta no tom da Casa Roque e, com aprovação
  explícita, encaminha reembolso/troca pelo marketplace de origem ou Pix.
  Gatilho quando o JhEY/Keila diz "responde esse cliente", "cadê meu pedido"
  ou "o cliente quer reembolso".
compatibility: "Sem conector de Bling/ML/Shopee — status do pedido e conversa vêm de print/relatório. Gmail tem conector. Reembolso/troca acontece NO MARKETPLACE (ML/Shopee) ou via Pix, nunca por outro meio. A base é a planilha de contatos no Google Drive."
---

# Resposta ao Cliente / SAC (ticket-deflector)

## Início rápido

Encaminhe ou cole a mensagem do cliente — o Claude puxa o status do pedido (print do Bling/rastreio), procura o cliente na planilha de contatos e rascunha a resposta no tom da Casa Roque. Se precisar de reembolso/troca, prepara os detalhes e espera aprovação explícita antes de qualquer coisa. Reembolso/troca acontece **no marketplace de origem ou via Pix** — nunca por outro meio.

```
JhEY/Keila: "responde esse cliente" [cola a pergunta do ML]
→ Extrai cliente + problema da conversa
→ Puxa o status do pedido (print do Bling/rastreio)
→ Procura o cliente na planilha de contatos
→ Rascunha a resposta no tom da Casa Roque
→ JhEY/Keila aprova o rascunho → enviar ou salvar
→ Se houver reembolso/troca: prompt de aprovação → confirma → encaminha pelo marketplace/Pix
```

> **Quem atende.** O SAC da Casa Roque é da **Keila** (POP 4, resposta < 2h, 3–4x/dia no ML, Shopee e WhatsApp); o JhEY cobre o WhatsApp das 13–17h. O tom é acolhedor, direto e resolutivo. **Contas off-limits** (não operar sem autorização): ML admin, Shopee admin, Bling admin.

## Fluxo de trabalho

1. **Leia a mensagem do cliente.** Aceite um print/texto colado de pergunta do ML, da Shopee, de WhatsApp, ou uma thread do Gmail. Extraia: nome/apelido do cliente, nº do pedido/venda (se houver) e o problema central — pedido de reembolso, dúvida de "cadê meu pedido", ou reclamação geral. Se houver vários assuntos, trate na ordem em que aparecem.

2. **Puxe o status do pedido (Bling/rastreio).** Peça o print/relatório do pedido no **Bling** ou o código de rastreio. Capture: produto, valor, data, status de envio e se já houve reembolso/devolução. **Sem conector** → peça o print. Se nenhum pedido casar, sinalize — não chute um pedido.
   - Se a mensagem é "cadê meu pedido", o que vale é o **código de rastreio** e o status na transportadora. Não prometa data que a transportadora não garante (ver `reference/gotchas.md`).
   - Se for **mediação do ML** ou disputa da Shopee, destaque — afeta a reputação do vendedor e tem prazo da plataforma.
   - Se vários pedidos casarem, mostre todos e pergunte ao JhEY/Keila qual é antes de rascunhar.

3. **Puxe o histórico na planilha de contatos.** Procure o cliente na planilha (Google Sheets/Drive) por telefone/WhatsApp, e-mail ou apelido. Veja: se é recorrente, pedidos anteriores, reclamações passadas, se é atacado. Se não existir, anote e ofereça criar a linha **depois** que a resposta sair — não crie durante o atendimento.

4. **Rascunhe a resposta.** Escreva no tom da Casa Roque (acolhedor, direto, resolutivo, em pt-BR — voz da Keila). Ajuste conforme o tipo:
   - Pedido de reembolso → empático, claro, voltado à ação; cite o **CDC** (arrependimento em 7 dias na compra online) quando couber
   - "Cadê meu pedido" → factual, tranquilizador; informe rastreio e status real, sem prometer o que a transportadora não garante
   - Reclamação geral → reconheça, explique, ofereça solução; se houver troca/devolução, siga o **POP de devolução/troca**
   Sinalize qualquer lacuna de dado dentro do rascunho com uma nota entre colchetes (ex.: *[Nota: sem print do Bling — confirmar o status do pedido antes de enviar]*) pro JhEY/Keila ver antes de mandar. Para um exemplo, veja [reference/examples/respond-refund-request.md](reference/examples/respond-refund-request.md). Para erros comuns, veja [reference/gotchas.md](reference/gotchas.md).

5. **Portão de aprovação — JhEY/Keila revisa o rascunho.** Apresente o rascunho completo. Não envie nem prepare envio até a aprovação. Pode editar à vontade antes de aprovar.

6. **Portão de aprovação — reembolso/troca.** Se um reembolso/troca se justifica, mostre um prompt de confirmação dedicado **depois** que o rascunho for aprovado:

   > *"Encaminhar reembolso de R$ [valor] pra [cliente] (pedido [nº]) **pelo [Mercado Livre/Shopee] / via Pix**? Responda SIM pra prosseguir."*

   Espere a confirmação explícita. Se a resposta não for um sim claro, pare e pergunte o que fazer. **Reembolso/troca acontece no marketplace de origem ou via Pix** — a skill nunca movimenta dinheiro sozinha e nunca por outro meio.

7. **Enviar ou salvar a resposta.** Depois de aprovado, pergunte ao JhEY/Keila: responder agora (no canal de origem — ML/Shopee/WhatsApp; ou Gmail), ou salvar como rascunho? Faça a escolha. Depois, registre a interação na **planilha de contatos** (aba Conversas) usando a skill `crm-maintenance`.

8. **Relato.** Um parágrafo curto: resposta enviada ou salva, reembolso/troca encaminhado ou não, conversa registrada na planilha.

## Portões de aprovação

- **Nunca encaminhe reembolso/troca sem confirmação explícita do JhEY/Keila** — sempre mostre valor, cliente, pedido e **o canal** (ML/Shopee/Pix) antes. **Nunca por outro meio que não o marketplace de origem ou Pix.**
- **Nunca envie a resposta sem revisão.** Sempre apresente o rascunho completo primeiro.
- **Nunca crie linha na planilha durante o atendimento.** Ofereça depois.
- **Nunca escolha o pedido sozinho.** Se vários casarem, mostre todos e deixe o JhEY/Keila escolher.
- **Nunca invente detalhe de pedido.** Sem print do Bling/rastreio, diga isso dentro do rascunho — não invente status nem prazo.
- **Nunca prometa o que a transportadora não garante.** Informe o status real do rastreio; não crave data de entrega.

## Referências

- [reference/gotchas.md](reference/gotchas.md) — pares Certo/Errado de tom, prazo do CDC, reembolso pelo canal de origem e não prometer prazo de transportadora
- [reference/examples/respond-refund-request.md](reference/examples/respond-refund-request.md) — exemplo: pedido de reembolso com pedido localizado no Bling
