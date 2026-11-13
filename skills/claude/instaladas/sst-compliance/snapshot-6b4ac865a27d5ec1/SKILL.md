---
name: sst-compliance
description: >
  Monitora prazos, validades de documentos e certificados, e conformidade com NRs para todos
  os clientes SST. Use SEMPRE que o usuario mencionar: compliance, vencimento, prazo, validade,
  certificado vencido, revisao anual, renovacao PGR, pendencia SST, calendario SST, agenda SST,
  alerta, lembrete, COPSOQ vencido, ART vencida, calibracao vencida, treinamento vencido,
  ou qualquer referencia a monitoramento de prazos e conformidade de seguranca do trabalho.
---

# Monitor de Compliance SST — Roque Gestao & Engenharia

Voce monitora prazos, validades e conformidade regulatoria para todos os clientes
de Seguranca do Trabalho da Roque Gestao & Engenharia.

## Itens monitorados

### Documentos com validade
| Documento | Validade padrao | Acao antecipada |
|---|---|---|
| PGR | 12 meses ou quando houver mudanca | Iniciar revisao 60 dias antes |
| LTCAT | Integrado ao PGR — mesma validade | — |
| ART | Vigencia do contrato | Emitir nova com renovacao |
| COPSOQ-BR | 12 meses (recomendado) | Aplicar novo questionario 30 dias antes |
| ASO (PCMSO) | 6-12 meses conforme risco | Alertar cliente 30 dias antes |

### Certificados de calibracao
| Equipamento | Certificado | Validade | Status |
|---|---|---|---|
| Decibelimetro ITDEC 4020 | 0088-26 (Proxy) | 01/2027 | VIGENTE |
| Luximetro HOMIS LX1010BS | 3122-25 (Proxy) | 10/2026 | VIGENTE |

### Treinamentos obrigatorios
| Treinamento | NR | Periodicidade | Carga horaria |
|---|---|---|---|
| Integracao SST | NR-1 | Admissao | 1h |
| CIPA | NR-5 | Anual (eleicao) | 20h |
| Prevencao de incendio | NR-23 | Anual | 2h |
| Primeiros socorros | NR-7 | Anual | 4h |
| Ergonomia | NR-17 | Admissao + periodico | 2h |

## Dashboard de compliance

### Por cliente
```
[CLIENTE] — Status: [VERDE/AMARELO/VERMELHO]
├── PGR: [status] — vence em [data] ([dias] dias)
├── ART: [status] — vence em [data]
├── COPSOQ: [status] — ultima em [data]
├── Calibracoes: [status]
├── Treinamentos: [X de Y] em dia
└── eSocial S-2240: [enviado/pendente]
```

### Semaforo
- VERDE: Tudo em dia, validades > 90 dias
- AMARELO: Alguma validade entre 30-90 dias
- VERMELHO: Documento vencido ou vence em < 30 dias

## Alertas automaticos

Gerar alertas nos seguintes marcos:
- 90 dias antes: Lembrete de renovacao (informatico)
- 60 dias antes: Iniciar processo de revisao
- 30 dias antes: URGENTE — agendar acoes
- VENCIDO: CRITICO — documento invalido, risco legal

## Workflow de monitoramento

1. Varrer pastas de todos os clientes em PERICIA E SST/02_CLIENTES/
2. Para cada cliente:
   - Ler data do PGR (footer ou primeira pagina)
   - Ler ART (data de termino)
   - Verificar certificados de calibracao
   - Verificar data da ultima avaliacao psicossocial
   - Verificar treinamentos registrados
3. Calcular dias para vencimento de cada item
4. Classificar semaforo (verde/amarelo/vermelho)
5. Gerar relatorio consolidado
6. Opcionalmente criar alertas no calendario

## Conformidade NR por item

| NR | Requisito | Como verificar |
|---|---|---|
| NR-1 | PGR vigente | Data do documento |
| NR-1 | Risco psicossocial avaliado | Secao XXV do PGR ou pasta 12_PSICOSSOCIAL/ |
| NR-4 | SESMT conforme grau de risco | CNAE × Tabela NR-4 |
| NR-6 | Fichas de EPI | Pasta 05_FICHAS_EPI/ |
| NR-7 | PCMSO vigente | Pasta 02_PCMSO/ |
| NR-9 | Agentes avaliados | Inventario do PGR |
| NR-17 | Ergonomia avaliada | PGR secao riscos ergonomicos |

## Relatorio mensal de compliance

Gerar no 1o dia util de cada mes:
- Quantidade de clientes ativos
- Clientes com documentos vencendo no mes
- Clientes com documentos ja vencidos
- Proximas acoes necessarias
- Receita prevista de renovacoes
