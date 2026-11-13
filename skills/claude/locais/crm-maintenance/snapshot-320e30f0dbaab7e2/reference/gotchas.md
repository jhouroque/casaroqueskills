# Pegadinhas

Casos-limite em que a skill `crm-maintenance` tem mais chance de poluir a base de contatos. Cada item usa o par Certo/Errado.

---

## Pegadinha: tentar "descobrir" telefone/e-mail de quem só apareceu no marketplace

**Por que importa:** Mercado Livre e Shopee **ocultam de propósito** o nome civil, telefone e e-mail do comprador — você só vê o apelido/usuário. Tentar cruzar o apelido com outra base, raspar a tela ou inferir o contato real fere as regras da plataforma e a **LGPD** (dado pessoal usado fora da finalidade). A base só pode guardar o que o cliente forneceu direto.

### ✗ Errado

> Pergunta no ML do apelido `cliente_mari19`. Vou procurar esse apelido no Google e no WhatsApp pra achar o telefone e completar o cadastro.

### ✓ Certo

> Pergunta no ML do apelido `cliente_mari19`. Registro como contato de marketplace (só o apelido) e deixo telefone/e-mail em branco. Se o JhEY confirmar que é a mesma Marina do WhatsApp, eu vinculo — senão, fica separado.

O dado oculto fica oculto. Só preenche telefone/e-mail quando o cliente informou direto (WhatsApp, e-mail, pedido do site).

---

## Pegadinha: criar contato duplicado por causa de e-mail/telefone formatado diferente

**Por que importa:** a busca casa por valor exato. `Sarah.Lin@email.com` e `sarah.lin@email.com`, ou `19 99876-5432` e `+5519998765432`, parecem distintos — e um duplicado silencioso aparece na base do JhEY. Isso destrói a confiança na skill.

### ✗ Errado

> Busquei `Sarah.Lin@email.com` na planilha — sem resultado. Criando novo contato: Sarah Lin (Sarah.Lin@email.com).

Cria um segundo contato; a Sarah que já existia em minúsculas vira duplicata.

### ✓ Certo

> Busquei `sarah.lin@email.com` (sem diferenciar maiúscula) e o telefone só com dígitos — sem resultado. Criando contato: Sarah Lin. Anunciando antes de gravar.

Normalize e-mail pra minúsculas e telefone pra só dígitos (DDD + número) antes de buscar. Anuncie a criação pro JhEY pegar duplicado.

---

## Pegadinha: colar a thread/print inteiro no resumo da conversa

**Por que importa:** a aba Conversas é pra bater o olho rápido, não um arquivo de transcrição. Um print de 15 mensagens colado no campo `Resumo` é inútil; um resumo de duas frases do que ficou combinado é acionável.

### ✗ Errado

> **Resumo:**
> *Cliente: oi, tudo bem? queria saber...*
> *Keila: oi! tudo sim...*
> *[mais 13 mensagens]*

O JhEY rola por cima toda vez.

### ✓ Certo

> **Resumo:** Marina perguntou se o trocador americano cabe no berço padrão e se tem em cinza. Confirmado que sim; enviado o link do site. Sem pedido fechado ainda.

O resumo nomeia a dúvida, a resposta e o estado (fechou ou não).

---

## Pegadinha: criar uma linha de pedido/negócio de atacado quando não dá pra identificar o pedido certo

**Por que importa:** pedido duplicado na planilha é difícil de desembaraçar — divide o histórico, bagunça o follow-up e o JhEY só percebe semanas depois, quando a recompra não bate.

### ✗ Errado

> Não achei pedido em aberto da Pousada Recanto. Criando "Pousada Recanto — novo pedido" e lançando o valor que imaginei.

Agora há dois pedidos da pousada e ninguém sabe qual é o real.

### ✓ Certo

> Não achei pedido em aberto da Pousada Recanto. A qual pedido isso se refere? Opções: (1) fechamento de 02/04 (R$ 3.480,00), (2) é um pedido novo — me manda o print da venda/NF do Bling. Ou prefere não registrar agora?

Pergunte. Nunca crie pedido no lugar do JhEY, e nunca chute valor.

---

## Pegadinha: marcar um contato como `Inativo` por conta própria

**Por que importa:** "sumiu há um tempo" não é a mesma coisa que "não atender mais". O cliente pode estar só fora de época (enxoval é sazonal). Marcar `Inativo` sozinho esconde da base gente que ainda compra.

### ✗ Errado

> Pousada Recanto sem conversa há 95 dias. Mudando `Status` para Inativo.

### ✓ Certo

> Pousada Recanto sem conversa nem pedido há 95 dias. Proponho mudar `Status` para **Parado** (não some da base, só sinaliza pra retomar). `Inativo` (arquivar de vez) eu não marco sozinho — quer que eu marque?

`Parado` é proposta automática; `Inativo` é decisão do JhEY. E nunca apagar a linha — histórico e LGPD pedem manter o registro.

---

## Pegadinha: sobrescrever uma anotação ou um follow-up que o JhEY definiu

**Por que importa:** o JhEY pode ter posto um follow-up que reflete um contexto que a skill não enxerga — uma ligação, um combinado pessoal, uma negociação de atacado em curso. Sobrescrever porque uma conversa recente sugere outra coisa apaga trabalho real.

### ✗ Errado

> `Próximo follow-up` está "aguardar a pousada decidir". A última conversa fala em orçamento de lençóis. Trocando para "mandar orçamento de lençóis".

### ✓ Certo

> `Próximo follow-up` está "aguardar a pousada decidir" (você definiu há 3 dias). A conversa de 12/06 sugere que o orçamento de lençóis também entrou. Proponho juntar ou trocar? Atual → Proposto: "aguardar a pousada decidir" → "aguardar decisão; depois mandar orçamento de lençóis". Aprova?

Mostre o valor atual, proponha a mudança explícita, espere aprovação.
