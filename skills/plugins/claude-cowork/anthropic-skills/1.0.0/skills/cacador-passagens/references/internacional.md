# Modo internacional

Use quando o destino é fora do Brasil. O caso vivo hoje é **Nova York em
dezembro de 2026**, casal (Jhonatas + Thomaz), saindo de GRU / CGH / VCP,
chegando em JFK / EWR / LGA, ida e volta, 4 a 8 noites entre 01 e 20/dez.
Objetivos da viagem: árvore do Rockefeller e comprar 2 iPhone Pro nos EUA.

## Semáforo — Nova York, por pessoa, ida e volta, COM bagagem despachada

| Faixa | Leitura |
|---|---|
| até R$ 2.900 | 🟢 comprar |
| R$ 2.900–3.500 | 🟡 bom, avaliar |
| R$ 3.500–4.200 | 🟠 caro |
| acima de R$ 4.200 | 🔴 passar |

Referência: a média de dezembro nessa rota é R$ 5.230. Para outro destino
internacional, peça a faixa dele; se precisar estimar, o piso costuma ficar em
torno de 55% da média histórica do mês.

## A armadilha da bagagem

O preço de vitrine do Explorar e da maioria dos posts é **sem bagagem
despachada**. A meta dele é sempre *com*. Antes de pintar qualquer número de
verde, confirme a bagagem na busca real — uma tarifa 🟢 sem bagagem vira 🟠
depois de somar US$ 75–150 por trecho em muitas cias americanas. Se não deu
para confirmar, reporte o número mas diga que a bagagem não foi verificada, e
não aplique o semáforo.

## Fechamento de custo

Sempre que houver preço de passagem, rode `scripts/custo_viagem.py` em vez de
fazer a conta na mão — ela tem IOF, imposto de importação escalonado e sales
tax, e errar um deles muda a recomendação. Cotação do dólar comercial do dia via
`https://economia.awesomeapi.com.br/last/USD-BRL` (o script já busca sozinho).

```
python scripts/custo_viagem.py --passagem 2900
python scripts/custo_viagem.py --help    # todos os parâmetros
```

Padrões embutidos: casal, 8 dias, 7 noites em Newark a US$ 90, alimentação US$
55/dia/pessoa, transporte US$ 180, passeios US$ 150, seguro R$ 500. O script
compara três cenários de aparelho contra comprar 2× iPhone 18 Pro na Apple
Brasil (R$ 27.200).

Pontos que costumam ser esquecidos e mudam o resultado:

- **Cota de isenção**: US$ 1.000 por pessoa na entrada aérea no Brasil. O que
  passa disso paga 50% sobre o excedente. Recondicionado a ~US$ 780 e novo em
  liquidação a ~US$ 899 cabem na cota; US$ 1.299 não cabe, e o imposto sozinho
  vira o item que decide o cenário.
- **Sales tax de New Jersey**: 6,625%. Delaware e New Hampshire são zero — vale
  mencionar quando a diferença for material.
- **IOF de 1,1%** em conta global / cartão pré-pago. Crédito internacional é
  bem mais caro; confira a alíquota vigente antes de assumir.

Ao apresentar, deixe claro que a comparação "vs. Apple Brasil" põe a **viagem
inteira** contra **só os aparelhos** — quando dá negativo, aquela diferença é o
custo real de viajar, e a viagem entrega muito mais que dois telefones. Não
apresente isso como se a viagem "não valesse a pena".

## Monitoramento de aparelho (às segundas)

Confira iPhone 17 Pro e 18 Pro 256 GB recondicionado em Back Market, RefurbMe,
Swappa e Apple Certified Refurbished. Avise se o **17 Pro cair abaixo de US$
800** — esse é o gatilho que muda o cenário mais barato do fechamento.

## Contexto que não precisa ser repetido a ele

Já foram a Nova York duas vezes, já têm visto, e compram recondicionado no
eBay/Back Market retirando nos EUA. Não levante o assunto de visto.
