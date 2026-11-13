# Custos, embalagem, transporte e margem

Esta é uma metodologia interna de decisão comercial. Não fixa alíquotas, nem representa regra legal de margem mínima.

## Comprar, entregar e sobrar

Com `q` na unidade base, conteúdo comercial `c`, mínimo `n_min` e múltiplo confirmado `k` em embalagens: `n = ceil(max(ceil(q/c), n_min)/k) × k`. A compra é `n×c`, e a sobra é `n×c−q`. Se algum desses parâmetros estiver desconhecido, a quantidade comprável permanece cenário.

Em rolos por cor, aplicar o mínimo a cada cor; não somar cores para escapar do mínimo sem permissão do fornecedor. Para material por kg, usar `kg = metros / rendimento` e arredondar à unidade comercial mínima por cor. Registrar perdas/cortes e a operação efetiva.

Mostrar três resultados: custo correspondente à quantidade entregue, desembolso integral da compra mínima e valor/quantidade do estoque excedente. A sobra não é lucro nem economia realizada. Usar preço que recupere todo o desembolso é uma opção prudencial, diferente da margem contábil sobre o custo consumido; identificar a base escolhida. Se aprovar financiar estoque com outras vendas, mostrar o efeito de caixa separadamente.

## Frete integral

Rotas possíveis: fornecedor→CasaRoque→órgão, ou fornecedor→órgão. Identificar quem coleta/transporta e a condição fiscal da entrega direta antes de fechar a operação. Duas rotas alternativas não são somadas como se ambas fossem realizadas.

Cotação exige origem, destino verdadeiro, volumes, peso/cubagem e valor da carga, além de modalidade, seguro, restrições, coleta, carga/descarga e prazo. Endereço cadastral do órgão não prova endereço da entrega. Peso de uma peça não substitui peso/medidas dos volumes embalados. Banner “frete grátis” não garante elegibilidade do CEP/quantidade.

Frete desconhecido: `null/pendente`. Zero só se houver condição comprovada ou trecho não aplicável, com justificativa. Provisão monetária pode apoiar decisão de risco, mas não vira cotação confirmada. Separar prazo da loja, transporte, recebimento e margem de segurança do cronograma.

Ratear por peso/cubagem quando conhecidos; na falta, valor de compra pode ser aproximação identificada. Conferir soma dos rateios contra o total de cada trecho. Em adjudicação parcial, calcular cada item isolado e combinações plausíveis com mínimos/frete fixo real; o total do lote não garante margem por item. Consolidar fornecedores pode reduzir frete e aumentar custo de compra: comparar ambos.

## Formação do preço

Se `C` é o custo direto por unidade de venda, `t` a soma de tributos e despesas percentuais efetivamente incidentes sobre a receita e `m` a margem desejada: `PV = C / (1−t−m)`. Denominador precisa ser positivo. Taxas com bases diferentes ou valores fixos são tratadas separadamente, não somadas cegamente a `t`.

Arredondar o preço unitário para cima em centavos quando for necessário preservar margem mínima; calcular o total pela quantidade e conferir a margem com o valor efetivamente arredondado. Custo100 e margem30%, sem tributo/despesa percentual, dá142,86; vender130 deixa23,08%, não30%. Esse exemplo é aritmético, não preço aprovado.

Margem de contribuição é `(venda−custos diretos−despesas variáveis)/venda`. Não é lucro líquido: despesas fixas, remuneração dos sócios e outros resultados precisam ser analisados à parte. Distinguir preço-meta, preço mínimo econômico e preço máximo aceitável do órgão. Não lançar abaixo do mínimo autorizado para vencer a disputa.

Para preço já proposto, calcular `C_max = PV × (1−t−m)` e comparar ao custo atualizado. A diferença é o limite suportado para despesas ainda não confirmadas; limite pequeno não é reserva de segurança. No cenário parcial, fazê-lo por item.

## Tributos e caixa

Verificar empresa e regime, competência, atividade/operação, NCM dos produtos, origem/destino e natureza de revenda ou transformação. Não usar guia DAS isolada, alíquota nominal ou percentual genérico como taxa efetiva atual. Obter apuração e validação contábil aplicáveis; não duplicar imposto já embutido no custo nem presumir crédito tributário.

Retenção que altera caixa não é necessariamente custo tributário adicional: conferir tratamento com contador. Corte, costura, beneficiamento, fracionamento e entrega por terceiro podem alterar operação/documentação; discriminar antes de definir preço. Validade longa requer avaliar capacidade de manter preço, disponibilidade e efeitos de mudança tributária, sem inventar proteção contratual.

Fluxo mínimo: sinal/compra, fretes, embalagem, tributos, data esperada de entrega/aceite, emissão da NF, liquidação e pagamento. Não trocar “30 dias após liquidação” por “30 dias após entrega”. Registrar capital necessário, prazo em risco e eventual custo financeiro verificável. Pedido de orçamento não é empenho nem garantia de compra; proposta enviada não autoriza comprar material automaticamente.
