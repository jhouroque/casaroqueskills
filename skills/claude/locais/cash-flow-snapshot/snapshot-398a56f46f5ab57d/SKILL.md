<!-- C:\Users\Jhonatas\AppData\Roaming\Claude\local-agent-mode-sessions\c5e8a475-a351-48d2-8db3-3f0857ad643d\1d524d29-2570-4e4b-8d1f-844a61e14635\local_f6e23d68-ce2b-4eec-b343-aeec8fb24add\outputs\cr-plugin\small-business\skills\cash-flow-snapshot\SKILL.md -->
---
name: cash-flow-snapshot
description: >
  Monta uma projeção de fluxo de caixa de 30/60/90 dias para a operação de
  e-commerce da Casa Roque. Lê contas a receber/pagar, prazos históricos de
  liberação dos repasses (Mercado Livre, Mercado Pago, Shopee), parcelas
  futuras do NuvemPago (3x), Pix/boleto, e os custos fixos conhecidos
  (fornecedores, folha, DAS, VT/VA, desconto automático da dívida no ML).
  Não há conector de Bling/marketplace — trabalha com relatórios/CSV exportados.
  Entrega um resumo no chat e uma planilha XLSX. Use quando o JhEY disser
  "projeta meu caixa", "fecha a folha esse mês?", "tô apertado", "quanto
  entra/sai esse mês", "vai sobrar?" ou falar em fôlego de caixa.
compatibility: "Trabalha com relatórios/CSV exportados do Bling, dos repasses ML/Mercado Pago/Shopee, do NuvemPago e extratos Pix/boleto (sem conector dedicado). Saída usa a skill xlsx. Conectores ativos só de apoio: Gmail, Google Agenda, Google Drive."
---

# Projeção de fluxo de caixa (cash-flow-snapshot)

Monta uma projeção de caixa de 30/60/90 dias com bandas de confiança (por
variância de liberação dos marketplaces) e riscos nomeados. Entrega em duas
partes: um resumo curto no chat e uma planilha XLSX auditável.

**Início rápido**

> "Vai dar pra fechar a folha esse mês?"

O Claude lê contas a receber/pagar e custos fixos dos relatórios/CSV que o JhEY
mandar, projeta entradas e saídas nas janelas de 30, 60 e 90 dias, aplica bandas
de confiança pela variância de liberação dos repasses, e aponta os riscos pelo nome.

---

## Fluxo de trabalho

### Passo 1 — Identificar as fontes de dados

A Casa Roque **não tem conector** de Bling, Mercado Livre, Mercado Pago, Shopee
ou NuvemPago. Então a fonte são os **relatórios/CSV exportados**. Peça nesta ordem
(o que o JhEY tiver à mão):

1. **Bling** — relatório de **contas a receber** e **contas a pagar** (CSV/PDF): fornecedor/cliente, valor, vencimento.
2. **Repasses Mercado Livre / Mercado Pago** — relatório de **liberações** (release): valor da venda, data da venda, data prevista de liberação (D+), se houve antecipação e a taxa.
3. **Repasses Shopee** — relatório de **saldo a liberar / repasses**: valor, data prevista de liberação.
4. **NuvemPago (site)** — relatório de **parcelas a receber** (vendas 3x sem juros): valor de cada parcela e data prevista.
5. **Extratos Pix / boleto** — entradas à vista (Pix) e boletos em aberto (site/atacado).

Se nada foi anexado, peça de forma objetiva:
> "Me manda o relatório de contas a receber/pagar do Bling (CSV) e o de repasses do ML e da Shopee. Se tiver vendas parceladas no site, manda também o de parcelas a receber do NuvemPago."

Anote quais fontes foram usadas no resultado — isso afeta a largura das bandas de confiança.

### Passo 2 — Puxar os dados

**Do Bling (contas a receber/pagar):**
- A receber: cliente, valor, vencimento, dias em aberto (foco em boletos/atacado).
- A pagar: fornecedor (espuma D23/D28, tecidos, plumante), valor, vencimento.

**Dos repasses ML / Mercado Pago / Shopee:**
- Para cada venda: valor bruto, comissão do marketplace (16%), valor líquido, **data prevista de liberação** (D+, varia por canal e por reputação).
- Se houver **antecipação de recebíveis**, registrar a taxa cobrada e a data antecipada — entra mais cedo, mas com desconto (ver `reference/gotchas.md`).

**Do NuvemPago (parcelas 3x):**
- Cada parcela futura: valor e data prevista de crédito.

**De Pix/boleto:**
- Pix = entrada imediata (D0/D+1). Boleto em aberto = entrada na data de pagamento (cliente pode atrasar).

Se as colunas do CSV estiverem ambíguas, mostre o cabeçalho e confirme o mapeamento antes de calcular (ver `reference/gotchas.md`).

### Passo 3 — Calcular prazos históricos de liberação

Para cada canal de entrada, calcule a partir do histórico de repasses:
- **Prazo médio de liberação** — dias entre a venda e o crédito efetivo (ex.: ML libera em ~D+X após entrega/confirmação; Shopee em ~D+Y).
- **Variância do prazo** — desvio-padrão do prazo de liberação nos últimos repasses.
- Use a variância para definir a largura da banda de confiança (Passo 4).

Se houver menos de 3 repasses de um canal no histórico, use o prazo médio do
canal como estimativa pontual e aplique banda padrão de **±30%**. Com histórico
suficiente (≥3 repasses), calcule a banda pela **variância real** — não assuma ±30%.

> Pix tem prazo ~0 e variância baixa: trate como banda de 5% (ver `reference/gotchas.md`, divisão por prazo ≈ 0).

### Passo 4 — Montar a projeção 30/60/90 dias

Três janelas: 0–30 dias, 31–60 dias, 61–90 dias.

Para cada janela, calcule:

| Linha | Método |
|---|---|
| Entradas previstas | Repasses ML/Shopee liberando na janela (ajustados pelo prazo médio) + parcelas NuvemPago da janela + Pix + boletos a vencer |
| Saídas previstas | Contas a pagar (Bling) na janela + folha do período (calendário §6 do CONTEXTO) + DAS (dia 20) + VT/VA + **desconto automático da dívida ML** |
| Caixa líquido | Entradas − Saídas |
| Banda de confiança | ± média ponderada da variância de liberação, como % das entradas previstas |

**Saídas fixas obrigatórias a incluir (CONTEXTO §5/§6):**
- **Folha**: Keila R$ 840,00 (saldo 60%, 5º dia útil) + Keila R$ 560,00 (adiantamento 40%, dia 20) + VT Keila R$ 250,00 (dia 20); Emerson R$ 1.400,00 (dia 10) + VT R$ 250,00 (dia 20); VA Keila e Emerson (dia 10) [confirmar valor do VA]; costureiras Cleusa e Vanda (dia 10, por demanda).
- **DAS Simples Nacional**: vence **dia 20** (alíquota efetiva ~10% sobre o faturamento do mês apurado).
- **Encargos**: FGTS 8% sobre o salário bruto (depósito mensal). Se a janela cruzar nov/dez, provisione **13º** (1ª parcela até 30/nov, 2ª até 20/dez).
- **Fornecedores**: espuma D23/D28 (R$ 653,33/m³), tecidos, plumante — conforme contas a pagar do Bling.
- **Desconto automático da dívida ML**: a dívida do grupo no Mercado Livre (Casa Roque ~R$ 80 mil, Casa Weber ~R$ 75 mil) é **descontada automaticamente no faturamento** antes do repasse. Ou seja, o repasse ML já chega líquido desse desconto — modele a entrada ML **já abatida**, não como uma saída separada (ver `reference/gotchas.md`).

Fórmula da banda de confiança:
```
banda_pct = desvio_padrao_medio_ponderado_dias / prazo_medio_liberacao_dias
baixo = caixa_liquido × (1 − banda_pct)
alto  = caixa_liquido × (1 + banda_pct)
```

Arredonde a banda_pct para uma casa decimal. Limite em ±50% — variância maior
significa que os dados são finos demais para modelar; nesse caso, sinalize como
risco (Passo 5) em vez de mostrar a banda.

### Passo 5 — Sinalizar riscos nomeados

Procure condições que empurrem a banda baixa para o negativo ou criem aperto de
caixa. Para cada risco, gere uma linha objetiva:

- **Aperto na folha:** "Folha + DAS de novembro (R$ X) caem entre os dias 5 e 20. Caixa na banda baixa no dia 19: R$ Y. Risco de faltar: R$ Z."
- **Liberação atrasada de repasse:** "O repasse Shopee de R$ X tem liberação prevista pra D+Y; isso joga a entrada pra fora da janela de 30 dias."
- **Dados finos:** "Só 2 repasses do canal no histórico — banda ajustada para o padrão de ±30%."
- **Sem conector / dados parciais:** "Rodando só com o CSV de contas a receber do Bling — sem o relatório de repasses do ML/Shopee. As bandas estão mais largas que o normal."
- **Antecipação com taxa:** "Antecipar o repasse ML de R$ X adianta a entrada em ~Y dias, mas custa ~Z% de taxa — fôlego imediato com custo (ver gotchas)."

Limite aos 5 riscos mais relevantes (maior impacto em R$ primeiro).

### Passo 6 — Entregar os resultados

**Resumo no chat** (sempre):
```
Projeção de caixa — [período] (fuso America/Sao_Paulo)
Fontes: [relatórios/CSV usados]

              Esperado    Baixo      Alto
30 dias:      R$ X.XXX    R$ X.XXX   R$ X.XXX
60 dias:      R$ X.XXX    R$ X.XXX   R$ X.XXX
90 dias:      R$ X.XXX    R$ X.XXX   R$ X.XXX

⚠ Riscos sinalizados: [quantidade]
  • [risco 1]
  • [risco 2]
  ...

⚠ Números de folha/imposto: validar com a Contabilizei antes de pagar/declarar.
```

Se for útil, gere também um **bloco curto pra colar no WhatsApp** (ex.: avisar a Keila/Emerson de que a folha está coberta) e ofereça **rascunho no Gmail** com a projeção. Nada é enviado sem aprovação (ver portões de aprovação).

**Planilha XLSX** (sempre):
Leia `xlsx/SKILL.md` antes de gerar. Produza uma planilha com três abas:

1. **Resumo** — a tabela 30/60/90 com bandas de confiança. Abaixo de cada janela,
   expanda sub-linhas com as transações que compõem as entradas (verde) e saídas
   (vermelho). Isso torna as estimativas auditáveis sem sair da aba.

2. **Detalhe** — todas as transações agrupadas por janela, ordenadas por data
   dentro de cada grupo. Inclua uma coluna de saldo acumulado e uma linha de
   subtotal ao fim de cada janela (total de entradas, total de saídas, líquido).
   Coloque as transações já passadas numa seção cinza no fim, para referência.
   Garanta que as três janelas tenham linhas mesmo se uma estiver vazia — use uma
   linha "Sem transações nesta janela".

3. **Riscos** — os riscos sinalizados com impacto em R$ e a janela afetada.

Salve como `projecao-caixa-[AAAA-MM-DD].xlsx`.

---

## Portões de aprovação

Sem ações destrutivas — a projeção em si é só leitura. Não precisa de aprovação
para gerar a projeção.

Antes de **enviar** qualquer rascunho (Gmail) ou bloco de WhatsApp, peça aprovação
explícita do JhEY. Rascunho primeiro, sempre.

Aviso obrigatório na entrega (envolve dinheiro/folha/imposto):
> "Esta projeção usa [fontes listadas] e não substitui o contador. Valide os
> números de folha, DAS e encargos com a Contabilizei antes de pagar/declarar."

---

## Arquivos de referência

| Arquivo | Carregar quando |
|---|---|
| `reference/gotchas.md` | Quando um relatório/repasse vier estranho, a variância estourar, ou surgir antecipação, dívida ML, estorno/devolução |
| `reference/examples/worked-example.md` | Quando precisar do modelo de saída para um novo formato de dados |
