# Modelo de saída

Esta é a estrutura exata que todo pulso segue. Não reordene as seções. Omita uma seção só se a fonte dela não retornou dado — nunca deixe cabeçalho vazio.

Variáveis em `{{chaves duplas}}` são marcadores — troque pelo valor calculado. Convenção de seta: ▲ subiu, ▼ caiu, ▬ estável (< 1% de variação). Sempre mostre o valor do delta depois da seta. Moeda em R$ com vírgula (R$ 1.234,56); datas dd/mm/aaaa; fuso America/Sao_Paulo.

---

```markdown
# Pulso do Negócio — {{dd/mm/aaaa}}

**Geral: {{🟢|🟡|🔴}} {{status em uma linha, ex.: "Vendas estáveis; 2 perguntas no ML sem resposta há 3h."}}**

## TL;DR

- {{Fato mais importante com número, ex.: "Vendas R$ 12.300 nos últimos 7 dias, ▼ 9% vs a semana anterior — Shopee caiu."}}
- {{Segundo, ex.: "Trocador americano em 3 unidades — risco de ruptura."}}
- {{Terceiro, ex.: "DAS de R$ 1.450,00 vence dia 20; caixa coberto."}}

---

## 💰 Caixa & Finanças — {{🟢|🟡|🔴}}

- **Saldo em conta**: R$ {{SALDO}} ({{▲|▼|▬}} R$ {{DELTA}} vs semana anterior)
- **Faturamento do mês**: R$ {{MES}} vs meta R$ {{META}} ({{PCT}}% da meta proporcional ao dia)
- **A receber**: R$ {{AR}} · **A pagar (próx. vencimentos)**: R$ {{AP}}

**Vencimentos próximos**
- {{obrigação}} — R$ {{valor}} ({{dd/mm}})
- {{ex.: "DAS Simples Nacional — R$ 1.450,00 (20/06)"}}

{{Se sem dado: "Caixa: n/d — sem relatório do Bling/extrato (me manda que eu fecho)."}}

---

## 📈 Vendas — {{🟢|🟡|🔴}}

- **Últimos 7 dias**: R$ {{V7}} ({{▲|▼|▬}} {{PCT}}% vs os 7 dias anteriores)
- **Por canal**: ML R$ {{ML}} · Shopee R$ {{SHOPEE}} · Site R$ {{SITE}} {{omita o que não veio}}
- **Ticket médio**: R$ {{TICKET}} (meta R$ 200,00)

{{Se sem dado: "Vendas: n/d — sem relatório do ML/Shopee/site."}}

---

## 🔮 Pré-venda (perguntas/leads) — {{🟢|🟡|🔴}}

- **Perguntas em aberto**: {{N}} (ML {{n}}, Shopee {{n}}, WhatsApp {{n}})
- **Mais antiga sem resposta**: {{tempo}} {{🟡 se > 2h | 🔴 se > 4h}}

**Precisa de resposta (POP 4, meta < 2h)**
- {{canal}} — {{N}} perguntas há {{tempo}}
- {{ou "Tudo respondido em < 2h."}}

---

## 📅 Esta Semana

- {{Reunião/prazo — quem, por que importa}}
- {{ex.: "Seg 9h — reunião com Thomas (tráfego)"}}
- {{ex.: "Sex 15h — batimento NF x estoque (POP 3)"}}
{{3–5 itens. Omita ruído interno.}}

---

## ✉️ Watch-list

- {{fonte}} — {{resumo em uma linha do que precisa de atenção}}
- {{ex.: "Estoque — trocador americano em 3 un (alerta Emerson)"}}
- {{ex.: "Gmail — cliente pedindo reembolso (pedido #1234)"}}
{{Ou: "Nada urgente detectado." — inclua explícito pro JhEY saber que a checagem rodou.}}

---

## ⚠️ Nº 1 do Dia

{{Uma coisa específica pra agir hoje. Nomeie valores, pessoas, prazos.
Não "revisar o caixa" — diga "Responda as 2 perguntas no ML paradas há 3h
(POP 4 pede < 2h) antes que vire nota baixa." ou "Repor o trocador americano
(3 un) — é campeão de venda e pode romper essa semana."}}

---

## Apêndice

**Janela**: {{intervalo de datas, dd/mm a dd/mm}}

**Fontes usadas**: {{lista do que retornou dado}}

**Fontes indisponíveis**: {{lista com motivo, ex.: "Bling — sem relatório anexado" ou "Gmail — erro de auth"}}

**Limiares**: {{notar qualquer limiar ainda no padrão "confirmar com o JhEY"}}
```

---

## Regras de formatação

1. **Valores**: R$ com vírgula decimal e ponto de milhar — `R$ 1.234,56`, `R$ 12.300,00`. Sem abreviar pra "k/m".
2. **Percentuais**: uma casa pra tendências (ex.: "▼ 8,3%"), inteiros nos demais.
3. **Datas**: dd/mm/aaaa em prosa e em metadados. Fuso America/Sao_Paulo.
4. **Espaço da seta**: `▲ R$ 2.000,00` não `▲R$ 2.000,00`.
5. **Tamanho**: mire uma página. Duas no máximo. Se uma seção inchar, enxugue.
6. **Sem conector de venda**: caixa e vendas podem vir "n/d" — é o esperado, não um erro. Mostre a lacuna com elegância e ofereça pedir o relatório.
