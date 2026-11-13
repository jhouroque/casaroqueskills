---
name: "venda-whatsapp-nf-boleto"
description: "Roteiro para emitir NF-e no Bling e boletos 30/60 no Inter da Casa Roque, com envio por Correios PAC e mensagem final ao cliente no WhatsApp, para pedidos B2B."
---

# Venda WhatsApp: NF-e (Bling) + boleto (Inter) + Correios PAC + mensagem ao cliente

Use quando o Jhonatas passar um pedido de cliente PJ do WhatsApp (dados da cliente, peças, valores, caixas) para faturar em boleto 30/60 e enviar por Correios. Emitente: Casa Roque (CNPJ 28.549.320/0001-14), NF série 1. Responda em pt-BR, direto, sem enrolar.

## Regras de segurança (inegociáveis)
- Bling, Inter e WhatsApp Business são contas sensíveis. Só aja com pedido explícito do Jhonatas no chat para esta venda.
- Nunca digite senha, token ou código de verificação. Se o login aparecer, peça para ele clicar em Entrar/autenticar e avisar. Não use credenciais preenchidas pelo navegador.
- Emissão de boleto e transmissão da NF-e são irreversíveis. Prepare tudo e peça ok final, a menos que ele já tenha dito 'emite'/'termina a nota'. Quando ele pedir 'até eu finalizar', salve a NF como Pendente e deixe a transmissão com ele.
- Subagentes são bloqueados pelo sistema de permissões para clicar em emissão; faça a emissão você mesmo, no chat, depois da autorização dele.
- Mensagem ao cliente no WhatsApp Web (aba já aberta no navegador dele): só envie se ele disser 'manda a msg'. Sem essa ordem, entregue o texto pronto para copiar. E-mail em nome dele só com autorização explícita.
- Não altere a resposta rápida salva 'codrastreio' do WhatsApp sem pedido explícito.

## Antes de começar
1. Chrome: use o navegador do perfil `jhouroque` (browser 'pc jhou escritorio'; ele pode ter vários navegadores conectados). Se não souber qual é, use switch_browser para ele escolher na tela. Aba nova para Bling e outra para Inter. A extensão desconecta às vezes: reconecte com switch_browser.
2. Confira dados que costumam divergir: endereço/CEP da mensagem x cadastro (pergunte qual vale), IE da cliente, e-mail, soma dos itens = total informado, quem paga o frete (o total geralmente não inclui frete).
3. Datas: hoje + 30 e + 60 dias em data fixa (ex.: 05/11 e 05/12). Avise se cair em fim de semana. O Bling calcula 30/60 dias exatos e a data pode sair um dia antes: corrija manualmente para bater com os boletos.
4. Valores: divida o total em 2 parcelas iguais (arredonde na 2ª se necessário).
5. Páginas do Bling são pesadas: screenshots podem dar timeout; espere/recarregue e use find/form_input por referência em vez de coordenadas.

## Bling: cadastro da cliente
Contatos: buscar por nome parcial (a busca por CNPJ formatado falha). Se não existir, criar: Pessoa Jurídica, razão social em maiúsculas, CNPJ, IE, contribuinte 1 - ICMS, CEP (clicar na lupa para preencher rua/bairro/cidade), número, e-mail (e e-mail para NF-e). O Bling pode demorar a achar a cliente recém-salva; digite só o primeiro nome + Seta p/ baixo + Enter.

## Bling: NF-e (Notas Fiscais, Incluir nota fiscal)
Fazer direto na NF de saída (série 1) é mais estável que passar pelo pedido de venda.
- Item único, a pedido do Jhonatas: descrição `ESPUMAS PARA ARTESANATO`, UN, quantidade 10, preço unitário = total/10 (3 casas, ex.: 202,544), total da nota = total do pedido. Código do produto não importa. As peças reais (qtd, unitário, total de cada uma) vão em Informações complementares.
- No item (lápis/janela): NCM 3909.50.29 (digitar sem pontos, informado pelo Jhonatas), CFOP 6101 (produção própria; 6102 só se for revenda; venda SP→BA é interestadual), aba ICMS: CSOSN 102 - Tributada sem permissão de crédito (o padrão veio 400 e está errado), aba IPI: 99 - Outras saídas, sem alíquota (Simples).
- Use form_input por referência para campos em janelas modais; coordenadas mudam quando a janela redimensiona.
- Pagamento: Condição `30 60` → Gerar parcelas → ajustar as datas e conferir o valor de cada parcela.
- Transporte: 'Transporte com logística cadastrada', integração `sigep`; ele preenche sozinho o serviço `PAC CONTRATO AG - PORTAL DE LIMEIRA` e a transportadora Portal de Limeira. Frete por conta: 0 - Remetente (CIF), salvo indicação contrária. Adicionar um objeto de postagem por caixa e, no ícone do caminhão de cada um, informar peso e Largura/Altura/Comprimento; Salvar em cada volume. CEP de origem 13.482-017. Não precisa de 'Obter cotação' para a NF. As etiquetas (DANFE Simplificado - Etiqueta, contrato 9912427155) saem depois da emissão, com um código de rastreio por volume.
- Volumes: quantidade = nº de caixas, peso bruto = soma, espécie Caixa(s).
- Informações complementares: lista das peças com unitário e total, total, condição de pagamento com datas, e as caixas (peso e medidas).
- Salvar: a NF fica Pendente. Transmitir só com o ok dele (ou se ele disser que já emite).
- Pontos a sinalizar: Consumidor final vem marcado; indicador de presença 2-Internet (para WhatsApp o mais correto é 9-outros); saldo de estoque do item pode estar negativo.

## Inter: boletos (conta CASAROQUE DECORACAO E ESPUMAS PARA ARTESANATO LTDA)
Cobrar ou Receber → Nova cobrança (um boleto por parcela; 'Parcelado' vem desabilitado, use 'Único').
1. Cliente: se não existir no Inter, 'Cadastrar cliente' (nome, CNPJ, e-mail, CEP preenche endereço, digitar número). Selecionar a cliente e Continuar.
2. Valor da parcela. Código de controle: máximo 12 caracteres, sem espaços (ex.: PARCELA-1-2). Descrição: 'Casa Roque - Venda de espumas - parcela 1/2'. Tipo Único.
3. Vencimento: digitar não funciona no campo; usar o calendário (navegar os meses com a seta).
4. Definições: multa 2% e juros 1% a.m., sem desconto (padrão: até 30 dias após o vencimento). Confira que as duas parcelas saíram com multa/mora: já houve boleto 2/2 sem o texto de multa e mora.
5. Revisão: o Pix cai na chave 28.549.320/0001-14 (CNPJ da Casa Roque). Emitir cobrança só com autorização. Baixar PDF depende de autorização; o Jhonatas costuma baixar e enviar à cliente.
6. Antes de repetir um boleto, confira em Gestão de Cobrança se já não foi emitido (ele pode estar avançando na tela ao mesmo tempo, e a tela de 'Cobrança emitida' pode ser dele).

## Mensagem ao cliente (modelo do Jhonatas, versão compacta usada em 05/10/2026)
Depois da NF autorizada, leia o PDF 'DANFE Simplificado - Etiqueta' (pdftotext): o código de rastreio de cada volume está abaixo de 'Volume: n/N' (formato AP 578 189 912 BR, escrever sem espaços), e confira o protocolo de autorização. Leia também os PDFs dos boletos para pegar vencimento e linha digitável. Se o Jhonatas já mandou o link da nota no chat, não repita. Modelo:

```
✨ Ótimas notícias! Seu pedido já está sendo embalado! ✨

🚚 Acompanhe sua entrega (N volumes):
Volume 1: *<código 1>*
Volume 2: *<código 2>*

Acompanhe em tempo real: https://www.melhorrastreio.com.br/

🌱 Embalagem a vácuo: deixe o produto "descansando" por 48h fora da embalagem e ele volta à forma original. Vídeo rápido: https://youtu.be/N-BL_PRtwUA

💳 Boletos (<n>x de R$ <valor>):
• 1/2 vence <data>: <linha digitável 1>
• 2/2 vence <data>: <linha digitável 2>

Se precisar de algo ou tiver qualquer dúvida, é só chamar! 📦
```

Envio no WhatsApp Web: Enter envia, então use shift+Enter para quebra de linha (ou monte linha a linha e clique no botão de enviar). Confira por screenshot antes e depois de enviar. Os PDFs dos boletos devem ser anexados (botão +); se os arquivos estiverem no computador dele e não acessíveis, peça para ele anexar. A versão longa original (com 'Estamos preparando seu pedido com muito carinho...' e explicação do vácuo) continua válida se ele preferir. Se ele pedir para mudar o tom ou o texto, ajuste o modelo e use a versão nova nas próximas vendas.

## Fechamento
- Confira os PDFs dos boletos (vencimento, valor, nº do documento, multa/mora, endereço do pagador).
- Vincular boletos às contas a receber da nota; mandar PDFs e DANFE/XML à cliente (WhatsApp e e-mail) só se ele pedir.
- Avisar quem embala (Miro/Emerson) com peso e medidas conferidos.
- Resumo final curto: nº da NF, status, valor, parcelas, volumes/peso, rastreios, pendências.

## Reutilizar em outras IAs
Esta sequência vira prompt para outro agente de navegador: dados da cliente, itens, parcelas e caixas em uma tabela, mais as regras acima. Para reduzir trabalho manual: integração Bling + Inter (boleto gerado direto do pedido) e Bling + Melhor Envio/Correios para etiquetas.