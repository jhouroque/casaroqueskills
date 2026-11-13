---
name: lead-triage
version: 0.1.1
description: >
  Prioriza os "leads" da Casa Roque por sinal de compra. Aqui não há CRM — leads
  são perguntas de pré-venda do Mercado Livre e Shopee, mensagens de WhatsApp e
  contatos do site (formulário e carrinho abandonado). Pontua por sinal de
  compra (pergunta sobre frete/prazo/disponibilidade = quente) e produz a lista
  "responda estes 5 primeiro", priorizando resposta em menos de 2h (POP 4, SAC).
  Use quando o JhEY pedir pra priorizar perguntas/leads, quem responder primeiro,
  ou falar do "pipeline".
---

# Triagem de perguntas/leads (lead-triage)

## Início rápido

Junte as perguntas/leads em aberto (ML, Shopee, WhatsApp, site), pontue por sinal de compra e mostre a lista ranqueada com pontos de fala. Prepara rascunhos de resposta e propõe horário na Agenda — nunca envia nem agenda sem aprovação do JhEY.

> **Sem CRM e sem conector de marketplace.** Não há HubSpot nem MCP de ML/Shopee. As perguntas/mensagens vêm de **print, export ou planilha** que o JhEY/Keila manda, ou são coladas. Quando faltar, peça o print das perguntas em aberto — nunca invente lead.

```
JhEY: "quem eu respondo primeiro?"
→ Junta perguntas/leads: ML, Shopee, WhatsApp, contatos do site
→ Pontua cada um por sinal de compra, urgência (tempo sem resposta) e canal
→ Devolve a lista ranqueada (tamanho adapta ao volume) com pontos de fala
→ Oferece rascunhar respostas e propor horário na Agenda
```

## Fluxo de trabalho

1. **Juntar as perguntas/leads.** Reúna as perguntas de pré-venda em aberto (ML, Shopee), mensagens de WhatsApp e contatos do site (formulário, carrinho abandonado). Use o modelo de pontuação em [reference/hubspot-scoring.md](reference/hubspot-scoring.md). Se nada foi anexado, peça: *"me manda o print das perguntas em aberto do ML e da Shopee, e as mensagens de WhatsApp sem resposta."* Não invente uma lista.

2. **Esclarecer se o gatilho for ambíguo.** Se o JhEY disse só "pipeline" sem qualificar, pergunte: *"Quer um panorama (quantas perguntas em aberto por canal) ou a lista priorizada de quem responder agora?"* — e roteie. Não pontue em cima de um "pipeline" cru.

3. **Pontuar cada pergunta/lead.** Aplique o modelo de quatro dimensões em [reference/hubspot-scoring.md](reference/hubspot-scoring.md):
   - **Sinal de compra** — pergunta sobre frete, prazo de entrega, disponibilidade/estoque, parcelamento ou desconto = quente. "Tem na cor X?" pesa mais que "que material é?".
   - **Urgência (tempo sem resposta)** — quanto mais perto/além das 2h (POP 4), mais sobe. SAC da casa responde em < 2h.
   - **Valor potencial** — ticket do produto perguntado (kit berço, espuma sob medida e atacado pesam mais que item avulso barato).
   - **Penalidade de já-respondido** — subtraia pontos se a pergunta já foi respondida há pouco (não cutuque o mesmo cliente duas vezes).

4. **Montar a lista ranqueada.** Ordene do maior pro menor score. Adapte o tamanho ao volume:
   - ≤ 10 perguntas → mostre todas
   - 11–30 → top 5
   - > 30 → top 8

   Para cada item: cliente (ou "comprador ML" quando o marketplace esconde o nome), canal, produto, score, um parágrafo de ponto de fala, há quanto tempo está em aberto. Se passou de 2h, marque: *"⚠ Fora da meta de SAC (< 2h) — responder já."*

5. **Oferecer rascunhos de resposta.** Pergunte: *"Rascunho resposta pra alguma?"* Se sim, escreva uma por pergunta, no tom da casa (cordial, objetivo, info correta de frete/prazo/estoque). Mostre o rascunho; não envie. No ML/Shopee o JhEY/Keila cola a resposta; no WhatsApp gere o bloco pronto pra colar.

6. **Oferecer horário na Agenda.** Pergunte: *"Bloqueio um horário pra você responder em lote?"* Se sim, veja na Google Agenda uma janela livre de 20–30 min nas próximas horas (evite slots com evento ±15 min). Proponha duas opções. Não crie o evento — o JhEY confirma.

## Portões de aprovação

- **Nunca envie uma resposta.** Só rascunho/bloco; o JhEY ou a Keila respondem no canal.
- **Nunca crie evento na Agenda.** Proponha horários; o JhEY bloqueia.
- **Nunca feche ou descarte uma pergunta** a menos que o JhEY peça.
- **Se zero perguntas baterem o filtro**, explique por quê e ofereça pedir o print atual — não fabrique lista.

## Referência

- [reference/hubspot-scoring.md](reference/hubspot-scoring.md) — modelo de pontuação de perguntas/leads por sinal de compra
- [reference/gotchas.md](reference/gotchas.md) — casos de borda: SAC < 2h, pergunta ≠ pedido, marketplace esconde o contato
- [reference/examples/happy-path-triage.md](reference/examples/happy-path-triage.md) — saída de exemplo: 7 perguntas ML/Shopee priorizadas, com rascunho e proposta de horário
