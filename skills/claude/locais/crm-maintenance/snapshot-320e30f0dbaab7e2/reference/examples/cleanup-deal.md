# Exemplo: faxina de um pedido de atacado parado

Cenário do caminho faxina — o JhEY pede pra auditar um contato/negócio de atacado específico; a skill levanta os achados e espera aprovação. Nada é gravado antes do "ok".

## Cenário

- Contato (aba Contatos): **Pousada Recanto** — `Tipo` Atacado, `Canal` WhatsApp, último pedido 02/04/2026, valor R$ 3.480,00, `Status` Ativo, `Próximo follow-up` "mandar orçamento de lençóis"
- Última conversa registrada na aba Conversas: 02/04/2026
- Conversas recentes (últimos 14 dias): print de WhatsApp de 12/06/2026 — a Keila mandou o orçamento de 40 lençóis e a pousada respondeu "fechado, podem faturar; pra próxima a gente repete em julho"
- Sem print de venda nova no Bling ainda (o pedido foi combinado no WhatsApp, mas o JhEY não anexou o relatório/NF)
- Nenhuma conversa sugere que o cliente virou inativo

## O JhEY diz

> "Confere o cadastro da Pousada Recanto, acho que tá desatualizado."

## Comportamento da skill

**Passo 1 — Identificar a intenção.**
Caminho faxina, mirado num contato nomeado.

**Passo 2 — Reunir contexto.**
Puxa a linha da Pousada Recanto na aba Contatos. Puxa as conversas dos últimos 14 dias (print de WhatsApp de 12/06). Confere a aba Conversas (última linha: 02/04).

**Passo 3 — Achar o contato.**
Contato nomeado direto — sem ambiguidade. `Tipo` já é Atacado.

**Passo 4 — Percorrer o checklist de higiene.**

A skill NÃO grava nada ainda. Produz esta lista de revisão:

> **Revisão de higiene — Pousada Recanto (Atacado)**
>
> **1. Última conversa registrada.** A planilha mostra 02/04/2026. Tem conversa mais nova: print de WhatsApp de 12/06/2026 (orçamento de 40 lençóis aprovado). Não está registrada na aba Conversas.
> **→ Proponho:** registrar a conversa de 12/06 na aba Conversas (canal WhatsApp).
>
> **2. Próximo follow-up.** Está "mandar orçamento de lençóis". O print de 12/06 mostra que o orçamento foi enviado e aprovado, e a pousada falou em repetir em julho.
> **→ Proponho:** `Próximo follow-up`: "mandar orçamento de lençóis" → "retomar recompra de lençóis — 01/07/2026".
>
> **3. Status do contato.** Está Ativo. Conversa de 12/06 confirma cliente ativo. Sem mudança.
> **→ Sem ação.**
>
> **4. Último pedido / valor.** Está 02/04/2026, R$ 3.480,00. O WhatsApp de 12/06 diz "podem faturar" 40 lençóis, mas **não tem print da venda/NF no Bling** — não sei o valor exato faturado.
> **→ Só sinalizar:** me manda o print da venda/NF do Bling desse pedido que eu atualizo `Último pedido` e o valor. Não vou preencher valor no chute.
>
> **5. Tipo.** Já está Atacado. Correto.
> **→ Sem ação.**
>
> **6. Dados de contato.** Telefone/WhatsApp preenchido. E-mail em branco — a pousada nunca informou e-mail. Sem fonte legítima pra preencher.
> **→ Sem ação.**
>
> **7. Duplicados / anotações.** Sem linha duplicada. Sem anotação contraditória.
> **→ Sem ação.**
>
> Aprova os itens 1 e 2 pra gravar? O item 4 fica pendente do print da venda.

**Passo 5 — Portão de aprovação.**
Espera o JhEY. Ele responde: *"Pode gravar 1 e 2. O print da venda eu te mando hoje à tarde."*

**Passo 6 — Executar o aprovado.**
- Acrescenta na aba Conversas: 12/06/2026 · Pousada Recanto · WhatsApp · "Orçamento de 40 lençóis aprovado; faturar; recompra prevista pra julho." · Pedido relacionado: (pendente do print)
- Atualiza `Próximo follow-up` → "retomar recompra de lençóis — 01/07/2026"
- NÃO mexe em `Último pedido` nem no valor (aguardando print)

**Relato.**

> Gravei na base da Pousada Recanto:
> - Conversa de 12/06 registrada (WhatsApp — orçamento de 40 lençóis aprovado)
> - Próximo follow-up → "retomar recompra de lençóis — 01/07/2026"
> Deixei o último pedido/valor como estava — me manda o print da venda/NF do Bling que eu fecho.
> [Planilha de contatos — Google Drive]

## O que este exemplo demonstra

- Todo campo do `reference/cleanup-checklist.md` aplicado a um contato de atacado
- Enquadramento atual → proposto em toda mudança
- Valor de pedido **não** preenchido sem print do Bling — pede a fonte em vez de chutar
- O JhEY aprova só os itens que quer — a skill respeita a seleção exata
- Status `Inativo` nunca tocado automaticamente
