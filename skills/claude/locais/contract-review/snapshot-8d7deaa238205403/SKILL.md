---
name: contract-review
description: >
  Revisão leve de contratos para a Casa Roque, sob lei brasileira (CDC, Código
  Civil, CLT, Lei de Locação 8.245/91), sem advogado na equipe. Lê o contrato de
  arquivo local, anexo do Gmail ou da plataforma de assinatura eletrônica
  (Gov.br/Clicksign/D4Sign/ZapSign); sinaliza cláusulas fora do padrão; explica o
  risco em português claro; e gera um redline (marcação de revisão) em DOCX
  separado. Casos típicos: fornecedor de espuma/tecido, agência de marketing,
  prestação de serviço, importação, locação do barracão. Use quando o JhEY disser
  "revisa esse contrato", "o que eu tô assinando", "tem alguma pegadinha",
  "sinaliza o que for arriscado", "confere o prazo de pagamento", ou anexar/
  encaminhar um contrato ou documento jurídico.
---

# Revisão de contrato (Casa Roque)

> **Status:** rascunho MVP · **Dono:** JhEY · **Versão:** 1.1.0
> **Categoria:** Jurídico & Ops

## Início rápido

Anexe o arquivo do contrato, encaminhe o e-mail com ele, ou cole o texto direto.

```
JhEY: "Revisa esse contrato do fornecedor de espuma e me fala o que eu devo
       contestar antes de assinar."
→ A skill lê o documento, identifica as partes e o tipo de contrato,
  analisa 8 categorias de risco, devolve um resumo por nível de severidade
  com um roteiro de negociação, e exporta um DOCX com redline.
```

> Esta skill **não é parecer jurídico**. Para qualquer cláusula 🔴 ou decisão que
> obrigue a Casa Roque, **validar com advogado/contador antes de assinar**.

## Fluxo

1. **Obter o contrato** — De uma destas três fontes, nesta ordem de preferência:
   - **Gmail**: buscar e-mails recentes com contrato anexado (ver `reference/gmail-fetch.md`)
   - **Assinatura eletrônica (Gov.br/Clicksign/D4Sign/ZapSign)**: baixar o PDF do
     documento pendente de assinatura ou já assinado (ver `reference/docusign-fetch.md`).
     Não há conector — é via download manual/anexo.
   - **Arquivo local ou texto colado**: ler o PDF (em blocos pelo parâmetro `pages`
     para arquivos com 10+ páginas) ou o DOCX pela ferramenta Read. Se o JhEY colar
     o texto direto, trabalhe com o que veio.

   Leia o documento inteiro antes de analisar. Cláusulas perigosas costumam estar nos
   anexos e tabelas do fim (anexo de preços, foro, multa).

2. **Identificar tipo de contrato e partes** — Determine o tipo (fornecimento/
   compra, prestação de serviço, agência/marketing, importação, locação do barracão,
   NDA/confidencialidade) e qual parte é a Casa Roque vs. a contraparte. Anote se for
   minuta-padrão da contraparte — costuma ser unilateral, e a contraparte espera
   contestação.

3. **Analisar 8 categorias de risco** — Trabalhe o contrato pela ótica de ops/
   financeiro de um pequeno empresário sem jurídico interno. As categorias estão
   ordenadas por severidade típica; use bom senso conforme o contexto.

   **Categoria 1: Pagamento e fluxo de caixa**
   - Prazo de pagamento: à vista / 28 dias é comum; 60+ dias merece sinalização; 90/120
     dias é ponto de negociação dura
   - Gatilho de pagamento: prazos de "aceite" que deixam a contraparte empurrar a
     aprovação indefinidamente
   - Multa/juros por atraso: a ausência é uma lacuna que vale anotar (Código Civil
     permite correção + juros + multa de até 2% sobre a dívida)
   - Exigências de faturamento/NF-e: formatos rígidos ou número de pedido que travam o
     pagamento por tecnicalidade
   - Reembolso de despesas: necessidade de aprovação prévia e tetos
   - Reajuste: índice (IPCA/IGP-M) e periodicidade (mínimo legal: anual) em contratos
     de prazo longo — ver `reference/gotchas.md`

   **Categoria 2: Responsabilidade e indenização**
   - Teto de responsabilidade: responsabilidade ilimitada é sempre bandeira vermelha
   - Indenização mútua x unilateral
   - Abrangência da indenização: "por toda e qualquer reclamação decorrente dos
     serviços" não é padrão
   - Exigências de seguro/garantia: viabilidade dos limites pedidos
   - Renúncia a danos indiretos/lucros cessantes: ausência = sinalizar com destaque

   **Categoria 3: Rescisão e saída**
   - Rescisão imotivada (denúncia): é mútua? Aviso prévio de 30 dias é típico
   - Multa rescisória: valor e proporcionalidade (ver `reference/gotchas.md`)
   - Rescisão por justa causa: prazo de cura; "infração relevante" vaga sem definição
   - Encerramento: pagamento do que está em andamento na rescisão
   - Sobrevivência de cláusulas: confidencialidade/indenização eternas = sinalizar

   **Categoria 4: Propriedade intelectual / criação**
   - Cessão de direitos x licença (relevante em contrato com agência: artes, vídeos,
     campanhas, conta de anúncios)
   - Ressalva de material preexistente — a ausência pode ceder por engano o que a Casa
     Roque já tinha
   - Amplitude da "obra/entregável": rascunhos, banco de criativos, acessos

   **Categoria 5: Escopo e mudança**
   - Clareza na definição do escopo
   - Processo de aditivo/mudança de escopo: ausência = escopo inchando sem pagamento
   - Critério de aceite: subjetivo ("a critério do contratante") x definido
   - Assimetria de prazo: a Casa Roque é penalizada por atraso, mas a contraparte não
     é por demora em aprovar

   **Categoria 6: Exclusividade e não concorrência**
   - Abrangência da exclusividade exigida da Casa Roque (ex.: agência que proíbe
     trabalhar com concorrente; fornecedor que exige compra mínima)
   - Definição de "concorrente" e duração
   - Não aliciamento de equipe: razoável; restrição ampla de mercado não é

   **Categoria 7: Confidencialidade e dados (LGPD)**
   - Abrangência: "toda informação compartilhada" sem exceções é ampla demais
   - Duração: 2–3 anos é típico; perpétua é agressiva
   - Tratamento de dados pessoais de clientes: a Casa Roque é controladora; conferir se
     o contrato tem cláusula de LGPD compatível com o porte e a sensibilidade do dado
   - Devolução/destruição após o fim do contrato

   **Categoria 8: Operacional**
   - Foro e resolução de conflitos; arbitragem obrigatória (cara para PME — sinalizar);
     foro distante de Limeira/SP
   - Renovação automática: janela e prazo de aviso para não renovar (perder uma janela
     de 60/90 dias é erro comum)
   - Cessão do contrato a terceiros, sobretudo se a contraparte for adquirida
   - Compra/volume mínimo e penalidade por não atingir
   - Direito de auditoria: abrangência e frequência

4. **Apresentar o resumo sinalizado** — Organize por severidade:

   **🔴 Bandeiras vermelhas (contestar antes de assinar)** — Para cada uma: cite a
   cláusula exata, explique o problema em linguagem simples, sugira redação alternativa
   específica.

   **🟡 Bandeiras amarelas (negociar, não impeditivas)** — Para cada uma: cite a
   cláusula, explique a preocupação, descreva como ficaria "melhor".

   **🟢 Pontos a observar (só ciência)** — Datas de pagamento, prazos de aviso, datas de
   renovação, exigências de seguro/garantia, contatos-chave.

   **📋 Resumo do contrato** — Em linguagem simples: quem faz o quê, por quanto, em que
   prazo, sob quais condições.

   **💡 Roteiro de negociação** — Para cada bandeira vermelha e amarela: o que pedir,
   como enquadrar o pedido, e como seria um meio-termo razoável.

5. **Exportar DOCX com redline** — Após apresentar o resumo, ofereça exportar um DOCX
   com as mudanças sugeridas em marcação de revisão. Use a skill `docx` para gerar um
   documento Word que:
   - Preserve a estrutura do contrato original
   - Marque exclusões sugeridas em tachado e inclusões em sublinhado
   - Inclua uma capa resumindo as mudanças

   Pergunte: "Quer que eu exporte um DOCX com redline pra você devolver à contraparte?"

## Approval gates

- Nunca trate a saída como parecer jurídico. **Sempre** recomende revisão de advogado/
  contador para bandeiras vermelhas ou decisões que obriguem a empresa, e o aviso:
  "Isto não é parecer jurídico — valide com advogado/contabilidade antes de assinar."
- Cite o texto real da cláusula, não paráfrase. O JhEY precisa do texto exato para a
  negociação.
- Sinalize o que **falta**, não só o que está escrito. Um contrato silencioso sobre
  teto de responsabilidade, multa ou reajuste costuma ser mais perigoso que um com
  termo desfavorável — a lei (Código Civil/CDC) preenche a lacuna, em geral a favor da
  contraparte.
- Não sinalize boilerplate padrão. Se a cláusula é justa e de mercado, pule. O JhEY quer
  sinal, não um recontar cláusula por cláusula.
- Compare com a norma de mercado ao sinalizar: "Pagamento em 90 dias é incomum em
  prestação de serviço — 28/30 dias é o usual."
- Ajuste a recomendação à relação de força. A minuta de compras de uma grande indústria
  de espuma é uma negociação diferente da de um pequeno fornecedor local.
- **Nunca envie o DOCX com redline à contraparte sem confirmação explícita do JhEY.**

## Conectores

**Sem conector de assinatura eletrônica.** Gov.br, Clicksign, D4Sign ou ZapSign
[confirmar qual o JhEY usa] entram via download do PDF / anexo. **Gmail** (anexos) e
**Google Drive** são os conectores ativos; use-os para localizar o arquivo. Detalhes em
`reference/docusign-fetch.md` e `reference/gmail-fetch.md`.

## Arquivos de referência

- `reference/gotchas.md` — pegadinhas BR (multa rescisória, foro, reajuste IGP-M/IPCA,
  exclusividade, CDC, boilerplate)
- `reference/docusign-fetch.md` — obter o contrato da assinatura eletrônica BR (sem conector)
- `reference/gmail-fetch.md` — achar o contrato anexado no Gmail
- `reference/examples/flagged-summary-saas.md` — exemplo trabalhado: revisão de contrato
  de agência de marketing
