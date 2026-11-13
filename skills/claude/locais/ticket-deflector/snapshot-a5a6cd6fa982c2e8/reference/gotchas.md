# Pegadinhas — ticket-deflector

Casos-limite que deram problema em teste ou revisão. Cada item usa o par Certo/Errado.

---

## Pegadinha: prometer reembolso/troca por um meio que não é o de origem

**Por que importa:** na Casa Roque o reembolso/troca acontece **no marketplace de origem (Mercado Livre, Shopee) ou via Pix**. Prometer "devolvo no seu cartão" ou citar qualquer outro meio (PayPal, etc.) confunde o cliente e cria uma promessa que a operação não cumpre — a venda foi pelo ML/Shopee e o estorno volta por lá.

### ✗ Errado

> Já vou processar o estorno de R$ 189,90 no seu cartão / pelo PayPal. Cai em 3 a 5 dias úteis.

### ✓ Certo

> Posso fazer o **reembolso integral de R$ 189,90 pelo próprio Mercado Livre** (volta pela mesma forma de pagamento da compra), ou a **troca** com etiqueta de retorno sem custo. Qual você prefere?

Reembolso sempre pelo canal de origem (ML/Shopee) ou Pix. A skill mostra o canal no prompt de aprovação e nunca movimenta dinheiro sozinha.

---

## Pegadinha: prometer prazo de entrega que a transportadora não garante

**Por que importa:** "cadê meu pedido" é metade do SAC. Cravar "chega amanhã" quando o rastreio não garante isso transforma um cliente nervoso num cliente que abre mediação/Reclame Aqui quando o prazo fura. Informe o status real; não invente data.

### ✗ Errado

> Seu pedido chega amanhã, pode ficar tranquila!

### ✓ Certo

> Seu pedido saiu para entrega e o último status do rastreio (código BR123456789) é "em trânsito - Campinas/SP", atualizado hoje. Pela rota, costuma chegar em 1–2 dias úteis, mas quem dá a data final é a transportadora. Vou acompanhar com você e, se travar, a gente aciona. *[Nota: confirmar o último status no rastreio antes de enviar]*

Status real + faixa estimada + quem garante o quê. Sem promessa que não depende da gente.

---

## Pegadinha: rascunho genérico em vez do tom da Casa Roque (Keila)

**Por que importa:** o valor da skill é a resposta soar como a Keila escreveu — acolhedora, direta, em pt-BR de gente. Um texto corporativo engessado é reescrito do zero, e o cliente sente o robô.

### ✗ Errado

> Prezado cliente,
>
> Agradecemos o seu contato. Pedimos desculpas pelos eventuais transtornos e informamos que sua solicitação será processada em até 5 dias úteis.
>
> Atenciosamente, Equipe de Atendimento

### ✓ Certo

> Olá, Ana Luiza! Que chato que a peça chegou com a costura aberta — sinto muito, não é o nosso padrão. Vou resolver rapidinho pra você: posso fazer a troca (etiqueta de retorno sem custo) ou o reembolso pelo Mercado Livre. Como prefere? Um abraço, Keila — Casa Roque

Acolhedor, primeiro nome, direto à solução, assinado pela Keila. Se faltar referência de tom, use o exemplo de `reference/examples/respond-refund-request.md`.

---

## Pegadinha: sinalizar a lacuna de dado no fim, não no ponto que importa

**Por que importa:** se não veio o print do Bling e o rascunho diz "seu reembolso de R$ X está a caminho", o JhEY/Keila manda uma informação falsa. A lacuna tem que aparecer no ponto exato em que afeta a mensagem.

### ✗ Errado

Rascunhar a resposta como se todo dado existisse e jogar um rodapé no fim: "Obs.: não achei o pedido no Bling."

### ✓ Certo

Inserir o aviso dentro do rascunho, na frase exata:

> Olá, Ana Luiza! Já estou verificando seu pedido *[Nota: sem print do Bling — confirmar nº e status do pedido antes de enviar]* e quero resolver isso rápido.

O JhEY/Keila vê o problema antes de clicar em enviar.

---

## Pegadinha: vários pedidos do mesmo cliente

**Por que importa:** um cliente com dois pedidos — um já reembolsado, outro não — quebra a busca "pega o mais recente" e gera o rascunho errado.

### ✗ Errado

Pegar o pedido mais recente sozinho e seguir sem avisar.

### ✓ Certo

Mostrar todos os pedidos que casam e pausar:

> *"Achei 2 pedidos dessa cliente no print do Bling: (1) R$ 99,00 · 14/03 · entregue · (2) R$ 189,90 · 09/06 · entregue. Qual é o desta conversa?"*

Espere o JhEY/Keila confirmar antes de rascunhar.

---

## Pegadinha: tratar mediação do ML como mensagem comum

**Por que importa:** quando o cliente abre **mediação** no Mercado Livre, a plataforma entra no meio, há **prazo** pra responder e o caso pesa na reputação do vendedor (taxa de reclamações, MercadoLíder). Responder com a calma de um SAC normal pode estourar o prazo e derrubar a reputação.

### ✗ Errado

> Tratar a mediação como uma pergunta qualquer, sem urgência e sem avisar o JhEY do prazo.

### ✓ Certo

> Sinalizar no topo: "Isto é uma **mediação aberta no ML** — tem prazo da plataforma pra responder e afeta a reputação do vendedor. Priorizei o rascunho. Resolvendo dentro do prazo, evita virar reclamação." E encadear com `handle-complaint` se precisar de tratativa completa.

Mediação é sempre destacada e priorizada. Reembolso/troca segue com aprovação, pelo próprio ML.
