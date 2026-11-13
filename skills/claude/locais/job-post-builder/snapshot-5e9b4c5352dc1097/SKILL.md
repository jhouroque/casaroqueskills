---
name: job-post-builder
description: >
  Monta pacotes completos de contratação CLT para a Casa Roque — anúncio de vaga +
  guia de entrevista com rubrica de pontuação + carta-proposta de emprego — a partir
  de um briefing curto. Dispara em: "preciso contratar", "tô contratando pra",
  "escreve um anúncio de vaga", "descrição de cargo", "vaga aberta", "anúncio de
  emprego", "perguntas de entrevista", "rubrica de pontuação", "monta uma proposta de
  emprego", "manda a proposta", "faz um pacote de contratação", ou qualquer pedido de
  recrutamento. Na dúvida, dispare — cobre o fluxo de contratação do anúncio até a
  carta-proposta para assinatura via Gov.br/Clicksign. NÃO triagem nem ranqueia
  candidatos.
---

# Montador de pacote de contratação (Casa Roque)

> **Status:** rascunho MVP · **Dono:** JhEY · **Versão:** 1.1.0
> **Categoria:** RH & Contratação (CLT)

Produz um pacote de contratação completo — anúncio de vaga, guia de entrevista e
carta-proposta de emprego — a partir de uma conversa curta sobre o cargo. A contratação
da Casa Roque é **CLT, carteira assinada**, regida pela legislação trabalhista
brasileira.

> ⚠️ **Antes de fechar qualquer contratação ou definir salário, validar com a
> Contabilizei (contador):** piso da CCT aplicável em Limeira/SP, eSocial, exames
> admissionais e enquadramento. Esta skill produz rascunhos — quem confirma valores e
> formaliza é o contador/advogado.

---

## Início rápido

Dispare quando o JhEY disser que precisa contratar alguém ou produzir qualquer documento
de contratação. A skill segue 6 fases: levantar contexto → pesquisar o mercado →
escrever o anúncio → montar o guia de entrevista → montar a carta-proposta → (se pedido)
preparar para assinatura via Gov.br/Clicksign.

**Exemplo de gatilho:**
> "Vou contratar mais um auxiliar pro barracão aqui em Limeira. Monta o anúncio e as
> perguntas de entrevista pra mim."

---

## Fluxo

1. **Levantar contexto do cargo** — Pergunte cargo, responsabilidades, requisitos,
   local, jornada (28h/44h), faixa salarial, processo de entrevista e como prefere
   entregar a carta-proposta (DOCX ou assinatura via Gov.br/Clicksign). Fonte: conversa /
   AskUserQuestion.
2. **Pesquisar vagas comparáveis** — Busque no Google Drive/Desktop anúncios e modelos já
   usados pela Casa Roque; faça busca web de 3–5 vagas reais do mesmo cargo na região
   (interior de SP). Fontes: conector de arquivos, busca web.
3. **Escrever o anúncio de vaga** — Rascunhe um anúncio informado pelo mercado usando
   `reference/job-post-structure.md`. Saída: `Vaga-[Cargo].docx` via skill `docx`.
4. **Montar guia de entrevista + rubrica** — Monte um guia por etapas usando
   `reference/interview-guide-structure.md`. Saída: `Guia-Entrevista-[Cargo].docx` via
   skill `docx`.
5. **Montar a carta-proposta de emprego** — Monte a carta com campos `[ENTRE COLCHETES]`
   usando `reference/offer-letter-template.md`. Saída: `Proposta-Emprego-[Cargo].docx`
   via skill `docx`.
6. **Preparar assinatura (se pedido)** — Prepare a carta-proposta para assinatura via
   **Gov.br/Clicksign/D4Sign/ZapSign** [confirmar qual o JhEY usa]. **Sem conector** — é
   anexo/manual. Exige aprovação explícita do JhEY antes de qualquer envio.

---

## Approval gates

Esta skill toca em ações externas na Fase 6. Valem as regras:

- **Nunca envie a proposta sem aprovação.** Gere o DOCX e o texto do e-mail; o JhEY revisa
  e confirma antes de qualquer envio para o candidato.
- **Nunca envie o e-mail de fallback sem aprovação.** Rascunhe no Gmail e mostre ao JhEY
  antes de enviar.
- **Nunca publique o anúncio.** Produza só o DOCX. Publicar em qualquer site de vagas
  (Catho, Indeed, grupos de WhatsApp/Facebook locais) é responsabilidade do JhEY.
- **Sempre avise:** validar piso da CCT, eSocial e exames com a Contabilizei antes de
  contratar/assinar.

A Fase 6 não avança além de "preparar para assinatura" sem o JhEY confirmar
explicitamente que revisou e quer enviar.

---

## Fase 1 — Entender o cargo

Antes de pesquisar ou escrever qualquer coisa, levante contexto suficiente. Pergunte ao
JhEY (conversa ou AskUserQuestion):

- **Cargo** — título exato (de preferência alinhado à CBO; ver `reference/gotchas.md`)
- **Setor / a quem responde** — escritório (POPs 1,3,4, perfil da Keila) ou barracão
  (POP 2, estoque/expedição, perfil do Emerson); a quem se reporta
- **Responsabilidades-chave** — 3–5 coisas que a pessoa vai tocar no dia a dia
- **Requisitos obrigatórios** — exigências reais (experiência, ensino, CNH se precisar)
- **Requisitos desejáveis** — preferíveis, não impeditivos
- **Local / jornada** — presencial em Limeira/SP; jornada (28h/semana como a Keila, ou
  44h padrão); turno
- **Regime e benefícios** — CLT (carteira assinada); contrato de experiência (45+45, até
  90 dias); VT (desconto até 6% do salário), VA; FGTS 8%; 13º; férias + 1/3
- **Faixa salarial** — piso da CCT do comércio (geral **R$ 2.006,57** / ingresso
  **R$ 1.817,25**, base FECOMERCIO/Sindilojas-SP) — **confirmar o sindicato/CCT aplicável
  em Limeira com a Contabilizei**; salário mínimo nacional é **R$ 1.621,00**. Marque que
  o valor precisa de validação do contador antes de fechar.
- **Já tem anúncio/modelo?** — pergunte se existe versão anterior no Google Drive/Desktop
- **Entrega da carta-proposta** — pergunte como prefere:
  - *Assinatura via Gov.br/Clicksign* — a skill prepara a carta e instrui o passo a passo
    de envio (sem conector — manual); o JhEY revisa antes de enviar
  - *Só o DOCX* — a skill salva a carta-proposta em DOCX e para; o JhEY cuida do envio

- **Processo de entrevista** — pergunte como o processo é estruturado:
  - Quantas etapas?
  - Quem conduz cada etapa? (ex.: JhEY, Thomas, responsável da área)
  - O que cada etapa avalia? (ex.: fit, experiência prática, atenção a detalhe)
  - Tem teste prático/prova de trabalho em alguma etapa? (ex.: bater estoque de teste,
    emitir uma NF de teste no Bling)

  Isto é crítico — o guia de entrevista será organizado por etapa, e cada etapa tem seu
  conjunto de perguntas. Se o JhEY ainda não souber, sugira um padrão simples pra PME e
  confirme antes de prosseguir.

  Padrão sugerido para cargo operacional/auxiliar em PME:
  | Etapa | Quem conduz | Foco |
  |---|---|---|
  | Triagem por telefone/WhatsApp | JhEY ou responsável | Comunicação, disponibilidade, logística (transporte, horário) |
  | Entrevista presencial | JhEY / responsável da área | Experiência prática, confiabilidade, fit com a rotina |
  | Teste prático (opcional) | Responsável da área | Atenção a detalhe na tarefa real (estoque, NF, costura) |

Capture a preferência de entrega na Fase 1 para o caminho da Fase 5/6 já ficar claro. Se
o JhEY já indicou (ex.: "manda pra assinar no Clicksign"), extraia da mensagem em vez de
perguntar de novo.

Se o JhEY já deu a maior parte na mensagem, extraia e confirme antes de seguir, em vez de
repetir perguntas. Uma pergunta objetiva é melhor que um formulário longo.

---

## Fase 2 — Pesquisar vagas comparáveis

Bons anúncios são ancorados no que o mercado de fato pede para o cargo. Faça os dois em
paralelo:

**A. Cheque os arquivos primeiro**
Busque no Google Drive e Desktop anúncios, modelos de carta-proposta ou guias de
entrevista que a Casa Roque já tenha. Use termos como o cargo, "vaga", "anúncio",
"proposta", "entrevista". Se achar, leia e use como base — preservando linguagem,
estrutura e requisitos já estabelecidos.

**B. Busca web de vagas comparáveis**
Busque vagas atuais do mesmo cargo em empresas comparáveis na região (comércio/e-commerce
no interior de SP). Boas fontes: Catho, Indeed, Vagas.com, grupos locais. Em 3–5 anúncios
reais, observe:
- Responsabilidades comuns listadas
- Requisitos recorrentes (esses são o mínimo de mercado)
- Como descrevem o impacto/escopo
- O que faz um anúncio soar atraente x genérico

Use a pesquisa para testar os requisitos do JhEY (falta algo padrão? está pedindo algo
incomum?) e para o anúncio soar atual e ancorado no mercado de Limeira.

---

## Fase 3 — Escrever o anúncio de vaga

Leia `reference/job-post-structure.md` para a estrutura completa e a orientação de escrita.

**Se um anúncio/descrição já existir (Fase 2):**
Use como template estrutural — espelhe nomes de seção, tom, ordem e qualquer boilerplate
que o JhEY já tenha (descrição da empresa, bloco de benefícios, como se candidatar). O
formato do JhEY é a fonte da verdade.

Compare com `reference/job-post-structure.md` e levante o que estiver faltando numa única
pergunta antes de escrever:

> "Seu anúncio atual tem responsabilidades e requisitos, mas não vi um gancho de abertura
> nem os benefícios CLT (VT, VA, FGTS). Quero adicionar, ou mantenho o seu formato?"

Só adicione o que faltava se o JhEY confirmar.

**Se nenhum anúncio for achado:**
Monte do zero usando `reference/job-post-structure.md` como template completo.

**De qualquer forma:**
- Comece pelo propósito/impacto, não só por tarefas
- Seja honesto sobre a rotina (turno, esforço físico no barracão, ritmo do e-commerce) —
  quem se identifica fica melhor
- Use linguagem inclusiva e **não discriminatória** (proibido exigir idade, sexo, estado
  civil, foto, "boa aparência" — ver `reference/gotchas.md`)
- Mantenha os requisitos enxutos — cada linha é um motivo de alguém não se candidatar
- Deixe explícito: **regime CLT (carteira assinada)**, jornada, local (Limeira/SP),
  benefícios (VT, VA), e contrato de experiência
- Se a faixa salarial não foi confirmada com o contador, não invente — escreva "a
  combinar / conforme CCT" e marque para confirmar

Salve como `Vaga-[Cargo].docx` pela skill `docx`. Leia `docx/SKILL.md` antes de gerar.

---

## Fase 4 — Montar guia de entrevista + rubrica

Leia `reference/interview-guide-structure.md` para o formato completo.

**Se um guia já existir (Fase 2):**
Use o guia existente como template estrutural — espelhe nomes de seção, ordem e formatação.
O formato do JhEY é a fonte da verdade; o arquivo de referência é checklist, não imposição.

Depois de mapear as seções existentes contra a referência, levante o que estiver faltando
numa pergunta curta antes de escrever:

> "Seu guia tem banco de perguntas e rubrica, mas não vi o mapa de etapas nem o roteiro de
> alinhamento pós-entrevista. Quero adicionar, ou mantenho sua estrutura?"

Só adicione se o JhEY confirmar. Não expanda o formato em silêncio.

**Se nenhum guia for achado:**
Monte do zero usando `reference/interview-guide-structure.md` como template completo.

**De qualquer forma, organize o guia por etapa, usando o processo capturado na Fase 1.**

Cada etapa é uma seção própria, com o nome da etapa e quem conduz no título, seguida de:
a competência que aquela etapa avalia, 4–6 perguntas comportamentais específicas, 2–3
sondagens de aprofundamento por pergunta, e uma rubrica 1/3/5 com âncoras para cada
competência da etapa.

**Princípios para guias de várias etapas:**
- Cada competência pertence a uma etapa — evite dois entrevistadores perguntando a mesma
  coisa. Se houver sobreposição, atribua ângulos diferentes.
- Em entrevista com mais de um avaliador, divida as perguntas explicitamente.
- Se houver teste prático, inclua uma seção de alinhamento estruturada para avaliá-lo — o
  que observar, como pontuar, perguntas de acompanhamento.
- O roteiro de alinhamento (debrief) vai no fim, depois de todas as etapas.
- As âncoras 1/3/5 devem ser escritas para este cargo, não genéricas.

Salve como `Guia-Entrevista-[Cargo].docx` pela skill `docx`.

---

## Fase 5 — Montar a carta-proposta de emprego

Leia `reference/offer-letter-template.md` para o template-base e as definições de campo.

**Se uma carta-proposta/modelo já existir (Fase 2):**
Use como template estrutural — preserve formatação, ordem de cláusulas, blocos de
assinatura e qualquer redação que o JhEY já tenha. A versão dele é a fonte da verdade.

Compare com `reference/offer-letter-template.md` e levante o que faltar numa única
pergunta antes de escrever:

> "Sua carta tem cargo e salário, mas não vi o contrato de experiência (45+45) nem o
> aviso de validação com a contabilidade. Quero adicionar, ou mantenho seu formato?"

Só adicione se o JhEY confirmar.

**Se nenhuma carta for achada:**
Monte do zero usando `reference/offer-letter-template.md` como template completo.

**De qualquer forma:**
- Use campos `[ENTRE COLCHETES]` claramente marcados para todo valor específico do
  candidato
- Inclua: cargo + **CBO**, salário, **regime CLT**, **contrato de experiência (ex.: 45 +
  45 dias)**, jornada, benefícios (VT com desconto de até 6%, VA), FGTS 8%, data de início
- **Não invente salário.** Se não foi confirmado com o contador, deixe
  `[SALÁRIO — confirmar piso da CCT com a Contabilizei]`
- Inclua o aviso de validação com contabilidade/advogado antes de assinar
- **Não** use "emprego à vontade / at-will" — isso é dos EUA. No Brasil vale a CLT
  (aviso prévio, FGTS, multa rescisória etc.)

Salve como `Proposta-Emprego-[Cargo].docx` pela skill `docx`.

**Depois, ramifique pela preferência de entrega capturada na Fase 1:**
- Se escolheu **assinatura via Gov.br/Clicksign** → siga para a Fase 6
- Se escolheu **só o DOCX** → pule a Fase 6, entregue o DOCX e encerre

---

## Fase 6 — Preparar a carta-proposta para assinatura (Gov.br/Clicksign)

**Não há conector de assinatura eletrônica** — o envio é manual pela plataforma que o
JhEY usar (Gov.br/Clicksign/D4Sign/ZapSign) [confirmar]. A skill prepara o documento e o
passo a passo; o JhEY executa o envio.

**Passo a passo:**

1. **Finalize o DOCX da carta-proposta** com os campos preenchidos (cargo, CBO, salário
   confirmado, jornada, benefícios, data de início, contrato de experiência). Se faltar
   salário confirmado, **pare** e peça ao JhEY antes de preparar para assinatura.

2. **Confirme os dados do candidato** — nome completo e e-mail (e CPF, se a plataforma
   pedir). Não prepare o envio sem nome e e-mail.

3. **Monte o e-mail/mensagem de encaminhamento** (rascunho, para o JhEY aprovar):
   > "Olá [Nome], é uma alegria te apresentar esta proposta de emprego para a vaga de
   > [Cargo] na Casa Roque. Segue para sua leitura e assinatura. Qualquer dúvida, estou à
   > disposição. — Jhonatas"

4. **Oriente o passo a passo da plataforma** (texto para o JhEY seguir):
   - Entrar no Gov.br/Clicksign/D4Sign/ZapSign
   - Subir o arquivo `Proposta-Emprego-[Cargo].docx` (ou PDF)
   - Adicionar o candidato como signatário (nome + e-mail)
   - Adicionar o JhEY como signatário/cópia
   - Posicionar o campo de assinatura e data na linha de aceite, no fim da carta
   - **Revisar e enviar** — só o JhEY clica em enviar

5. **Não envie nada automaticamente.** Devolva ao JhEY o DOCX pronto + o rascunho do
   e-mail + o passo a passo, e diga:
   > "A carta-proposta está pronta pra assinatura. Revisa o documento e o e-mail; quando
   > aprovar, sobe no Gov.br/Clicksign e envia pro candidato. Quer que eu ajuste algo
   > antes?"

**Fallback (Gmail):** Se preferir, rascunhe no Gmail um e-mail para o candidato com o
DOCX anexado e uma nota para subir na plataforma de assinatura. **Mostre o rascunho ao
JhEY antes de qualquer envio.**

---

## Entregando o pacote

Com os três arquivos prontos, apresente juntos:

Um resumo listando os três entregáveis pelo cargo: o anúncio de vaga (pronto pra
publicar), o guia de entrevista (compartilhar com quem entrevista) e a carta-proposta
(preparada para assinatura via Gov.br/Clicksign ou pronta pra envio manual).

Lembre o JhEY:
- A carta-proposta e o salário precisam de **validação da Contabilizei** (piso da CCT de
  Limeira, eSocial, exames admissionais) antes do uso
- A faixa salarial deve ser confirmada com o contador antes de publicar o anúncio
- Exames **admissional** e registro no **eSocial** são obrigatórios antes do início
- Esta skill **não** triagem nem ranqueia candidatos

---

## Conectores

**Conectores ativos:** Gmail (rascunho/anexo), Google Drive (achar modelos), Canva (se
quiser arte do anúncio). **Sem conector de assinatura eletrônica** — Gov.br/Clicksign/
D4Sign/ZapSign [confirmar] entram via anexo/manual.

---

## Arquivos de referência

Carregue ao chegar na fase — não carregue tudo de uma vez:

| Arquivo | Carregar quando |
|---|---|
| `reference/job-post-structure.md` | Fase 3 — antes de escrever o anúncio |
| `reference/interview-guide-structure.md` | Fase 4 — antes de escrever o guia |
| `reference/offer-letter-template.md` | Fase 5 — antes de escrever a carta-proposta |
| `reference/gotchas.md` | Qualquer fase — pegadinhas BR (CCT, eSocial, não discriminação) |
| `reference/examples/worked-example.md` | Para referência do formato esperado de saída |
