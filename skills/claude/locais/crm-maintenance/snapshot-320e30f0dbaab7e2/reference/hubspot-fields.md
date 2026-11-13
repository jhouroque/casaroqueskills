# Campos da planilha de contatos

As colunas da planilha de contatos da Casa Roque (Google Sheets/Drive) que a skill `crm-maintenance` lê e grava. Só os campos listados aqui estão no escopo — qualquer outra coluna que o JhEY tenha na planilha fica intocada.

> **Não há CRM.** A "base" é uma planilha com duas abas: **Contatos** (uma linha por cliente) e **Conversas** (uma linha por interação). Datas dd/mm/aaaa, fuso America/Sao_Paulo, R$ com vírgula.

## Aba Contatos — gravar

| Coluna | Uso |
|---|---|
| `Nome` | Nome do cliente. No marketplace só vem o **apelido/usuário** do comprador — registre o apelido e marque que é apelido. Não invente nome civil. |
| `Canal` | Por onde veio/compra: `Mercado Livre`, `Shopee`, `Site`, `WhatsApp`, `Instagram`. Se compra em mais de um, liste o principal. |
| `Telefone/WhatsApp` | Número com DDD. Só preencha se o cliente informou direto (WhatsApp, e-mail, pedido do site). **O marketplace oculta o telefone** — deixe em branco quando o contato veio só de pergunta de ML/Shopee. |
| `E-mail` | E-mail real (Gmail, pedido do site). Marketplace não expõe e-mail real — deixe em branco. Identificador para deduplicar. |
| `Tipo` | `Varejo` (padrão) ou `Atacado` (B2B/revenda). Atacado tende a recomprar — agende follow-up. |
| `Último pedido` | Data (dd/mm/aaaa) e nº do pedido/venda do Bling ou do marketplace, quando informado. |
| `Valor último pedido` | R$ com vírgula (ex.: R$ 189,90). Para atacado, o valor do último fechamento. |
| `Status` | `Ativo`, `Parado` (sem interação há > 90 dias) ou `Inativo` (não comprar/arquivado). Nunca apague — mude o status. |
| `Próximo follow-up` | Data (dd/mm/aaaa) do próximo contato planejado, quando houver. Em branco se não há follow-up agendado. |

Não grave outras colunas que o JhEY tenha criado (anotações pessoais, tags próprias). Esses campos são dele — nunca sobrescreva.

## Aba Contatos — ler (para busca)

| Coluna | Uso |
|---|---|
| `Telefone/WhatsApp` | Chave de busca principal (cliente que veio por WhatsApp). |
| `E-mail` | Chave de busca (cliente do site ou Gmail). Comparação sem diferenciar maiúscula/minúscula. |
| `Nome` · `Canal` · `Tipo` | Exibidos ao JhEY na hora de resolver ambiguidade. |

## Aba Conversas — gravar

| Coluna | Uso |
|---|---|
| `Data` | dd/mm/aaaa (data da interação, não a de hoje). |
| `Contato` | Nome/apelido que liga à aba Contatos. |
| `Canal` | `WhatsApp`, `Telefone`, `E-mail`, `Pergunta ML`, `Pergunta Shopee`, `Instagram`. |
| `Resumo` | 1–2 frases: o que o cliente quis e o que ficou combinado. Não cole a thread/print inteiro. |
| `Pedido relacionado` | Nº do pedido/venda, se a conversa for sobre uma compra. Em branco se for pré-venda. |

## Aba Contatos — campos de "negócio"/pedido de atacado (faxina, só com aprovação)

Para clientes `Tipo = Atacado`, o "pedido em aberto" é tratado como um negócio em andamento. Campos propostos só com aprovação:

| Coluna | Regra |
|---|---|
| `Próximo follow-up` | Propor atualização; gravar só com "ok" explícito do JhEY. |
| `Último pedido` / `Valor último pedido` | Propor atualização quando a conversa recente indicar fechamento; gravar só com aprovação. |
| `Status` | Propor `Parado` quando não há interação há > 90 dias; **nunca** dar por "ganho/perdido" sozinho. |

**Nunca grave** `Status = Inativo`, nem apague linha, nem mexa em colunas próprias do JhEY numa faxina. Isso é decisão dele.

## Regras de registro

- Toda linha da aba **Conversas** precisa ligar a um contato da aba **Contatos** (pelo `Nome`/apelido ou `Telefone/WhatsApp`).
- Se o contato for criado na hora (durante o registro de uma conversa), crie a linha na aba Contatos **antes** de gravar a conversa, pra ligação não ficar órfã.
- Não crie linha de conversa pra alguém que não participou daquela interação. Uma conversa = um cliente.
- Use sempre os valores de `Canal` da lista acima — não invente rótulos novos (mantém os filtros da planilha funcionando).
