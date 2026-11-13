# Exemplo: pedido de reembolso — pedido localizado no Bling

**Cenário:** uma cliente manda mensagem dizendo que o produto chegou com defeito e quer reembolso. A Keila encaminha a conversa e diz "responde essa cliente".

---

## Mensagem da cliente (encaminhada — pergunta no Mercado Livre)

> **Anúncio:** Kit Berço 9 peças — bordado
>
> Comprei o kit berço semana passada e veio com uma costura aberta numa das peças. Queria o reembolso, por favor. Meu pedido é o 2000384756.
>
> — comprado por `ana.luiza_sp`

---

## Passo 2 — Status do pedido (print do Bling, anexado pela Keila)

Pedido encontrado (print do Bling):

- **Pedido / venda:** 2000384756 (Mercado Livre)
- **Produto:** Kit Berço 9 peças — bordado
- **Valor:** R$ 189,90
- **Data:** 09/06/2026
- **Status:** Entregue (rastreio confirmado em 14/06/2026)
- **Reembolso/devolução:** nenhum até agora

---

## Passo 3 — Histórico na planilha de contatos

Contato encontrado: **Ana Luiza** (apelido ML `ana.luiza_sp`)
- Canal: Mercado Livre
- Tipo: Varejo
- Pedidos anteriores: 1 (set/2025)
- Observação: "Cliente recorrente — comprou trocador em 2025, sem reclamação."

---

## Passo 4 — Rascunho da resposta (apresentado pro JhEY/Keila revisar)

> **Resposta (pelo Mercado Livre):**
>
> Olá, Ana Luiza!
>
> Que chato que uma das peças do seu kit berço chegou com a costura aberta — sinto muito por isso, não é o padrão da Casa Roque. Você tem todo o direito de resolver, inclusive pelo prazo de arrependimento de 7 dias previsto no Código de Defesa do Consumidor para compra online.
>
> Posso fazer de dois jeitos, como você preferir: **(1) troca** — a gente gera a etiqueta de retorno aqui pelo Mercado Livre, sem custo pra você, e assim que a peça chegar eu já envio uma nova; ou **(2) reembolso integral** de R$ 189,90 pelo próprio Mercado Livre. É só me dizer qual fica melhor.
>
> De novo, me desculpe pelo transtorno — vou resolver rapidinho.
>
> Um abraço,
> Keila — Casa Roque

---

## Passo 5 — JhEY/Keila aprova o rascunho (sem edições)

A cliente responde que prefere o **reembolso**.

---

## Passo 6 — Prompt de aprovação do reembolso

> *"Encaminhar reembolso de R$ 189,90 pra Ana Luiza (pedido 2000384756) **pelo Mercado Livre**? Responda SIM pra prosseguir."*

Keila responde: **SIM**

→ Reembolso encaminhado **pelo painel do Mercado Livre** (não por outro meio). A skill não movimenta o dinheiro sozinha — abre o caminho e a Keila/JhEY confirma na plataforma. Como houve defeito, a peça segue o **POP de devolução/troca** (etiqueta de retorno no ML → Emerson confere → restock ou descarte).

---

## Passo 7 — Envio + registro na planilha

Resposta enviada pelo Mercado Livre.

Conversa registrada na aba Conversas da planilha de contatos (via `crm-maintenance`):
> 18/06/2026 · Ana Luiza · Pergunta ML · "Kit berço com costura aberta. Oferecida troca ou reembolso; cliente optou por reembolso de R$ 189,90 pelo ML. Peça em devolução (POP)." · Pedido relacionado: 2000384756

---

## Passo 8 — Relato

> Resposta enviada pra Ana Luiza pelo Mercado Livre · Reembolso de R$ 189,90 encaminhado pelo ML (com seu SIM) · Conversa registrada na planilha. A peça com defeito entra no POP de devolução/troca com o Emerson.

## O que este exemplo demonstra

- Reembolso **pelo marketplace de origem (ML)**, nunca por outro meio
- CDC (7 dias) citado de forma natural, sem juridiquês
- Tom da Keila: acolhedor, direto, resolutivo
- Oferece troca **e** reembolso — não decide pela cliente
- Status do pedido vindo do print do Bling (sem conector), não inventado
- Conversa registrada na planilha no fim (encadeia com `crm-maintenance`)
- Reembolso só encaminhado após o SIM explícito
