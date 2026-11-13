---
name: art-creanet
description: >
  Prepara todos os dados para emissao de ART (Anotacao de Responsabilidade Tecnica) no
  sistema CreaNet do CREA-SP. Use SEMPRE que o usuario mencionar: ART, anotacao de
  responsabilidade, CREA, CreaNet, emitir ART, registrar ART, boleto CREA, responsabilidade
  tecnica, ou qualquer referencia a registro profissional de engenharia para servicos SST.
  Ative tambem quando um PGR for finalizado e o proximo passo natural for emitir a ART.
---

# ART CreaNet — Roque Gestao & Engenharia

Voce prepara todos os dados necessarios para emissao de ART de Obra ou Servico no
sistema CreaNet (CREA-SP), gerando um roteiro completo com campos pre-preenchidos
prontos para copiar e colar.

## Dados do profissional (fixos)

| Campo | Valor |
|---|---|
| Nome | JHONATAS ROQUE DE SOUZA |
| Titulo | Engenheiro Mecanico, Engenheiro de Seguranca do Trabalho |
| RNP | 2623224978 |
| CREA-SP | 5071626112-SP |
| CPF | 397.684.448-94 |
| Empresa Contratada | (em branco — autonomo) |

## Estrutura da ART (Resolucao 1.025/2009 - Anexo I - Modelo A)

A ART de Obra ou Servico tem 6 secoes:

### 1. Responsavel Tecnico
Dados pre-carregados pelo sistema ao fazer login.

### 2. Dados do Contrato
- Contratante: razao social do cliente
- CPF/CNPJ: digitar CNPJ → sistema puxa razao social
- Endereco completo do cliente
- Data do contrato (celebrado em)
- Valor do servico em R$
- Tipo: Pessoa Juridica de Direito Privado
- Vinculada a Art n.: deixar em branco (salvo se complementar ART anterior)

### 3. Dados da Obra/Servico
- Mesmo endereco do contratante (para servicos SST in loco)
- Data de inicio e previsao de termino
- Finalidade: Comercial / Industrial / Residencial (conforme CNAE)
- Proprietario: socio-administrador do cliente
- CPF/CNPJ: mesmo da empresa

### 4. Atividade Tecnica
- Tipo: Elaboracao
- Codigo: 1
- Descricao: Laudo de conformidade tecnica em seguranca do trabalho
- Quantidade: 1,00000
- Unidade: unidade

### 5. Observacoes
Texto padrao (adaptar por cliente):

```
Elaboracao de Programa de Gerenciamento de Riscos (PGR) com Laudo Tecnico das
Condicoes Ambientais do Trabalho (LTCAT) integrado [e Avaliacao de Riscos
Psicossociais (COPSOQ-BR) se aplicavel], conforme NR-1 (Portaria SEPRT n.
6.730/2020[, atualizada pela Portaria MTE n. 1.419/2024]) e art. 58 da Lei
n. 8.213/1991, para a empresa [RAZAO SOCIAL], [nome fantasia], CNPJ
[XX.XXX.XXX/XXXX-XX], Grau de Risco [X] (NR-4), CNAE [XX.XX-X/XX], com
[XX] ([extenso]) colaboradores, abrangendo os setores: [lista de setores].
Inclui: inventario de riscos ocupacionais, [avaliacao de riscos psicossociais
conforme NR-1 (risco geral X,XX - [CLASSIFICACAO], metodologia COPSOQ-BR),]
plano de acao com cronograma de implementacao de [XX] medidas de prevencao,
e classificacao dos Grupos de Exposicao Similar (GES). Documento ref.:
[NOME_ARQUIVO], datado de [DD/MM/AAAA].
```

### 6. Declaracoes
Acessibilidade: marcar que NAO se aplica (servicos SST nao envolvem obra civil).

## Workflow

1. Ler dados do cliente da pasta PERICIA E SST/02_CLIENTES/[CLIENTE]/
2. Ler CREA credentials de 01_EMPRESA/CREDENCIAIS/
3. Verificar se existe ART anterior na pasta 09_ART/
4. Gerar documento .docx com roteiro completo (tabelas campo-valor)
5. Incluir texto de observacoes pronto para copiar
6. Incluir passo a passo do CreaNet (11 passos)
7. Incluir comparativo com ART anterior se existir
8. Salvar na pasta 09_ART/ do cliente

## Valor da ART CREA-SP (referencia 2026): ~R$ 100,90

## Passo a passo CreaNet
1. Acessar https://www.creanet.crea-sp.org.br
2. Login com CPF e senha
3. Menu: ART > Registrar ART > ART de Obra ou Servico
4. Secao 1 ja carregada
5. Secao 2: digitar CNPJ
6. Completar endereco, valor, data
7. Secao 3: mesmo endereco, finalidade
8. Secao 4: Elaboracao > Laudo conformidade > 1 unidade
9. Secao 5: colar texto de observacoes
10. Secao 6: acessibilidade nao se aplica
11. Revisar > Confirmar > Gerar boleto > Pagar

Apos pagamento, salvar PDF da ART na pasta 09_ART/ do cliente.
