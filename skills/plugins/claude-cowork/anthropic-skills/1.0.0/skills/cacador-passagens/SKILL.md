---
name: cacador-passagens
description: Caça passagens aéreas nacionais e internacionais e cruzeiros com o método do Google Flights "Explorar" (mapa de preços por destino) e do Logitravel para cruzeiro saindo de Santos, com semáforo de preço, rotulagem de origem de cada número e cálculo de custo líquido da viagem. Use SEMPRE que o Jhonatas falar em passagem aérea, voo, promoção de passagem, "quanto está indo para X", "onde está barato", milhas, cruzeiro, navio, Google Flights, Explorar, ou pedir para monitorar/caçar preço de viagem — inclusive quando ele só disser "e aí, achou alguma coisa?" dentro de uma rotina de monitoramento. Também use quando ele pedir custo total de uma viagem, comparação de comprar iPhone/eletrônico nos EUA vs. Brasil, ou orçamento de viagem com dólar do dia.
---

# Caçador de passagens

## Por que esta skill existe

O Jhonatas não caça passagem buscando uma data — ele busca **o mapa**. Abre o
Google Flights → Explorar, fixa a origem (VCP, GRU ou CGH), põe um país ou
região inteira como destino, escolhe um preset de duração e lê os balões de
preço espalhados pelo mapa. Isso mostra em três segundos onde está barato, o
que uma busca por data nunca mostra. O mesmo instinto vale para cruzeiro: ele
fixa o porto (Santos) e olha o que sai de lá, não uma data específica.

O erro mais caro aqui é **publicar um número sem dizer de onde ele veio**. Ele
toma decisão de milhares de reais em cima disso. Um preço de cache de rota
apresentado como tarifa confirmada faz ele perder a passagem boa ou comprar uma
ruim. Por isso a rotulagem abaixo não é burocracia — é o núcleo da skill.

## Escolha o modo

| Ele quer... | Vá para |
|---|---|
| EUA, Europa, qualquer destino internacional | `references/internacional.md` |
| Destino no Brasil, ou "onde está barato pra viajar" | `references/nacional.md` |
| Cruzeiro, navio, sair de Santos | `references/cruzeiro.md` |

Leia o arquivo do modo antes de reportar — cada um tem faixa de preço,
armadilha e formato próprios. O que está aqui no SKILL.md vale para os três.

## O problema de acesso, e como resolver

O Google Flights **não é acessível** de um sandbox na nuvem (sem rede pra lá), e
Kayak, Skyscanner e Momondo bloqueiam páginas de busca com data no robots.txt.
A fonte mais confiável dele só existe no navegador dele. Trate isso como a
decisão número um de cada execução:

**1. Navegador do usuário disponível** (Claude in Chrome via ponte de
dispositivo, `mcp__remote-devices__*`) → caminho bom, vá direto ao Explorar.

**2. Sem navegador** (sessão agendada na nuvem, desktop desconectado) → caia
para os blogs de promoção, que são leitura pública e funcionam da nuvem. Para
cruzeiro, o Logitravel também é legível da nuvem — veja o arquivo do modo.

Não gaste tempo tentando o passo 1 numa sessão agendada — a ponte não existe
nessas execuções. Diga isso em uma linha e siga em frente.

## Método Explorar (base dos dois modos aéreos)

Reproduza o resultado, não os cliques. Navegue para
`https://www.google.com/travel/explore` e configure:

- **De onde**: o aeroporto. Rode **mais de uma origem** — GRU e VCP divergem
  muito para o mesmo destino no mesmo dia. Em 31/08/26, Nova York estava R$
  3.154 de GRU e R$ 4.596 de VCP. Só olhar VCP porque é mais perto de casa
  custa bem mais que o transfer até Guarulhos.
- **Para onde**: aceite região ampla ("Estados Unidos", "Brasil") quando a
  pergunta for "onde está barato". Cidade só quando o destino já está decidido.
- **Datas**: os presets "Viagem de uma semana nos próximos seis meses" e
  "Viagem de fim de semana..." são o que gera o mapa. Para um mês específico
  (ex.: dezembro), trave o mês no seletor de datas flexíveis — senão o mapa
  mistura seis meses e devolve o mais barato de um mês que não interessa. Esse
  é o erro mais fácil de cometer e o mais difícil de perceber depois.

Leia **os dois lados**: os balões no mapa (visão geral) e os cards da coluna
esquerda, que trazem data exata, paradas e duração. **Reporte pelo card**, que
tem data; o balão sozinho não dá para confirmar depois.

Trocar o preset de "uma semana" para "fim de semana" muda o preço bastante —
sempre diga qual preset gerou o número.

## Fallback: blogs de promoção

Em ordem de confiabilidade:

1. melhoresdestinos.com.br — o melhor, publica faixa de datas e origem
2. passageirodeprimeira.com — forte em milhas e pontos
3. passagenspromo.com.br
4. aeroin.net, panrotas.com.br — mais notícia de setor que tarifa

Extraia sempre: **data de publicação, origem exata, período de viagem coberto,
e se tem bagagem**. Posts misturam origens (um preço é do Rio, outro de São
Paulo) e misturam meses no título. Já aconteceu de um post anunciar "fim de ano
por R$ 2.760" e, no corpo, esse preço ser de janeiro. Confira o corpo antes de
reportar o título.

Sites das companhias (Copa, Avianca, LATAM, GOL, Azul, Arajet, American,
United, Delta) servem para confirmar uma tarifa achada, não para descobrir uma.

## Rotulagem obrigatória

Cada número publicado carrega um destes rótulos. Sem rótulo, não publica.

- **[PROMO PUBLICADA]** — tarifa anunciada por blog, com data de publicação e
  período de viagem. O achado mais confiável de todos.
- **[GOOGLE FLIGHTS]** — lido ao vivo no Explorar ou na busca. Diga a data do
  card, o preset usado e se é com ou sem bagagem.
- **[LOGITRAVEL]** — lido ao vivo no buscador de cruzeiro. Diga a data de saída
  e o tipo de cabine.
- **[CACHE DE ROTA]** — valor de página de rota (Skyscanner, Kayak, Decolar,
  Mundi). Escreva junto: "indicativo, não confirmado, precisa checar no
  buscador".
- **[ESTIMATIVA]** — qualquer cálculo próprio.

## Formato do relatório

Ele é engenheiro, lê rápido e odeia enrolação. Relatório longo é falha, não
zelo. Português, e o formato segue o que você achou:

**Achado 🟢 ou 🟡:**

```
🚨 ACHEI — [rótulo] R$ X/pessoa · casal R$ Y
Datas: DD/MM a DD/MM · Cia · N escalas · GRU→JFK
Bagagem: sim/não · publicado em DD/MM
Link: ...
⚠️ Confirmar no site antes de comprar.
```

**Só cache de rota:** no máximo 3 linhas, deixando claro que é indicativo.

**Nada relevante:** UMA linha. "Sem promo publicada hoje. Termômetro: R$ X
(rótulo)." Não invente conteúdo para preencher espaço — o silêncio informa.

Quando comparar origens ou presets, mostre os dois números lado a lado: a
diferença costuma ser a informação mais acionável do relatório.

Nunca reserve nem compre nada. A skill informa; a decisão é dele.

## O que guardar na memória

Quando ele fixar uma meta nova de preço, uma data nova, ou trocar o destino,
grave em `/topics/viagens.md` (método e faixas) ou no arquivo da viagem
específica em `/areas/`. Preço de uma busca pontual não vale a pena guardar —
expira sozinho.
