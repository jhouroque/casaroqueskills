# Modelo da operação — Importação por conta e ordem

## Base legal

**Instrução Normativa RFB nº 1.861/2018** (modalidades de importação no Brasil):

1. **Por conta própria** — importador compra, estoca e revende. Responde por tudo.
2. **Por conta e ordem de terceiros** ← **MODELO DA ROQUE** — trading importa em nome do adquirente final. DI em nome do adquirente.
3. **Por encomenda** — trading importa em nome próprio com encomendante predeterminado.

A Casa Roque (como articuladora via Roque Gestão) opera no modelo **(2) por conta e ordem**.

## Fluxo operacional completo

```
ETAPA 1 — NEGOCIAÇÃO (China)
    JhEY ↔ Yuki (Alibaba Messenger + email)
    → Cotação, PI (Proforma Invoice), condições, MOQ
    → Alibaba Trade Assurance Order aberta

ETAPA 2 — PAGAMENTO CHINA
    JhEY faz PIX em BRL → Ant International / Alipay
    → USD FOB é debitado na plataforma Alibaba
    → (pode ser 100%, 30/70, 20/80)

ETAPA 3 — PRODUÇÃO + EMBARQUE
    Yuki produz (30-45 dias típico)
    Yuki embarca no freight forwarder REACH (ou indicado pelo Osvaldo)
    Yuki envia invoice final + PL + BL (draft depois original)

ETAPA 4 — PRÉ-EMBARQUE / BL
    Osvaldo confirma BL, agência marítima
    Se BL Telex Released: carga liberada sem BL físico

ETAPA 5 — CHEGADA EM SANTOS
    Container chega no porto
    Osvaldo abre DI no SISCOMEX → em nome do ADQUIRENTE (Vizu Home/Decor/CasaWeber/Fabritex)
    Osvaldo solicita NUMERÁRIO ao JhEY (R$ estimado: impostos + frete + despacho)
    JhEY repassa pro cliente, cliente paga Osvaldo

ETAPA 6 — DESEMBARAÇO
    Osvaldo paga II/IPI/ICMS/PIS-Cofins/AFRMM/THC com o numerário
    Carga sai do porto → frete rodoviário → barracão do cliente

ETAPA 7 — NF DE ENTRADA
    Osvaldo pede emissão de NF entrada ao JhEY/cliente
    JhEY emite NF no Bling (pra cliente emite)

ETAPA 8 — FECHAMENTO FINAL
    Osvaldo reconcilia: numerário recebido vs. gastos reais
    Envia fatura 1000012XXX + saldo favorável (devolução) ou acréscimo
    Devolve saldo via PIX ao adquirente

ETAPA 9 — COMISSÃO 1%
    JhEY calcula: USD FOB × câmbio + numerário + complementos − devolução = TOTAL
    1% desse TOTAL → comissão Roque Engenharia
    Emite NFS-e → cobra cliente
```

## Por que esse modelo é seguro fiscalmente

- Receita Federal vê: adquirente (Mariane/cliente) importou DIRETO. Roque Gestão prestou serviço de consultoria/gestão.
- Tributação Roque: só **ISS** sobre os 1% (simples nacional anexo III/V, ~6-15%) — não paga PIS/Cofins/II/IPI/ICMS sobre a mercadoria.
- Tributação cliente: paga todos os impostos de importação (II/IPI/ICMS/PIS-Cofins) normal — tem crédito desses tributos se for CNPJ produtivo.

## O que formalizar (pendência)

1. **Contrato de serviço de gestão de comércio exterior** entre Roque Gestão e cada cliente (Mariane, CasaWeber, Fabritex).
2. **Registro SISCOMEX como "por conta e ordem"** — o cliente deve ter feito isso no momento do habilitação Radar.
3. **NFS-e modelo** com código de serviço:
   - 17.04 — Assessoria ou consultoria de qualquer natureza
   - 17.20 — Consultoria e assessoria econômica ou financeira
   - Ou código específico de comércio exterior da prefeitura

## Diferença entre Casa Roque e Roque Gestão

| Empresa | CNPJ | O que faz na operação |
|---|---|---|
| **Casa Roque Indústria e Comércio** | (CNPJ próprio) | **NADA nessa operação.** É a marca de varejo de persianas do JhEY. Vende no NuvemShop, Shopee, Mercado Livre. |
| **Roque Gestão & Engenharia Empresarial** | (CNPJ próprio) | **Articula e fatura 1%.** É a prestadora de serviço do JhEY. Também presta SST (Fabritex). |
| **Vizu Home / Vizu Decor** | 32.362.801/0001-93 · 34.877.749/0001-33 | **Adquirente legal.** DI em nome delas. Paga tudo. Mariane é a dona. |
| **Casaweber** | 31.826.903/0001-50 | Adquirente. Provavelmente parceiro do JhEY em enxovais. |
| **Fabritex** | 31.710.730/0001-00 | Adquirente. Cliente de tecidos. |
