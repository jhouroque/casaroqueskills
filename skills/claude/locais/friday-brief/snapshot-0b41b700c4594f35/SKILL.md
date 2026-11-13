---
name: friday-brief
description: Entrega o pulso de sexta da Casa Roque — receita vs semana anterior, mais vendidos, ROI/CPC dos Ads da semana, ganhos e o que vigiar. Roda na sexta, depois do relatório de tráfego do Thomas e antes do batimento das 15h. Aceita janela de comparação de 7 ou 14 dias. Gatilho com "pulso de sexta", "como a gente foi essa semana", "fechamento da semana" ou "resumo de sexta".
allowed-tools: Read, WebFetch, Bash
---

Rode o pulso de sexta — ganhos e vigias. Puxe os números, mostre o que importa e dê ao JhEY um quadro limpo do fim de semana. **Roda na sexta, depois do relatório de tráfego do Thomas (POP 5) e antes do batimento das 15h (Keila + Emerson).**

> **Sem conector de venda.** Receita e vendas vêm de **relatório/CSV/print do Bling e dos marketplaces** que o JhEY anexa, mais o relatório de tráfego que o Thomas manda toda sexta. Sem dado anexado, marque "n/d" e ofereça pedir o relatório — nunca invente número.

Interprete os argumentos:
- `--lookback` (padrão `7d`) — `7d` para uma semana ou `14d` para comparação móvel de duas semanas

## Passo 1 — Pulso de receita

Usando o fluxo da skill `business-pulse`:

1. Some a receita do período (ML + Shopee + site) a partir do relatório/CSV do Bling ou dos marketplaces.
2. Calcule a variação de receita semana a semana.
3. Mostre as 3 maiores fontes de receita (produto / canal) ranqueadas por contribuição.

Se nada foi anexado, peça objetivamente: "me manda o relatório de vendas dos últimos 7 dias do Bling ou um print do ML/Shopee que eu fecho o pulso."

## Passo 2 — Detalhe de vendas

1. Liste os **5 mais vendidos** (produto) por volume e receita.
2. Liste os **3 que ficaram abaixo** do esperado vs o período anterior.
3. Sinalize qualquer item com pico ou queda súbita (> 20% de variação).

Use os produtos reais da casa quando aparecerem: trocadores, berços, kits/ninhos, espumas (D23/D28/D33/D44), lençóis, plumante.

## Passo 3 — ROI / CPC dos Ads da semana

A partir do **relatório de tráfego que o Thomas manda toda sexta** (POP 5):

1. **ROI** da semana — meta da casa **> 3x**. Sinalize se ficou abaixo.
2. **CPC** médio — meta **< R$ 2,00**. Sinalize se estourou.
3. Conversão do site (meta 3%) e gasto da semana (Performance Max ~R$ 35/dia na conta 568-607-6835), se vierem no relatório.

Se o relatório do Thomas ainda não chegou, marque a seção "n/d — aguardando relatório do Thomas" e siga.

## Passo 4 — Resumo de ganhos e vigias

Formate a saída assim:

```
Pulso de Sexta — {dd/mm/aaaa}

GANHOS
• {ganho 1}
• {ganho 2}
• {ganho 3}

VIGIAR
• {vigia 1} — {ação recomendada}
• {vigia 2} — {ação recomendada}

Receita da semana: R$ {valor} ({▲/▼}X% vs semana anterior)
Ads: ROI {X}x (meta >3x) · CPC R$ {Y} (meta <R$ 2,00)
```

## Falhas de fonte

Rode com o que estiver à mão — degrade com elegância. Sem relatório de vendas, marque "n/d — sem relatório do Bling/marketplace" e siga com Ads e perguntas. Sem relatório do Thomas, pule a seção de Ads e anote. Se nada de receita nem tráfego veio, pare e diga: "Sem dado de vendas nem o relatório do Thomas. Me manda um dos dois que eu rodo o pulso de sexta."

## Portões de aprovação

- **Nunca envie nem poste o brief automaticamente.** Sempre mostre primeiro pro JhEY revisar.
- **Nunca cancele nem altere nada.** Só superfície dados e recomendações.
- **Nunca poste número ruim sem avisar.** Queda de vendas ou ROI abaixo de 3x → sinalize antes de gerar bloco de WhatsApp.

## Saída

Termine com o brief formatado e pergunte ao JhEY: "Quer que eu gere um rascunho no Gmail, um bloco pra colar no WhatsApp da equipe, ou salve no Drive?"
