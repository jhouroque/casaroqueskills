<!-- C:\Users\Jhonatas\AppData\Roaming\Claude\local-agent-mode-sessions\c5e8a475-a351-48d2-8db3-3f0857ad643d\1d524d29-2570-4e4b-8d1f-844a61e14635\local_f6e23d68-ce2b-4eec-b343-aeec8fb24add\outputs\cr-plugin\small-business\skills\plan-payroll\SKILL.md -->
---
name: plan-payroll
description: >
  Responde "dá pra fechar a folha esse mês?" para a Casa Roque. Encadeia a
  projeção de caixa (cash-flow-snapshot) com a cobrança de pendências
  (invoice-chase) e compara o saldo projetado com o total da folha do período
  (calendário §6: Keila, Emerson, costureiras, VT/VA) mais provisões (FGTS 8%,
  13º se nov/dez). Use quando o JhEY disser "fecha a folha?", "dá pra pagar a
  equipe esse mês?", "tô apertado pro dia 10/dia 20" ou pedir para planejar a folha.
allowed-tools: Read, Bash
---

Roda o pipeline de confiança da folha encadeando duas skills. O JhEY aprova a
cada passagem — nunca envie cobrança nem dê uma projeção como fechada sem
confirmação explícita.

Parâmetros:
- `--horizonte` (padrão `30`) — janela da projeção em dias (30, 60 ou 90)
- `--data-folha` (opcional) — a data-alvo da folha. **Padrão = próximo evento de
  folha do calendário §6**, NÃO "próxima sexta". Os eventos são: **dia 10**
  (Emerson R$ 1.400,00 + VA + costureiras), o **5º dia útil** (saldo Keila
  R$ 840,00) e o **dia 20** (adiantamento Keila R$ 560,00 + VTs R$ 250,00 cada +
  DAS). Use a data do próximo desses eventos a partir de hoje (fuso America/Sao_Paulo).

## Passo 1 — Projeção de caixa (cash-flow-snapshot)

Aciona o fluxo da skill `cash-flow-snapshot`:
1. Peça/leia os relatórios: contas a receber/pagar do **Bling** (CSV), repasses
   **Mercado Livre / Mercado Pago / Shopee**, parcelas **NuvemPago**, Pix/boleto.
   (Não há conector — trabalhe com os arquivos enviados.)
2. Inclua os custos fixos do período: fornecedores (espuma, tecidos), folha
   (calendário §6), DAS (dia 20), VT/VA, e o **desconto automático da dívida ML**
   (já abatido no repasse líquido — não lançar duas vezes).
3. Produza a projeção 30/60/90 (use o `--horizonte` pedido) com bandas de confiança
   pela variância de liberação dos repasses.
4. Sinalize riscos nomeados — ex.: "a folha + DAS de novembro caem entre os dias
   5 e 20, e na banda baixa o caixa do dia 19 fica R$ 4.200,00 abaixo do total."
5. Entregue resumo no chat + planilha XLSX.
6. Apresente ao JhEY. Espere um "ok, vê o que dá pra cobrar/antecipar" explícito
   antes do Passo 2.

Se a projeção mostrar a folha **confortavelmente coberta**, pergunte se ainda
vale cobrar pendências/antecipar repasse ou se para por aqui.

## Passo 1b — Comparar saldo projetado × total da folha do período

Monte a conta da folha do período-alvo usando os valores do CONTEXTO §6 (não invente):

| Item | Valor | Data |
|---|---|---|
| Keila — saldo 60% | R$ 840,00 | 5º dia útil |
| Keila — adiantamento 40% | R$ 560,00 | dia 20 |
| Keila — VT | R$ 250,00 | dia 20 |
| Emerson — salário | R$ 1.400,00 | dia 10 |
| Emerson — VT | R$ 250,00 | dia 20 |
| VA Keila + Emerson | [confirmar valor] | dia 10 |
| Cleusa (costureira, por demanda) | [confirmar valor do mês] | dia 10 |
| Vanda (lençóis, R$ 2,00/lençol) | [confirmar qtde × R$ 2,00] | dia 10 |
| **Provisão FGTS 8%** (sobre salário bruto CLT Keila + Emerson) | ~R$ 224,00/mês | depósito mensal |
| **Provisão 13º** (só se o período cruzar nov/dez) | 1ª parcela até 30/nov · 2ª até 20/dez | nov/dez |

> Dissídio de 6% pendente desde out/2025 para Keila e Emerson — se já tiver sido
> aplicado, ajuste os salários; senão, sinalize que o número pode subir.

Compare o **saldo projetado na data-folha (banda baixa)** com o **total da folha
do período**. Conclua: **coberto**, **aperto** (cobre no esperado mas não na banda
baixa) ou **gap** (não cobre). Mostre o valor da diferença em R$.

## Passo 2 — Cobrar pendências / antecipar (invoice-chase)

Depois da aprovação do Passo 1, aciona o fluxo da skill `invoice-chase`:
1. Levante o que está em aberto: **boletos do site/atacado**, **pedidos B2B/atacado
   aguardando pagamento** (a Casa Roque vende quase tudo à vista — marketplace/Pix/
   cartão já são pagos; o foco da cobrança é o que NÃO é à vista).
2. Ordene por valor × dias em atraso × histórico do cliente.
3. Para cada um, rascunhe um lembrete no tom certo (gentil para bom pagador, firme
   para quem atrasa sempre). Envio via **Gmail/WhatsApp** — nunca PayPal.
4. Considere também **antecipação de repasse** como alternativa para fechar o gap
   (mostrando a taxa) — mas isso é decisão do JhEY.
5. Apresente a lista ordenada com os rascunhos. Mostre o impacto no caixa se um
   subconjunto top-N for pago/antecipado dentro do horizonte — isso fecha o gap do Passo 1b?
6. Espere um "manda esses" explícito (por item ou em lote) antes de enviar.

## Portões de aprovação (obrigatórios)

- Nunca envie lembrete sem aprovação do JhEY — só rascunho até o "manda".
- Nunca trate a projeção como definitiva sem o aval do JhEY.
- Onde envolve folha/imposto/encargos: **validar com a Contabilizei antes de
  pagar/declarar**.
- Se faltar um relatório (Bling, repasses), pare, diga qual faltou, e pergunte se
  o JhEY manda o arquivo ou se seguimos só com o que tem (sinalizando a lacuna).

## Saída

Encerre com um parágrafo de recapitulação: veredito da folha (coberto / aperto /
gap com valor em R$), o que foi rascunhado e pra quem, e o novo saldo projetado
se as cobranças/antecipações entrarem. Lembrete final: validar folha e DAS com a
Contabilizei antes de pagar.
