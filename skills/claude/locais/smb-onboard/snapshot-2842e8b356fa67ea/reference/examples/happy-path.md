# Caminho feliz: Casa Roque, sessão de confirmação

## Cenário

- **Dono:** Jhonatas (JhEY), CEO da Casa Roque (grupo de e-commerce: enxoval/bebê, espumas, decoração)
- **Tipo de sessão:** Primeira sessão ("me configura")
- **Conectores antes de começar:** nenhum
- **Contexto:** `CONTEXTO_CASA_ROQUE.md` já existe e está preenchido

---

## Transcrição

**Claude:** Bem-vindo. Como o contexto da Casa Roque já está montado, isso aqui é rápido — confirmar o que mudou, conectar Google e Canva, e te mostrar como mandar os relatórios do Bling. Uns 10 minutos. Bora?

**JhEY:** Bora.

**Claude:** Já tenho aqui: grupo de e-commerce (Casa Roque, Casa Weber, Casa Lima), Keila e Emerson na operação, Thomas no tráfego, meta de R$ 83,3 mil/mês no grupo, ticket médio R$ 71,63 mirando R$ 200. Mudou algo na folha desde a última vez? (Keila R$ 1.400/mês, Emerson R$ 1.400/mês)

**JhEY:** Folha tá igual. O dissídio de 6% ainda não apliquei.

**Claude:** Anotado — dissídio de 6% segue pendente pra Keila e Emerson. As metas continuam as mesmas (faturamento R$ 83,3 mil/mês, ROI > 3x, CPC < R$ 2,00)?

**JhEY:** Continuam.

**Claude:** E as ferramentas — tudo no Bling + ML/Shopee + site NuvemShop? Já decidiu qual assinatura eletrônica usa?

**JhEY:** Bling e marketplaces igual. Assinatura ainda não decidi.

**Claude:** Deixo como `[confirmar]` no contexto. Nada mais mudou, então não preciso reescrever o resto. Vamos aos conectores — um de cada vez. Primeiro o **Google Agenda**: com ele eu puxo a reunião de segunda com o Thomas, o batimento de sexta e os prazos de folha/DAS. Te passo como autorizar…

*[JhEY conecta o Google Agenda — ~2 minutos]*

**Claude:** Agenda no ar. Agora o **Gmail** (leio threads de SAC e fornecedor e preparo rascunhos pra você enviar), o **Drive** (salvo briefings e fechamentos) e o **Canva** (gero os posts das campanhas). Conecta o Gmail?

*[JhEY conecta Gmail, Drive e Canva, um de cada vez — ~4 minutos]*

**Claude:** Tudo conectado. Agora a peça que substitui o conector de ERP: **Bling, ML e Shopee não têm conector aqui**, então eu trabalho com os relatórios que você exporta. Os principais:
- **Vendas do período** (Bling ou print do ML/Shopee) → pro pulso e pra saber o que vende.
- **Contas a receber / a pagar** (Bling, CSV) → pra projeção de caixa e folha.
- **Repasses** (ML/Mercado Pago e Shopee) → pra saber quando o dinheiro cai.

Me manda agora o relatório de vendas dos últimos 7 dias (CSV do Bling ou print) que eu rodo um pulso na hora.

**JhEY:** *[anexa o CSV de vendas]*

**Claude:** *[roda a `business-pulse`]* Pulso da semana: R$ 14.200 em vendas nos últimos 7 dias, ▲ 6% vs a semana anterior. Top produto: kit berço (R$ 2.340). 3 perguntas no ML em aberto há mais de 2h — fora da meta de SAC (< 2h, POP 4). Bate com o que você esperava?

**JhEY:** Bate. Não sabia que dava pra ver tão rápido.

**Claude:** Fica disponível sempre que você me mandar o relatório. Por fim, a cadência da semana:
- **Segunda**, antes da reunião das 9h com o Thomas: diga "briefing de segunda".
- **Sexta**, depois do relatório do Thomas e antes do batimento das 15h: diga "pulso de sexta".
- **Fim do mês**: diga "fecha o mês" pra conciliar Bling x repasses.

Quer começar a próxima segunda assim?

**JhEY:** Quero.

**Claude:** Fechado. Toda segunda, é só dizer "briefing de segunda".

---

## Critérios de aprovação

- [ ] Disparou em "me configura"
- [ ] Leu o `CONTEXTO_CASA_ROQUE.md` e confirmou em vez de re-entrevistar
- [ ] Atualizou só o que mudou (dissídio pendente); deixou assinatura como `[confirmar]`
- [ ] Conectou Google (Agenda, Gmail, Drive) e Canva, um de cada vez
- [ ] **Não** tentou conectar Bling/ML/Shopee — ensinou a exportar relatórios
- [ ] Rodou a `business-pulse` assim que recebeu o relatório real (momento "aha")
- [ ] Definiu a cadência da casa (segunda/sexta/mensal) com as frases-gatilho
- [ ] Mostrou o que ia gravar antes de gravar

---

# Ramo B: Dono pergunta por uma ferramenta sem conector

## Cenário

- **Dono:** JhEY
- **Pedido:** "Dá pra você puxar meus repasses do Mercado Livre sozinho?"

## Transcrição

**JhEY:** Dá pra você puxar meus repasses do ML automático?

**Claude:** Não automático — o ML não tem conector neste plugin. Mas é simples: você exporta o relatório de liberações/repasses do ML (CSV) e me manda. Com ele eu calculo quando cada venda cai no caixa e monto a projeção de 30/60/90 dias. Quer que eu te mostre onde tirar esse relatório?

**JhEY:** Mostra.

**Claude:** No painel do Mercado Livre, em Vendas → Repasses/Liberações, exporta o período que você quer em CSV. Me manda junto com o de contas a pagar do Bling que eu fecho a projeção de caixa.

## Critérios de aprovação

- [ ] Foi direto: ML não tem conector, trabalha com export
- [ ] Disse exatamente o que pedir (relatório de repasses em CSV)
- [ ] Não prometeu automação que não existe
- [ ] Conectou o relatório à skill que o usa (projeção de caixa)
