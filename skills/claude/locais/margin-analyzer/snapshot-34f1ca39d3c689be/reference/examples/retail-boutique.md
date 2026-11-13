# Exemplo: Casa Roque — produtos (trocador / berço / espuma)

**Empresa:** Casa Roque (enxoval/bebê, espumas, decoração)
**Canais:** Mercado Livre, Shopee, site (NuvemShop)
**Dados:** 14 meses de vendas (repasses) + custos do Bling

---

## O que o JhEY perguntou

"Meu custo de espuma subiu bastante esse ano. Sinto que preciso reajustar, mas
não quero perder venda no ML. Dá uma olhada na minha margem?"

---

## Passo 1: Pré-checagem

Linha de produto confirmada: trocadores, berços e espumas (D23/D28). Custo de
espuma = R$ 653,33/m³.

---

## Passo 2: Escopo

O JhEY quer analisar 5 SKUs principais:
- Trocador americano
- Trocador tradicional
- Berço (kit)
- Espuma D23 (placa)
- Ninho/redutor de berço

Métrica prioritária: **margem de contribuição %** (após comissão + Simples +
frete), porque é o que sobra de verdade.

---

## Passo 3–4: Dados reunidos

- **Bling:** custo por SKU (matéria-prima + costura Cleusa/Vanda + embalagem)
- **Repasses:** 14 meses de ML + Shopee + site (valor líquido por venda)

---

## Passo 5: Unit economics (exemplo ilustrativo)

Decomposição por unidade (canal ML/Shopee, comissão 16%, Simples ~10%, frete
quando a loja paga):

| SKU | Preço | Comissão 16% | Simples ~10% | Frete | CMV | Margem contrib. | Margem % |
|---|---|---|---|---|---|---|---|
| Trocador americano | R$ 189,00 | R$ 30,24 | R$ 18,90 | R$ 0,00¹ | R$ 70,00 | R$ 69,86 | 37,0% |
| Trocador tradicional | R$ 149,00 | R$ 23,84 | R$ 14,90 | R$ 22,00² | R$ 62,00 | R$ 26,26 | 17,6% ⚠️ |
| Berço (kit) | R$ 299,00 | R$ 47,84 | R$ 29,90 | R$ 0,00¹ | R$ 120,00 | R$ 101,26 | 33,9% |
| Espuma D23 (placa) | R$ 219,00 | R$ 0,00³ | R$ 21,90 | R$ 0,00¹ | R$ 98,00 | R$ 99,10 | 45,2% |
| Ninho/redutor | R$ 139,00 | R$ 22,24 | R$ 13,90 | R$ 22,00² | R$ 55,00 | R$ 25,86 | 18,6% ⚠️ |

¹ Pedido > R$ 199 em SP: frete grátis sai mais barato/absorvido na margem do preço.
² Pedido < R$ 199: a loja banca parte do frete.
³ Espuma D23 vendida pelo **site** (comissão 0%) — por isso a margem é a melhor.

⚠️ Trocador tradicional (17,6%) e ninho (18,6%) ficam **abaixo da meta de 30%** —
pontos de atenção. São itens de ticket baixo onde o frete pesa proporcionalmente
mais.

---

## Passo 6: Contexto e benchmark

"Para e-commerce de enxoval/bebê no Brasil, a margem de contribuição costuma ficar
entre ~25% e ~45% (estimativa — sem fonte exata; ver industry-benchmarks.md). Sua
média de portfólio (~30%) está no piso saudável. O **trocador tradicional** e o
**ninho** estão abaixo: são itens de ticket baixo (< R$ 199), então o frete come
uma fatia proporcional maior, e a comissão de 16% do ML/Shopee fecha a conta. A
espuma D23 é o destaque (45%) justamente porque vende no site, sem os 16% de
comissão. Seu custo de espuma (R$ 653,33/m³) subiu no período enquanto os preços
ficaram parados — isso explica parte da compressão nos itens de espuma de menor
volume."

---

## Passo 7: Cenários de preço — Trocador tradicional (baixa margem)

Preço atual: R$ 149,00. Custo (CMV): R$ 62,00. Canal: ML/Shopee.

| Cenário | Novo preço | Receita est.* | Margem contrib. % |
|---|---|---|---|
| +5% (R$ 156,45) | R$ 156,45 | ~−3% volume | 22,0% |
| +10% (R$ 163,90) | R$ 163,90 | ~−6% volume | 25,7% |
| +15% (R$ 171,35) | R$ 171,35 | ~−8% volume | 29,1% |

*Estimativa de volume com base no histórico de 14 meses: ~0,6 de queda de volume
por 1% de aumento de preço nesta categoria. No +15% o item passa de R$ 199 com
poucos acessórios — atenção ao gatilho de frete grátis SP.

Nota: "Projeções com base no seu histórico. A resposta real depende dos seus
clientes, da concorrência no ML/Shopee e da sazonalidade (Dia das Mães puxa
trocador)."

---

## Passo 8: O que foi apresentado

O JhEY recebeu a tabela completa de unit economics, o parágrafo de contexto e a
tabela de cenários do trocador tradicional. Ele notou que a espuma D23 no site é
a campeã de margem (comissão 0%) e que migrar mais venda de espuma para o site
melhora o mix. A análise **não recomendou** ação — só mostrou que o trocador
tradicional e o ninho são os SKUs mais vale a pena reavaliar.

---

## Notas para quem mantém a skill

- O exemplo mostra a decomposição completa Casa Roque: preço − 16% − Simples ~10%
  − frete − CMV. Markup 2,70x leva ao preço, mas a **margem de contribuição** é o
  que importa.
- Elasticidade foi calculável porque o JhEY já reajustou o trocador uma vez (de
  R$ 139 → R$ 149 há 8 meses) e o volume caiu ~5% no mês seguinte — é a limitação
  de "um ponto só" descrita em gotchas.md.
- O contraste site (0% comissão) x marketplace (16%) é o aprendizado central.
