---
name: whatsapp-pericia
description: >
  Processa evidencias extraidas do WhatsApp (audios, imagens, documentos) para uso em
  pericias trabalhistas e laudos tecnicos. Use SEMPRE que o usuario mencionar: WhatsApp,
  audio, evidencia, pericia, laudo pericial, transcricao, midia, prova trabalhista,
  processo trabalhista, reclamacao trabalhista, chat WhatsApp, mensagem, backup WhatsApp,
  export WhatsApp, ou qualquer referencia a processar comunicacoes do WhatsApp como
  evidencia tecnica ou legal.
---

# Processador de Evidencias WhatsApp — Roque Gestao & Engenharia

Voce processa evidencias extraidas do WhatsApp para suportar pericias trabalhistas
e laudos tecnicos de seguranca do trabalho.

## Tipos de evidencia processados

| Tipo | Extensoes | Processamento |
|---|---|---|
| Audios | .opus, .ogg, .mp3, .m4a | Transcrever com Whisper → catalogar |
| Imagens | .jpg, .png, .webp | Classificar, extrair texto (OCR), catalogar |
| Documentos | .pdf, .doc, .xlsx | Extrair conteudo, classificar |
| Videos | .mp4, .3gp | Extrair frames chave, transcrever audio |
| Texto | _chat.txt | Parsear conversas com timestamps |

## Workflow completo

### 1. Inventario
```bash
# Contar arquivos por tipo
find /pasta/evidencias -type f | sed 's/.*\.//' | sort | uniq -c | sort -rn
```

### 2. Classificacao automatica
Categorias de conteudo:
- **INSTRUCAO_TRABALHO**: Ordens sobre como executar tarefas
- **CONDICAO_AMBIENTE**: Fotos/descricoes do ambiente
- **RECLAMACAO_SST**: Queixas sobre seguranca
- **EPI_EPP**: Discussoes sobre equipamentos de protecao
- **ACIDENTE**: Relatos de acidentes ou quase-acidentes
- **HORARIO**: Registros de jornada, horas extras
- **ASSEDIO**: Indicios de assedio moral ou sexual
- **ADMINISTRATIVO**: Comunicacoes gerais sem relevancia pericial
- **OUTRO**: Nao classificado

### 3. Transcricao de audios
Usar Whisper (OpenAI) via linha de comando:
```bash
whisper audio.opus --language pt --model medium --output_format txt
```

Para lotes grandes (>100 audios), processar em paralelo com GNU parallel.

### 4. Catalogacao
Gerar planilha .xlsx com:
| Arquivo | Tipo | Data/Hora | Remetente | Categoria | Resumo | Relevancia |
|---|---|---|---|---|---|---|
| audio_001.opus | Audio | 2025-03-15 14:32 | Supervisor | INSTRUCAO | Pedido de hora extra | ALTA |

### 5. Relatorio de evidencias
Documento .docx com:
- Sumario executivo (total de evidencias por categoria)
- Linha do tempo cronologica
- Evidencias de alta relevancia destacadas
- Transcricoes completas em anexo
- Cadeia de custodia (hash SHA-256 de cada arquivo)

## Cadeia de custodia digital

Para garantir integridade das evidencias:
```bash
# Gerar hash de cada arquivo
sha256sum * > CHECKSUMS.sha256

# Verificar integridade
sha256sum -c CHECKSUMS.sha256
```

## Metricas de processamento

Exemplo real (caso Vizu Home):
- 2.386 audios processados
- 1.384 arquivos de midia
- 4 categorias principais identificadas
- Tempo de processamento: ~45 minutos

## Consideracoes legais

- Evidencias de WhatsApp sao admissiveis em juizo (STJ, REsp 1.547.860/DF)
- Manter cadeia de custodia inalterada
- Nao editar ou alterar arquivos originais
- Registrar data/hora de extracao
- Preservar metadados EXIF de imagens
- Ata notarial recomendada para evidencias criticas
