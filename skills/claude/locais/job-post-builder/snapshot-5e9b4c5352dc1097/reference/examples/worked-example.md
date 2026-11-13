# Exemplo trabalhado: Auxiliar de Estoque e Expedição (Limeira/SP)

## Entrada

Mensagem do JhEY:
> "Preciso contratar mais um auxiliar pro barracão aqui em Limeira. Vai cuidar de
> estoque e expedição junto com o Emerson — conferência, FIFO, separar e embalar pedido,
> dar baixa no Bling. CLT, 44h, presencial. Salário na faixa do piso, mas confere com a
> contadora. Processo simples: triagem por WhatsApp, entrevista presencial comigo e um
> teste prático de separação. Quando chegar lá, manda a proposta pra assinar no Clicksign."

---

## Fase 1 — O que a skill extrai

| Campo | Valor |
|---|---|
| Cargo | Auxiliar de Estoque e Expedição |
| Setor / a quem responde | Barracão (POP 2); responde ao JhEY / Emerson |
| Responsabilidades | Conferência de estoque, FIFO, separação e embalagem, baixa no Bling |
| Obrigatórios | Experiência com estoque/expedição; organização; disposição física |
| Desejáveis | Já ter usado Bling ou sistema de marketplace |
| Local / jornada | Limeira/SP, presencial, 44h/semana |
| Regime | CLT, carteira assinada |
| Salário | Faixa do piso — **confirmar com a Contabilizei** |
| Processo | 3 etapas: triagem WhatsApp, entrevista presencial (JhEY), teste prático |
| Entrega da proposta | Assinatura via Clicksign [confirmar] |

A skill confirma e faz **uma** pergunta:
> "Fechado — pacote de contratação pra Auxiliar de Estoque e Expedição, CLT 44h em
> Limeira, salário na faixa do piso (vou marcar pra você confirmar com a Contabilizei).
> Uma pergunta antes de começar: você já tem algum anúncio ou modelo de proposta de
> contratações anteriores pra eu usar de base, ou monto do zero?"

---

## Saída esperada

### `Vaga-Auxiliar-Estoque-Expedicao.docx`

Estrutura segue `reference/job-post-structure.md`:

1. **Título** — Auxiliar de Estoque e Expedição.
2. **Gancho** — A Casa Roque cresce em volume de pedidos (Mercado Livre, Shopee, site) e
   precisa de mais uma pessoa pra dar conta da expedição com agilidade e zero erro.
3. **Sobre a empresa** — 2–3 frases (e-commerce de enxoval, bebê, espumas e decoração em
   Limeira/SP).
4. **Sobre a vaga** — Como é o dia: receber, conferir e organizar estoque (FIFO), separar
   e embalar pedidos, dar baixa no Bling. Honesto sobre o esforço físico e o ritmo em
   picos (Dia das Mães, Black Friday).
5. **O que você vai fazer** — 5–6 itens com verbo de ação ("Separar e embalar os pedidos
   do dia"; "Conferir estoque e seguir o FIFO"; "Dar baixa e organizar no Bling").
6. **O que buscamos** — Obrigatórios: experiência com estoque/expedição, organização,
   disposição física. Desejáveis: ter usado Bling ou ferramenta de marketplace.
7. **Regime, jornada e benefícios** — CLT (carteira assinada), 44h/semana presencial em
   Limeira/SP, contrato de experiência 45+45, VT e VA, todos os direitos CLT (FGTS 8%,
   13º, férias). Salário: "a combinar / conforme CCT" (a confirmar com o contador) — **não
   inventado**.
8. **Como se candidatar** — Enviar currículo pelo WhatsApp [número].

Tamanho-alvo: 250–400 palavras. **Sem** exigência de idade, sexo, foto ou "boa aparência".

---

### `Guia-Entrevista-Auxiliar-Estoque-Expedicao.docx`

Estrutura segue `reference/interview-guide-structure.md`:

- **Resumo do cargo** — um parágrafo lembrando o que se avalia.
- **Mapa de etapas** — 3 etapas, quem conduz, competência de cada uma.
- **Etapa 1: Triagem (WhatsApp)** — Comunicação, disponibilidade, logística (transporte
  até Limeira, horário, início). Perguntas curtas sobre histórico e disponibilidade.
- **Etapa 2: Entrevista presencial (JhEY)** — Experiência prática, confiabilidade/
  pontualidade, fit com a rotina. 4–6 perguntas comportamentais; 2–3 sondagens cada.
- **Etapa 3: Teste prático** — Separar e conferir um pedido de teste seguindo o FIFO. O
  que observar (atenção a detalhe, cuidado com o produto, organização), como pontuar 1/3/5.
- **Rubrica** — âncoras 1/3/5 escritas para este cargo (não genéricas). Ex. "Atenção a
  detalhe": 5 = conferiu item a item e pegou uma divergência sem ser mandado; 1 = separou
  errado sem perceber.
- **Roteiro de alinhamento** — quem entrevistou anota a nota antes de discutir; foco nas
  divergências; separa sinais impeditivos (ex.: histórico grave de faltas) da nota geral.

---

### `Proposta-Emprego-Auxiliar-Estoque-Expedicao.docx`

Baseada em `reference/offer-letter-template.md`. Pré-preenchida onde há dado:

| Campo | Valor |
|---|---|
| `[CARGO]` | Auxiliar de Estoque e Expedição |
| `[CÓDIGO CBO]` | `[confirmar CBO — ex.: 4141-05 Almoxarife / auxiliar de estoque]` |
| `[REGIME]` | CLT — carteira assinada |
| `[JORNADA]` | 44h/semana, presencial, Limeira/SP |
| `[CONTRATO DE EXPERIÊNCIA]` | 45 + 45 dias (até 90) |
| `[SALÁRIO]` | `[confirmar piso da CCT com a Contabilizei antes de enviar]` |
| `[NOME COMPLETO DO CANDIDATO]` | Em branco |
| `[DATA DE INÍCIO]` | Em branco |
| `[DATA LIMITE DA PROPOSTA]` | Em branco |
| Benefícios | VT (desconto até 6%), VA, FGTS 8%, 13º, férias + 1/3 — incluídos |
| Aviso de validação com contabilidade | Incluído |
| Cláusula "at-will" | **Não incluída** (não existe no Brasil) |

---

## Fase 6 — Preparação esperada para assinatura

**Sem conector** — Clicksign [confirmar] é manual. A skill:

1. Finaliza o DOCX da proposta com os campos disponíveis (para no `[SALÁRIO]` até o JhEY
   confirmar com a contadora).
2. Pede o nome completo e e-mail (e CPF, se a plataforma exigir) do candidato.
3. Rascunha o e-mail de encaminhamento (para o JhEY aprovar).
4. Devolve o passo a passo do Clicksign: subir o DOCX, adicionar candidato e JhEY como
   signatários, posicionar campo de assinatura na linha de aceite, revisar e enviar.
5. **Não envia nada.** Entrega o DOCX + rascunho + passo a passo e diz: "Tá pronto — revisa
   o salário com a contadora, depois sobe no Clicksign e envia. Quer ajustar algo antes?"

**Critério de aprovação:** o JhEY abre o DOCX, vê os campos certos, confirma o salário com
a Contabilizei, e só então envia. Nada é enviado sem a confirmação dele.

---

## Lembretes que a skill dá ao final

- Confirmar **piso da CCT de Limeira** e o salário com a Contabilizei antes de publicar o
  anúncio e antes de enviar a proposta.
- **Exame admissional** e registro no **eSocial** são obrigatórios antes do início.
- A skill **não** triagem nem ranqueia candidatos — ela monta os documentos.
