---
name: sst-audit
description: >
  Audita e compara documentos SST para verificar consistencia, completude e conformidade
  com NRs. Use SEMPRE que o usuario mencionar: auditoria, comparar PGR, verificar documento,
  inconsistencia, revisar SST, conformidade NR, checklist SST, comparativo, diff PGR,
  validar PGR, conferir dados, conferir CNPJ, conferir equipamentos, ou qualquer pedido de
  verificacao cruzada entre documentos de seguranca do trabalho.
---

# Auditoria SST — Roque Gestao & Engenharia

Voce audita documentos de Seguranca do Trabalho comparando versoes, verificando
consistencia interna e conformidade com normas regulamentadoras.

## Tipos de auditoria

### 1. Comparativo entre PGRs (cross-client)
Compara PGR de referencia (modelo/final) com PGR do novo cliente.
Verifica se todos os dados foram corretamente personalizados.

### 2. Auditoria interna (single document)
Verifica consistencia dentro de um unico PGR.

### 3. Auditoria de pasta completa
Verifica se todas as 14 subpastas tem os documentos necessarios.

## Checklist de verificacao (comparativo cross-client)

### Dados da empresa (CRITICO)
- [ ] Razao social correta (sem resquicios do cliente anterior)
- [ ] CNPJ correto (exatamente 14 digitos: XX.XXX.XXX/XXXX-XX)
- [ ] CNAE correto
- [ ] Grau de risco correto (conferir CNAE × NR-4)
- [ ] Endereco completo e correto
- [ ] Nome do socio/administrador
- [ ] Pronome de tratamento (Sr./Sra.)

### Instrumentacao (CRITICO)
- [ ] Decibelimetro: INSTRUTEMP ITDEC 4020, cert. 0088-26, Proxy Metrologia, val. 01/2027
- [ ] Luximetro: HOMIS LX1010BS, cert. 3122-25, Proxy Metrologia, val. 10/2026
- [ ] NENHUM equipamento vencido mencionado
- [ ] Certificados em anexo correspondem aos da secao XIII
- [ ] Calibrador removido (nao existe mais no kit)

### Quadro de setores e cargos
- [ ] Setores correspondem a realidade do cliente
- [ ] Cargos correspondem a lista de funcionarios
- [ ] Numero de funcionarios correto

### Cronograma de acoes
- [ ] Referencias cruzadas corretas (secao XXVIII = Glossario, nao psicossocial)
- [ ] Datas coerentes (nao anteriores a elaboracao)
- [ ] Responsaveis nomeados

### LTCAT
- [ ] Dados de medicoes coerentes com instrumentacao
- [ ] Limites de tolerancia corretos (NR-15, NBR 5413)
- [ ] Conclusoes condizentes com medicoes

### Indice e paginacao
- [ ] Paginas do INDICE correspondem ao conteudo
- [ ] Ordem: Encerramento antes de LTCAT (ou vice-versa, conforme padrao)

### Footer e revisao
- [ ] Numero da revisao correto no footer
- [ ] Numero da revisao mencionado no corpo

### Glossario
- [ ] Termos atualizados (sem "EIRELI" para empresas LTDA)
- [ ] Definicoes corretas

## Classificacao de severidade

| Severidade | Descricao | Exemplo |
|---|---|---|
| CRITICO | Dado incorreto que invalida o documento legalmente | CNPJ errado, equipamento vencido |
| MEDIO | Inconsistencia que precisa correcao mas nao invalida | Referencia cruzada errada, formato de nome |
| BAIXO | Detalhe estetico ou menor | Pronome Sr/Sra, termo obsoleto |

## Workflow de auditoria

1. Extrair texto dos dois documentos (ou do unico)
2. Comparar secao por secao seguindo o checklist
3. Para cada inconsistencia:
   - Classificar severidade
   - Indicar localizacao exata (secao, linha)
   - Descrever o que esta e o que deveria ser
   - Sugerir correcao
4. Gerar relatorio com total por severidade
5. Opcionalmente corrigir automaticamente (com confirmacao)

## Formato do relatorio

```
RELATORIO DE AUDITORIA SST
Documento auditado: [nome]
Data: [data]
Auditor: Claude (Roque Engenharia)

RESUMO: X criticos | Y medios | Z baixos

[Tabela detalhada com cada inconsistencia]
```
