---
name: sst-onboarding
description: >
  Cria toda a estrutura de pastas e documentos iniciais para onboarding de novo cliente SST
  na Roque Gestao & Engenharia. Use SEMPRE que o usuario mencionar: novo cliente, onboarding,
  setup cliente, estrutura de pastas, pasta do cliente, organizar documentos SST, criar pasta,
  primeiro atendimento SST, contrato SST, checklist cliente, ou qualquer referencia a iniciar
  trabalho com um cliente novo de seguranca do trabalho.
---

# Onboarding Cliente SST — Roque Gestao & Engenharia

Voce cria toda a estrutura de pastas, coleta dados e gera documentos iniciais para
um novo cliente de Seguranca do Trabalho.

## Estrutura de pastas (14 subpastas)

```
PERICIA E SST/02_CLIENTES/[NOME_CLIENTE]/
├── 01_PGR_LTCAT/          # PGR com LTCAT integrado
├── 02_PCMSO/              # Programa de Controle Medico (parceiro medico)
├── 03_MEDICOES/           # Certificados de calibracao e laudos de medicao
├── 04_TREINAMENTOS/       # Registros de treinamentos NR
├── 05_FICHAS_EPI/         # Fichas de entrega de EPI (se aplicavel)
├── 06_OSS/                # Ordens de Servico de Seguranca
├── 07_INTEGRACAO/         # Documentos de integracao SST
├── 08_FUNCIONARIOS/       # Documentos por funcionario
│   └── [NOME_FUNCIONARIO]/
├── 09_ART/                # ARTs emitidas (CREA)
├── 10_ESOCIAL/            # Eventos S-2240 e comprovantes
├── 11_FOTOS/              # Registro fotografico do ambiente
├── 12_PSICOSSOCIAL/       # Avaliacao COPSOQ-BR
├── 13_EVIDENCIAS/         # Evidencias e documentacao extra
└── 14_CONTRATOS/          # Contratos e propostas comerciais
```

## Dados necessarios para onboarding

### Obrigatorios
- Razao social completa
- CNPJ
- CNAE principal e secundarios
- Endereco completo (rua, numero, bairro, cidade, UF, CEP)
- Nome do socio-administrador
- CPF do socio-administrador
- Numero de funcionarios
- Lista de setores e cargos
- Area total do estabelecimento (m2)
- Grau de risco (NR-4, por CNAE)
- Nome fantasia

### Desejaveis
- Contrato social ou ultimo aditivo
- Lista nominal de funcionarios com CPF
- PPRA/PGR anterior (se houver)
- PCMSO vigente
- Fotos do ambiente de trabalho
- Contato do RH ou responsavel

## Checklist de onboarding

1. [ ] Criar estrutura de 14 pastas
2. [ ] Coletar dados da empresa (razao social, CNPJ, CNAE, grau risco)
3. [ ] Coletar lista de funcionarios com setores e cargos
4. [ ] Tirar/receber fotos dos ambientes de trabalho
5. [ ] Verificar CNAE × grau de risco (NR-4)
6. [ ] Agendar visita tecnica
7. [ ] Realizar medicoes (ruido e iluminancia)
8. [ ] Aplicar questionario COPSOQ-BR
9. [ ] Elaborar PGR com LTCAT integrado
10. [ ] Gerar OSS para cada cargo
11. [ ] Gerar documentos de integracao
12. [ ] Emitir ART no CreaNet
13. [ ] Gerar eventos S-2240 para eSocial
14. [ ] Entregar documentacao completa ao cliente

## Proposta comercial padrao

Valores de referencia (2026):
- PGR + LTCAT ate 10 funcionarios: R$ 800,00
- PGR + LTCAT de 11 a 30 funcionarios: R$ 800,00 - R$ 1.200,00
- Avaliacao psicossocial COPSOQ-BR: inclusa no PGR
- ART: ~R$ 100,90 (taxa CREA-SP)
- Renovacao anual: 50% do valor inicial

## Workflow automatizado

1. Usuario informa: nome do cliente + CNPJ (minimo)
2. Skill cria as 14 pastas
3. Busca dados complementares se possivel (CNAE, endereco)
4. Gera checklist .md com status de cada item
5. Prepara template de PGR personalizado
6. Agenda proximas acoes (medicoes, COPSOQ, ART)
