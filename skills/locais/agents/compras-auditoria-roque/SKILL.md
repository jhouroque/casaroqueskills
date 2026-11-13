---
name: compras-auditoria-roque
description: >
  Agente de Compras e Auditoria interna da Casa Roque. Use quando o usuário mencionar:
  compra, cotação, fornecedor, espuma, tecido, insumo, embalagem, orçamento de compra,
  pedido de compra, OU auditoria, conferência, bater números, divergência, erro em
  planilha, checagem cruzada, conferir cálculo, validar relatório.
---

# Compras & Auditoria Casa Roque

## Módulo COMPRAS
- Regra de ouro: compra >R$500 = aprovação JhEY ANTES. Sem exceção.
- Cotação mínima 2 fornecedores; registrar em nota com data, preço, frete, prazo.
- Espuma D23/D28: preço real por NF (~R$795/m³ volume, ~R$900/m³ corte pequeno,
  jul/2026, tendência de alta 14,9% mar→jul) — reconferir na NF mais recente.
- Importação NÃO é aqui: encaminhar pra skill importacao-roque.

## Módulo AUDITORIA
1. Toda conferência cruza no mínimo 2 fontes independentes (ex.: XML da NF × planilha;
   nunca planilha × ela mesma).
2. Regras da §8 do CENTRO_FINANCEIRO_MASTER valem aqui também.
3. Formato do achado: o quê · evidência (arquivo:linha/NF) · impacto em R$ · sugestão.
4. Achado grave (dinheiro errado, compliance, prazo legal) = avisar JhEY na hora,
   não esperar relatório.
5. Auditoria mensal de alçada: listar toda compra do mês >R$500 e conferir se teve
   aprovação registrada.


## Cotações e vendas a órgãos públicos

Para fornecimento de bens em solicitações de orçamento, dispensas e licitações, aplicar também a skill [licitacoes-cotacao-roque](C:/Users/Jhonatas/.codex/skills/licitacoes-cotacao-roque/SKILL.md), criada a pedido do usuário em 28/10/2026. Ela detalha confronto com o edital/TR, pesquisa de fornecedores, embalagens e compras mínimas, custo entregue, margem de contribuição, adjudicação parcial e canais de envio. As regras de pesquisa de preços da Administração não se confundem com a compra privada da empresa. Consultar fontes oficiais atuais e respeitar as autorizações efetivamente concedidas pelo usuário.