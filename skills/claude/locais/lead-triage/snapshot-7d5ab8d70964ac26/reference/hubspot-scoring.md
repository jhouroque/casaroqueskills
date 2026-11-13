# Modelo de pontuação de perguntas/leads por sinal de compra — lead-triage

> A Casa Roque **não tem CRM**. "Leads" = perguntas de pré-venda (ML, Shopee), mensagens de WhatsApp e contatos do site (formulário, carrinho abandonado). Como não há conector, os dados vêm de **print/export/planilha** ou colados. Este modelo pontua por **sinal de compra** e **urgência de SAC (< 2h, POP 4)**.

---

## Campos a coletar (do print/export/planilha)

| Campo | Usado para |
|---|---|
| Nome do cliente (ou "comprador ML/Shopee") | Exibição — o marketplace às vezes esconde o nome real |
| Canal (ML / Shopee / WhatsApp / site) | Exibição + peso de canal |
| Produto perguntado | Sinal de compra + valor potencial |
| Texto da pergunta/mensagem | Sinal de compra (frete/prazo/disponibilidade/parcelamento) |
| Data/hora da pergunta | Urgência — tempo sem resposta vs meta de 2h |
| Já respondida? | Penalidade de já-respondido |
| Carrinho abandonado (sim/não) | Sinal de compra alto (estava a um passo de comprar) |

---

## Modelo de pontuação (composto 0–100)

Quatro dimensões, cada uma 0–25. Some para o composto.

### Sinal de compra (0–25)
O que a pergunta revela sobre intenção de comprar.

| Sinal | Pontos |
|---|---|
| Pergunta sobre **frete/prazo de entrega** ("chega quando em [cidade]?") | +15 |
| Pergunta sobre **disponibilidade/estoque** ("tem na cor X?", "tem pronta entrega?") | +15 |
| Pergunta sobre **parcelamento/desconto/Pix** | +12 |
| **Carrinho abandonado** no site | +12 |
| Pergunta técnica genérica ("que densidade é essa espuma?") | +6 |
| Só elogio/avaliação, sem intenção de compra | +2 |

(Some os sinais que aparecerem, teto em 25.)

### Urgência — tempo sem resposta (0–25)
Meta de SAC: responder em **< 2h** (POP 4).

| Tempo em aberto | Pontos |
|---|---|
| Passou de 2h (fora da meta) | +25 |
| 1h–2h (chegando perto) | +18 |
| 30min–1h | +10 |
| < 30min | +5 |

### Valor potencial (0–25)
Ticket do produto perguntado (ticket médio da casa R$ 71,63; meta R$ 200).

| Produto / contexto | Pontos |
|---|---|
| Atacado, espuma sob medida, kit berço/enxoval completo | 25 |
| Produto acima do ticket médio (kits, plumante, lençóis em conjunto) | 18 |
| Produto na faixa do ticket médio | 12 |
| Item avulso barato | 6 |

### Penalidade de já-respondido (subtraída do composto)

| Situação | Subtrai |
|---|---|
| Já respondida há < 1h | −25 |
| Já respondida há 1–4h | −10 |
| Já respondida, aguardando retorno do cliente | −5 |
| Ainda sem resposta | 0 |

---

## Regra de ouro

Pergunta sobre **frete, prazo ou disponibilidade é lead quente** — quem pergunta isso está decidindo a compra. Priorize esses **sempre** e dentro da janela de 2h. Pergunta puramente técnica (material, densidade) é mais fria — responde com qualidade, mas não fura a fila de uma dúvida de frete prestes a virar venda.
