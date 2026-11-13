---
name: review-contract
description: Revisa um contrato em português claro, sob lei brasileira (CDC, Código Civil, CLT, Lei de Locação), sinaliza bandeiras de risco com nível de severidade, e produz um DOCX/PDF com redline (marcação de revisão) para o JhEY usar na negociação. Aceita caminho de arquivo opcional ou o PDF baixado da plataforma de assinatura.
allowed-tools: Read, WebFetch, Bash
---

Rode a revisão de contrato. Leia o documento, explique o que ele diz, sinalize o que for
arriscado e produza um redline para o JhEY usar na negociação.

Interprete o argumento:
- `CAMINHO_DO_ARQUIVO` — caminho de um PDF/DOCX local, ou o PDF baixado da plataforma de
  assinatura eletrônica (Gov.br/Clicksign/D4Sign/ZapSign). Se omitido, peça o arquivo.

## Passo 1 — Carregar o contrato

Usando o fluxo da skill `contract-review`:

1. Se vier um caminho de arquivo: leia o documento do Drive/Desktop/anexo.
2. Se vier o PDF da assinatura eletrônica: leia o PDF baixado (sem conector — é manual).
3. Se não vier nada: peça ao JhEY o PDF/DOCX (anexo do Gmail, arquivo, ou texto colado)
   antes de prosseguir. Leia o documento inteiro, incluindo anexos do fim.

## Passo 2 — Resumo em português claro

Produza um resumo de 3 parágrafos:
1. **O que esse contrato faz** — o negócio em termos simples (quem, o quê, quanto, prazo)
2. **Principais obrigações** — o que a Casa Roque tem que fazer e quando
3. **Principais direitos** — o que a Casa Roque recebe e quais as saídas/rescisão

## Passo 3 — Lista de bandeiras

Para cada risco, classifique a severidade: 🔴 Alta / 🟡 Média / 🟢 Baixa

Sinalize no mínimo:
- Renovação automática com janela curta de cancelamento
- Reajuste/preço alterável unilateralmente ou sem índice (IPCA/IGP-M)
- Multa rescisória desproporcional (ver `contract-review/reference/gotchas.md`)
- Cessão ampla de propriedade intelectual / ativos (ex.: conta de anúncios, artes)
- Responsabilidade ilimitada ou sem teto
- Exclusividade
- Foro distante de Limeira/SP ou arbitragem obrigatória
- Pagamento ou entregáveis ambíguos

Formate cada bandeira como:
```
{Severidade} {Nome da cláusula} — {o que ela diz em português claro} — Redline sugerido: {ajuste}
```

## Passo 4 — Redline

Gere uma lista de sugestões específicas em formato de marcação jurídica:
```
Cláusula {número}: EXCLUIR "[texto original]" / INSERIR "[texto sugerido]"
Motivo: {uma frase}
```

Ofereça exportar como DOCX (ou PDF) com redline, para o Drive/Desktop.

## Falha de conector

Não há conector de assinatura eletrônica. Se nenhum arquivo for informado, peça ao JhEY
o PDF/DOCX (anexo do Gmail, arquivo local, ou texto colado). Esta skill funciona 100%
offline com um arquivo local.

## Approval gates

- **Nunca assine, envie ou altere o documento na plataforma de assinatura.** Apresente a
  revisão e espere o JhEY agir.
- **Sempre avise:** "Isto não é parecer jurídico — valide com advogado/contabilidade
  antes de assinar."
- **Nunca apague nem sobrescreva o documento original.**

## Saída

Apresente o resumo em português claro, a lista de bandeiras e o redline. Pergunte ao JhEY
se deve exportar uma cópia com redline e onde salvar.
