"""Tabela de câmbio R$/USD médio mensal (fonte BCB/PTAX). Atualizar manualmente quando mudar mês."""

CAMBIO_MEDIO = {
    "2024-01": 4.95, "2024-02": 4.95, "2024-03": 5.00, "2024-04": 5.10,
    "2024-05": 5.15, "2024-06": 5.30, "2024-07": 5.50, "2024-08": 5.55,
    "2024-09": 5.50, "2024-10": 5.60, "2024-11": 5.65, "2024-12": 5.85,
    "2025-01": 5.95, "2025-02": 5.80, "2025-03": 5.75, "2025-04": 5.65,
    "2025-05": 5.60, "2025-06": 5.65, "2025-07": 5.70, "2025-08": 5.75,
    "2025-09": 5.80, "2025-10": 5.95, "2025-11": 6.05, "2025-12": 6.10,
    "2026-01": 6.10, "2026-02": 6.05, "2026-03": 5.95, "2026-04": 5.85,
}

def cambio(data_str):
    """Aceita 'YYYY-MM' ou texto tipo 'abr/2026'. Retorna câmbio médio do mês."""
    meses = {"jan":"01","fev":"02","mar":"03","abr":"04","mai":"05","jun":"06",
             "jul":"07","ago":"08","set":"09","out":"10","nov":"11","dez":"12"}
    s = data_str.lower().strip()
    # YYYY-MM
    if len(s) >= 7 and s[:4].isdigit() and s[5:7].isdigit():
        return CAMBIO_MEDIO.get(s[:7], 5.80)
    # textual mes/YYYY
    for nm, num in meses.items():
        if nm in s:
            import re
            m = re.search(r'20\d{2}', s)
            if m:
                return CAMBIO_MEDIO.get(f"{m.group(0)}-{num}", 5.80)
    return 5.80  # fallback
