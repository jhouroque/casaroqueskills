# Assinatura eletrônica BR: obter o contrato para revisão

No Brasil a Casa Roque usa assinatura eletrônica via **Gov.br, Clicksign, D4Sign ou
ZapSign** [confirmar qual o JhEY usa]. **Nenhuma delas tem conector/MCP neste plugin** —
o documento entra por **download manual ou anexo de e-mail**, não por API.

## Como obter o PDF

1. **Peça ou baixe o PDF do contrato.** O JhEY abre a plataforma (Gov.br, Clicksign,
   D4Sign ou ZapSign), localiza o documento (pendente de assinatura ou já assinado) e
   baixa o PDF. Diga:

   ```
   "Baixa o PDF do contrato na plataforma de assinatura (Gov.br/Clicksign/D4Sign/
   ZapSign) e me anexa aqui — ou encaminha o e-mail com o anexo."
   ```

2. **Leia o PDF baixado** pela ferramenta Read. Para 10+ páginas, leia em blocos pelo
   parâmetro `pages` (ver `gotchas.md` da skill — termos perigosos costumam estar nos
   anexos do fim).

3. Se o documento chegou por e-mail, use o caminho de `gmail-fetch.md` para localizar o
   anexo.

## O que NÃO fazer

- **Não assine, não clique em "assinar"/"concluir", não avance o documento** em nenhuma
  plataforma. Esta skill é **só de revisão**.
- Não altere o documento na plataforma.
- Não inicie um novo envio/envelope de assinatura.

## Fallback

Se o JhEY não tiver o PDF em mãos:

```
"Sem o arquivo eu não reviso. Me manda o PDF do contrato (baixado da plataforma de
assinatura), o anexo do e-mail, ou cola o texto direto aqui."
```
