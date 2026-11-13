---
name: pacote-sst-funcionario
description: >
  Gera o pacote completo de documentos SST para um funcionario especifico: OSS, Integracao,
  Ficha de EPI (se aplicavel), Carta de Oposicao Sindical e Roteiro Sindicato. Use SEMPRE
  que o usuario mencionar: documentos do funcionario, OSS, ordem de servico, integracao SST,
  ficha de EPI, admissao SST, novo funcionario SST, pacote admissional, carta oposicao,
  sindicato, CIPA, ou qualquer documento individual de seguranca por trabalhador.
---

# Pacote SST Funcionario — Roque Gestao & Engenharia

Voce gera todos os documentos de SST necessarios para um funcionario especifico,
seja na admissao ou em revisao periodica.

## Documentos do pacote

### 1. OSS — Ordem de Servico de Seguranca (NR-1, art. 1.7)
Informa ao trabalhador os riscos do seu cargo e medidas de prevencao.

Conteudo:
- Dados da empresa e do funcionario
- Cargo e setor
- Riscos identificados (do inventario do PGR)
- Medidas de prevencao (EPC/EPI)
- Procedimentos em emergencia
- Obrigacoes do trabalhador
- Assinatura do funcionario e responsavel

### 2. Integracao SST (NR-1, art. 1.7.1)
Registro de integracao do trabalhador com informacoes de SST.

Conteudo:
- Dados do funcionario
- Data e local da integracao
- Topicos abordados (riscos, emergencia, EPI, CIPA)
- Carga horaria minima: 1 hora
- Assinatura do funcionario e instrutor

### 3. Ficha de EPI (NR-6, art. 6.6.1) — SE APLICAVEL
Registro de entrega de EPIs ao funcionario.

**REGRA IMPORTANTE**: Se o cargo NAO requer EPI (ex: administrativo, comercio
sem riscos fisicos), a ficha e DISPENSADA. Registrar no PGR como "EPI dispensado".

Conteudo (quando aplicavel):
- Dados do funcionario
- EPIs entregues (descricao, CA, quantidade)
- Data de entrega e devolucao
- Assinatura de recebimento
- Orientacao sobre uso e conservacao

### 4. Carta de Oposicao Sindical
Modelo para o funcionario se opor ao desconto assistencial sindical.

Conteudo:
- Dados do funcionario
- Dados do sindicato da categoria
- Manifestacao de oposicao
- Base legal (art. 8, V da CF; Precedente Normativo 119 TST)
- Espaco para assinatura

### 5. Roteiro Sindicato
Guia para o funcionario protocolar a carta de oposicao no sindicato.

Conteudo:
- Endereco e horario do sindicato
- Documentos necessarios (RG, CPF, carteira de trabalho)
- Passo a passo do protocolo
- Prazo para entrega (geralmente 10 dias antes do desconto)

## Dados necessarios

| Dado | Fonte |
|---|---|
| Nome completo | Lista de funcionarios do cliente |
| CPF | Lista de funcionarios |
| Cargo | PGR → Quadro de setores |
| Setor | PGR → Quadro de setores |
| Data admissao | Cliente/RH |
| Riscos do cargo | PGR → Inventario por ambiente |
| EPIs recomendados | PGR → Inventario (se houver) |
| Sindicato | Conforme CNAE e convencao coletiva |

## Workflow

1. Ler dados do funcionario (nome, CPF, cargo, setor, data admissao)
2. Ler PGR do cliente (riscos do setor/cargo)
3. Verificar se o cargo requer EPI
4. Gerar OSS personalizada
5. Gerar documento de Integracao
6. Gerar Ficha de EPI (se aplicavel) ou registrar dispensa
7. Gerar Carta de Oposicao Sindical
8. Gerar Roteiro Sindicato
9. Salvar tudo em 08_FUNCIONARIOS/[NOME]/

## Formato dos documentos

- Todos em .docx (padrao Roque)
- Logo marsala no cabecalho
- Fonte Arial
- Assinatura digital do responsavel tecnico
- Campo de assinatura para o funcionario
