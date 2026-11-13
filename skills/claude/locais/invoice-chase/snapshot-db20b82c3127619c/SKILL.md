<!-- C:\Users\Jhonatas\AppData\Roaming\Claude\local-agent-mode-sessions\c5e8a475-a351-48d2-8db3-3f0857ad643d\1d524d29-2570-4e4b-8d1f-844a61e14635\local_f6e23d68-ce2b-4eec-b343-aeec8fb24add\outputs\cr-plugin\small-business\skills\invoice-chase\SKILL.md -->
---
name: invoice-chase
version: 0.2.0
description: >
  Rascunha lembretes de cobrança a partir dos relatórios do Bling (contas a
  receber) e dos pedidos do site/atacado da Casa Roque. Como a Casa vende quase
  tudo à vista (marketplace, Pix, cartão — já pagos), o foco da cobrança é:
  boletos em aberto (site/atacado), pedidos aguardando pagamento, e vendas
  B2B/atacado. Tom casado com o histórico do cliente (gentil para bom pagador,
  firme para quem atrasa sempre). Envio via Gmail/WhatsApp com aprovação — nunca
  PayPal. Use quando o JhEY disser "quem tá me devendo", "tem boleto em aberto?",
  "cobra o atacado", ou pedir pra acompanhar pagamentos pendentes.
---

# Cobrança (invoice-chase)

## Início rápido

Levante o que está em aberto (boletos/atacado/B2B), pontue cada cliente pelo
histórico de pagamento, rascunhe um lembrete no tom certo e apresente ao JhEY.
Nada é enviado até ele aprovar.

```
JhEY: "quem tá me devendo?"
→ Puxa contas a receber em aberto do Bling (boletos, atacado, B2B)
→ Cruza com Pix/repasses recentes pra não cobrar quem já pagou
→ Pontua cada cliente: bom pagador / atrasa às vezes / atrasa sempre
→ Rascunha lembretes no tom certo (Gmail/WhatsApp)
→ Mostra tabela-resumo + rascunhos. Espera o "manda esses".
```

> **Atenção (a maioria das vendas já está paga):** vendas em Mercado Livre, Shopee,
> Pix e cartão são pré-pagas — o dinheiro já entrou (ou está em repasse a liberar).
> **Não cobre cliente de marketplace.** Cobre só o que NÃO é à vista: boleto do
> site, pedidos B2B/atacado com prazo, e pedidos do site aguardando pagamento.

## Configuração (só na 1ª vez)

Pergunte ao JhEY antes de rodar pela primeira vez:

1. **Canal de envio**: "Prefere que os lembretes saiam por **Gmail** (rascunho) ou
   como **bloco pra colar no WhatsApp**?" — guarde a resposta e use nas próximas.
   (Não há PayPal nem disparo automático — sempre rascunho/bloco, com aprovação.)
2. **Fonte das pendências**: "As pendências de boleto/atacado saem do **relatório
   de contas a receber do Bling**? Me manda o CSV/PDF quando quiser rodar." — como
   não há conector, a skill trabalha com o relatório exportado.

Não pergunte de novo nas próximas execuções.

## Fluxo de trabalho

1. **Levante as pendências a receber.** Peça/leia o **relatório de contas a receber
   do Bling** (CSV/PDF) e filtre os itens em aberto com mais de 1 dia de atraso —
   focando em **boleto (site/atacado)**, **pedidos B2B/atacado** e **pedidos do site
   aguardando pagamento**. Ignore vendas de marketplace/Pix/cartão (já pagas).

2. **Cruze com o que já entrou.** Para cada cliente em aberto, confira nos extratos
   (Pix, repasses, NuvemPago) se o pagamento já caiu:
   - Se aparecer um pagamento recente que bate com o pedido, marque como **"talvez
     já pago — conferir"** e **tire da fila de cobrança**.
   - Se o JhEY não tiver o extrato à mão, marque "histórico de Pix/repasse não
     conferido" e peça confirmação antes de enviar. Não cobre no escuro.

3. **Pontue cada cliente.** Leia [reference/tone-matching.md](reference/tone-matching.md)
   para a lógica de pontuação. Resultado: `bom-pagador`, `atrasa-as-vezes` ou `atrasa-sempre`.

4. **Rascunhe os lembretes.** Um por cliente — consolide vários pedidos/boletos em
   aberto num só. Case o tom com a pontuação. Veja
   [reference/examples/gentle-reminder.md](reference/examples/gentle-reminder.md) e
   [reference/examples/firm-reminder.md](reference/examples/firm-reminder.md).

5. **Apresente os rascunhos ao JhEY.** Mostre primeiro uma tabela-resumo:

   | Cliente | Valor em aberto | Dias de atraso | Tom | Enviar via |
   |---|---|---|---|---|
   | Móveis Bela Casa (atacado) | R$ 1.840,00 | 18 dias | Gentil | Rascunho Gmail |
   | Decorações Lima ME | R$ 620,00 | 47 dias | Firme | Bloco WhatsApp |

   Depois mostre cada rascunho por inteiro. Espere o JhEY dizer "manda esses" ou
   aprovar um a um.

6. **Enviar ou deixar pronto — só após aprovação.**
   - Gmail: deixe como **rascunho** na conta do JhEY (ele revisa e envia).
   - WhatsApp: entregue o **bloco de texto pronto pra colar** (o JhEY/Keila cola).
   - Nunca dispare nada sem aprovação explícita.

7. **Relate o que aconteceu.** Liste o que virou rascunho/bloco, o que foi enviado
   (se o JhEY já mandou), e o que ficou marcado (talvez já pago, excluído).

## Portões de aprovação

- **Nunca envie nem deixe pronto sem aprovação explícita do JhEY.** Apresente todos
  os rascunhos primeiro; espere o sinal verde.
- **Nunca inclua quem já pagou** (marketplace/Pix/cartão, ou pagamento recente que
  bate com o pedido). Marque "talvez já pago — conferir".
- **Nunca cobre um cliente que não esteja no relatório do Bling.** Sem cobrança de memória.
- **Uma aprovação cobre um lote.** Adicionar um cliente ou mudar um rascunho depois
  da aprovação começa uma nova rodada.

## Referência

- [reference/tone-matching.md](reference/tone-matching.md) — lógica de pontuação, tom, fórmulas de assunto
- [reference/gotchas.md](reference/gotchas.md) — modos de falha conhecidos
- [reference/examples/gentle-reminder.md](reference/examples/gentle-reminder.md) — exemplo de e-mail pra bom pagador
- [reference/examples/firm-reminder.md](reference/examples/firm-reminder.md) — exemplo de e-mail pra quem atrasa sempre
