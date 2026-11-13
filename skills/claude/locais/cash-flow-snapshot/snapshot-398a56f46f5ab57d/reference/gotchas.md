<!-- C:\Users\Jhonatas\AppData\Roaming\Claude\local-agent-mode-sessions\c5e8a475-a351-48d2-8db3-3f0857ad643d\1d524d29-2570-4e4b-8d1f-844a61e14635\local_f6e23d68-ce2b-4eec-b343-aeec8fb24add\outputs\cr-plugin\small-business\skills\cash-flow-snapshot\reference\gotchas.md -->
# Pegadinhas — projeção de caixa (Casa Roque)

Casos de borda e modos de falha conhecidos. Formato Certo/Errado.

---

## 1. Faturamento bruto ≠ caixa: o repasse já vem líquido

**Errado:** Usar o valor **bruto** da venda no marketplace como entrada de caixa.
A Casa Roque vende em ML e Shopee, e o que cai na conta é o **repasse líquido**:
faturamento − comissão 16% − **desconto automático da dívida do grupo no ML**.

**Certo:** Modele a entrada pelo **valor líquido do repasse** (o que o relatório
de repasses do ML/Mercado Pago/Shopee mostra como "a liberar"). A dívida do ML
(Casa Roque ~R$ 80 mil, Casa Weber ~R$ 75 mil) é abatida **na origem**, então
**não** lance esse desconto como uma saída separada — ele já está dentro do
repasse líquido. Lançar dos dois lados conta a dívida em dobro.

---

## 2. Liberação de repasse não é à vista — tem prazo D+

**Errado:** Assumir que a venda no marketplace vira caixa no dia. ML e Shopee
**seguram o dinheiro** (geralmente até depois da entrega/confirmação, com prazo
que varia por canal e por reputação do vendedor).

**Certo:** Use a **data prevista de liberação** do relatório de repasses, não a
data da venda. Calcule o prazo médio e o desvio-padrão por canal a partir do
histórico (ML costuma ser mais longo que Shopee). É essa variância que define a
banda de confiança. Se o relatório não trouxer a data prevista, pergunte: "qual
o prazo médio de liberação que você vê hoje no ML e na Shopee?".

---

## 3. Antecipação de recebíveis adianta o caixa, mas come margem

**Errado:** Tratar uma antecipação de repasse (Mercado Pago/Shopee/NuvemPago)
como entrada cheia na data antecipada. A antecipação **cobra taxa** — entra menos.

**Certo:** Se o JhEY antecipou (ou pergunta se compensa antecipar), registre o
**valor líquido após a taxa** na data antecipada, e sinalize o custo como risco:
"antecipar R$ X adianta a entrada em ~Y dias, mas custa ~Z% — fôlego imediato
com custo". Não confunda fôlego de caixa com lucro: antecipar resolve liquidez,
não melhora margem. Em dúvida sobre a taxa, peça o número no relatório.

---

## 4. Colunas de CSV variam entre Bling, ML e Shopee

**Errado:** Exigir nomes exatos de coluna ("Data", "Valor", "Tipo"). O Bling
exporta "Vencimento", "Histórico", "Valor"; o relatório de repasses do ML usa
"Data de liberação", "Valor líquido"; a Shopee usa outros rótulos ainda. Parsing
rígido falha calado.

**Certo:** Faça correspondência aproximada dos cabeçalhos (data → vencimento →
data de liberação; valor → valor líquido; tipo → histórico → categoria). Mostre
a linha de cabeçalho e confirme o mapeamento antes de calcular — uma pergunta é
melhor que uma projeção errada em silêncio. Atenção ao **separador decimal**:
relatórios BR usam vírgula (R$ 1.234,56); não interprete o ponto de milhar como decimal.

---

## 5. Estorno / devolução tira dinheiro que já tinha entrado

**Errado:** Ignorar devoluções e estornos. No e-commerce de enxoval/bebê há
troca e devolução (POP de devolução: SAC → etiqueta de retorno → conferência do
Emerson → reembolso ou reenvio). Um reembolso **debita** um repasse que já tinha
sido contado como entrada.

**Certo:** Se o relatório de repasses mostrar débitos por estorno/devolução/disputa,
abata-os da entrada do canal na janela correspondente. Se houver muita devolução
no histórico, considere uma reserva conservadora (ex.: % médio de devolução) e
sinalize: "estou descontando ~X% de devolução com base no histórico — confere?".

---

## 6. Folha não é um número só — é um calendário (e tem dia 20 cheio)

**Errado:** Lançar "folha" como uma saída única no fim do mês, como se fosse
salário americano quinzenal. A folha da Casa Roque é **escalonada** (CONTEXTO §6)
e o **dia 20 acumula** várias obrigações.

**Certo:** Distribua as saídas pelas datas reais: saldo da Keila R$ 840,00 no 5º
dia útil; Emerson R$ 1.400,00 + VA + costureiras no dia 10; **dia 20 = DAS +
adiantamento Keila R$ 560,00 + VTs R$ 250,00 cada**. Provisione FGTS 8% mensal e,
se a janela cruzar nov/dez, o 13º (1ª parcela até 30/nov, 2ª até 20/dez). Sempre
feche com o aviso: validar valores com a Contabilizei antes de pagar.

---

## 7. A fórmula da banda quebra quando o prazo de liberação é ≈ 0

**Errado:** Dividir o desvio-padrão por um prazo médio de 0 (caso do Pix, que cai
na hora) gera divisão por zero ou banda infinita.

**Certo:** Se o prazo médio for ≤ 1 dia (Pix), fixe a banda em 5% (variância
baixa, crédito quase imediato). Não tente a divisão.
