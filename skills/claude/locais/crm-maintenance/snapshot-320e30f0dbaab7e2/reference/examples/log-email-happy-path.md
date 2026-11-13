# Exemplo: registrar uma pergunta de marketplace num contato existente (caminho feliz)

Cenário do caminho e-mail/pergunta — chega uma pergunta no Mercado Livre de um comprador que já está na planilha; o contato resolve sem ambiguidade e a conversa registra limpo.

## Cenário

- O JhEY encaminha/cola o print de uma **pergunta no Mercado Livre** sobre o anúncio do kit berço
- A pergunta é do comprador de apelido **`cliente_mari19`**: "Esse kit serve em berço americano? Quantas peças vêm?"
- Na aba Contatos já existe uma linha **Marina** com `Canal` WhatsApp — e o JhEY confirma que `cliente_mari19` é a mesma Marina (ela já tinha falado no WhatsApp antes)
- A Keila respondeu a pergunta no próprio ML

## O JhEY diz

> "Anota essa pergunta do ML na conversa da Marina."

## Comportamento da skill

**Passo 1 — Identificar a intenção.**
Caminho e-mail/pergunta (pergunta de marketplace).

**Passo 2 — Reunir contexto.**
Lê o print: canal Mercado Livre, apelido `cliente_mari19`, pergunta sobre o kit berço (serve em berço americano + quantidade de peças), respondida pela Keila. **Atenção:** o ML mostra só o apelido — não há nome civil, telefone nem e-mail nessa tela.

**Passo 3 — Achar o contato na planilha.**
- O JhEY já indicou que `cliente_mari19` = Marina (linha existente). Sem ambiguidade.
- **Não** tenta cruzar/“descobrir” o telefone a partir do apelido do ML — a vinculação veio do JhEY, que tem o contexto. Sem essa confirmação, a skill deixaria como contato separado e perguntaria (ver `reference/gotchas.md`).

**Passo 4 — Executar.**
Acrescenta uma linha na aba Conversas:
- `Data`: 18/06/2026
- `Contato`: Marina
- `Canal`: Pergunta ML
- `Resumo`: "Perguntou se o kit berço serve em berço americano e quantas peças vêm. Respondido no ML."
- `Pedido relacionado`: (em branco — pré-venda)

Como a Marina já apareceu por dois canais (WhatsApp + ML), anota o apelido do ML na observação do contato pra futuras vinculações (sem sobrescrever campos do JhEY).

**Passo 5 — Portão de aprovação.**
Contato já existia — sem anúncio de criação. O registro da conversa é inline porque o JhEY pediu explicitamente.

**Passo 6 — Relato.**

> Registrei na conversa da Marina:
> - 18/06 · Pergunta ML (`cliente_mari19`) · dúvida sobre kit berço (serve em berço americano? quantas peças?) — respondida no ML
> Marquei que `cliente_mari19` no ML é a Marina, pra próxima já cair certo.
> [Planilha de contatos — Google Drive]

## O que torna isto o caminho feliz

- Vinculação apelido-do-ML → contato confirmada pelo JhEY (não inferida pela skill)
- Sem dado de cliente "descoberto" — o ML oculta telefone/e-mail e a skill respeita isso
- Resumo foca na dúvida e na resposta, não no print inteiro
- Canal registrado como `Pergunta ML` (valor padrão), mantendo os filtros da planilha
