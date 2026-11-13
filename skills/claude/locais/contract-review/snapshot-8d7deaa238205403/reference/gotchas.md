# Pegadinhas (revisão de contrato BR)

Casos de borda na análise de contratos sob lei brasileira. Pares Bom / Ruim.

> Tudo aqui é orientação prática, **não parecer jurídico**. Bandeira vermelha ou
> decisão que obrigue a empresa → validar com advogado/contabilidade antes de assinar.

---

## Pegadinha: sinalizar boilerplate padrão como bandeira vermelha

**Por que importa:** Sinalizar demais ensina o JhEY a ignorar o resumo. Se tudo é
bandeira vermelha, nada é.

### ✗ Ruim

```
O contrato tem cláusula de confidencialidade mútua padrão, 2 anos.
Claude: "🔴 Bandeira vermelha: cláusula de confidencialidade impõe obrigação às duas partes."
```

Confidencialidade mútua de 2 anos é norma de mercado. Sinalizar como vermelha destrói a
relação sinal/ruído.

### ✓ Bom

```
O contrato tem cláusula de confidencialidade mútua padrão, 2 anos.
Claude: [pula; não sinaliza]
```

Reserve bandeiras vermelhas para termos de fato fora do padrão. Cláusula boilerplate e
justa, omita.

---

## Pegadinha: cláusula ausente não some da análise

**Por que importa:** Para a Casa Roque, a ausência de proteção padrão (teto de
responsabilidade, índice de reajuste, processo de aditivo) costuma ser mais perigosa que
uma cláusula desfavorável — a lei (Código Civil/CDC) preenche a lacuna, em geral a favor
da contraparte.

### ✗ Ruim

```
O contrato não tem teto de responsabilidade.
Claude: [não menciona; só analisa o que está escrito]
```

O JhEY assina achando que a responsabilidade é limitada. Não é.

### ✓ Bom

```
O contrato não tem teto de responsabilidade.
Claude: "🔴 Ausente: não há limitação de responsabilidade. Sem teto, a exposição segue
o Código Civil (reparação integral do dano). Prática usual é limitar ao valor pago nos
12 meses anteriores à reclamação. Sugiro incluir: 'A responsabilidade total de cada
parte fica limitada ao valor efetivamente pago nos 12 (doze) meses anteriores ao fato
gerador.'"
```

Trate cláusula ausente-mas-padrão como bandeira vermelha. Rotule "Ausente".

---

## Pegadinha: multa rescisória desproporcional

**Por que importa:** É a pegadinha brasileira mais comum em contrato de prestação de
serviço e fornecimento. Multa de "100% do valor total do contrato" para rescisão
antecipada é abusiva e travaria a saída da Casa Roque. O Código Civil (art. 413) permite
ao juiz **reduzir** multa manifestamente excessiva, mas é muito melhor negociar antes de
assinar do que discutir depois.

### ✗ Ruim

```
Cláusula: "Em caso de rescisão antecipada, a CONTRATANTE pagará multa de 100% do valor
global do contrato."
Claude: [não comenta — "é só a multa padrão"]
```

### ✓ Bom

```
Claude: "🔴 Multa rescisória desproporcional. A cláusula cobra 100% do valor global se
você rescindir antes do fim — você pagaria o contrato inteiro sem receber o serviço.
Prática razoável é multa proporcional ao que falta (ex.: 1 a 3 mensalidades, ou um
percentual do saldo). Sugiro: 'multa equivalente a 20% das parcelas vincendas, limitada
a 3 (três) mensalidades.' O art. 413 do Código Civil permite reduzir multa excessiva,
mas é melhor ajustar agora."
```

---

## Pegadinha: reajuste sem índice ou abaixo do mínimo legal

**Por que importa:** Contrato de prazo longo (fornecimento, locação do barracão,
agência) precisa de índice de reajuste definido (**IPCA** ou **IGP-M**) e periodicidade.
No Brasil o reajuste de preço por índice tem **periodicidade mínima anual** (Lei
10.192/2001). Contrato que permite reajuste "a qualquer tempo a critério do fornecedor"
ou silencioso sobre o índice é risco de caixa.

### ✗ Ruim

```
Cláusula: "Os preços poderão ser reajustados a critério da CONTRATADA."
Claude: [não sinaliza]
```

### ✓ Bom

```
Claude: "🟡 Reajuste em aberto. 'A critério da contratada' deixa o reajuste sem regra —
pode subir a qualquer momento. Fixe índice e periodicidade: 'reajuste anual pela
variação do IPCA (ou IGP-M) acumulado nos 12 meses.' Periodicidade mínima de reajuste no
Brasil é anual (Lei 10.192/2001). O IGP-M oscila mais que o IPCA — para a Casa Roque, o
IPCA costuma ser mais previsível."
```

---

## Pegadinha: foro distante e arbitragem cara

**Por que importa:** PME não tem caixa para litigar fora da sua comarca nem para
arbitragem (custa caro). Foro eleito em outra cidade/estado, ou cláusula de arbitragem
obrigatória, encarece e dificulta qualquer disputa para a Casa Roque (Limeira/SP).

### ✗ Ruim

```
Cláusula: "Fica eleito o foro da Comarca de [cidade distante]; conflitos resolvidos por
arbitragem na Câmara X."
Claude: [não comenta]
```

### ✓ Bom

```
Claude: "🟡 Foro distante + arbitragem. Eleger foro em [cidade distante] e impor
arbitragem encarece muito qualquer disputa para você. Peça foro da Comarca de Limeira/SP
(ou do domicílio da Casa Roque) e, se for contrato de consumo, lembre que o CDC garante
o foro do domicílio do consumidor. Arbitragem só compensa em contrato de valor alto."
```

---

## Pegadinha: contrato com fornecedor x relação de consumo (CDC)

**Por que importa:** O CDC protege a Casa Roque quando ela é **destinatária final** do
produto/serviço (ex.: software, serviço contratado para uso próprio), mas **não** se
aplica como escudo quando ela compra insumo para revenda/transformação (espuma, tecido —
aí é relação empresarial, Código Civil). Confundir os dois leva a recomendação errada.

### ✗ Ruim

```
Contrato de compra de espuma para fabricar trocadores.
Claude: "Pelo CDC você tem 7 dias de arrependimento e garantia estendida..."
```

Errado — compra de insumo para transformação é relação empresarial (B2B), regida pelo
Código Civil, não pelo CDC.

### ✓ Bom

```
Claude: "Atenção: como você compra a espuma como insumo (revenda/fabricação), isto é
relação empresarial (Código Civil), não consumo — o CDC não te dá arrependimento de 7
dias aqui. Negocie garantia, prazo de troca por defeito e tolerância de medida
diretamente no contrato, porque a lei não preenche isso a seu favor automaticamente."
```

Quando a Casa Roque for **destinatária final** (ex.: assinatura de um SaaS de gestão),
aí sim o CDC vale e deve ser usado.

---

## Pegadinha: PDF grande truncado no meio da análise

**Por que importa:** Contratos com 20–30+ páginas costumam guardar os termos mais
perigosos em anexos, tabelas de preço e "condições gerais" no fim. Se o PDF for lido só
até a página 15, termos-chave passam batido.

### ✗ Ruim

```
A skill lê as páginas 1–10 de um contrato de 40 páginas. O Anexo de Preços e a multa
(a partir da página 28) ficam de fora. A skill produz um resumo "limpo".
```

### ✓ Bom

```
Leia o PDF em blocos: páginas 1–10, 11–20, 21–40. Analise todos os blocos antes de
produzir o resumo. Se um título mencionar "Anexo", "Apêndice" ou "Condições Gerais",
sinalize explicitamente e garanta que foi lido.
```

Sempre leia o documento inteiro. Use o parâmetro `pages` para fatiar PDFs grandes.

---

## Pegadinha: minuta da contraparte x minuta negociada

**Por que importa:** A recomendação tem que casar com a relação de força. Contestar tudo
numa minuta de compras de uma grande indústria de espuma é diferente de negociar com um
fornecedor pequeno local — a grande costuma ser inegociável em boa parte das cláusulas.

### ✗ Ruim

```
Minuta de uma grande indústria, com termos padrão de compras.
Claude: "🔴 Esse prazo de pagamento de 60 dias tem que virar 28 dias. O jurídico deles
         vai aceitar."
```

Recomendação irreal queima o capital de negociação do JhEY.

### ✓ Bom

```
Claude: "🟡 Pagamento em 60 dias. É mais longo que o usual (28/30 dias), mas comum em
         minuta de compras de indústria grande. Vale pedir 45 dias como meio-termo — pode
         rolar, principalmente em compra recorrente. Se for minuta-padrão de empresa
         grande, prazo de pagamento costuma ser inegociável na primeira compra."
```

Case a recomendação com a relação de força. Marque amarela, não vermelha. Reconheça a
realidade.
