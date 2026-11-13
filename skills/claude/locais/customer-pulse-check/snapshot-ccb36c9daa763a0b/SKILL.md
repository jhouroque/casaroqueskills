---
name: customer-pulse-check
description: Sintetiza os temas das avaliações ML/Shopee, reclamações/mediações, Reclame Aqui, SAC WhatsApp e comentários do Instagram da Casa Roque numa lista dos 3 problemas mais resolvíveis, com rascunhos de resposta. Aceita um argumento opcional de data inicial.
allowed-tools: Read, WebFetch, Bash
---

Rode a síntese da voz do cliente. Reúna os sinais de feedback de todas as fontes disponíveis, identifique os temas que dá pra resolver de fato e produza rascunhos de resposta que o JhEY/Keila revisam e enviam.

> **Sem conector de marketplace.** Avaliações, reclamações, mediações, Reclame Aqui e Instagram vêm de **print/export** anexado ou texto colado. Gmail tem conector. Sem fonte, não invente número — marque `n/d` e ofereça pedir o print. Datas dd/mm/aaaa, R$ com vírgula.

Interprete os argumentos:
- `--desde` (padrão: últimos 30 dias) — data inicial `aaaa-mm-dd` da janela

## Passo 1 — Reunir os sinais de feedback

Usando o fluxo da skill `customer-pulse`:

1. Reúna as avaliações do ML/Shopee do período (nota + comentário) — print/export.
2. Reúna reclamações, **mediações do ML** e disputas da Shopee — print/relatório.
3. Reúna o Reclame Aqui do período — print/export.
4. Reúna o SAC no WhatsApp (prints) e os comentários do Instagram (@casaroque.design).
5. Puxe as threads do Gmail (termos: `reembolso cancelar troca devolução defeito atrasou quebrado errado faltando não chegou reclamação`).
6. Se houver arquivos de export (CSV de avaliações, export do Reclame Aqui) no Drive/Files, leia e parseie.
7. Conte o total de sinais por fonte.

## Passo 2 — Extração de temas

Agrupe todos os sinais em temas recorrentes. Para cada tema:
- Conte quantos sinais o mencionam
- Classifique: Qualidade do produto / Entrega / Pagamento-repasse / Comunicação / Expectativa errada (anúncio) / Outro
- Avalie o impacto: 🔴 Alto (risco de reputação/mediação/perda de cliente) / 🟡 Médio / 🟢 Baixo

Destaque **mediação do ML** sempre à parte — afeta a reputação do vendedor e tem prazo da plataforma (ver `customer-pulse/reference/gotchas.md`).

## Passo 3 — Top 3 problemas resolvíveis

Usando o fluxo da skill `ticket-deflector`:

Selecione os 3 temas por: frequência × impacto. Para cada um:
1. Diga o problema em uma frase
2. Explique a causa-raiz (quando evidente)
3. Sugira uma correção operacional concreta (ex.: revisar a descrição do anúncio, ajustar o POP de devolução/troca, antecipar aviso de prazo)
4. Rascunhe um template de resposta ao cliente, no tom da Casa Roque (empático, direto, em pt-BR)

Formato do template de resposta:
```
Assunto: Re: {tema do contato}

Olá, {primeiro nome}!

Obrigada por falar com a gente. {Reconhecimento da experiência dele em 1-2 frases}.

{O que vamos fazer / o que aconteceu / a solução oferecida}.

{Próximo passo ou oferta}.

Um abraço,
Equipe Casa Roque
```
> O SAC da Casa Roque é feito pela **Keila** (POP 4). O tom é acolhedor e resolutivo. Reembolso/troca segue o **POP de devolução/troca** e acontece **no marketplace de origem (ML/Shopee) ou via Pix** — nunca prometa estorno por outro meio. Cite o **CDC** (direito de arrependimento de 7 dias em compra online) quando couber. Tudo com aprovação do JhEY/Keila antes de enviar.

## Passo 4 — Tabela-resumo

Formate a saída assim:

```
Voz do Cliente — {intervalo}
Total de sinais: {n} (Avaliações ML/Shopee: {n} | Mediações/reclamações: {n} | Reclame Aqui: {n} | SAC WhatsApp: {n} | Instagram: {n} | Gmail: {n})
Média de avaliação: {x,x}★ vs meta 5,0★   [ou "n/d — sem print"]

TOP 3 PROBLEMAS RESOLVÍVEIS
1. {Problema} ({frequência}) — {impacto} — Correção: {correção em uma linha}
2. {Problema} ({frequência}) — {impacto} — Correção: {correção em uma linha}
3. {Problema} ({frequência}) — {impacto} — Correção: {correção em uma linha}
```

## Falhas de conector

Rode com o que estiver disponível — este comando degrada com elegância. Sem print das avaliações, marque "Avaliações ML/Shopee: n/d — sem print" e siga. Sem prints do Reclame Aqui/mediações, idem. Se nenhuma fonte foi anexada e o Gmail não tem nada, pare e diga ao JhEY: "Não recebi nenhuma fonte de feedback. Me manda pelo menos um print das avaliações do ML/Shopee, do Reclame Aqui ou um export de reviews que eu rodo."

## Portões de aprovação

- **Nunca envie resposta automaticamente.** Apresente rascunhos pro JhEY/Keila revisarem.
- **Nunca prometa reembolso/troca aqui.** Sinalize a opção; reembolso/troca é sempre pelo marketplace de origem (ML/Shopee) ou Pix, com aprovação do JhEY/Keila.
- **Nunca exponha dado pessoal do cliente no resumo** — use primeiro nome + inicial (ou o apelido do marketplace). Atenção à LGPD.

## Saída

Apresente a tabela-resumo, depois cada template de resposta. Pergunte ao JhEY/Keila quais templates querem usar e espere a aprovação explícita antes de preparar o envio.
