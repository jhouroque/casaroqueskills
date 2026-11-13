# Gmail: achar o contrato anexado

Use o conector Gmail (conta jhouroque@gmail.com) para localizar contratos anexados em
e-mails recentes.

## Buscar e-mails com contrato

Use `search_threads` com uma busca focada em anexos recentes:

```
Busca: "has:attachment (contrato OR contracto OR acordo OR fornecedor OR locação OR
proposta OR minuta OR NDA OR confidencialidade) newer_than:30d"
```

Ajuste os termos ao caso: para fornecedor de espuma/tecido use "fornecimento", para
agência use "agência OR marketing OR assessoria", para o barracão use "locação OR
aluguel OR imóvel".

## O que fazer com o resultado

1. Apresente uma lista curta (assunto, remetente, data) se houver vários candidatos.
2. Peça ao JhEY para confirmar qual antes de baixar.
3. Use `get_thread` para abrir o thread, localize e leia o anexo (PDF/DOCX).

## Fallback

Se o Gmail não estiver conectado ou não houver anexo correspondente:

```
"Não achei um contrato anexado recente no Gmail — me encaminha o e-mail ou anexa o
arquivo direto aqui."
```

## O que NÃO fazer

- Não leia e-mails sem relação com o contrato (nada de vasculhar a caixa toda).
- Não envie nenhuma resposta ou rascunho durante a revisão.
