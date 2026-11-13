# Referência da Canva Connect API

Base URL: `https://api.canva.com/rest/v1`
Auth: token Bearer (OAuth 2.0). Escopos necessários: `design:content:read`, `design:content:write`, `asset:read`, `asset:write`, `brandtemplate:content:read` (só Enterprise).

> A Casa Roque usa **Canva Pro** (conta casaroque.design). Os endpoints de **brand template / autofill** são exclusivos de Enterprise — no Pro, vale a trilha **Cópia de design (Pro/Teams)** abaixo. Os endpoints de upload de asset e export funcionam no Pro.

---

## Sumário

1. [Requisitos por plano](#requisitos-por-plano)
2. [Brand templates (Enterprise)](#brand-templates-enterprise)
3. [Autofill (Enterprise)](#autofill-enterprise)
4. [Cópia de design (Pro/Teams)](#cópia-de-design-proteams)
5. [Upload de asset](#upload-de-asset)
6. [Export](#export)
7. [Códigos de erro](#códigos-de-erro)

---

## Requisitos por plano

| Recurso | Free | Pro | Teams | Enterprise |
|---------|------|-----|-------|------------|
| Criar designs | ✓ | ✓ | ✓ | ✓ |
| Listar designs próprios | ✓ | ✓ | ✓ | ✓ |
| Brand templates (leitura) | — | — | — | ✓ |
| Autofill de brand template | — | — | — | ✓ |
| Upload de asset (brand kit) | — | — | — | ✓ |
| Upload de asset (usuário) | — | ✓ | ✓ | ✓ |

> **Casa Roque = Pro.** Use a trilha Pro/Teams: seleção manual de template + upload de asset + export. Não tente autofill de brand template (retorna `PERMISSION_DENIED` fora do Enterprise).

---

## Brand templates (Enterprise)

**Listar brand templates:**
```
GET /brand-templates?query={palavra-chave}&ownership=organization
```
Campos de interesse:
- `id` — passar pro autofill
- `title` — nome legível
- `thumbnail.url` — imagem de prévia
- `dataset[].label` — rótulos dos campos de autofill (ex.: "Titulo", "NomeProduto")

Filtre por `title` contendo o tipo de arte (ex.: "post quadrado", "story", "banner").

---

## Autofill (Enterprise)

Preenche os campos variáveis de um brand template e cria um design novo:

```
POST /autofills
{
  "brand_template_id": "<template_id>",
  "title": "Dia das Mães — Post 1",
  "data": {
    "Titulo": { "type": "text", "text": "O trocador que toda mãe queria" },
    "ImagemProduto": { "type": "image", "asset_id": "<asset_id_subido>" }
  }
}
```

Resposta: `{ "job": { "id": "<job_id>", "status": "queued" } }`

Faça polling em `GET /autofills/{job_id}` até `status == "success"`. A resposta inclui `result.design.id` — use pra exportar.

---

## Cópia de design (Pro/Teams) — **trilha da Casa Roque**

Não há endpoint direto de "copiar template" no Pro/Teams. Fluxo:

1. `GET /designs?ownership=any&query={nome do template}` — lista designs por nome
2. Mostre os 3 melhores ao JhEY; pegue a confirmação
3. `POST /designs` com `asset_type` pra criar um design em branco no tamanho certo e descreva o que o JhEY precisa ajustar manualmente no Canva.

No Pro/Teams a geração é semi-manual: o Claude cria a base do design e preenche o que a API permite; o JhEY aplica as edições de marca no Canva (cores/fontes @casaroque.design) e devolve o ID do design pro export.

---

## Upload de asset

Use quando o plano referencia fotos de produto guardadas no disco do JhEY ou no Google Drive.

**Passo 1 — Iniciar o upload:**
```
POST /asset-uploads
{ "name_base64": "<base64(nome_do_arquivo)>", "types": ["image/jpeg"] }
```
Resposta: `{ "job": { "id": "<job_id>" }, "upload_url": "<url_s3_assinada>" }`

**Passo 2 — Subir o arquivo:**
```
PUT <upload_url>
Content-Type: image/jpeg
Body: <bytes do arquivo>
```

**Passo 3 — Polling até pronto:**
`GET /asset-uploads/{job_id}` → espere `status == "success"` → capture `asset.id`.

Tamanho máximo: 100 MB. Tipos suportados: `image/jpeg`, `image/png`, `image/webp`.

---

## Export

**Por que exportar todo design:** a miniatura da resposta do autofill em `design.canva.ai/...` é uma URL de CDN autenticada e de vida curta — expira em minutos e vira placeholder "Show Image" quebrado se embutida numa imagem markdown depois de expirar. A saída de `POST /exports` é uma **URL permanente**, segura pra embutir na prévia do chat, usar no banner que o JhEY sobe na NuvemShop e agendar no Content Planner do Canva.

Sempre exporte cada design após gerar, antes de mostrar prévias.

```
POST /exports
{
  "design_id": "<design_id>",
  "format": {
    "type": "png",
    "export_quality": "regular",
    "pages": [1]
  }
}
```

Faça polling em `GET /exports/{job_id}` até `status == "success"`. A resposta inclui `urls[]` — use `urls[0]` como link de prévia e como arquivo do banner/post.

**Equivalentes MCP do Canva** (quando usar o conector Canva do Cowork em vez de REST direto):

| Necessidade | Ferramenta MCP | Retorna |
|------|---------|---------|
| URL de prévia permanente | `export-design` | URL de download permanente (segura pra embutir) |
| Miniatura por página (mais estável que a do autofill, não permanente) | `get-design-thumbnail` | URL da miniatura da página |
| Só metadados do design | `get-design` | Título, dono, nº de páginas, miniatura |
| Subir da máquina do JhEY | `upload-asset-from-url` | `asset_id` (uma URL por chamada) |

**Tamanhos por canal (Casa Roque):**

| Canal | Tipo | Dimensões |
|---------|------|-----------|
| Instagram feed | `png` | 1080×1080 (quadrado) |
| Instagram story / capa de Reels | `png` | 1080×1920 |
| Facebook feed | `png` | 1200×630 |
| Banner home NuvemShop | `png` | 1920×600 (confirmar o tamanho do tema da loja — ver gotchas) |

---

## Limites de taxa e orçamento de geração

**Limite rígido:** 100 requisições por minuto por token.

**Custo por design:** ~5 chamadas de API — 1 geração (`POST /autofills` no Enterprise ou `POST /designs` no Pro) + 1 `POST /exports` + ~3 rodadas de polling (`GET /autofills/{job_id}`, `GET /exports/{job_id}`). A cadência de polling deve ser 3-5 segundos; polling mais rápido queima cota sem acelerar.

**Teto seguro:** ~15-20 designs por minuto deixa folga sob os 100 req/min.

**Ritmo recomendado (usado pela Etapa 3):**

```
3 candidatas por linha × 1 linha por vez × 30s entre linhas
= 6 designs (~30 chamadas) por 30 segundos
= 12 designs / minuto, cerca da metade do teto
```

**Fórmula do orçamento de pré-voo:**

```
total_designs = (linhas que vão pro Canva) × (candidatas por linha, padrão 3)
total_chamadas ≈ total_designs × 5
tempo_geração ≈ (total_designs / 12) minutos
```

**Padrão de recuo para `RATE_LIMIT_EXCEEDED`:**

1. 1ª vez na sessão → espere 60s, tente essa candidata de novo. Trata como pico transitório.
2. 2ª vez na mesma sessão, ou qualquer erro de `quota_exceeded` / teto diário → pare a geração e mostre o progresso ao JhEY. Não tente de novo. A skill pergunta se ele quer (a) cair pra 1 candidata por linha restante, (b) pausar e retomar em 60 minutos, ou (c) parar e ir pras legendas com o que já foi gerado.

---

## Códigos de erro

| Código | Significado | O que fazer |
|------|---------|-----------|
| `PERMISSION_DENIED` | Escopo faltando ou plano errado | Confira o plano (Casa Roque = Pro, sem autofill/brand template); peça pra reconectar o Canva com os escopos certos |
| `DESIGN_NOT_FOUND` | ID de design errado | Liste os designs de novo e confirme o ID |
| `AUTOFILL_FIELD_NOT_FOUND` | Nome de campo do template não bate (Enterprise) | Chame `GET /brand-templates/{id}` e releia `dataset[].label` |
| `RATE_LIMIT_EXCEEDED` | Requisições demais | 1ª vez: espere 60s, tente uma vez. 2ª vez: pare e pergunte ao JhEY (ver Limites de taxa acima) |
| `JOB_FAILED` | Job assíncrono falhou | Confira `job.error.message`; causa comum é asset grande demais |
