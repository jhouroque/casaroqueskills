# Pegadinhas — smb-onboard (Casa Roque)

## Pegadinha: Tentar conectar Bling, ML ou Shopee

**Por que importa:** Não existe MCP de Bling, Mercado Livre, Shopee, NuvemShop, NuvemPago ou Contabilizei neste plugin. Ficar procurando "conectar o Bling" trava o onboard e frustra o JhEY.

### ✗ Ruim

> "Agora vamos conectar o Bling pra eu puxar suas vendas automaticamente."

Promete um conector que não existe.

### ✓ Bom

> "Bling, ML e Shopee não têm conector aqui — então eu trabalho com os relatórios que você exporta. Te mostro como tirar o de vendas e o de contas a receber; quando você me manda o CSV, eu rodo tudo. Os conectores deste plugin são Gmail, Agenda, Drive e Canva."

---

## Pegadinha: Re-entrevistar do zero quando o contexto já existe

**Por que importa:** O `CONTEXTO_CASA_ROQUE.md` já tem empresa, equipe, metas e calendário, tudo verificado pelo CEO. Refazer a entrevista inteira desperdiça o tempo do JhEY e ignora a fonte de verdade.

### ✗ Ruim

> "Pra começar, me conta: que tipo de negócio você tem? Quantas pessoas trabalham com você? Quais suas três maiores dores?"

Ignora o contexto que já existe.

### ✓ Bom

> "Já tenho o contexto da Casa Roque aqui: grupo de e-commerce (enxoval/bebê, espumas, decoração), Keila e Emerson na operação, meta de R$ 83,3 mil/mês. Mudou algo na folha, nas metas ou nas ferramentas desde a última vez?"

Confirma e atualiza só o que mudou.

---

## Pegadinha: Sugerir Slack/Teams pra avisar a equipe

**Por que importa:** A equipe da Casa Roque (Keila, Emerson, Thomas) se comunica por **WhatsApp**, não Slack/Teams. Oferecer postar em Slack confunde e nunca vai funcionar — não há conector.

### ✗ Ruim

> "Quer que eu poste o briefing no canal do Slack da equipe?"

Ferramenta que a Casa Roque não usa.

### ✓ Bom

> "Quando o brief ficar pronto, eu gero um bloco curto pra você colar no WhatsApp da equipe, e um rascunho no Gmail se quiser registrar. Você revisa e manda."

WhatsApp (texto pra colar) + Gmail (rascunho). Nunca depende de conector de Slack/Teams.

---

## Pegadinha: Despejar todas as confirmações de uma vez

**Por que importa:** Várias perguntas juntas viram formulário, não conversa. O JhEY responde por cima ou abandona.

### ✗ Ruim

> "Confirma pra mim: (1) folha, (2) metas, (3) ferramentas, (4) calendário, (5) cadência."

### ✓ Bom

Pergunte uma de cada vez, espere a resposta completa, siga pra próxima. Como o contexto já existe, na maioria das vezes é só um "segue igual" — não force as cinco se o JhEY já confirmou que nada mudou.

---

## Pegadinha: Gravar mudança no contexto sem mostrar antes

**Por que importa:** O `CONTEXTO_CASA_ROQUE.md` é a fonte de verdade de todas as skills. Escrita silenciosa pode quebrar um número que o CEO verificou.

### ✗ Ruim

> "Pronto, atualizei o contexto da Casa Roque!"

Sem prévia, sem aprovação.

### ✓ Bom

> "Você disse que o salário do Emerson subiu. Vou trocar no contexto:
> • Antes: Emerson R$ 1.400,00/mês
> • Depois: Emerson R$ [novo valor]/mês
> Confirma que gravo?"

Mostre atual vs proposto, espere o "ok", aí grave.

---

## Pegadinha: Pular o "provar valor"

**Por que importa:** Se o JhEY conecta o Google mas o Claude vai direto pra cadência, o momento "aha" não acontece. Rodar uma skill com um relatório real é o que mostra que valeu a pena.

### ✗ Ruim

> "Google conectado! Agora vamos definir a cadência semanal."

### ✓ Bom

> "Google conectado. Me manda o relatório de vendas dos últimos 7 dias do Bling (CSV) que eu rodo a `business-pulse` agora e te mostro o pulso."
> *[roda a skill, mostra o resultado]*
> "Isso fica disponível sempre. Agora a cadência da semana…"
