---
name: casa-roque-site-seo
description: Auditar e melhorar a loja Casa Roque em Nuvemshop, Locaweb e ferramentas Google, mantendo registro verificável de SEO, indexação, Merchant, GA4 e Ads.
---

# SEO do site Casa Roque

Use esta skill quando a tarefa for continuar a auditoria ou correção do site `csroque.com.br` e suas integrações Google. A pasta `seo site` da Casa Roque no OneDrive contém o relatório de execução e os dados de 14/10/2026. Esses dados são uma linha de base datada; releia o painel atual antes de agir.

## Onde está o material

- `relatorio-completo-seo-casa-roque-2026-10-14.docx`: histórico, decisões e roteiro em linguagem simples.
- `Relatorios e planilhas/`: diagnósticos e planilhas de trabalho.
- `Exportacoes Nuvemshop/`: sete snapshots do catálogo. O CSV usa Windows 1252 e separador `;`. A última exportação é a que termina em `17919986991865443121653859280.csv`.
- `Dados de apoio/`: registro da revisão MPN.

## Método de continuidade

1. Antes de qualquer alteração, inspecione o painel atual da Nuvemshop e a página pública com `www`. Não trate o número datado de um relatório como estado atual.
2. Separe os quatro problemas: indexação orgânica no Search Console, acesso HTTPS ao domínio sem `www`, aprovação de produtos no Merchant Center e medição de conversões no GA4/Ads. Um resultado de um sistema não prova o outro.
3. Para produto ou categoria, confira nome, foto, descrição, SKU, variações e URL antes de escrever título/descrição SEO. Salve, recarregue o cadastro, confira a página pública e registre uma nova exportação quando editar um grupo.
4. Na Locaweb, preserve os registros de e-mail Zoho/SPF. Em 14/10/2026 os registros A da raiz já apontavam para `185.133.35.21` e `185.133.35.22`, e o `www` era CNAME para a Nuvemshop. TXT não é a causa demonstrada da falha SSL.
5. O domínio `csroque.com.br` sem `www` ainda precisa de vinculação na Nuvemshop. Houve bloqueio de revisão automática por possível impacto em DNS/SSL; a aprovação específica do usuário está pendente. Não publique essa alteração por inferência. Depois de autorizada, mantenha `www` como principal e verifique HTTPS, redirecionamento e `robots.txt` antes de mexer no Merchant.
6. No Merchant Center, não solicite revisão do alerta de página de destino enquanto o acesso público falhar. Após corrigir o domínio, teste amostras de produto, preço, estoque e frete, alinhe o site reivindicado e só então peça revisão.
7. Alegações sobre refluxo e sono de bebês exigem revisão pelo responsável técnico antes de publicação. Não prometa segurança clínica em títulos ou textos SEO. Veja `Relatorios e planilhas/revisao-sono-seguro-casa-roque.md`.
8. Não altere GTIN/MPN/SKU sem conferir embalagens, fabricante e integração de estoque. Não consolide cadastros parecidos sem revisar fotos, estoque e histórico de pedidos.
9. Diferencie fato confirmado, hipótese e pendência. Registre em cada relatório a data, a tela ou arquivo de origem, a ação efetuada e como foi verificada.

## Ferramentas usadas nesta auditoria

- Nuvemshop: `https://casaroque.lojavirtualnuvem.com.br/admin/products` e `https://casaroque.lojavirtualnuvem.com.br/admin/settings/domains/list`.
- Site público: `https://www.csroque.com.br/`.
- Search Console: `https://search.google.com/search-console?resource_id=sc-domain%3Acsroque.com.br`.
- Merchant Center: `https://merchants.google.com/mc/settings/website?a=119410901`.
- Google Analytics: `https://analytics.google.com/`.
- Google Tag Manager: `https://tagmanager.google.com/`.
- Google Ads: `https://ads.google.com/`.
- Perfil da Empresa: `https://business.google.com/`.
- PageSpeed Insights: `https://pagespeed.web.dev/`.

Para operar páginas autenticadas no Chrome desta tarefa, use a ferramenta de navegador disponível no ambiente atual e confirme a conta/perfil antes de editar. Para relatórios Word, siga a skill de documentos e verifique a renderização quando o ambiente permitir.
