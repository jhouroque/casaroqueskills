<!-- C:\Users\Jhonatas\AppData\Roaming\Claude\local-agent-mode-sessions\c5e8a475-a351-48d2-8db3-3f0857ad643d\1d524d29-2570-4e4b-8d1f-844a61e14635\local_f6e23d68-ce2b-4eec-b343-aeec8fb24add\outputs\cr-plugin\small-business\skills\canva-creator\SKILL.md -->
---
name: canva-creator
description: >
  Pega um plano de conteúdo aprovado e executa a campanha ponta a ponta para a
  Casa Roque: monta o calendário de postagem, gera as artes no Canva (conta Pro
  casaroque.design) para os posts de social, escreve legendas e o texto de
  e-mail, e prepara a publicação — agendando no Content Planner do Canva,
  publicando no Instagram/Facebook (@casaroque.design), gerando banner pro site
  NuvemShop e deixando rascunho de e-mail no Gmail. Não há HubSpot/CRM. O Canva
  é usado para artes de social e banners; o e-mail é texto puro, surgido inline
  pro JhEY enviar pelo Gmail. Cada passo precisa de aprovação. Use quando o JhEY
  disser "faz o conteúdo", "gera os posts", "cria as artes", "transforma isso
  numa campanha" ou entregar um plano aprovado pra executar.
compatibility: "Canva Pro (casaroque.design, Content Planner ativo) é central aqui. Sem HubSpot/CRM — publicação via Content Planner do Canva, Instagram/Facebook, banner NuvemShop e rascunho no Gmail. Conectores ativos: Canva, Gmail, Google Agenda, Google Drive. Sem conector de NuvemShop — o banner é exportado e subido manualmente pelo JhEY."
---

# Canva Creator (canva-creator)

## Escopo

Esta skill executa uma campanha em cinco etapas sequenciais, cada uma com aprovação do JhEY:

```
plano → calendário → inventário de assets → artes no Canva → texto → publicação/agendamento
```

| Trilha | Canais | O que a skill produz |
|--------|--------|----------------------|
| Canva (social) | Instagram, Facebook | Arte no Canva + legenda + agendamento no Content Planner do Canva (ou publicação Instagram/Facebook) |
| Canva (banner) | Site NuvemShop | Banner exportado (PNG) pro JhEY subir no admin da NuvemShop |
| Texto puro | E-mail | Assunto + linha de prévia + corpo, surgido inline pro JhEY enviar pelo Gmail |

**O Canva não é usado para gerar o corpo do e-mail** — sem template, sem autofill de e-mail, sem cópia de design, sem export de e-mail. O e-mail é texto puro porque o autofill de template de e-mail gera imagens-placeholder quando há mais espaços de imagem que fotos, e as miniaturas de variação não renderizam na prévia do chat. Se o JhEY pedir uma arte de e-mail no Canva, veja `reference/gotchas.md` para a resposta de redirecionamento.

> **Importante:** não há Instagram/Facebook como conector dedicado e não há conector de NuvemShop. A publicação acontece de duas formas: (1) **agendar no Content Planner do Canva** (a forma preferida pra Instagram/Facebook, porque o Canva Pro casaroque.design já tem o Content Planner ligado), ou (2) entregar a arte/legenda e o **banner exportado** pro JhEY publicar/subir manualmente. Sempre rascunho/prévia primeiro — nada vai ao ar sem o "ok" do JhEY.

---

## Pré-voo

Antes da Etapa 1, confirme:

1. **Plano.** O JhEY referenciou ou colou um plano aprovado. Se não:
   "Preciso do plano de conteúdo antes de montar a campanha. Você tem um da skill `content-strategy`, ou quer que eu monte um agora?"

2. **Plano de Canva.** A Casa Roque usa **Canva Pro** (conta casaroque.design). No Pro, a seleção de template é manual, a partir da biblioteca da conta (não há autofill de brand template — isso é só Enterprise). Trabalhe na trilha Pro/Teams (ver `reference/canva-api.md`).

3. **Publicação.** Como não há HubSpot, defina o destino de cada linha (ver `reference/hubspot-staging.md`):
   - Instagram/Facebook → **Content Planner do Canva** (agendar) ou entregar pro JhEY publicar.
   - Site → **banner NuvemShop** (exportar PNG; o JhEY sobe no admin).
   - E-mail → **rascunho no Gmail** (texto puro).

4. **Assets de marca.** Confirme o caminho das fotos de produto (no disco ou no Drive) ou que o brand kit da Casa Roque está no Canva. Identidade: @casaroque.design (cores/fontes da marca no Canva Pro).

5. **Orçamento de geração.** Estime o volume de artes do Canva e mostre antes da Etapa 1. Padrão: 3 candidatas por linha que vai pro Canva; cada arte custa ~5 chamadas de API (autofill/cópia + export + polling).

   ```
   Orçamento de geração desta campanha:
     Linhas Canva (social + banner): 8
     Candidatas por linha:           3   (padrão — diga "1 candidata" pra usar 1)
     Total de artes:                 24
     Chamadas de API (aprox.):       ~120  (geração + export + polling)

   Limite do Canva: 100 requisições/minuto. Vai levar ~2-3 minutos de
   geração, dentro do limite do seu plano. Pode seguir?
   ```

   Se o total de artes passar de 30, recomende modo 1 candidata por linha logo de cara — campanha grande estoura o limite rápido. O JhEY pode trocar o padrão para 1, 2 ou 3 antes da Etapa 1. Fixe o valor escolhido pela sessão toda.

---

## Fluxo de trabalho

### Etapa 1 — Calendário de postagem

Puxe do plano: temas de conteúdo, canais, frequência, datas fixas (lançamentos, ofertas, datas sazonais — Dia das Mães, Black Friday, Natal, Dia das Crianças, volta às aulas).

Monte uma tabela de calendário com uma coluna `Trilha` que roteia cada linha pra Canva (social), Canva (banner) ou texto puro:

| Data | Canal | Trilha | Tema | Tipo de arte | Ângulo da legenda/assunto |
|------|-------|--------|------|--------------|---------------------------|
| 02/05 | Instagram feed | Canva (social) | Dia das Mães — trocadores | Post quadrado | "O trocador que toda mãe queria" |
| 05/05 | Site NuvemShop | Canva (banner) | Dia das Mães — kits | Banner home | "Kit enxoval com 3x sem juros" |
| 06/05 | E-mail | Texto puro | Dia das Mães — kits | Corpo de e-mail | "Presente de Dia das Mães que dura" |

Marque toda linha de e-mail como `Texto puro` antes de apresentar. Limite a 30 dias salvo se o plano disser outra coisa. Sinalize conflitos de agenda (dois posts do mesmo produto no mesmo dia) logo de cara.

**Checkpoint 1.** Apresente o calendário. Pergunte: "Bate com o plano? Alguma data pra mexer, canal pra incluir ou tema pra trocar?" Itere até aprovar e então repita a divisão em voz alta — "N linhas vão pro Canva, M linhas vão pra texto puro" — antes de seguir. Pegar um erro de roteamento aqui é de graça; pegar depois de gerar as artes, não.

---

### Etapa 2 — Inventário de assets (só linhas Canva)

Linhas de e-mail pulam esta etapa inteira. Para cada linha `Canva (social)` ou `Canva (banner)`, monte um inventário do que o template precisa e do que já existe.

1. **Liste cada espaço de imagem pelo nome.** Post quadrado do Instagram costuma ter 1–2 espaços; carrossel e banner de site podem ter 3+. Liste um a um (`Imagem_Header`, `Imagem_Produto1`, `Imagem_Produto2`, …) — nunca resuma como "imagens de produto".
   - Pro/Teams (caso da Casa Roque): conte cada retângulo de imagem distinto do template.

2. **Inventarie os assets disponíveis.** Texto do plano (nomes de produto, oferta, chamadas, preços), fotos de produto já no Canva (`GET /v1/assets`) ou no disco/Drive, cores e fontes da marca (@casaroque.design).

3. **Monte a tabela de lacunas, espaço por espaço.** Uma linha por espaço por arte — não por arte.

   | Data | Nome do espaço | Tipo | Asset disponível | Status |
   |------|----------------|------|------------------|--------|
   | 02/05 | Imagem_Hero | imagem | trocador_americano.jpg → asset_id pendente | subir |
   | 02/05 | Titulo | texto | "O trocador que toda mãe queria" | pronto |
   | 09/05 | Imagem_Produto1 | imagem | — | **FALTANDO** |

4. **Resolva as lacunas com o JhEY.** Se o template tem mais espaços de imagem que o plano deu fotos, pare e pergunte:

   ```
   O template "Carrossel Dia das Mães" tem 5 espaços de imagem. O plano me deu
   1 foto (trocador_americano.jpg). Como preencho os outros 4?

     1. Repetir a mesma foto nos 5 espaços
     2. Você me manda 4 fotos (caminho dos arquivos / link do Drive)
     3. Escolher um template mais simples, com menos espaços
   ```

   Nenhuma chamada de geração até o JhEY escolher. Gerar com espaço vazio produz arte cheia dos placeholders padrão do Canva (paisagem genérica).

5. **Suba as fotos faltantes e capture o asset ID verificado.** Suba via `POST /v1/asset-uploads`, faça polling em `GET /v1/asset-uploads/{job_id}` até `status == "success"`. Registre `asset.id` da resposta — é o único valor que funciona num campo de imagem do autofill. Passar string vazia, URL, caminho de arquivo ou ID velho renderiza silenciosamente a paisagem padrão do Canva no lugar da foto.

6. **Confirme o inventário.** Mostre ao JhEY a tabela completa, espaço por espaço, com tudo resolvido e cada `asset.id` de imagem confirmado. Última parada antes das chamadas de API do Canva.

---

### Etapa 3 — Geração das artes no Canva

Antes de qualquer chamada de API do Canva, releia o calendário e derrube qualquer linha cuja `Trilha` não seja `Canva (social)` nem `Canva (banner)`. Linhas de e-mail não passam por esta etapa.

Gere as artes **uma linha do calendário por vez**, com 3 candidatas por linha (ou o valor escolhido no pré-voo). Cada linha segue o mesmo loop: gerar candidatas → verificar → exportar → conferir visualmente → refazer as que falharam → apresentar → esperar a escolha do JhEY → próxima linha. Pause 30 segundos entre linhas. Isso limita a rajada a 3 gerações + 3 exports por ~30s — bem abaixo do limite de 100 req/min do Canva. Não paralelize várias linhas; uma por vez é a proteção que evita estourar a cota no meio da campanha.

**Cadência de polling.** Faça polling do status do job a cada 3-5 segundos, não mais rápido. Intervalo menor queima cota sem acelerar.

**URLs de prévia — só um tipo é seguro pra embutir.** A resposta do autofill devolve miniaturas `design.canva.ai` que expiram em minutos; embutir como imagem markdown gera placeholders "Show Image" quebrados. URLs de export permanentes (`export-download.canva.com` ou a ferramenta MCP `export-design`) não expiram. O carrossel nativo do Cowork renderiza o resultado do autofill direto pela sessão autenticada do conector — deixe renderizar sozinho, não re-embuta.

#### Loop por linha

1. **Resolver o template.** (Uma vez por sessão — mesmo template entre as linhas, salvo se o calendário misturar tipos de arte.)
   - Pro/Teams: `GET /v1/designs?ownership=any&query={nome do template}`, mostre os 3 melhores ao JhEY, confirme um antes de gerar.

2. **Gerar as candidatas da linha em paralelo.** Dispare as 3 candidatas da linha juntas (ou N do pré-voo).
   - Pro/Teams: `POST /v1/designs` para criar cópias. Descreva as edições de texto e imagem que o JhEY aplica no Canva; colete os IDs de design de volta.

3. **Verificar o status do job.** Para cada candidata, confirme que `GET /autofills/{job_id}` retornou `status == "success"` e que `result.design.id` existe. Trate erros por design:
   - `JOB_FAILED` → leia `job.error.message`, corrija os valores ou os asset IDs, tente de novo uma vez.
   - `RATE_LIMIT_EXCEEDED` (1ª vez na sessão) → espere 60s, tente essa candidata de novo uma vez. Cobre picos transitórios.
   - `RATE_LIMIT_EXCEEDED` (2ª vez na sessão) **ou** qualquer erro de `quota_exceeded` / teto diário → pare a geração na hora. Não tente de novo. Mostre o progresso e pergunte:

     ```
     O Canva está limitando a campanha. Status até aqui:
       ✓ Geradas:   Posts 1-4 (12 artes)
       ⏸ Faltam:    Posts 5-8 (12 artes ainda não geradas)

     Como sigo?
       1. Trocar pra 1 candidata por linha restante (4 artes no total) — termina agora
       2. Pausar a campanha — retomar em 60 minutos quando a cota voltar
       3. Parar a geração — trabalhar com o que temos, ir pras legendas
     ```

     Espere a escolha do JhEY. Não fique em loop de retry.

4. **Exportar cada candidata aprovada pra um PNG permanente.** Dispare os exports da linha em paralelo.
   - REST: `POST /v1/exports` com `format.type: "png"`, polling em `GET /v1/exports/{job_id}` até sucesso, capture `urls[0]`.
   - MCP Canva: `export-design` com o ID do design.

   Essas URLs permanentes são o que entra nas prévias, no banner que o JhEY sobe na NuvemShop e no agendamento do Content Planner. A miniatura da resposta do autofill nunca é usada adiante.

5. **Conferir visualmente cada export.** Olhe a imagem e rejeite qualquer uma destas — todas indicam espaço não preenchido ou asset errado:
   - Paisagem genérica com nuvens e morros verdes (placeholder padrão do Canva).
   - Retângulos cinza sólidos onde deveria ter foto.
   - Texto lorem-ipsum ou texto padrão do template.
   - Assunto que não bate com o plano (produto errado, marca errada — confira a identidade @casaroque.design).

   Se uma candidata reprovar: revise o inventário do espaço afetado, corrija o `asset.id`, regenere só aquela candidata, re-exporte, reconfira.

6. **Refazer por candidata em falha parcial.** Se 1 de N candidatas da linha falhou no Passo 3 ou 5, regenere só aquela — não refaça a linha toda nem apresente carrossel parcial quebrado. Se a segunda tentativa também falhar:

   ```
   A terceira candidata do post de 09/05 segue falhando — o Canva retornou
   [erro / placeholder renderizado]. Como sigo?

     1. Pula — apresento as outras 2 e sigo
     2. Troca pra um template mais simples só nessa candidata
     3. Tenta de novo com outra foto
   ```

7. **Apresentar as candidatas da linha.** Deixe o carrossel nativo do Cowork renderizar o resultado. Abaixo, um pedido em texto:

   ```
   As candidatas de 09/05 estão prontas — passa pelo carrossel acima.
   Qual eu uso no post de 09/05?
   ```

   Se o carrossel não renderizar ou uma posição vier quebrada, embuta as URLs de export PNG permanentes do Passo 4. Último recurso: link da URL de edição do Canva (`https://www.canva.com/d/{design_id}`). Nunca re-embuta URLs `design.canva.ai`.

8. **Pause 30 segundos e vá pra próxima linha.**

**Checkpoint 2.** Satisfeito quando o JhEY escolheu uma arte por linha do calendário. Se ele quiser refazer, regenere só aquela candidata.

---

### Etapa 4 — Texto

Para cada linha do calendário, escreva o texto. Linhas de social ganham legenda; linhas de e-mail ganham o e-mail completo. Tom: objetivo, próximo, sem enrolação corporativa — a voz da @casaroque.design.

**Legendas de social** — Instagram, Facebook:

- Tamanho: adequado ao canal (Instagram ≤ 2.200 caracteres; Facebook ≤ 500 recomendado).
- Estrutura: gancho → um benefício do produto → CTA → 3-5 hashtags (não 30).
- Voz: siga os marcadores de tom do plano. Linguagem da Casa Roque é direta e calorosa — nada de "Temos o prazer de anunciar".
- Sem encheção. Abra com o valor.
- CTA real: "compra no site (link na bio)", "chama no direct", "3x sem juros no site", "frete grátis SP acima de R$ 199".

**E-mail** — o Claude escreve o e-mail inteiro; sem Canva:

- Assunto: ≤ 50 caracteres, específico, sem clickbait. "Enxoval com 3x sem juros" ganha de "Não perca!".
- Linha de prévia (preheader): ≤ 90 caracteres, complementa o assunto sem repetir.
- Corpo: prosa simples, 100-250 palavras. Primeira linha que prende → 1-2 parágrafos de substância → 1 CTA claro → assinatura.
- Voz: mesmos marcadores de tom do social.
- Sem referência a imagem. Não escreva "veja a imagem acima". Se o JhEY quiser visual, ele adiciona no Gmail.
- Um CTA por e-mail.

Apresente legendas inline abaixo de cada linha de social. Apresente o e-mail completo inline abaixo de cada linha de e-mail:

```
Assunto: <assunto>
Prévia: <linha de prévia>

<corpo>
```

Para exemplos trabalhados, veja [reference/examples/boutique-brief-campaign.md](reference/examples/boutique-brief-campaign.md).

**Checkpoint 3.** "Alguma legenda ou e-mail pra reescrever? Diz a data e o que mudar." Itere até aprovar.

---

### Etapa 5 — Publicação/agendamento (sem HubSpot) + entrega do e-mail

Sem HubSpot/CRM. A publicação acontece pelo Content Planner do Canva, Instagram/Facebook, banner NuvemShop e rascunho no Gmail. Referência de campos e fluxo em [reference/hubspot-staging.md](reference/hubspot-staging.md).

1. **Instagram/Facebook — agendar no Content Planner do Canva.** Para cada linha `Canva (social)`:
   - Use o **Content Planner** do Canva Pro (casaroque.design) pra agendar a arte + legenda na data/hora do calendário.
   - Conta de destino: @casaroque.design (Instagram) e a página do Facebook conectada.
   - Status: **agendado** (nunca publicar direto sem o "ok" final do JhEY).
   - Se o Content Planner não estiver acessível na sessão, entregue a arte (PNG export) + legenda pro JhEY publicar manualmente e diga isso explicitamente.

2. **Site — banner NuvemShop.** Para cada linha `Canva (banner)`:
   - Entregue o **PNG exportado** do banner (Etapa 3) + o texto/CTA.
   - Diga o caminho: **NuvemShop admin → Loja → Banners/Slides** (o JhEY sobe manualmente — não há conector de NuvemShop).
   - Lembre o tamanho recomendado do banner (ver `reference/gotchas.md`).

3. **E-mail — rascunho no Gmail.** Para cada linha de e-mail:
   - Deixe o texto (assunto + prévia + corpo) como **rascunho no Gmail** (ou inline pro JhEY colar). Nunca enviar sem aprovação.

4. **Confirmar a fila.** Liste o que foi agendado/preparado: data, canal, prévia da legenda (60 caracteres), status. Para o Content Planner, forneça o link do calendário do Canva.

**Checkpoint final.**

```
Resumo da campanha Dia das Mães:

Instagram/Facebook (Content Planner do Canva):
  02/05 — "O trocador que toda mãe queria" — AGENDADO
  09/05 — "3 jeitos de montar o cantinho da troca" — AGENDADO
  (você cancela ou edita qualquer post no Content Planner antes de ir ao ar)

Banner do site (NuvemShop):
  05/05 — "Kit enxoval com 3x sem juros" — PNG pronto. Sobe em:
          NuvemShop admin → Loja → Banners.

E-mail (rascunho no Gmail):
  06/05 — "Presente de Dia das Mães que dura" — rascunho salvo no Gmail,
          revisa e envia quando quiser.

Algo pra mudar antes de fechar?
```

---

## Portões de aprovação

- **Nenhuma chamada de Canva pra linha de e-mail.** Reconfira a coluna `Trilha` antes de toda chamada de API.
- **Nada vai ao ar sem o "ok".** Posts ficam **agendados** no Content Planner; banner e e-mail ficam prontos pro JhEY publicar/enviar. O JhEY controla a publicação.
- **Sempre mostre o orçamento de geração no pré-voo.** O JhEY vê o total de artes e aprova antes da Etapa 1.
- **Uma linha por vez na Etapa 3.** Candidatas de uma linha disparam em paralelo, mas as linhas são sequenciais com 30s de pausa — é a proteção da cota.
- **No segundo erro de cota, pare e pergunte.** Nunca fique em loop de retry.
- **Sempre exporte pro PNG permanente antes de apresentar.** Sucesso do job não garante que a arte renderizou certo.
- **Nunca embuta URLs `design.canva.ai` nas mensagens.** Expiram.
- **Nunca regenere a linha inteira quando uma candidata falha.** Só por candidata.
- **Nunca escolha um template sozinho no Pro/Teams.** Sempre confirme com o JhEY.
- **Nunca pule o inventário espaço por espaço.** Template multi-espaço renderiza paisagem-placeholder quando algum espaço fica vazio.
- **Nunca pule o Checkpoint 1.** Gerar antes do calendário aprovado é a maior fonte de retrabalho desta skill.

---

## Arquivos de referência

- [reference/canva-api.md](reference/canva-api.md) — endpoints da Canva Connect API, upload de asset, formatos de export, equivalentes MCP
- [reference/hubspot-staging.md](reference/hubspot-staging.md) — publicação/agendamento sem HubSpot (Content Planner do Canva, Instagram/Facebook, banner NuvemShop, rascunho no Gmail)
- [reference/gotchas.md](reference/gotchas.md) — padrões Certo/Errado de cada modo de falha (tamanhos de post IG/FB, banner NuvemShop, marca/identidade @casaroque.design)
- [reference/examples/boutique-brief-campaign.md](reference/examples/boutique-brief-campaign.md) — exemplo completo (Dia das Mães — trocadores e kits)
