# Pegadinhas — customer-pulse

## Pegadinha: estimar a nota de avaliação quando não veio print

**Por que importa:** a Casa Roque não tem conector de ML/Shopee. A nota (★) e o volume de avaliações dependem de print/export. Chutar "deve estar uns 4,5" gera um número falso num indicador que o JhEY usa pra meta (5,0★).

### ✗ Errado
> A média deve estar por volta de 4,6★ neste mês.

### ✓ Certo
Sem print na primeira rodada: registre `Avaliações ML/Shopee: n/d — sem print` na seção Fontes e na seção "Avaliação x meta". Ofereça uma vez: "me manda o print das avaliações do ML e da Shopee que eu calculo a média vs a meta 5,0★." Não insista.

---

## Pegadinha: citação literal parafraseada ou resumida

**Por que importa:** o JhEY precisa ver a palavra real do cliente — não a interpretação do Claude. Paráfrase destrói a credibilidade do relatório e esconde o tom (irritação, elogio).

### ✗ Errado
**Tema: Atraso na entrega** (8 sinais)
> Os clientes relataram que as entregas chegaram depois do esperado.

### ✓ Certo
**Tema: Atraso na entrega** (8 sinais)
> "Comprei com prazo pro Dia das Mães e chegou 4 dias depois. Frustrante." — [ML]
> "Pedido atrasou e ninguém respondia." — [WhatsApp]

---

## Pegadinha: tratar amostra pequena como tendência

**Por que importa:** com poucas avaliações na semana, uma única nota 1★ derruba a média e parece "crise". Enxoval/bebê é sazonal — o volume oscila muito (Dia das Mães, Black Friday, Natal). Reportar "queda na satisfação" com base em 3 avaliações engana o JhEY.

### ✗ Errado
> Satisfação despencou: média 3,3★ esta semana (de 5,0).

### ✓ Certo
> 3 avaliações esta semana (amostra pequena): duas 5★ e uma 1★ (atraso). A 1★ puxou a média pra 3,7★, mas com n=3 não dá pra ler como tendência. Vale resolver o caso de atraso e reavaliar com mais volume.

Sempre mostre o tamanho da amostra ao lado da nota. Com n baixo, sinalize que não é tendência.

---

## Pegadinha: tratar mediação do Mercado Livre como reclamação comum

**Por que importa:** quando o cliente abre **mediação** no ML, a plataforma entra no meio e o caso afeta a reputação do vendedor (taxa de reclamações, MercadoLíder). É mais grave que um SAC normal e tem prazo da plataforma pra responder. Misturar mediação no balaio das reclamações comuns esconde a urgência.

### ✗ Errado
> 5 reclamações neste mês (juntando SAC, WhatsApp e mediação do ML no mesmo número).

### ✓ Certo
> 3 conversas de SAC + 2 **mediações abertas no ML** (estas afetam a reputação do vendedor e têm prazo da plataforma — priorizar). Detalhe as mediações separado e, se precisar responder/resolver, encaminhe pra `handle-complaint` (que tem o portão de aprovação).

Mediação é sempre destacada à parte. Esta skill só diagnostica — tratativa e resposta passam por aprovação na `handle-complaint`/`ticket-deflector`.

---

## Pegadinha: marketplace sem conector tratado como "cliente sem feedback"

**Por que importa:** se a skill pula avaliações, mediações e Reclame Aqui em silêncio só porque não veio print, o JhEY acha que não há feedback — quando, na real, é só falta de export. As fontes existem; faltou anexar.

### ✗ Errado
> Sem dados de avaliação. Relatório só com Gmail.

### ✓ Certo
> Fontes puxadas: Avaliações ML/Shopee `n/d — sem print`; Reclame Aqui `n/d — sem print`; Gmail 9; SAC WhatsApp (prints) 7. Oferta única: "me manda os prints das avaliações do ML/Shopee e do Reclame Aqui que eu fecho o pulso completo." Entrega o resto normalmente.

A lacuna fica explícita e o JhEY decide se manda os prints ou segue com o pulso parcial.
