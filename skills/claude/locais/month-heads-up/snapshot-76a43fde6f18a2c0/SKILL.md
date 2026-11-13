<!-- C:\Users\Jhonatas\AppData\Roaming\Claude\local-agent-mode-sessions\c5e8a475-a351-48d2-8db3-3f0857ad643d\1d524d29-2570-4e4b-8d1f-844a61e14635\local_f6e23d68-ce2b-4eec-b343-aeec8fb24add\outputs\cr-plugin\small-business\skills\month-heads-up\SKILL.md -->
---
name: month-heads-up
description: >
  Roda no dia 25 — mostra a prévia de caixa dos próximos 30 dias da Casa Roque e
  destaca o que precisa de atenção antes de virar o mês: DAS (dia 20), folha
  (calendário §6), fornecedores e a meta de faturamento do mês. Use quando o JhEY
  disser "como tá o mês que vem?", "prévia do mês", "o que vem aí de conta", ou no
  lembrete do dia 25. Aceita horizonte opcional de 30 ou 60 dias.
allowed-tools: Read, Bash
---

Roda a prévia de virada de mês. Puxa os dados de caixa pra frente e dá ao JhEY um
"é isso que os próximos 30 dias parecem" com pontos concretos pra acompanhar.

Parâmetros:
- `--horizonte` (padrão: `30`) — janela da projeção em dias (`30` ou `60`)

## Passo 1 — Posição de caixa atual

Usando o fluxo da skill `cash-flow-snapshot` (sem conector — trabalhe com os
relatórios/CSV que o JhEY enviar):

1. Saldo atual em conta + Pix do dia (entrada imediata).
2. Repasses **a liberar** do Mercado Livre / Mercado Pago e da Shopee (valor
   líquido, já abatido da comissão 16% e do desconto automático da dívida ML).
3. Parcelas a receber do **NuvemPago** (vendas 3x do site) e boletos em aberto.
4. Combine para o total disponível + a entrar.

## Passo 2 — Obrigações que vêm aí

1. Custos fixos dos próximos 30 dias (folha §6, fornecedores de espuma/tecidos,
   DAS, VT/VA).
2. **Destaque obrigatório das datas-chave do mês:**
   - **DAS Simples Nacional — vence dia 20** (alíquota efetiva ~10% sobre o faturamento apurado).
   - **Folha (calendário §6):** saldo Keila R$ 840,00 (5º dia útil); Emerson R$ 1.400,00 + VA + costureiras (dia 10); adiantamento Keila R$ 560,00 + VTs R$ 250,00 cada (dia 20).
   - **Fornecedores** com vencimento no período (espuma D23/D28, tecidos, plumante).
   - **FGTS 8%** mensal; e **13º** se o mês for nov ou dez.
3. Boletos/atacado vencidos ou a vencer em até 14 dias.
4. Sinalize qualquer pagamento que jogue o saldo abaixo de uma reserva confortável
   (padrão: < R$ 5.000,00, ou metade da média de despesa mensal do JhEY) [confirmar a reserva-alvo com o JhEY].

## Passo 3 — Projeção de caixa + meta do mês

1. Projete o líquido de 30 dias: saldo atual + entradas previstas − obrigações conhecidas.
2. Identifique a **semana mais apertada** (menor saldo projetado).
3. Sinalize se alguma semana fica negativa.
4. **Compare com a meta de faturamento do mês** (CONTEXTO §5): grupo R$ 83,3 mil/mês
   (R$ 1 mi/ano); por empresa — Casa Lima R$ 137.250, Casa Weber R$ 87.000, Casa
   Roque R$ 25.750. Mostre quanto já foi faturado no mês (dos relatórios) × meta, e
   o ritmo necessário pra fechar.
   > Se o tema Casa Weber surgir: lembrar que é MEI (teto R$ 81 mil/**ano**), então
   > a meta de R$ 87 mil/mês é incompatível com MEI — sinalizar **risco de
   > desenquadramento** (alerta, não afirmação de irregularidade).

## Passo 4 — Duas coisas pra observar

No máximo dois pontos concretos e acionáveis:
- Qual boleto/atacado cobrar agora (ou repasse a antecipar).
- Qual despesa adiar/negociar.

Formato:

```
Prévia do mês — {data atual} (fuso America/Sao_Paulo)
Horizonte: próximos {X} dias

Caixa hoje: R$ {valor}
Projetado no fim do período: R$ {valor}
Semana mais apertada: {período} — projetado R$ {valor}
Faturamento do mês: R$ {parcial} de R$ {meta} ({%}) — ritmo p/ fechar: R$ {valor}/dia

DUAS COISAS PRA OBSERVAR
1. {item} — {por que importa} — sugestão: {ação}
2. {item} — {por que importa} — sugestão: {ação}

Datas do mês: DAS dia 20 · folha dias 5(útil)/10/20 · fornecedores {datas}
⚠ Folha/DAS: validar com a Contabilizei antes de pagar/declarar.
```

## Falhas de fonte de dados

Sem conector de Bling/marketplace: se faltar o relatório de repasses, rode só com
o que tem (ex.: saldo + contas a pagar do Bling) e avise: "rodei sem o relatório
de repasses do ML/Shopee — entradas de marketplace estimadas/de fora; me manda o
CSV pra fechar". Não dê número de marketplace que você não tem.

## Portões de aprovação

- **Nunca inicie pagamentos nem envie e-mail/mensagem automaticamente.** Apresente
  os dados e as ações para o JhEY decidir. Se útil, ofereça rascunho no Gmail e
  bloco pra colar no WhatsApp — só envia após aprovação.
- **Nunca projete faturamento que não esteja nos relatórios.** Use estimativas
  conservadoras e diga que são estimativas.
- Onde envolve DAS/folha/encargos: **validar com a Contabilizei**.

## Saída

Apresente a prévia formatada e ofereça rascunhar os lembretes de cobrança para
qualquer boleto/atacado sinalizado (via Gmail/WhatsApp, com aprovação).
