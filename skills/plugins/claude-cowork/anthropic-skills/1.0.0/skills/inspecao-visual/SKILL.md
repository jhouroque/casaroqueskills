---
name: inspecao-visual
description: >
  Comparação visual página a página de documentos .docx para identificar e corrigir
  diferenças de formatação, layout, cores, tabelas e imagens. Use quando o usuário
  mencionar: comparar documentos, inspeção visual, verificar layout, checar formatação,
  diferenças entre PGRs, conferir tabelas, cores fora do padrão, logo desalinhado,
  copiar estilo de outro documento, igualar formatação, ou qualquer auditoria visual
  de documentos DOCX.
---

# Inspeção Visual e Layout — Comparação de Documentos DOCX

Skill para comparar visualmente dois documentos .docx página a página,
identificar diferenças de formatação, layout, cores, tabelas, imagens e estrutura,
e corrigir automaticamente o documento alvo para coincidir com o documento referência.

## Quando usar

- Comparar formatação de dois PGRs ou laudos técnicos
- Verificar se tabelas, cores, bordas e estilos estão iguais ao template
- Detectar imagens/logos desalinhados ou redimensionados incorretamente
- Auditar diferenças visuais entre revisões de um documento
- Corrigir layout de documento para coincidir com padrão da empresa

## Workflow completo

### 1. Preparar documentos para comparação

```bash
# Converter ambos os documentos para PDF
python scripts/office/soffice.py --headless --convert-to pdf REFERENCIA.docx
python scripts/office/soffice.py --headless --convert-to pdf ALVO.docx

# Gerar imagens página a página (JPEG 150dpi)
mkdir -p compare_ref compare_alvo
pdftoppm -jpeg -r 150 REFERENCIA.pdf compare_ref/ref
pdftoppm -jpeg -r 150 ALVO.pdf compare_alvo/alvo

# Verificar contagem
ls compare_ref/ | wc -l
ls compare_alvo/ | wc -l
```

### 2. Mapear páginas equivalentes

Documentos diferentes podem ter paginações distintas.
Criar mapa de equivalências:

```
# Exemplo de mapeamento Fabritex V17 → Vizu REV05:
# ref p57 → alvo p46: Cronograma heading + PRIORIDADES
# ref p58: Nota legal (caixa com borda)
# ref p59-60: TREINAMENTO/CAPACITAÇÃO (tabela Gantt)
# ref p61-66: RECOMENDAÇÕES E AÇÕES (tabela Gantt)
# ref p67 → alvo p47-48: PLANILHA DE REGISTROS
```

### 3. Comparar visualmente

Usar o Read tool para visualizar pares de páginas lado a lado.
Para cada par, verificar:

**Estrutura:**
- Mesmos títulos e seções presentes?
- Ordem das seções idêntica?
- Elementos ausentes no alvo?

**Tabelas:**
- Mesma quantidade de colunas e linhas?
- Headers iguais (texto, negrito, alinhamento)?
- Cores de fundo das células (shading)?
- Bordas (estilo, espessura, cor)?
- Largura das colunas proporcional?

**Texto:**
- Mesma fonte e tamanho?
- Negrito, itálico, sublinhado corretos?
- Alinhamento (esquerda, centro, justificado)?
- Espaçamento entre parágrafos?

**Imagens:**
- Logos presentes e posicionados corretamente?
- Dimensões corretas (não esticado/comprimido)?
- Imagens de localização (Google Maps) atualizadas?

**Cores:**
- Cores de prioridade: FF5050 (vermelho), FF8B00 (laranja), FFFF00 (amarelo), 92D050 (verde), 00AFEF (azul)
- Headers de tabela: D9D9D9 (cinza claro), F1F1F1 (cinza muito claro)
- Cores consistentes com o padrão da empresa

### 4. Identificar diferenças

Documentar cada diferença encontrada com:
- Página da referência e do alvo
- Tipo: [ESTRUTURA | TABELA | TEXTO | IMAGEM | COR | LAYOUT]
- Severidade: [CRÍTICO | IMPORTANTE | MENOR]
- Descrição precisa da diferença
- Localização no XML (linha aproximada)

### 5. Corrigir via XML

```bash
# Desempacotar o documento alvo
python scripts/office/unpack.py ALVO.docx alvo_unpacked/

# Editar document.xml com Edit tool
# Usar grep -n para localizar elementos:
grep -n "TEXTO_PROCURADO" alvo_unpacked/word/document.xml

# Tipos comuns de correção:

# A) Adicionar cor de fundo em célula de tabela:
# Inserir <w:shd w:val="clear" w:color="auto" w:fill="FF5050"/> dentro de <w:tcPr>

# B) Corrigir largura de coluna:
# Alterar <w:tcW w:w="VALOR" w:type="dxa"/>

# C) Adicionar tabela inteira:
# Gerar XML programaticamente (ver build_gantt.py como referência)

# D) Corrigir fonte/tamanho:
# Alterar <w:sz w:val="TAMANHO"/> dentro de <w:rPr>

# E) Adicionar negrito/itálico:
# Inserir <w:b/> ou <w:i/> dentro de <w:rPr>

# F) Texto box com borda:
# Usar mc:AlternateContent com wps:wsp e wps:txbx

# Reempacotar
python scripts/office/pack.py alvo_unpacked/ ALVO_CORRIGIDO.docx --original ALVO.docx

# Validar
python scripts/office/validate.py ALVO_CORRIGIDO.docx
```

### 6. Verificar correções

```bash
# Gerar PDF e imagens da versão corrigida
python scripts/office/soffice.py --headless --convert-to pdf ALVO_CORRIGIDO.docx
mkdir -p compare_fix
pdftoppm -jpeg -r 150 ALVO_CORRIGIDO.pdf compare_fix/fix

# Comparar visualmente com Read tool
# Verificar cada correção aplicada
```

## Tabelas Gantt — Geração Programática

Para copiar tabelas Gantt (cronograma) de um documento referência:

```python
# Estrutura de uma tabela Gantt padrão Roque:
# Colunas: # | Descrição | Colaboradores | Classificação | 12 meses | Status | Responsável
# Grid: 432 | 5111 | 691 | 716 | 410x12 | 405 | 2483 = ~14,758 DXA (landscape)
# Cada item tem 2 sub-linhas: P (Previsto) e R (Realizado)

# Elementos XML essenciais:
# - <w:tblLayout w:type="fixed"/> — layout fixo para controlar larguras
# - <w:textDirection w:val="btLr"/> — texto vertical em headers
# - <w:vMerge w:val="restart"/> e <w:vMerge/> — merge vertical P/R
# - <w:shd w:val="clear" w:color="auto" w:fill="COR"/> — cor de fundo
# - <w:gridSpan w:val="N"/> — merge horizontal

# Cores de prioridade padrão:
PRIORITY_COLORS = {
    5: "FF5050",  # Intolerável (vermelho)
    4: "FF8B00",  # Substancial (laranja)
    3: "FFFF00",  # Moderado (amarelo)
    2: "92D050",  # Aceitável (verde)
    1: "00AFEF",  # Irrelevante (azul)
}
```

## Section Breaks para orientação

```xml
<!-- Paisagem (para tabelas Gantt) -->
<w:sectPr>
  <w:pgSz w:w="16840" w:h="11910" w:orient="landscape"/>
  <w:pgMar w:top="1134" w:right="1701" w:bottom="1134" w:left="851"/>
</w:sectPr>

<!-- Retrato (padrão) -->
<w:sectPr>
  <w:pgSz w:w="11910" w:h="16840"/>
  <w:pgMar w:top="1701" w:right="1134" w:bottom="851" w:left="1134"/>
</w:sectPr>
```

## Caixa de texto com borda (Legal text box)

Para notas legais em caixa com borda, usar mc:AlternateContent com:
- wps:wsp para WML-based rendering
- v:shape para VML fallback
- w:txbxContent para o conteúdo textual
- a:ln w:w="6350" para borda de 0.5pt

## Regras de validação paraId

- Valores devem ser < 0x80000000 (hex 8 dígitos, primeiro dígito 0-7)
- Devem ser únicos em todo o documento
- Usar counter incremental para garantir unicidade

## Checklist de inspeção final

- [ ] Todas as tabelas com cores de prioridade corretas
- [ ] Tabelas Gantt com estrutura P/R para cada item
- [ ] Caixa legal com borda presente após tabela PRIORIDADES
- [ ] Section breaks corretos (portrait/landscape)
- [ ] Contagem de páginas no ENCERRAMENTO atualizada
- [ ] Logos/imagens no tamanho correto
- [ ] Fontes e tamanhos consistentes
- [ ] Headers e footers preservados
- [ ] Validação pack.py sem erros
