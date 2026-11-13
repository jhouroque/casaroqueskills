---
name: customer-pulse
version: 0.2.0
description: >
  Junta o que os clientes da Casa Roque andam dizendo — avaliações do Mercado
  Livre e da Shopee, reclamações e mediações dos marketplaces, Reclame Aqui,
  SAC no WhatsApp e comentários no Instagram (mais reviews colados/exportados)
  — num relatório de temas com evidência literal e uma lista "faça estas 3
  coisas esta semana". Gatilho quando o JhEY pergunta como os clientes estão,
  pede uma análise das avaliações, o que estão falando, ou sobre
  reclamações/mediações. Meta: avaliação 5,0★.
---

# Pulso do Cliente (customer-pulse)

## Início rápido

Pergunte: *"Como os clientes estão neste mês?"*

O Claude junta avaliações do ML/Shopee, reclamações e mediações dos marketplaces, prints do SAC no WhatsApp, comentários do Instagram e qualquer review colado dos últimos 30 dias, agrupa em 3–5 temas com evidência literal e entrega a lista "faça estas 3 coisas esta semana".

> **Sem conector de marketplace.** A Casa Roque **não tem** MCP de Mercado Livre, Shopee, Reclame Aqui nem Instagram. As avaliações, reclamações, mediações e comentários vêm de **print/export** que o JhEY ou a Keila anexam, ou de texto colado. O Gmail **tem** conector. Quando faltar a fonte, registre na seção "Fontes" e siga — nunca invente número de avaliação ou volume (ver `reference/gotchas.md`).

## Fluxo de trabalho

1. **Defina a janela de tempo.** Padrão: últimos 30 dias. Se o JhEY indicar um intervalo, use o dele.

2. **Reúna as avaliações do ML e da Shopee.** Pegue as avaliações do período (nota em estrelas + comentário). **Sem conector** → peça o print/export: "me manda o print das avaliações recentes do ML e da Shopee". Se não veio nada, registre `Avaliações ML/Shopee: n/d — sem print` na seção Fontes e siga. **Não estime a nota** (ver `reference/gotchas.md`).

3. **Reúna reclamações e mediações dos marketplaces.** Reclamações abertas, mediações do Mercado Livre (quando o cliente aciona a plataforma) e disputas da Shopee. **Sem conector** → print/relatório. Se vier 0, registre `Mediações/reclamações: 0` e siga — sem alarde. A mediação do ML é sensível: ver `reference/gotchas.md`.

4. **Reúna o Reclame Aqui.** Reclamações públicas no Reclame Aqui da Casa Roque no período. **Sem conector** → print/export. Reclamação pública pesa mais na reputação — destaque, mas não infle a amostra (1 reclamação pública ≠ tendência).

5. **Reúna o SAC no WhatsApp.** Prints das conversas de atendimento (a Keila atende 3–4x/dia, POP 4; o JhEY cobre 13–17h temporariamente). Extraia o assunto e 1–2 frases por conversa. **Sem conector de WhatsApp** → texto colado/print.

6. **Reúna os comentários do Instagram (@casaroque.design).** Comentários e DMs com dúvida, elogio ou reclamação no período. **Sem conector** → print. Trate como sinal de marca/atendimento, não de pós-venda transacional.

7. **Puxe as threads do Gmail.** Busque threads no período com termos como: `reembolso cancelar troca devolução defeito atrasou atraso quebrado errado faltando não chegou insatisfeito reclamação`. Extraia o assunto e um trecho de 1–2 frases por thread.

8. **Aceite reviews colados (opcional).** Se o JhEY colar texto de avaliações (ML, Shopee, Google, Reclame Aqui), inclua no conjunto marcado como `[Avaliação]`. Sem conector necessário.

9. **Extraia os temas.** Agrupe toda a evidência em 3–5 temas recorrentes. Cada tema deve ter:
   - Um rótulo de uma frase (ex.: "Atraso na entrega gerando reclamação repetida")
   - 2–3 citações **literais** com a tag da fonte: `[ML]`, `[Shopee]`, `[Reclame Aqui]`, `[WhatsApp]`, `[Instagram]`, `[Gmail]` ou `[Avaliação]`
   - Uma contagem de sinais (quantos itens tocam o tema)

   Citação literal é inegociável — **nunca parafraseie**. Veja o antipadrão em `reference/gotchas.md`.

10. **Gere a lista "faça estas 3 coisas".** Ordene os temas por contagem de sinais. Pegue os 3 primeiros e escreva um passo concreto e acionável pro JhEY por tema. Formate como checklist numerado. Amarre cada ação aos POPs/ operação quando fizer sentido (ex.: ajustar POP de devolução/troca, revisar a foto do anúncio, treinar a Keila num roteiro de resposta).

11. **Entregue o relatório.** Estruture a saída nesta ordem:
    - **Cabeçalho** — H2 com "Pulso do Cliente" e o intervalo de datas.
    - **Fontes puxadas** — lista com a contagem de sinais por fonte (avaliações ML/Shopee, mediações/reclamações, Reclame Aqui, SAC WhatsApp, Instagram, Gmail, reviews colados). Marque a fonte que veio `n/d` por falta de print.
    - **Temas** — para cada tema, um rótulo numerado em negrito com a contagem de sinais, seguido de 2 citações literais como blockquote, cada uma com a fonte.
    - **Avaliação x meta** — se houver nota informada, mostre a média do período vs a **meta 5,0★** (manter > 4,5). Sem nota, escreva "n/d — sem print das avaliações". Nunca chute a nota.
    - **Faça estas 3 coisas esta semana** — lista numerada de três passos concretos e acionáveis, cada um ligado a um dos temas do topo.

    Para um exemplo completo, veja [reference/examples/example-report.md](reference/examples/example-report.md).

## Portões de aprovação

Esta skill é **somente leitura** — não posta, não envia, não responde nem altera registro. Não há portão de aprovação. Se um tema sugerir responder um cliente ou abrir uma tratativa, encaminhe pra `handle-complaint` ou `ticket-deflector` (que têm os portões) — aqui é só diagnóstico.

## Referências

- [reference/gotchas.md](reference/gotchas.md) — viés de avaliação, amostra pequena, mediação do ML, marketplace sem conector, exigência de citação literal
- [reference/examples/example-report.md](reference/examples/example-report.md) — exemplo completo de relatório da Casa Roque
