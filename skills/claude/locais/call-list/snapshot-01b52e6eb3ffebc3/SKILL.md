---
name: call-list
description: Lista os 5 contatos mais importantes pra responder/contatar hoje na Casa Roque — perguntas quentes do ML/Shopee, mensagens de WhatsApp e contatos de atacado — com pontos de fala e bloqueio de horário na Google Agenda. Mira resposta em menos de 2h (SAC, POP 4). Aceita quantidade e data opcionais.
allowed-tools: Read, WebFetch, Bash
---

Rode a priorização de contatos. Varra as perguntas/leads, ranqueie por urgência e oportunidade, puxe o contexto da pergunta e deixe o JhEY pronto pra responder rápido — meta de SAC **< 2h** (POP 4).

> **Sem CRM e sem conector de marketplace.** Não há HubSpot nem MCP de ML/Shopee. Perguntas e mensagens vêm de **print, export ou planilha** que o JhEY/Keila manda, ou coladas. Sem dado, peça o print das perguntas/mensagens em aberto.

Interprete os argumentos:
- `--n` (padrão `5`) — quantos contatos mostrar (1–10)
- `--date` (padrão hoje) — data pra montar a lista (`AAAA-MM-DD`)

## Passo 1 — Varrer perguntas/leads

Usando o fluxo da skill `lead-triage`:

1. Reúna as perguntas de pré-venda em aberto (ML, Shopee), mensagens de WhatsApp e contatos de atacado/site (últimos dias).
2. Para cada um, puxe o contexto da conversa (a pergunta em si e o histórico, se houver no print/thread).
3. Pontue cada contato por:
   - **Urgência**: há quanto tempo está sem resposta (quanto mais perto/além das 2h, mais sobe).
   - **Sinal de compra**: pergunta sobre frete, prazo, disponibilidade, parcelamento ou desconto = quente.
   - **Valor potencial**: ticket do produto perguntado (kit berço, espuma sob medida, atacado pesam mais).
   - **Canal**: pergunta de marketplace e WhatsApp na frente; contato de site/carrinho abandonado em seguida.

## Passo 2 — Ranquear e escolher o top N

Ranqueie todos e escolha o top `--n`. Em empate, prefira quem tem sinal de compra forte e está há mais tempo sem resposta.

Para cada contato, monte um cartão:

```
{Posição}. {Cliente ou "comprador ML"} — {canal}
Produto: {item} | Em aberto há: {X} | Sinal: {frete/prazo/disponibilidade/...}

PONTOS DE FALA
• {ponto da pergunta/contexto}
• {ponto da pergunta/contexto}
• {pergunta a fazer / info a confirmar — ex.: estoque, prazo}

OBJETIVO: {uma frase — fechar a venda / tirar dúvida de frete / confirmar estoque}
```

Marque "⚠ Fora da meta de SAC (< 2h)" em qualquer contato que já passou de 2h em aberto.

## Passo 3 — Bloquear horário na Agenda

Para os contatos da lista, ofereça bloquear 20 minutos na Google Agenda na data alvo (uma janela única pra responder em lote funciona bem).

Mostre o bloco proposto:
```
{horário} — Responder: {Cliente/comprador} ({canal})
```

Espere o JhEY confirmar quais bloquear antes de criar eventos na Agenda.

## Passo 4 — Rascunhar respostas

Para qualquer contato com pergunta em aberto, rascunhe uma resposta curta no tom da casa (cordial, objetivo, info correta de frete/prazo/estoque):
```
{Cliente},

{Uma frase respondendo a dúvida — frete/prazo/disponibilidade}. {Uma frase com o próximo passo claro}.

Casa Roque
```

No ML/Shopee o JhEY/Keila cola a resposta no canal; no WhatsApp gere o bloco pronto pra colar.

## Falhas de fonte

Sem o print/export das perguntas, pare e peça: "me manda o print das perguntas em aberto do ML/Shopee e as mensagens de WhatsApp que eu monto a lista." Se a Google Agenda estiver indisponível, pule o bloqueio e anote "Agenda indisponível — bloqueio pulado". O contexto de cada pergunta vem do que foi anexado.

## Portões de aprovação

- **Nunca envie respostas automaticamente.** Só rascunhos/blocos pro JhEY aprovar.
- **Nunca crie bloco na Agenda sem confirmação** — mostre a lista proposta primeiro.
- **Nunca feche ou descarte uma pergunta automaticamente.**

## Saída

Apresente a lista ranqueada com os pontos de fala. Depois mostre os blocos propostos na Agenda e peça confirmação. Por fim, mostre os rascunhos de resposta e pergunte quais enviar.
