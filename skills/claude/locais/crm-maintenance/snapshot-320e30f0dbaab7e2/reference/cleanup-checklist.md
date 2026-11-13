# Checklist de higiene da planilha

Os campos que a skill `crm-maintenance` confere numa faxina da planilha de contatos, mais a evidência exigida pra sinalizar cada um. Roda quando o JhEY diz "confere o cadastro da fulana" ou "esse pedido de atacado tá atualizado?", mirado num contato específico.

Percorra todos os itens. Apresente os achados como uma lista de revisão; grave só o que o JhEY aprovar. Datas dd/mm/aaaa, R$ com vírgula.

## 1. Última conversa registrada

**Confira:** A última conversa registrada na aba Conversas é mais antiga que a interação real mais recente (e-mail, WhatsApp, pergunta de ML/Shopee) com esse contato?

**Evidência pra sinalizar:** Uma thread no Gmail, print de WhatsApp ou pergunta de marketplace nos últimos 14 dias com o contato, mais nova que a última linha de conversa dele.

**Ação proposta:** Oferecer registrar a conversa que faltou na aba Conversas. Isso, por si, atualiza a referência de "última conversa".

## 2. Próximo follow-up

**Confira:** O `Próximo follow-up` ainda reflete o que ficou combinado na última conversa?

**Evidência pra sinalizar:** O campo diz "mandar orçamento" e uma conversa posterior mostra que o orçamento já foi enviado. Ou o campo está vazio e uma conversa recente combinou um próximo passo claro (cliente de atacado pediu pra retomar no mês que vem).

**Ação proposta:** Propor uma nova data/ação (ou deixar em branco se o follow-up já foi feito). Mostre atual → proposto lado a lado.

## 3. Status do contato

**Confira:** As interações recentes sugerem que o status mudou — virou `Parado` (sem contato há > 90 dias) ou voltou a ser `Ativo` (comprou de novo)?

**Evidência pra sinalizar:** Sem nenhuma conversa nem pedido há mais de 90 dias → candidato a `Parado`. Pedido novo num contato que estava `Parado` → volta a `Ativo`.

**Ação proposta:** **Só sinalizar `Inativo` — nunca marcar sozinho.** Para `Parado`/`Ativo`, propor a mudança e mostrar a evidência. `Inativo` (não comprar/arquivar) é decisão do JhEY.

## 4. Último pedido / valor

**Confira:** A última conversa/print referencia um pedido mais recente que o registrado em `Último pedido`?

**Evidência pra sinalizar:** Print de uma venda nova no Bling/marketplace, ou um fechamento de atacado confirmado na conversa, com data ou valor diferente do que está na planilha.

**Ação proposta:** Propor atualizar `Último pedido` e `Valor último pedido`. Mostre atual → proposto. Sem print/relatório que confirme, **não preencha valor** — peça o print.

## 5. Tipo (varejo x atacado)

**Confira:** O `Tipo` bate com o comportamento real? Um cliente que fechou compra em quantidade/revenda deveria estar como `Atacado`.

**Evidência pra sinalizar:** Conversa pedindo preço por quantidade, CNPJ informado, recompra recorrente — e o contato está como `Varejo`.

**Ação proposta:** Propor mudar para `Atacado` e agendar um `Próximo follow-up`. Mostre atual → proposto.

## 6. Dados de contato faltando ou ocultos pelo marketplace

**Confira:** Faltam `Telefone/WhatsApp` ou `E-mail` que dá pra preencher com uma fonte legítima?

**Evidência pra sinalizar:** O cliente informou o WhatsApp numa conversa, ou o pedido do site traz o e-mail real — mas a planilha está em branco.

**Ação proposta:** Propor preencher **só com dado que o cliente forneceu direto**. **Nunca** tente "descobrir" telefone/e-mail de um comprador que só apareceu em pergunta de marketplace — o ML/Shopee oculta isso de propósito e raspar/burlar fere as regras da plataforma e a LGPD (ver `reference/gotchas.md`).

## 7. Duplicados e higiene de anotações

**Confira:** Existem duas linhas que parecem o mesmo cliente (mesmo telefone, mesmo e-mail, ou apelido de marketplace muito parecido)? Há anotação antiga (> 90 dias) que contradiz o estado atual?

**Evidência pra sinalizar:** Duas linhas com o mesmo `Telefone/WhatsApp`; ou uma anotação "cliente sumiu" num contato que acabou de comprar.

**Ação proposta:** Propor consolidar as duplicadas numa linha (manter a mais completa, anexar o que falta) — **mostrar lado a lado e esperar aprovação**. Para anotação contraditória, **acrescente** uma nova observação esclarecendo o estado atual — **nunca apague nem reescreva** a antiga.

## Formato de saída

Apresente os achados como lista numerada, cada item mostrando:
- O que foi sinalizado
- A evidência (assunto do e-mail + data, ou canal + data da conversa, ou nº/data do pedido no print)
- A ação proposta (ou "só sinalizar" para `Inativo`)

Depois peça aprovação item a item ou em bloco. Grave só o que for aprovado.
