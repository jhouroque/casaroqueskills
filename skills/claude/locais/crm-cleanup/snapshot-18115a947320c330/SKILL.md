---
name: crm-cleanup
description: Faz uma faxina na planilha de contatos da Casa Roque (Google Sheets/Drive) — acha pedidos/contatos de atacado parados, linhas duplicadas e campos faltando, e corrige o que o JhEY aprovar. Aceita um argumento opcional de escopo: pedidos, contatos ou tudo.
allowed-tools: Read, WebFetch, Bash
---

Rode uma faxina na **planilha de contatos** usando o fluxo de faxina da skill `crm-maintenance`. Aja na hora — o JhEY digitou /crm-cleanup, então pule a etapa de detectar intenção.

> **Não há CRM.** A base é uma planilha no Google Sheets/Drive (abas **Contatos** e **Conversas**). O Drive tem conector. Pedido e dado de cliente vêm de print/relatório (CSV/PDF) do Bling/marketplace, que não têm conector. Datas dd/mm/aaaa, R$ com vírgula.

Interprete os argumentos:
- `--escopo` (padrão: `tudo`) — `pedidos` só pra auditar negócios/pedidos de atacado, `contatos` só pra deduplicar/checar campos, `tudo` pros dois

## Passo 1 — Achar pedidos/contatos de atacado parados

Se o escopo inclui pedidos:

1. Puxe os contatos `Tipo = Atacado` da aba Contatos.
2. Sinalize os que estão sem conversa nem pedido há mais de 90 dias (`Status` ainda Ativo, mas frio).
3. Para cada parado: mostre nome, canal, último pedido (data/valor), `Status` e `Próximo follow-up`.
4. Proponha ações por contato: atualizar follow-up, mudar `Status` para Parado, acrescentar observação. **Nunca** dar por "ganho/perdido" nem marcar `Inativo` sozinho.

Apresente a lista completa de parados antes de mexer em qualquer coisa.

## Passo 2 — Achar contatos duplicados

Se o escopo inclui contatos:

1. Busque na aba Contatos linhas que parecem a mesma pessoa: mesmo `Telefone/WhatsApp` (só dígitos), mesmo `E-mail` (sem diferenciar maiúscula), ou nome/apelido muito parecido no mesmo canal.
2. Para cada par/grupo de duplicatas: mostre as linhas lado a lado — nome, canal, telefone, e-mail, último pedido, última conversa.
3. Proponha qual linha manter (a mais completa) e quais campos juntar.

Apresente todos os grupos de duplicatas antes de consolidar qualquer um. **Lembre:** apelido de marketplace ≠ telefone/e-mail; não force vínculo entre um contato de ML/Shopee e um de WhatsApp sem o JhEY confirmar (ver `crm-maintenance/reference/gotchas.md`).

## Passo 3 — Achar campos faltando

1. Confira os contatos `Ativos` por campos faltando: `Canal`, `Status`, `Tipo`. Para clientes que compraram, `Último pedido`/`Valor`.
2. Confira `Telefone/WhatsApp` e `E-mail` faltando — mas só proponha preencher com dado que o cliente **forneceu direto** (numa conversa, no pedido do site). **Nunca** tente descobrir contato de comprador que só apareceu em pergunta de marketplace (LGPD + regras da plataforma).
3. Apresente uma tabela das linhas com campos faltando e o que falta.

## Passo 4 — Aplicar as correções aprovadas

1. Percorra cada achado dos Passos 1–3.
2. Aplique só as mudanças que o JhEY aprovar explicitamente.
3. Reporte cada mudança feita, com o link da planilha quando der.

## Falhas de conector

Se o Google Drive/Sheets estiver fora do ar, pare — este comando precisa da planilha como fonte. Diga ao JhEY: "Não consegui abrir a planilha de contatos no Drive. Confirma o acesso nas configurações do Cowork e roda /crm-cleanup de novo." Se faltar o print/relatório do Bling pra confirmar um valor de pedido, sinalize o item e siga — não preencha valor no chute.

## Portões de aprovação

- **Nunca apague linha.** Nem contato, nem conversa, nem pedido. Se o JhEY pedir, diga que a skill não apaga (histórico + LGPD) e oriente a marcar `Status = Inativo` ou arquivar.
- **Nunca mude `Status` para Inativo nem dê um pedido por ganho/perdido sem aprovação explícita.** Mesmo com indício forte. `Parado` pode propor; `Inativo` é decisão do JhEY.
- **Nunca consolide duplicatas sozinho.** Mostre lado a lado e espere aprovação por par.
- **Diffs lado a lado em toda mudança.** Mostre valor atual e valor proposto; espere aprovação item a item.

## Saída

Termine com um resumo: X contatos/pedidos atualizados, Y duplicatas consolidadas, Z campos preenchidos. Inclua o link da planilha.
