# Pegadinhas — lead-triage (Casa Roque)

---

## Pegadinha: "Pipeline" cru dispara pontuação quando o JhEY só quer um panorama

**Por que importa:** "Pipeline" sozinho é ambíguo — o JhEY pode querer só saber quantas perguntas estão em aberto por canal, não uma lista pontuada.

### ✗ Ruim
```
JhEY: "como tá meu pipeline?"
Claude: [pontua tudo e devolve lista ranqueada de 12 perguntas]
```

### ✓ Bom
```
JhEY: "como tá meu pipeline?"
Claude: "Quer um panorama (quantas perguntas em aberto por canal) ou a lista
         priorizada de quem responder agora?"
```

---

## Pegadinha: Estourar a meta de SAC de 2h

**Por que importa:** A casa responde SAC em **< 2h** (POP 4, Keila). Pergunta de pré-venda parada vira venda perdida e nota baixa. Tempo sem resposta é o maior peso de urgência.

### ✗ Ruim
```
Lista ordenada só por valor do produto. Uma pergunta de frete parada há 3h
fica em quarto lugar atrás de itens caros recém-chegados.
```

### ✓ Bom
```
Qualquer pergunta em aberto > 2h sobe pro topo com a marca:
"⚠ Fora da meta de SAC (< 2h) — responder já."
Tempo sem resposta pesa tanto quanto o valor do produto.
```

---

## Pegadinha: Tratar pergunta como se fosse pedido

**Por que importa:** Uma pergunta no ML/Shopee **não é uma venda fechada** — é intenção. Marcar como pedido, descontar do estoque ou prometer envio antes de o cliente comprar gera erro operacional (meta < 2%) e expectativa furada.

### ✗ Ruim
```
Cliente pergunta "tem o kit em cinza?" → Claude trata como pedido,
sugere emitir NF e separar o produto.
```

### ✓ Bom
```
Pergunta = oportunidade a responder, não pedido. Confirme estoque (POP 2),
responda com frete/prazo/disponibilidade, e só após o cliente comprar é que
entra o fluxo de NF/etiqueta (POP 1). A skill só prioriza e rascunha a resposta.
```

---

## Pegadinha: O marketplace esconde o contato do cliente

**Por que importa:** ML e Shopee **não expõem** telefone/e-mail do comprador antes (e muitas vezes depois) da venda. Tentar "ligar pro lead" ou pedir o WhatsApp do cliente no marketplace não funciona — e pedir contato por fora viola as regras das plataformas.

### ✗ Ruim
```
Claude monta a lista com "ligar para o cliente" e tenta achar o telefone
do comprador do Mercado Livre.
```

### ✓ Bom
```
Trate como "comprador ML/Shopee" e responda DENTRO do canal (pergunta do
anúncio / chat do marketplace). Só WhatsApp e contatos do site (formulário)
têm contato direto. Nunca proponha puxar o cliente do marketplace pra fora.
```

---

## Pegadinha: Propor horário na Agenda que conflita com evento

**Por que importa:** Propor um horário em que o JhEY já tem a reunião do Thomas (seg 9h) ou o batimento (sex 15h) quebra a confiança na hora.

### ✗ Ruim
```
Claude propõe "sexta 15:00" sem olhar a Agenda.
O JhEY tem o batimento com Keila e Emerson nesse horário (POP 3).
```

### ✓ Bom
```
Consulte a Google Agenda antes de propor qualquer horário.
Só proponha janelas sem evento ±15 min. Lembre dos fixos: reunião Thomas
seg 9h e batimento sex 15h. Sem janela livre, diga e ofereça outro dia.
```

---

## Pegadinha: Inventar leads quando não veio print

**Por que importa:** Não há conector de ML/Shopee. Sem o print/export das perguntas, não há base — preencher com leads imaginários é pior que não responder.

### ✗ Ruim
```
JhEY: "quem eu respondo primeiro?" (nada anexado)
Claude: [inventa 5 perguntas plausíveis de clientes]
```

### ✓ Bom
```
JhEY: "quem eu respondo primeiro?" (nada anexado)
Claude: "Me manda o print das perguntas em aberto do ML e da Shopee, e as
         mensagens de WhatsApp sem resposta, que eu pontuo e priorizo."
```
