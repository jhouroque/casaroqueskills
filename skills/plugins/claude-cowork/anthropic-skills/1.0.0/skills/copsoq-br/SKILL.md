---
name: copsoq-br
description: >
  Avaliacao de riscos psicossociais usando metodologia COPSOQ-BR (Copenhagen Psychosocial
  Questionnaire validado para o Brasil). Use SEMPRE que o usuario mencionar: psicossocial,
  COPSOQ, risco psicossocial, saude mental no trabalho, estresse ocupacional, NR-1 psicossocial,
  Portaria MTE 1.419/2024, questionario psicossocial, tabulacao psicossocial, laudo psicossocial,
  avaliacao psicossocial, assedio moral, burnout, carga mental, organizacao do trabalho,
  relacoes interpessoais, ou qualquer tema de saude mental ocupacional. Ative tambem quando
  o usuario pedir para incorporar psicossocial em PGR existente.
---

# Avaliacao Psicossocial COPSOQ-BR — Roque Gestao & Engenharia

Voce conduz avaliacoes de riscos psicossociais conforme NR-1 (Portaria MTE 1.419/2024)
usando a metodologia COPSOQ-BR validada cientificamente para o Brasil.

## Base legal

- NR-1 (Portaria SEPRT 6.730/2020, atualizada pela Portaria MTE 1.419/2024)
  exige identificacao e avaliacao de riscos psicossociais no PGR
- COPSOQ-BR: versao brasileira validada do Copenhagen Psychosocial Questionnaire
- Referencia: Fernandes & Pereira (2023), validacao brasileira

## Fluxo completo (5 etapas)

### Etapa 1 — Questionario

Gerar questionario COPSOQ-BR personalizado com identidade visual Roque Engenharia.
20 questoes divididas em 4 dimensoes + 1 saude/bem-estar:

| Dimensao | Questoes | O que avalia |
|---|---|---|
| Organizacao do Trabalho | Q1-Q5 | Ritmo, autonomia, pausas, metas, horas extras |
| Relacoes Interpessoais | Q6-Q8 | Apoio chefia, apoio colegas, comunicacao |
| Conteudo e Natureza | Q9-Q12 | Esforco fisico, monotonia, significado, desenvolvimento |
| Saude e Bem-Estar | Q13-Q16 | Estresse, satisfacao, insonia, esgotamento |
| Contexto Organizacional | Q17-Q20 | Reconhecimento, estabilidade, assedio, equilibrio |

Escala Likert 1-5: Nunca(1), Raramente(2), As vezes(3), Frequentemente(4), Sempre(5)

Para questoes positivas (Q3, Q7, Q8, Q12, Q14, Q17, Q20): inverter escala.

### Etapa 2 — Aplicacao

- Aplicar anonimamente a TODOS os colaboradores
- Minimo: 100% do efetivo para empresas com ate 10 funcionarios
- Formato: impresso ou Google Forms
- Prazo: 1 semana para resposta

### Etapa 3 — Tabulacao

Calcular medias por dimensao e geral:

```
Media por questao = soma_respostas / n_respondentes
Media por dimensao = soma_medias_questoes_da_dimensao / n_questoes_da_dimensao
Media geral = soma_todas_medias_dimensoes / n_dimensoes
```

### Etapa 4 — Classificacao de risco

| Faixa | Classificacao | Acao requerida |
|---|---|---|
| 1,00 - 1,99 | BAIXO | Monitoramento anual |
| 2,00 - 2,99 | MEDIO | Plano de acao em 90 dias |
| 3,00 - 3,99 | ALTO | Intervencao imediata em 30 dias |
| 4,00 - 5,00 | CRITICO | Acao emergencial + PCMSO |

### Etapa 5 — Laudo e integracao ao PGR

O laudo deve conter:
- Dados da empresa e periodo de avaliacao
- Metodologia (COPSOQ-BR com referencia academica)
- Resultados por dimensao com grafico radar
- Classificacao geral de risco
- Questoes com maior desvio (risco pontual)
- Recomendacoes especificas por dimensao
- Cronograma de reavaliacao

Integracao ao PGR:
- Adicionar como secao XXV (antes do Encerramento)
- Atualizar item do cronograma para "REALIZADO" com resultado
- Referenciar o laudo completo na pasta 03_PSICOSSOCIAL/

## Formato do laudo (docx, padrao Roque)

- Logo marsala Roque no cabecalho
- Cor principal: #5B1A2E (marsala/burgundy)
- Fonte: Arial
- Tabelas com bordas cinza, cabecalho com fundo marsala texto branco
- Grafico radar das 5 dimensoes
- Assinatura digital do responsavel tecnico

## Modelo de dados (exemplo real Vizu Home)

```
Respondentes: 3 de 3 (100%)
Organizacao do Trabalho: 1,50 (BAIXO)
Relacoes Interpessoais: 1,33 (BAIXO)
Conteudo e Natureza: 2,50 (MEDIO) ← ponto de atencao
Saude e Bem-Estar: 1,28 (BAIXO)
Contexto Organizacional: 1,05 (BAIXO)
RISCO GERAL: 1,53 (BAIXO)

Destaques: Q9 esforco fisico 2,67 MEDIO | Q10 monotonia 2,33 MEDIO
```
