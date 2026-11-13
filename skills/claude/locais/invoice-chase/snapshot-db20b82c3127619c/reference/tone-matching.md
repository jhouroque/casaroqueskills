<!-- C:\Users\Jhonatas\AppData\Roaming\Claude\local-agent-mode-sessions\c5e8a475-a351-48d2-8db3-3f0857ad643d\1d524d29-2570-4e4b-8d1f-844a61e14635\local_f6e23d68-ce2b-4eec-b343-aeec8fb24add\outputs\cr-plugin\small-business\skills\invoice-chase\reference\tone-matching.md -->
# Calibragem de tom

Lógica de pontuação e diretrizes de tom para a cobrança da Casa Roque.

## Pontuação

Pontue cada cliente usando o histórico de pagamento dos últimos 12 meses (relatório
do Bling + extratos de Pix/repasse). Mínimo de 3 pedidos para pontuar; menos de 3
cai em `atrasa-as-vezes` por padrão.

| Pontuação | Critério |
|---|---|
| `bom-pagador` | Pagou em dia ou adiantado em ≥ 75% dos pedidos |
| `atrasa-as-vezes` | Pagou atrasado em 25–50% dos pedidos, ou menos de 3 pedidos no histórico |
| `atrasa-sempre` | Pagou atrasado em > 50% dos pedidos |

"Em dia" = pagamento identificado até a data de vencimento do boleto/pedido.

## Tom por pontuação

| Pontuação | Tom | Caráter |
|---|---|---|
| `bom-pagador` | Gentil | Cordial, supõe esquecimento. Abre dando margem. |
| `atrasa-as-vezes` | Neutro | Profissional, sem julgamento. Acompanhamento factual. |
| `atrasa-sempre` | Firme | Direto, com prazo. Sem calor, sem acusação. |

## Linhas de assunto

- Gentil: `Lembrete rápido: boleto do pedido #[N] — R$ [valor]`
- Neutro: `Acompanhamento: boleto do pedido #[N] — R$ [valor] em aberto`
- Firme: `Aviso de vencimento: boleto do pedido #[N] — R$ [valor] ([X] dias em atraso)`

## Estrutura do corpo (todos os tons)

Todo lembrete inclui: número do(s) pedido(s), valor total em aberto, vencimento
original, dias de atraso, e o meio de pagamento (2ª via do boleto ou **Pix da Casa
Roque** — oferecer os dois é o que mais funciona no atacado BR).

Acréscimos por tom:
- **Gentil**: uma frase de acolhimento ("sei como corre o dia a dia")
- **Neutro**: nenhuma — só os fatos
- **Firme**: uma frase de prazo ("peço a regularização até [data]")

Uma única ação por lembrete. Nunca duas.

## Notas de contexto BR

- **Pix é o caminho mais rápido pra receber** — ofereça sempre como alternativa ao boleto.
- **WhatsApp costuma ter resposta mais rápida que e-mail** no atacado/B2B. Tenha
  pronto o bloco pra colar no WhatsApp além do rascunho no Gmail.
- **Juros/multa de mora**: não inclua no texto por padrão. Se o JhEY quiser cobrar
  encargo, alinhar antes com ele e com a Contabilizei (não inventar percentual).
- **Marketplace não se cobra**: ML/Shopee/Pix/cartão já são pré-pagos. Esta skill
  só calibra tom para boleto/atacado/B2B em aberto.

## Regra de consolidação

Se um cliente tem vários pedidos/boletos em aberto, junte tudo num só lembrete.
Liste cada item (número do pedido, valor, vencimento) e depois o total. Use a
pontuação do cliente, não a do pedido mais atrasado.
