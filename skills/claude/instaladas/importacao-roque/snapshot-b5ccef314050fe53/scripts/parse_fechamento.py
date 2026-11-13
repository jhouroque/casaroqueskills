"""Extrai dados estruturados de um email de fechamento do Osvaldo.

Uso:
    from parse_fechamento import parse
    dados = parse(email_text)
    # → {"invoice": "ST25311A", "di": "26/0564654-7", "fatura": "1000013015",
    #    "total_enviado_rs": 58050.00, "saldo_devolvido_rs": 1095.02,
    #    "data_fechamento": "14/04/2026", "empresa": "Vizu Home"}
"""
import re

def parse(texto):
    t = texto.replace("\r", "").replace("\n", " ")
    d = {}

    # Invoice — ST seguido de 4-6 dígitos + letra opcional
    m = re.search(r"(?:invoice|ST)\s*(ST\s*)?(\d{4,6}[AaBb]?)", t, re.IGNORECASE)
    if m: d["invoice"] = ("ST" + m.group(2)).upper()

    # DI
    m = re.search(r"DI\s*(?:número|numero|nº)?\s*(\d{2}[/.]\d{6,7}[-/]?\d)", t, re.IGNORECASE)
    if m: d["di"] = m.group(1)

    # Fatura Osvaldo
    m = re.search(r"[Ff]atura\s+(?:número|numero)?\s*(\d{10})", t)
    if m: d["fatura_osvaldo"] = m.group(1)

    # Total enviado
    m = re.search(r"total\s+enviado\s+de\s+[Rr]\$\s*([\d.]+(?:,\d{2})?)", t, re.IGNORECASE)
    if m: d["total_enviado_rs"] = _to_float(m.group(1))

    # Saldo favorável
    m = re.search(r"saldo\s+favorável\s+(?:para\s+a\s+\w+\s+)?(?:no\s+valor\s+)?de\s+[Rr]\$\s*([\d.]+(?:,\d{2})?)", t, re.IGNORECASE)
    if m: d["saldo_devolvido_rs"] = _to_float(m.group(1))

    # Data do fechamento (DD.MM.YYYY ou DD/MM/YYYY)
    m = re.search(r"(\d{2})[/.](\d{2})[/.](20\d{2})", t)
    if m: d["data_fechamento"] = f"{m.group(1)}/{m.group(2)}/{m.group(3)}"

    # Empresa
    for emp in ["Vizu Home", "Vizu Decor", "Casaweber", "Casa Weber", "Fabritex", "Mariane"]:
        if emp.lower() in t.lower():
            d["empresa"] = emp
            break

    # Navio
    m = re.search(r"(?:Navio|vessel|embarque no Navio)\s+([\w\s]+?)(?:,|\.|\s+fornecedor|\s+com|\s+invoice|\s*$)", t, re.IGNORECASE)
    if m: d["navio"] = m.group(1).strip()[:30]

    return d

def _to_float(s):
    return float(s.replace(".", "").replace(",", "."))

if __name__ == "__main__":
    exemplo = """Bom dia Jhonatas
    Segue o fechamento da importação vinda com a invoice ST25311A.
    Nossa fatura número 1000013015 teve um saldo favorável para a Vizu Home,
    no valor de r$ 1.095,02, de um total enviado de r$ 58.050,00 em 14.04.2026.
    DI numero 26/0564654-7"""
    import json
    print(json.dumps(parse(exemplo), indent=2, ensure_ascii=False))
