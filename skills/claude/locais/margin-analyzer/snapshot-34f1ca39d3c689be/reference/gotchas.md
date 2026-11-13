# Pegadinhas (margem Casa Roque)

## Pegadinha: confundir markup com margem

O JhEY usa markup **2,70x**. É tentador concluir "então minha margem é 170%". Não é.

**Por que importa:** markup é sobre o custo; margem é sobre o preço — e ainda saem
comissão (16%), Simples (~10%) e frete antes de sobrar.

### ✗ Errado
"Você aplica markup 2,70x, então sua margem é ~170%."

### ✓ Certo
"Markup 2,70x leva o custo ao preço. Mas a **margem** é o que sobra do preço
**depois** de comissão (16% no ML/Shopee), Simples (~10%) e frete. Num item de
marketplace, a margem de contribuição costuma cair pra ~25–40%, não 170%."

---

## Pegadinha: tratar faturamento como lucro

O JhEY vê R$ 78 mil de repasse e pensa que ganhou isso. Não — é o que **entrou**.

**Por que importa:** mostrar faturamento sem casar com comissão, Simples, CMV e
frete dá falsa sensação de folga.

### ✗ Errado
"Seu faturamento no mês foi R$ 78.000,00."

### ✓ Certo
"Faturamento de R$ 78.000,00. Depois de comissão (~R$ 10.900), Simples (~R$ 7.600),
CMV (~R$ 31.200), folha, Ads e frete, o resultado foi ~R$ 17.200 — margem ~22%."

---

## Pegadinha: esquecer que comissão + frete + Simples comem a margem do marketplace

**Por que importa:** o mesmo trocador a R$ 149 rende muito menos no ML que no site.
No ML saem 16% de comissão; em pedido < R$ 199, a loja ainda banca parte do frete;
e o Simples incide sobre tudo.

### ✗ Errado
"O trocador a R$ 149 com custo de R$ 62 tem margem de ~58%."
(Isso é só preço − CMV; ignora comissão, Simples e frete.)

### ✓ Certo
```
Preço:           R$ 149,00
(−) Comissão 16%: R$ 23,84
(−) Simples ~10%: R$ 14,90
(−) Frete:        R$ 22,00 (pedido < R$ 199 em SP)
(−) CMV:          R$ 62,00
(=) Margem contrib.: R$ 26,26 → 17,6%  ← bem diferente de 58%
```
Sempre decomponha preço − comissão − Simples − frete − CMV. No **site**, comissão
= 0% e a conta melhora.

---

## Pegadinha: usar preço de tabela em vez do preço efetivo

Cupons (Shopee), campanhas e desconto Pix reduzem o que cai por venda. O repasse
reflete o valor real; o preço anunciado no Bling pode ser o de tabela.

**Por que importa:** calcular margem com preço de tabela infla o resultado.

### ✗ Errado
Usar o preço anunciado do Bling como receita e o repasse só para custo → margem
parece melhor que a real.

### ✓ Certo
Use o **valor líquido do repasse** (ML/Shopee/NuvemPago) como receita real e o
Bling para custo. Sinalize diferença entre preço de tabela e valor recebido — vale
mostrar.

---

## Pegadinha: ignorar o custo real da espuma

Espuma D23/D28 custa R$ 653,33/m³. Um item de espuma sem o volume (m³) não tem CMV
confiável.

**Por que importa:** chutar o custo da espuma erra a margem dos itens que mais
importam pra Casa Roque (espumas são foco da Casa Roque).

### ✗ Errado
Assumir um custo "redondo" pra placa de espuma sem saber o volume.

### ✓ Certo
Peça o volume da peça e calcule: `m³ × R$ 653,33 + corte/encape + costura`. Se o
JhEY não souber o volume, pergunte — não estime.

---

## Pegadinha: elasticidade de um único reajuste

O JhEY reajustou o trocador uma vez, o volume caiu um mês e voltou. Declarar "5% de
aumento = 3% de queda" como lei é overfit a um evento.

**Por que importa:** um ponto não é padrão. Sazonalidade (Dia das Mães, Black
Friday) ou um anúncio podem ter movido o volume, não o preço.

### ✗ Errado
"Em março você subiu 8% e o volume caiu 4%. Elasticidade = −0,5."

### ✓ Certo
"Em março você subiu 8% e o mês seguinte caiu 4%. É **uma observação só** — a
relação real varia. Uso como guia e mostro uma faixa de cenários."

---

## Pegadinha: apresentar cenário como previsão

As tabelas de cenário são matemática, não previsão. A resposta real depende da
concorrência no ML/Shopee, da sazonalidade e do cliente.

### ✗ Errado
"Se subir 10%, você fatura R$ 55 mil no próximo mês."

### ✓ Certo
"Se subir 10% e o volume cair ~5% (com base no histórico), a receita fica ~R$ 53
mil. É projeção grosseira — o resultado real depende dos seus clientes e da
concorrência."

---

## Pegadinha: Simples de serviço tratado como o do comércio

A Casa Roque (comércio) é Anexo I. Um serviço (ex.: Roque Engenharia) pode cair em
**outro anexo**, com alíquota diferente.

### ✗ Errado
Aplicar ~10% (Anexo I) sobre receita de serviço sem ressalva.

### ✓ Certo
"Para serviço, o Simples pode ser de **anexo diferente** do comércio — a alíquota
muda. Uso um efetivo ilustrativo aqui e marco para **confirmar com a Contabilizei**."
