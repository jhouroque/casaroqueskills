# Calculadora de custos e preços para análise

`scripts/avaliar_custo.py` usa somente a biblioteca padrão do Python 3.10+ e aritmética `Decimal`. Analisa **um item, uma unidade de entrega e uma embalagem comercial de um fornecedor por execução**. Não transmite dados, consulta fornecedores, cria pedidos ou autoriza assinatura.

## Como executar

Na pasta da skill:

```powershell
python scripts/avaliar_custo.py entrada.json --saida resultado.json
python scripts/avaliar_custo.py --self-test --saida ../VALIDACAO_CALCULADORA.json
```

Também aceita JSON pela entrada padrão: omitir o arquivo ou informar `-`. Sem `--saida`, escreve o resultado na saída padrão. Código de saída 0 significa cálculo completo, simulação calculável ou testes aprovados; código 2 significa entrada inválida, pendência ou teste que falhou. **Código 0 não significa autorização comercial.**

Não há valores comerciais padrão. Prefira números como strings decimais com ponto, por exemplo `"0.30"`. Números JSON também são lidos diretamente como `Decimal`. Não usar vírgula decimal, símbolos monetários, `NaN` ou `Infinity`. Chaves JSON duplicadas são rejeitadas.

## Contrato de entrada

| Campo | Conteúdo obrigatório |
|---|---|
| `quantidade_entrega` | Quantidade positiva na unidade solicitada. Pode ser fracionada quando a unidade permitir. |
| `unidade_entrega` | Nome da unidade: metro, folha, peça etc. A calculadora não faz conversão semântica. |
| `conteudo_embalagem` | Quantidade positiva **nessa mesma unidade** contida em uma embalagem comercial. |
| `preco_embalagem` | Objeto de valor documentado, relativo à embalagem inteira. |
| `moq_embalagens` | Quantidade mínima inteira e positiva de embalagens do SKU. |
| `multiplo_embalagens` | Múltiplo inteiro e positivo confirmado para a compra. Informar 1 somente com fundamento. |
| `multiplo_confirmado` | `true` apenas quando o múltiplo estiver esclarecido. Não deduzir de caixa master ou quantidade pré-preenchida. |
| `modo_logistico` | `direto` ou `via_empresa`. |
| `fretes` | Lista de rotas com valores documentados, inclusive quando gratuitos. |
| `custos_fixos` | Objetos de valor para `embalagem`, `carga`, `descarga` e `outros`. Pode incluir campos adicionais, como `trabalho` e `perdas`. |
| `aliquota_efetiva` | Objeto com fração da venda informada por fonte fiscal apropriada. A calculadora não apura essa alíquota. |
| `taxas_percentuais` | Lista de taxas adicionais sobre a receita, cada uma com `nome`, `valor`, `natureza` e `justificativa`. |
| `justificativa_sem_taxas` | Obrigatória quando a lista de taxas adicionais estiver vazia. |
| `margem_alvo` | Fração da receita, por exemplo `"0.30"` para 30%. Não é acréscimo sobre o custo. |
| `avaliar_parcial` | Booleano explícito. `false` deixa a adjudicação parcial sem avaliação. |
| `parcial` | Obrigatório quando `avaliar_parcial` for `true`; contrato abaixo. |

Cada valor monetário ou percentual documentado tem esta forma:

```json
{
  "valor": "25.00",
  "natureza": "confirmado",
  "justificativa": "Identificação da cotação, data, rota ou documento que sustenta este valor."
}
```

`natureza` aceita somente `confirmado` ou `estimado`. A ferramenta não verifica se a justificativa é verdadeira ou suficiente: isso é responsabilidade da conferência. **Qualquer estimativa transforma a saída calculável em `SIMULACAO`.** Nunca converter uma provisão em valor confirmado porque o usuário aceitou olhar o cenário.

Um valor desconhecido deve permanecer `null`. Um zero exige justificativa específica, como gratuidade expressa do fornecedor ou ausência comprovada daquela despesa. Campos ausentes, justificativas vazias e `null` geram pendências e bloqueiam os preços. Um dado confirmado pelo site como quantidade inicial não basta, sozinho, para confirmar mínimo ou múltiplo.

## Fretes sem dupla contagem

Cada rota acrescenta ao objeto de valor os campos `id`, `trecho`, `origem` e `destino`:

```json
{
  "id": "coleta_fornecedor_ate_casaroque",
  "trecho": "fornecedor_empresa",
  "origem": "Unidade de expedição do fornecedor identificada na cotação",
  "destino": "CasaRoque",
  "valor": null,
  "natureza": "confirmado",
  "justificativa": "Frete ainda não cotado; informar preço incluindo coleta e despesas da rota."
}
```

- `direto`: exige uma rota `fornecedor_orgao`.
- `via_empresa`: exige `fornecedor_empresa` e `empresa_orgao`; o destino da primeira deve coincidir com a origem da segunda.
- A calculadora rejeita IDs, trechos e pares origem/destino duplicados. Também rejeita misturar transporte direto com os dois trajetos via empresa.
- Consolidar coleta, pedágios e subtaxas da mesma rota em um valor explicado. Não lançar o mesmo encargo novamente em `outros`.
- Valores são os custos **atribuídos a este item no contexto identificado**. Se veio de rateio de um lote, documentar a base, os demais itens e a validade desse rateio na justificativa. A ferramenta não inventa nem executa rateio.
- Não presumir retirada pelo usuário. A cotação deve prever o terceiro responsável por coleta e entrega e todos os custos necessários.

As validações de rota evitam duplicidades declaradas. Não detectam duas despesas iguais escondidas em descrições diferentes, nem verificam distâncias ou endereços reais.

## Adjudicação parcial

Com `avaliar_parcial: true`, informar:

```json
{
  "quantidade_entrega": "1",
  "custos_exclusivos_confirmados": true,
  "condicoes_compra_mantidas": true,
  "modo_logistico": "direto",
  "fretes": [
    {
      "id": "frete_exclusivo_item",
      "trecho": "fornecedor_orgao",
      "origem": "Fornecedor",
      "destino": "Órgão",
      "valor": "60.00",
      "natureza": "estimado",
      "justificativa": "Exemplo sintético de custo exclusivo; ainda sem cotação real."
    }
  ],
  "custos_fixos": {
    "embalagem": {"valor": "10.00", "natureza": "estimado", "justificativa": "Provisão exclusiva do exemplo."},
    "carga": {"valor": "0", "natureza": "estimado", "justificativa": "Hipótese de carga incluída no frete do exemplo."},
    "descarga": {"valor": "0", "natureza": "estimado", "justificativa": "Hipótese de descarga incluída no frete do exemplo."},
    "outros": {"valor": "0", "natureza": "estimado", "justificativa": "Hipótese de inexistência de outras despesas no exemplo."}
  }
}
```

Esse objeto fica dentro da chave `parcial` do JSON principal. A quantidade parcial não pode exceder a principal. Embalagem, preço, MOQ, múltiplo, tributos e margem são reaproveitados do item principal; a quantidade comprada e as sobras são recalculadas. **Fretes e custos fixos precisam ser informados novamente e não são herdados do lote.**

O reaproveitamento exige `condicoes_compra_mantidas: true`: confirmar que preço, embalagem, MOQ, múltiplo e encargos permanecem aplicáveis na adjudicação parcial. Se o preço depender de desconto por volume ou as condições mudarem, fazer **nova execução completa com os valores recalculados**. O mínimo monetário global do fornecedor precisa de conferência separada. Frete exclusivo, sozinho, não prova viabilidade da parcial.

`custos_exclusivos_confirmados` confirma que o cenário não depende de ganhar outros itens; não confirma o preço de uma estimativa. As naturezas dos valores continuam obrigatórias. Se faltar qualquer dado da avaliação parcial solicitada, nenhum dos contextos libera preços de análise. Com `avaliar_parcial: false`, o resultado registra `NAO_AVALIADA`: não concluir que ganhar só esse item seria viável.

## Cálculos e arredondamentos

1. Embalagens necessárias = teto para o múltiplo confirmado de `máximo(quantidade / conteúdo, MOQ)`.
2. Quantidade comprada = embalagens × conteúdo. Sobra física = comprado − entregue.
3. Desembolso em produtos = embalagens × preço da embalagem, arredondado ao centavo.
4. Custo consumido = desembolso em produtos × quantidade entregue / quantidade comprada. Os cálculos de preço conservam a precisão decimal dessa divisão.
5. Estoque excedente mostrado em reais = desembolso menos custo consumido mostrado. Essa diferença equilibra o centavo residual, evitando que arredondamentos independentes alterem o desembolso.
6. Fretes e custos fixos monetários são arredondados individualmente ao centavo e incorporados integralmente ao item. Não se distribui parte desses valores ao estoque excedente.
7. Para a margem pretendida, `preço unitário = custo total do critério / quantidade / (1 − alíquota efetiva − taxas − margem)`, arredondado **para cima** em duas casas.
8. Com quantidade fracionada, o total comercial da linha é arredondado ao centavo. Se esse arredondamento reduzir a receita abaixo do necessário, o preço unitário é elevado novamente para preservar a margem calculada.

Monetários usam `ROUND_HALF_UP`; preços unitários usam `ROUND_CEILING`. Valores e quantidades precisam ser finitos; quantidades devem ser positivas, preços/custos não negativos e MOQ/múltiplo inteiros positivos. A soma de alíquota, taxas e margem precisa ser menor que 1. A ferramenta limita a 100 dígitos/expoente para rejeitar números impraticáveis; não usa `float` nos cálculos.

## Dois critérios: margem de contribuição e caixa

Para cada contexto completo, a saída apresenta:

| Cenário | Base para formar o preço | Interpretação |
|---|---|---|
| `consumo` | Produtos efetivamente entregues + fretes + fixos | Mantém o excedente como estoque. Pode atender à margem e deixar caixa negativo por causa da compra mínima. |
| `recuperacao_integral_desembolso` | Toda a compra mínima + fretes + fixos | Busca recuperar todo o dinheiro desembolsado naquela venda. O excedente continua sendo estoque; não vira custo consumido por causa desse critério. |

Ambos mostram receita, encargos pela alíquota informada, contribuição depois do custo consumido, margem de contribuição e resultado de caixa. No critério de recuperação integral, `margem_pelo_criterio_de_preco` mede a relação com o desembolso inteiro, enquanto `margem_contribuicao_sobre_consumido` usa o custo consumido. Não apresentar o primeiro como margem contábil ou lucro líquido.

Custos de R$ 100, sem frete adicional, taxas ou tributos **somente em um exemplo sintético**, exigem R$ 142,86 para margem de 30%. Com alíquota informada de 10%, exigem R$ 166,67. O teste do MOQ usa 18 pacotes de 2 unidades para entregar 5: compra 36, sobra 31 e evidencia a diferença entre margem e caixa.

## Estados e limites

| Status | Significado |
|---|---|
| `INVALIDO` | Estrutura/valor contraditório ou matematicamente inválido. Corrigir os erros. |
| `PENDENTE` | Falta dado, justificativa ou confirmação. Preços ficam `null`; quantidades conhecidas podem aparecer para auxiliar a conferência. |
| `SIMULACAO` | Entradas calculáveis, com pelo menos uma estimativa. Não é oferta pronta. |
| `CALCULO_COMPLETO` | Aritmética concluída com entradas declaradas confirmadas. Não prova veracidade, disponibilidade ou autorização. |

**`aprovado_para_assinatura` e `preco_final_liberado` permanecem sempre `false`.** `preco_unitario_analise` é uma referência calculada. Preços finais exigem revisão técnica, fiscal, comercial, prazo, estoque, transporte e aprovação no fluxo da proposta.

A ferramenta não verifica mínimo monetário global do fornecedor, compra conjunta de diversos itens, tributação legal, créditos fiscais, retenções, juros/financiamento, vencimento de cotação, capital disponível, prazo de recebimento ou capacidade de produzir. Esses pontos precisam ser avaliados no procedimento da skill. Caso existam custos fixos aplicáveis de trabalho, perdas ou financiamento, registrá-los explicitamente; não escondê-los na margem. A decisão de margem superior para transformação permanece com o usuário.

## Testes

`--self-test` cobre margem após tributos e taxas, frete desconhecido, zero sem justificativa, MOQ e múltiplos, sobras e conciliação de centavos, diferença entre contribuição e caixa, estimativas, entradas negativas/não finitas, logística duplicada e frete exclusivo parcial. Os dados são sintéticos e não constituem cotações ou parâmetros reais da CasaRoque.
