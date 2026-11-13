# Fontes de dados

Mapa de cada seção do pulso pra fonte que a produz na Casa Roque. **Dispare o que for conector num único lote paralelo** — não puxe em série.

> **Conectores ativos:** Gmail, Google Agenda, Google Drive, Canva. **Sem conector:** Bling, Mercado Livre, Shopee, NuvemShop (site), NuvemPago. As seções de caixa e venda trabalham com **relatórios/CSV exportados, prints ou extrato** que o JhEY anexa.

## Caixa & Finanças (Bling / extrato bancário)

| Métrica | Fonte | Notas |
|---|---|---|
| Saldo em conta | Extrato bancário / print | Saldo atual; mostre delta vs a semana anterior se houver |
| Faturamento do mês | Relatório de vendas do Bling (mês) | Acumulado do mês vs meta (grupo ~R$ 83,3 mil/mês; Casa Lima R$ 137.250, Casa Weber R$ 87.000, Casa Roque R$ 25.750) |
| Contas a receber | Relatório de contas a receber do Bling | Boletos/atacado em aberto; repasses ML/Shopee a liberar |
| Contas a pagar | Relatório de contas a pagar do Bling | Fornecedores (espuma D23/D28, tecidos, plumante), folha, DAS, VT/VA |
| Vencimentos próximos | Bling + calendário §6 | Folha (dias 5/10/20), DAS (dia 20), desconto automático da dívida no ML |

**Tratamento sem conector:** não há MCP de Bling. Se o JhEY não anexou relatório/extrato, marque a seção inteira de Caixa como "n/d — sem relatório do Bling/extrato" e siga. Não tente de novo nem fique pedindo. Ofereça uma vez: "me manda o relatório de contas a receber/pagar do Bling e o saldo (print do extrato) que eu fecho a parte de caixa."

## Vendas (Mercado Livre / Shopee / site NuvemShop)

| Métrica | Fonte | Notas |
|---|---|---|
| Total 7 dias | Relatório/export de vendas (ML, Shopee, site) | Soma dos últimos 7 dias |
| Tendência 7d vs 7d | Mesmo relatório | Últimos 7 dias vs os 7 anteriores; calcule o delta % |
| Por canal | Export de cada canal ou consolidado do Bling | ML e Shopee (−16% comissão), site (margem cheia, ticket maior) |
| Ticket médio | Pedidos / faturamento | Comparar com a meta (R$ 71,63 → R$ 200,00) |

Use o que tiver. Se vierem os três canais, reporte consolidado e por canal. Se vier só um, reporte e anote a lacuna. **Sem conector** → relatório/CSV/print.

## "Pipeline" = perguntas e leads (ML / Shopee / WhatsApp)

> Não há CRM na Casa Roque. O equivalente a "pipeline" é o **fluxo de pré-venda**: perguntas nos marketplaces, mensagens de WhatsApp e contatos do site.

| Métrica | Fonte | Notas |
|---|---|---|
| Perguntas em aberto (ML/Shopee) | Print / informe da Keila (POP 4) | Quantas perguntas de pré-venda esperando resposta |
| Mensagens WhatsApp | Informe do JhEY/Keila | Cliente aguardando (JhEY atende 13–17h, temporário) |
| Contatos do site | Formulário/NuvemShop / Google Sheets | Base simples de contatos quando houver |
| Tempo de resposta | POP 4 | Meta < 2h; sinalizar o que passou |

Sem conector — depende de print/informe. Se não houver dado, marque "n/d" e siga.

## Compromissos (Google Agenda) — conector ativo

| Métrica | Ferramenta | Notas |
|---|---|---|
| Itens-chave da semana | `list_events` | Semana atual; reunião com Thomas (seg 9h), batimento (sex 15h, POP 3), relatório de tráfego (sex) |
| Próximos 7 dias | `list_events` | Visão pra frente; destacar prazos (envio de NFs ao contador dia 5; DAS dia 20) |

## Watch-list (Gmail + SAC marketplace + estoque)

| Métrica | Fonte | Notas |
|---|---|---|
| Threads urgentes (Gmail) | `search_threads` | Query: `is:important OR is:starred` nos últimos 7 dias — **conector ativo** |
| Reclamações/cancelamentos (Gmail) | `search_threads` | Termos: "reclamação", "cancelar", "reembolso", "urgente", "Reclame Aqui", "devolução" nos últimos 7 dias |
| SAC marketplace | Print / informe da Keila (POP 4) | Perguntas/mensagens ML/Shopee/WhatsApp sem resposta > 2h |
| Estoque baixo | Informe do Emerson (POP 2) | Itens com < 5 unidades — nomear produto e quantidade |

**Fallback de Gmail:** se a chamada falhar (auth instável — problema conhecido), pule a watch-list de e-mail em silêncio e adicione "Gmail indisponível" ao apêndice. Não jogue o erro no corpo do pulso.

## Mídia (Google Ads — via Thomas)

| Métrica | Fonte | Notas |
|---|---|---|
| ROI / CPC | Relatório do Thomas (sexta) | Metas: ROI > 3x, CPC < R$ 2,00. Conta 568-607-6835 (PMax R$ 35/dia). Sem conector — só se o Thomas tiver mandado o relatório |

Inclua só se houver dado. Omita a seção se não veio nada.

## Varredura de riscos

Rode junto com as métricas — não espere as métricas terminarem.

| Risco | Fonte | Condição-gatilho |
|---|---|---|
| SAC atrasado | ML/Shopee/WhatsApp | Perguntas sem resposta > 2h (POP 4) |
| Estoque baixo | Emerson (POP 2) | Item com < 5 unidades |
| Conta a pagar à vista | Bling | Vencimento próximo sem caixa coberto (folha, DAS, fornecedor) |
| Queda de vendas | Relatório de venda | 7d vs 7d abaixo do threshold |
| Gmail urgente | Gmail | `is:important` ou termos de reclamação/cancelamento |
| Mídia fora da meta | Thomas | CPC > R$ 2,00 ou ROI < 3x |

## Paralelização

Tudo que for conector (Gmail, Google Agenda) dispara num único lote. As fontes sem conector (Bling, ML, Shopee, NuvemShop, SAC, estoque) dependem de anexo/informe — se não vierem, a seção entra como "n/d" e a fonte aparece em "Fontes indisponíveis" no fim do pulso. Se uma falhar, as outras seguem normal.
