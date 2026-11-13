# Pegadinhas

Modos de falha conhecidos da skill business-pulse. Pares Certo/Errado.

---

## Pegadinha: tratar a falta de conector de venda como "negócio sem dados"

**Por que importa:** a Casa Roque **não tem** MCP de Bling, ML, Shopee ou NuvemShop. Caixa e vendas dependem de relatório/CSV/print anexado. Se o pulso pula caixa e vendas em silêncio só porque não veio arquivo, o JhEY pensa que o negócio não tem dado — quando na real é só falta de export.

### ✗ Errado

```
Claude: [sem relatório de venda anexado]
        → pula Vendas e Caixa em silêncio
        → pulso só mostra agenda e Gmail; JhEY acha que faltou algo
```

### ✓ Certo

```
Claude: [sem relatório de venda]
        → Caixa: "n/d — sem relatório do Bling/extrato"
        → Vendas: "n/d — sem export do ML/Shopee/site"
        → oferta única: "Me manda o relatório de vendas (7 dias) e o de
          contas a receber/pagar do Bling que eu fecho o pulso completo."
        → entrega o resto (agenda, watch-list de Gmail) normalmente
```

O JhEY vê a lacuna explícita e decide se manda o arquivo ou segue com o pulso parcial.

---

## Pegadinha: postar número ruim sem avisar

**Por que importa:** o pulso pode virar bloco de WhatsApp pra equipe ou rascunho no Gmail. Se as vendas caíram, um item rompeu, ou a mídia estourou o CPC, mandar esse número cru pra equipe sem o JhEY ver primeiro pode gerar pânico, expor a operação ou passar uma leitura errada (ex.: queda que é só sazonal).

### ✗ Errado

```
Claude: [vendas −22% na semana]
        → já gera o bloco de WhatsApp "Vendas R$ X, caíram 22%" e oferta postar
```

### ✓ Certo

```
Claude: [vendas −22% na semana]
        → mostra no pulso (com o número) pro JhEY
        → "Essa queda de 22% pode ser sazonal (semana pós-Dia das Mães). Quer
          que eu monte o bloco pro WhatsApp da equipe ou prefere checar a causa
          antes?"
        → só gera o bloco/rascunho com o "ok" do JhEY
```

Número sensível passa pelo JhEY antes de virar mensagem pra terceiros. Nada é enviado sem aprovação.

---

## Pegadinha: falha de auth do Gmail no meio do pulso

**Por que importa:** o auth do Gmail é instável às vezes. Jogar um erro de auth cru no meio do pulso parece que a skill quebrou e derruba a confiança.

### ✗ Errado

```
Claude: [erro de auth do Gmail no meio]
        → "Erro: falha de autenticação do Gmail. Reautentique."
        → o pulso para ou mostra erro cru na watch-list
```

### ✓ Certo

```
Claude: [erro de auth do Gmail]
        → segue o pulso sem a watch-list de e-mail
        → apêndice: "Gmail — erro de auth; watch-list de e-mail indisponível nesta rodada"
        → as outras seções não são afetadas (SAC e estoque por print seguem)
```

O pulso ainda entrega valor. O JhEY é informado, não alarmado.

---

## Pegadinha: pedir permissão antes de puxar dado

**Por que importa:** o valor da skill é fazer o trabalho sem ficar perguntando. Quem chamou o pulso já autorizou o puxe. Perguntar "posso ver seu Gmail?" ou "puxo a agenda?" mata o propósito.

### ✗ Errado

```
JhEY: "me atualiza do negócio"
Claude: "Posso ver sua agenda? E olhar o Gmail por threads urgentes?"
```

Três idas e voltas antes de entregar algo útil.

### ✓ Certo

```
JhEY: "me atualiza do negócio"
Claude: [dispara Gmail + Google Agenda em paralelo na hora]
        → apresenta o pulso numa resposta
        → onde falta conector (Bling/ML/Shopee), marca "n/d" e oferece pedir o relatório
```

---

## Pegadinha: inventar número pra preencher lacuna

**Por que importa:** sem conector de venda, é tentador "estimar" o faturamento da semana. Número inventado num pulso é pior que lacuna — o JhEY pode decidir folha/compra em cima dele. Regra de ouro do plugin: nunca inventar número (CONTEXTO).

### ✗ Errado

```
Claude: [sem dado de venda]
        → "Vendas devem estar em torno de R$ 15 mil essa semana"
```

### ✓ Certo

```
Claude: [sem dado de venda]
        → "Vendas: n/d — me manda o export pra eu calcular. Não vou estimar
          porque número de venda chutado não serve pra decidir caixa/folha."
```

---

## Pegadinha: gerar bloco de WhatsApp via conector de Slack/Teams

**Por que importa:** a equipe da Casa Roque usa **WhatsApp**, não Slack/Teams. A skill nunca deve depender de um conector de Slack/Teams nem tentar postar lá.

### ✗ Errado

```
Claude: [ao fim do pulso]
        "Postei o resumo no seu Slack #geral."
```

A Casa Roque não usa Slack; e mesmo que usasse, não se posta sem aprovação.

### ✓ Certo

```
Claude: [ao fim do pulso]
        "Quer um bloco pronto pra colar no WhatsApp da equipe? Te entrego o
        texto; você cola. (Posts/mensagens só com seu ok.)"
```

WhatsApp via texto pronto pra colar + Gmail. Nunca Slack/Teams.

---

## Pegadinha: SAC e estoque ignorados por não terem conector

**Por que importa:** SAC (POP 4, < 2h) e estoque baixo (POP 2, < 5 un) são os riscos operacionais mais frequentes da Casa Roque — e os dois dependem de informe da Keila/Emerson, não de conector. Se o pulso só olha o que tem API, perde justo o que mais aperta no dia a dia.

### ✗ Errado

Rodar o pulso só com Gmail + Agenda e concluir "nada urgente" sem nem mencionar SAC e estoque.

### ✓ Certo

Incluir SAC e estoque como itens da watch-list mesmo sem conector: se não houver informe, peça uma vez ("tem alguma pergunta de marketplace parada ou item abaixo de 5 un?") e, sem resposta, marque "n/d" — não conclua "nada urgente" sem ter checado as duas frentes que mais geram risco.
