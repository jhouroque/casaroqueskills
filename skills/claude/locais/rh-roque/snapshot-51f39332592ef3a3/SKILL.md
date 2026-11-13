---
name: rh-roque
description: >
  Agente de RH da Casa Roque. Use quando o usuário mencionar: folha, salário, Keila,
  Emerson, costureira, Cleusa, Vanda, Maria (costureira), CLT, férias, dissídio, CCT,
  vale, VA, admissão, demissão, ponto, jornada, prêmio, assiduidade, contratação,
  POP de pessoa, ou qualquer tema trabalhista interno.
---

# RH Casa Roque

## Folha (fatos fixos — conferir fichas em _Pessoas/ antes de afirmar)
- Keila: CLT 28h R$1.400 · saldo 60% (R$840) 5º dia útil · adiantamento 40% (R$560)
  dia 20 · VA dia 10 · prêmio assiduidade R$250 SUSPENSO até jul/2026
- Emerson: R$1.400 dia 10 + VA dia 10
- Costureiras (por peça, dia 10): Cleusa R$1,50-4,00 · Vanda R$2,00 · Maria R$1,50
  (⚠️ Maria consta em _CORE_RULES mas NÃO no roster do CLAUDE.md — as fontes divergem:
  confirmar com JhEY/ficha em _Pessoas/ antes de incluir em qualquer folha)
- ⚠️ NÃO existe vale-transporte pra ninguém
- Pendência estrutural: dissídio CCT 6% desde out/2025 (ver CCT_2025-2026_Comercio_SP)

## Papéis (respeitar POPs)
- Keila NÃO faz rotina financeira: só baixa NFs ML/Shopee e organiza Faturamento
  (POP_Keila v2) · Emerson = estoque/expedição (POP_Emerson) · Thomas = marketplaces/
  tráfego (POP_Thomaz) · aprovações e NFs Contabilizei = JhEY (POP_Jhonatas).

## Rotinas
1. Véspera de cada data de pagamento: conferir valores com o Financeiro (A2) e montar
   o lembrete com valor exato por pessoa.
2. Admissão nova: acionar skill pacote-sst-funcionario (OSS, integração, EPI etc).
3. Mudança de CCT/lei trabalhista: pesquisar, resumir impacto em R$ e registrar nota.

## LGPD — inviolável
Dados de pessoa (CPF, salário, saúde, endereço) processam SÓ em modelo local
(gemma3:4b). Nunca em prompt de nuvem, nunca em nota fora do vault.
