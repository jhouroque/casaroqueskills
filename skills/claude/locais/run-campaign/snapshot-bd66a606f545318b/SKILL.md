<!-- C:\Users\Jhonatas\AppData\Roaming\Claude\local-agent-mode-sessions\c5e8a475-a351-48d2-8db3-3f0857ad643d\1d524d29-2570-4e4b-8d1f-844a61e14635\local_f6e23d68-ce2b-4eec-b343-aeec8fb24add\outputs\cr-plugin\small-business\skills\run-campaign\SKILL.md -->
---
name: run-campaign
description: Roda uma campanha de marketing da Casa Roque ponta a ponta — análise de vendas (Bling/ML/Shopee), plano de conteúdo, artes no Canva e publicação (Instagram/Facebook via Content Planner, banner NuvemShop, Google Ads). Sem HubSpot/CRM. Gatilhos "rodar campanha", "vendas caíram", "preciso de mais clientes", "bora bombar uma data". Aceita argumentos opcionais de janela e canal.
allowed-tools: Read, WebFetch, Bash
---

Rode a campanha inteira encadeando as skills na ordem. O JhEY aprova em cada handoff — nunca avance um portão sem confirmação explícita. Nada vai ao ar sem o "ok".

Argumentos:
- `--janela` (padrão `90d`) — quanto olhar pra trás na análise de vendas
- `--canal` (padrão `todos`) — `instagram`, `site`, `ads` ou `todos`

## Passo 1 — Análise de vendas + plano de conteúdo (content-strategy)

Dispare o fluxo da skill `content-strategy`:
1. Leia os dados de venda dos relatórios/CSV do Bling, Mercado Livre, Shopee e site (NuvemShop) na janela escolhida. Não há conector — peça o export se faltar ("me manda o relatório de vendas por produto do Bling, 90 dias, CSV").
2. Identifique o quadro: campeões, parados, queda de vendas (qual produto, qual período, magnitude) e a data sazonal que está chegando (Dia das Mães, Black Friday, Natal, Dia das Crianças, volta às aulas).
3. Produza o plano de 30 dias: o que empurrar, qual oferta rodar, o que segurar (Instagram @casaroque.design + blog NuvemShop).
4. Apresente o plano ao JhEY. Espere o "aprovado, monta as artes" explícito antes de seguir.

Se o JhEY editar o plano, incorpore e reapresente.

## Passo 2 — Artes + preparo da publicação (canva-creator)

Após aprovar o Passo 1, dispare o fluxo da skill `canva-creator`:
1. Use o plano aprovado do Passo 1 como entrada.
2. Monte o calendário de postagem alinhado às prioridades do plano.
3. Gere as artes no Canva (Pro, casaroque.design) pra cada post/banner — aprovação a cada arte antes de seguir.
4. Escreva legendas (Instagram/Facebook) e o texto de e-mail.
5. Prepare a publicação SEM HubSpot: **agendar no Content Planner do Canva** (Instagram/Facebook), **banner exportado pro site NuvemShop** (o JhEY sobe), **rascunho de e-mail no Gmail**. Status sempre agendado/rascunho — nada publicado.
6. Apresente a campanha preparada ao JhEY. Espere o "aprovado, pode pôr no ar" explícito antes do Passo 3.

## Passo 3 — Distribuição paga (Google Ads) — opcional

Após aprovar o Passo 2, se a campanha pede alcance pago (e o `--canal` inclui `ads`), trabalhe o tráfego junto com o Thomas (gerente de tráfego, KPIs ROI > 3x, CPC < R$ 2,00):

1. Não há conector de Google Ads no plugin — a operação da conta é do Thomas. A skill **prepara o briefing**, não mexe na conta:
   - Conta ativa: **568-607-6835** (Performance Max, R$ 35/dia). [confirmar se vai subir verba ou criar campanha nova pra a data]
   - Produto-foco da campanha (do plano), público e criativos (as artes do Passo 2).
   - Metas: ROI > 3x, CPC < R$ 2,00, conversão do site 3%.
2. Produza dois entregáveis:
   - **Briefing de tráfego** — produto, oferta, criativos, verba sugerida e metas, pro Thomas executar no Google Ads (resumo no chat + rascunho no Gmail + bloco pra colar no WhatsApp).
   - **Resumo orgânico** — o que vai ao ar no Instagram/Facebook (Content Planner) e o banner do site, pra alinhar o orgânico com o pago.
3. Bloqueie um horário na Google Agenda pro JhEY/Thomas revisarem a campanha antes de subir verba.
4. Apresente os dois. Espere o "pode subir" explícito antes de marcar a campanha como "no ar".

> Se o `--canal` não inclui `ads`, encerre no Passo 2 (orgânico + banner + e-mail) e ofereça o briefing de tráfego como passo opcional.

## Portões de aprovação (invioláveis)

- Nunca avance entre passos sozinho. Cada handoff precisa de aprovação explícita do JhEY.
- Nunca ponha post/banner/e-mail no ar sem o "ok". Posts ficam agendados no Content Planner; banner e e-mail ficam prontos pro JhEY subir/enviar.
- Nunca mexa na conta do Google Ads — a skill prepara o briefing; quem opera é o Thomas.
- Se faltar uma fonte de dados (relatório de venda) ou um conector (Canva, Gmail), pare, diga o que faltou e pergunte se peço o arquivo, tento de novo ou aborto.

## Saída

Encerre com um resumo de um parágrafo: queda/oportunidade identificada, artes geradas, o que foi agendado no Content Planner, banner pronto, e-mail em rascunho, briefing de tráfego entregue (se aplicável). Sem HubSpot — toda a distribuição é Instagram/Facebook (Content Planner), site (banner NuvemShop), e-mail (Gmail) e, opcional, Google Ads via Thomas.
