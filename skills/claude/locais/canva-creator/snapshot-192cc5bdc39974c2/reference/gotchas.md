# Pegadinhas

Modos de falha comuns da skill canva-creator. Pares Certo/Errado.

---

## Pegadinha: gerar QUALQUER arte de e-mail no Canva

**Por que importa:** o e-mail é texto puro nesta skill. O autofill de template de e-mail no Canva gera imagens-placeholder (paisagens de estoque, retângulos em branco) quando há mais espaços de imagem que fotos, e as miniaturas não renderizam no chat. A decisão é: e-mail é texto, ponto. Gerar uma arte de e-mail no Canva — mesmo uma — é regressão.

### ✗ Errado

```
Calendário com 6 linhas de social + 2 de e-mail.
→ Etapa 3 gera 6 artes de social + 2 artes de e-mail.
→ As de e-mail saem com tiles-placeholder.
```

Ou qualquer variação: "vou gerar o template de e-mail só de referência", "achei um template de e-mail, quer ver?", "aqui uma arte pro e-mail de 06/05…" — todas proibidas.

### ✓ Certo

```
Etapa 1: Calendário com coluna Trilha.
  - 6 linhas marcadas Canva (social)
  - 2 linhas marcadas Texto puro (sem Canva)
Etapa 3: Gera exatamente 6 artes. Linhas de e-mail não passam por nenhum endpoint do Canva.
Etapa 4: Escreve 6 legendas + 2 e-mails (assunto + prévia + corpo) em texto.
Etapa 5: Agenda 6 posts no Content Planner. Deixa 2 e-mails como rascunho no Gmail.
```

Se o JhEY pedir uma arte de e-mail no Canva ("faz uma versão Canva do e-mail de 06/05?"), redirecione: "Essa skill mantém e-mail como texto porque a trilha de e-mail no Canva gera imagens-placeholder. Se quiser um e-mail desenhado no Canva, monta direto no Canva que eu te ajudo com o texto aqui."

---

## Pegadinha: tamanho errado de arte por canal (IG/FB/banner)

**Por que importa:** cada canal tem um tamanho. Post quadrado do Instagram é 1080×1080; story/Reels é 1080×1920 (9:16); Facebook feed é 1200×630; banner da NuvemShop segue o **tema da loja** (varia). Exportar no tamanho errado corta a arte, deixa borda branca ou pixela.

### ✗ Errado

Exportar tudo em 1080×1080 e usar o mesmo arquivo no story (que vira quadrado no meio da tela), no Facebook (que corta) e no banner do site (que estica).

### ✓ Certo

Exportar cada linha no tamanho do canal:
- Instagram feed → 1080×1080
- Instagram story/Reels → 1080×1920
- Facebook feed → 1200×630
- Banner home NuvemShop → confirmar a dimensão do tema (ex.: 1920×600) **antes** de exportar; pergunte ao JhEY ou peça um print do banner atual do site.

---

## Pegadinha: banner do site sem confirmar a dimensão do tema NuvemShop

**Por que importa:** não há conector de NuvemShop, e cada tema de loja tem um tamanho de banner diferente. Entregar um banner que não encaixa no slot da home gera retrabalho — o JhEY sobe, fica torto, e tem que voltar.

### ✗ Errado

Gerar o banner num tamanho qualquer ("uns 1200×400 deve servir") e mandar pro JhEY subir.

### ✓ Certo

Antes de gerar o banner, perguntar: "Qual o tamanho do banner da home no seu tema da NuvemShop? Se não souber, me manda um print do banner atual do site que eu pego a proporção." Gerar no tamanho certo e nomear o arquivo pela posição (home, categoria).

---

## Pegadinha: arte fora da identidade @casaroque.design (marca/logo)

**Por que importa:** o Canva Pro da Casa Roque tem brand kit (cores, fontes, selo @casaroque.design). Gerar arte com cor/fonte aleatória ou sem o selo da marca quebra a identidade e parece de outra loja.

### ✗ Errado

Usar um template colorido qualquer da galeria pública do Canva, com fonte fora do padrão e sem o selo da marca.

### ✓ Certo

Usar template da **biblioteca da conta** casaroque.design, aplicar as cores/fontes do brand kit e incluir o selo @casaroque.design. Se uma arte sair fora do padrão na conferência visual (Etapa 3, Passo 5), reprovar e refazer.

---

## Pegadinha: gerar sem plano de orçamento

**Por que importa:** o Canva limita a 100 requisições/minuto por token, e cada arte custa ~5 chamadas. Uma campanha de 10 linhas com 4 candidatas gera 40 artes e ~200 chamadas. Sem orçamento de pré-voo, o JhEY estoura a cota no meio e fica com 4 posts feitos e o resto travado.

### ✗ Errado

```
Calendário aprovado → dispara 4 candidatas × 8 linhas em paralelo
→ ~160 chamadas em 90s → RATE_LIMIT_EXCEEDED no post 5 → loop de retry → travado.
```

### ✓ Certo

```
Pré-voo: "8 linhas Canva × 3 candidatas = 24 artes, ~120 chamadas. Sigo no padrão de 3?"
Etapa 3: linha 1 (3 candidatas em paralelo) → pausa 30s → linha 2 → … ~12 artes/min.
Se a cota estourar: para, mostra o progresso, pergunta se cai pra 1 candidata, pausa 1h, ou vai pras legendas.
```

---

## Pegadinha: pular o Checkpoint 1 (aprovação do calendário) antes de gerar

**Por que importa:** gerar 10+ artes custa chamadas, tempo e atenção. Se o calendário tem data errada, canal errado, ou o JhEY muda de ideia sobre um tema, todo o trabalho vai pro lixo. O checkpoint do calendário é o lugar mais barato pra pegar desalinhamento.

### ✗ Errado

Receber o plano → já começar a gerar as 12 artes → apresentar antes de o JhEY aprovar o cronograma.

JhEY: "Peraí, não queria post na semana do dia 15, vou viajar."

### ✓ Certo

Apresentar a tabela do calendário primeiro. Esperar o "tá bom" explícito antes de abrir uma única chamada de API do Canva.

---

## Pegadinha: template com mais espaços de imagem que o plano deu fotos

**Por que importa:** carrossel do Instagram e banner de site podem ter 3+ espaços. Quando o plano dá 1 foto e o template pede 3, os espaços vazios renderizam a paisagem padrão do Canva (nuvens e morros verdes). A arte parece "pronta" até o JhEY abrir.

### ✗ Errado

Inventário com uma linha por arte ("Carrossel — precisa de Hero"). Subir 1 foto. Gerar. Carrossel sai com o slide 1 ok e os slides 2-3 com paisagem genérica idêntica.

### ✓ Certo

Inventário espaço por espaço. Mostrar a lacuna:

```
O template "Carrossel Dia das Mães" tem 3 espaços de imagem. O plano me deu 1 foto.
Como preencho os outros 2?
1. Repete a mesma foto nos 3
2. Te mando 2 fotos
3. Template de 1 imagem
```

Esperar a escolha antes de gerar. Não deixar placeholder ir ao ar.

---

## Pegadinha: confiar no `status: success` sem exportar e conferir visualmente

**Por que importa:** job de sucesso significa que o Canva aceitou e produziu um design — não que ele tem as imagens certas. Se um `asset_id` estava vazio, velho ou do tipo errado, o job ainda retorna `success` e a arte sai com placeholder. A única forma de saber é olhar.

### ✗ Errado

```
Job status: success ✓
result.design.id: presente ✓
→ Apresenta pro JhEY
```

Resultado: o JhEY abre o carrossel e vê paisagem de estoque em 3 de 4 artes.

### ✓ Certo

Depois do sucesso, exporte cada design pra PNG permanente via `POST /exports` (ou `export-design` MCP). Olhe cada PNG e confirme que tem asset real — não a paisagem padrão, nem retângulo cinza, nem lorem-ipsum. Só apresente após passar na conferência visual.

---

## Pegadinha: uma arte do lote falha em renderizar

**Por que importa:** quando 1 de 4 artes do lote falha (erro de job, URL de prévia expirada, placeholder) e você apresenta o carrossel parcial assim mesmo, o JhEY vê três artes reais e um retângulo cinza "Show Image". Ele perde a confiança no resto do carrossel mesmo estando ok.

### ✗ Errado

```
Artes da semana 1 prontas:
[Opção A — prévia real]
[Opção B — prévia real]
[Opção C — prévia real]
[Opção D — placeholder Show Image]
Qual eu uso?
```

### ✓ Certo

Ao detectar a arte quebrada no Passo 5 da conferência, regenere só aquela com o asset_id certo. Re-exporte, reconfira. Só apresente quando as quatro tiverem prévia permanente e verificada. Se a segunda tentativa também falhar, pergunte ao JhEY se pula, troca o template ou tenta outra foto.

---

## Pegadinha: passar valor inválido pro campo de imagem do autofill

**Por que importa:** quando um campo de imagem recebe string vazia, caminho de arquivo, URL ou `asset_id` velho/inválido, o Canva não dá erro — renderiza silenciosamente o placeholder padrão do template (paisagem genérica). A arte parece "finalizada", mas a imagem-hero é arte de estoque, não a foto do produto.

### ✗ Errado

Subir a foto → não esperar o job de upload terminar → passar o `job_id` (não o `asset.id`) no autofill → arte sai com paisagem em vez da foto do produto.

### ✓ Certo

Subir via `POST /v1/asset-uploads` → polling em `GET /v1/asset-uploads/{job_id}` até `status == "success"` → extrair `asset.id` → passar esse ID exato no campo de imagem. Verificar que todo campo de imagem tem `asset.id` confirmado antes de gerar.

---

## Pegadinha: embutir URLs de miniatura do CDN do Canva no markdown

**Por que importa:** a resposta do autofill devolve URLs de CDN autenticadas e de vida curta de `design.canva.ai`. Expiram em minutos. Se o Claude embute como imagem markdown (`![](design.canva.ai/...)`), viram placeholders "Show Image" quebrados na hora que a mensagem aparece.

### ✗ Errado

Gerar 8 artes → embutir cada miniatura de CDN como `![Hero 1](https://design.canva.ai/xxx)` → todas viram placeholder cinza porque expiraram antes de renderizar.

### ✓ Certo

Ou deixar o carrossel nativo do Cowork renderizar o resultado automaticamente, ou exportar cada design via `POST /exports` e embutir a URL de export **permanente**. Último recurso: link da URL de edição permanente (`https://www.canva.com/d/{design_id}`). Nunca re-embutir URLs `design.canva.ai`.

---

## Pegadinha: listar designs um por um como blocos de imagem separados

**Por que importa:** quando o Claude lista cada design como bloco separado ("Hero 1 / [imagem] / Hero 2 / [imagem]"), as imagens viram placeholders cinza "Show Image" quebrados. Apresentar todos juntos num lote agrupado dispara o carrossel lado a lado do Cowork, que renderiza certo.

### ✗ Errado

```
Hero 1 — Trocador americano
[Show Image]
Ver no Canva: https://canva.com/d/xxx

Hero 2 — Kit enxoval
[Show Image]
Ver no Canva: https://canva.com/d/yyy
```

### ✓ Certo

Apresentar todos os designs numa resposta agrupada pra renderizar como carrossel lado a lado. Abaixo, um único pedido:

```
Aqui estão 4 artes pra semana 1. Passa pelo carrossel acima e me diz qual fica.
```

---

## Pegadinha: gerar designs em série em vez de em paralelo

**Por que importa:** gerar um por vez faz o JhEY esperar N idas e voltas em vez de uma. Dispare todas as gerações de um lote de uma vez e apresente a escolha depois que todos terminarem.

### ✗ Errado

Gerar design 1 → esperar → mostrar → design 2 → esperar → mostrar → … × 8. O JhEY assiste a um gotejamento de 10 minutos.

### ✓ Certo

Disparar todas as candidatas do lote de uma vez → polling concorrente → ao terminar, exportar cada → conferir → apresentar.

---

## Pegadinha: escolher um template sozinho no Pro/Teams

**Por que importa:** Pro/Teams não tem API de brand template. Se o Claude chuta um template pelo nome e gera com o errado, o JhEY recebe artes na cor/fonte errada e tem que refazer no Canva.

### ✗ Errado

```
Achei o template "Post Quadrado — Azul". Uso esse em todos os posts.
```
…seguido de 8 artes em azul quando a marca @casaroque.design é outra paleta.

### ✓ Certo

```
Achei 3 templates na sua biblioteca do Canva que servem pros posts de feed:
1. Post Quadrado — Enxoval  (editado em abr/2026)
2. Promo Bebê — Areia        (editado em mar/2026)
3. Destaque Produto          (editado em jan/2026)

Qual eu uso?
```

---

## Pegadinha: deriva de voz nas legendas ao longo de um calendário longo

**Por que importa:** ao escrever 12–20 legendas de uma vez, o tom escorrega — as primeiras seguem a voz do plano, as últimas viram texto de marketing genérico. O JhEY percebe na hora.

### ✗ Errado

Post 1: "O trocador que toda mãe queria 🤍" (bate com o plano: "calorosa, próxima")
Post 10: "Eleve a experiência do enxoval com nossa coleção premium." (deriva corporativa)

### ✓ Certo

Antes de escrever, fixe 2–3 marcadores de voz do plano (ex.: "direta, calorosa, sem enrolação"). Releia a primeira legenda antes de escrever cada nova. Se o JhEY apontar deriva em alguma, releia aquela e use como ponto de recalibração pras restantes.

---

## Pegadinha: agendar no Content Planner sem conferir se a data está no futuro

**Por que importa:** se o calendário foi montado numa data anterior e o JhEY só agora vai agendar, algumas datas podem ter passado. Agendar no passado não faz sentido e confunde a fila.

### ✗ Errado

Montar calendário em 01/04 pra posts de maio → JhEY aprova em 15/05 → tentar agendar o post de "30/04, 10h" que já passou.

### ✓ Certo

Antes de agendar no Content Planner, compare cada data/hora com o horário atual (America/Sao_Paulo). Se alguma passou, sinalize: "O post de 30/04 já passou. Pulo ou reagendo pra próxima semana?"
