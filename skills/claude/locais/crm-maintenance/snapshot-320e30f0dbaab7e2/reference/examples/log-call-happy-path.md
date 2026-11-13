# Exemplo: registrar uma conversa de WhatsApp (contato que não existia)

Cenário do caminho conversa — chega uma conversa de WhatsApp de um cliente que ainda não está na planilha de contatos.

## Cenário

- A Keila acabou de atender no WhatsApp da loja (faixa 13–17h, hoje 18/06/2026)
- Cliente: número +55 19 99876-5432, se apresentou como "Marina"
- Assunto: perguntou se o trocador americano cabe no berço padrão e se tem em cinza; a Keila confirmou que sim e mandou o link do produto no site
- A Marina **não** está na aba Contatos da planilha
- O JhEY cola/encaminha o print da conversa

## O JhEY diz

> "Registra essa conversa do WhatsApp na base."

## Comportamento da skill

**Passo 1 — Identificar a intenção.**
Caminho conversa (WhatsApp).

**Passo 2 — Reunir contexto.**
Lê o print: data 18/06/2026, número +55 19 99876-5432, nome informado "Marina", assunto trocador americano (medida + cor cinza), Keila mandou o link do site. Sem pedido fechado ainda — é pré-venda.

**Passo 3 — Achar o contato na planilha.**
- Busca na aba Contatos por `Telefone/WhatsApp` = 19 99876-5432 → não existe.
- Anuncia a criação do contato:

> *"A Marina (WhatsApp 19 99876-5432) não está na base. Vou criar a linha e marcar como pré-venda. Confirma?"*

Cria a linha na aba Contatos: `Nome` Marina · `Canal` WhatsApp · `Telefone/WhatsApp` 19 99876-5432 · `Tipo` Varejo · `Status` Ativo · `E-mail` (em branco — não informado) · `Último pedido` (em branco — pré-venda).

**Passo 4 — Executar.**
Acrescenta uma linha na aba Conversas:
- `Data`: 18/06/2026
- `Contato`: Marina
- `Canal`: WhatsApp
- `Resumo`: "Perguntou se o trocador americano cabe no berço padrão e se tem em cinza. Confirmado que sim; enviado o link do produto no site."
- `Pedido relacionado`: (em branco — pré-venda)

Como é pré-venda quente, propõe um follow-up:
> *"Quer que eu agende `Próximo follow-up` pra 21/06 — checar se a Marina fechou o trocador?"*

**Passo 5 — Portão de aprovação.**
A criação do contato foi anunciada antes de gravar. O registro da conversa é inline porque o JhEY pediu explicitamente "registra essa conversa". O follow-up só é gravado se o JhEY topar.

**Passo 6 — Relato.**

> Registrei na base:
> - Novo contato: Marina (WhatsApp 19 99876-5432) — Varejo, Ativo
> - Conversa de 18/06 (WhatsApp — dúvida sobre trocador americano cinza; enviado link do site)
> Sugeri follow-up dia 21/06 pra ver se ela fechou — quer que eu agende?
> [Planilha de contatos — Google Drive]

## O que este exemplo demonstra

- Criar contato a partir de uma conversa de WhatsApp, com anúncio antes de gravar
- Telefone preenchido porque o cliente informou direto (legítimo) — sem e-mail, que ela não deu
- Resumo curto na aba Conversas, não o print inteiro
- Follow-up de pré-venda proposto, não gravado sem aprovação
- Nenhum dado de cliente "descoberto" por fora — só o que veio na conversa
