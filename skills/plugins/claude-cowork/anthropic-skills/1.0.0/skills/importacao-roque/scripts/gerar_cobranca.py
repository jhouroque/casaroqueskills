"""Gera PDF de cobrança sintética para a Mariane (ou outro cliente).

Uso:
    python3 gerar_cobranca.py ST25311A
    (busca dados no xlsx e gera PDF em _cobrancas/)
"""
import sys, os, json
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT

MARSALA = colors.HexColor("#573333")
DOURADO = colors.HexColor("#A98D5F")
CREME = colors.HexColor("#F5EFE6")
CINZA = colors.HexColor("#4A4A4A")
VERDE = colors.HexColor("#4A7D2F")

def fmt_rs(v):
    if v is None or v == 0: return "—"
    s = f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {s}"

def fmt_usd(v):
    if v is None or v == 0: return "—"
    return f"USD {v:,.2f}"

def gerar_cobranca_pdf(dados, out_path):
    """dados = dict com: invoice, empresa, navio, data, usd_fob, cambio, numerario_rs,
    complementos_rs, devolucao_rs, observacao, pix_roque"""

    # Cálculos
    rs_china = (dados.get("usd_fob") or 0) * (dados.get("cambio") or 5.80)
    numerario = dados.get("numerario_rs") or 0
    complementos = dados.get("complementos_rs") or 0
    devolucao = dados.get("devolucao_rs") or 0
    total = rs_china + numerario + complementos - devolucao
    comissao = total * 0.01

    doc = SimpleDocTemplate(out_path, pagesize=A4,
                            leftMargin=2*cm, rightMargin=2*cm,
                            topMargin=1.5*cm, bottomMargin=1.5*cm,
                            title=f"Cobrança {dados.get('invoice','')}",
                            author="Roque Gestão & Engenharia")

    styles = getSampleStyleSheet()
    h1 = ParagraphStyle("h1", parent=styles["Title"], fontSize=18, textColor=MARSALA,
                        alignment=TA_CENTER, spaceAfter=4)
    sub = ParagraphStyle("sub", parent=styles["Normal"], fontSize=11, textColor=CINZA,
                         alignment=TA_CENTER, spaceAfter=14)
    h2 = ParagraphStyle("h2", parent=styles["Heading2"], fontSize=12, textColor=DOURADO,
                        spaceBefore=8, spaceAfter=6)
    body = ParagraphStyle("b", parent=styles["Normal"], fontSize=10, leading=14,
                          textColor=CINZA)
    small = ParagraphStyle("s", parent=body, fontSize=8, textColor=CINZA)

    story = []
    story.append(Paragraph("COBRANÇA — IMPORTAÇÃO", h1))
    story.append(Paragraph(
        f"<b>{dados.get('invoice','')}</b>  ·  {dados.get('empresa','')}  ·  "
        f"{dados.get('navio','')}  ·  {dados.get('data','')}", sub))

    # Breakdown financeiro
    linhas = [
        ["COMPONENTE", "DETALHE", "VALOR"],
        ["CHINA (FOB Alibaba)",
         f"{fmt_usd(dados.get('usd_fob'))} × R$ {dados.get('cambio',5.80):.2f}",
         fmt_rs(rs_china)],
        ["BRASIL (Numerário Osvaldo)",
         "Impostos + frete marítimo + despacho",
         fmt_rs(numerario)],
    ]
    if complementos:
        linhas.append(["Complementos", "Lavagem / ajudantes / frete rodoviário", fmt_rs(complementos)])
    if devolucao:
        linhas.append(["Devolução (saldo favorável)", "Devolvido pelo Osvaldo após fechamento real",
                       "(–) " + fmt_rs(devolucao)])
    linhas.append(["TOTAL DA IMPORTAÇÃO", "", fmt_rs(total)])
    linhas.append(["COMISSÃO ROQUE ENGENHARIA (1%)", "", fmt_rs(comissao)])

    t = Table(linhas, colWidths=[6*cm, 7*cm, 4*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), MARSALA),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 10),
        ("GRID", (0, 0), (-1, -1), 0.3, DOURADO),
        ("ROWBACKGROUNDS", (0, 1), (-1, -3), [colors.white, CREME]),
        ("BACKGROUND", (0, -2), (-1, -2), DOURADO),
        ("TEXTCOLOR", (0, -2), (-1, -2), colors.white),
        ("FONTNAME", (0, -2), (-1, -2), "Helvetica-Bold"),
        ("BACKGROUND", (0, -1), (-1, -1), VERDE),
        ("TEXTCOLOR", (0, -1), (-1, -1), colors.white),
        ("FONTNAME", (0, -1), (-1, -1), "Helvetica-Bold"),
        ("FONTSIZE", (0, -1), (-1, -1), 12),
        ("ALIGN", (2, 0), (2, -1), "RIGHT"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(t)
    story.append(Spacer(1, 0.6*cm))

    if dados.get("observacao"):
        story.append(Paragraph("<b>Observação:</b> " + dados["observacao"], small))
        story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph("Dados para pagamento", h2))
    story.append(Paragraph(
        "<b>Roque Gestão & Engenharia Empresarial</b><br/>"
        f"PIX: {dados.get('pix_roque', 'jhouroque@gmail.com')}<br/>"
        f"NFS-e será emitida após o pagamento (prazo 48h)", body))

    story.append(Spacer(1, 0.6*cm))
    story.append(Paragraph(
        "_" * 100 + "<br/>"
        "Roque Gestão & Engenharia Empresarial · Jhonatas Roque · "
        "jhouroque@gmail.com · csroque.com.br",
        small))

    doc.build(story)

if __name__ == "__main__":
    # Demo com ST25311A
    dados = {
        "invoice": "ST25311A",
        "empresa": "Vizu Home Ltda",
        "navio": "Xin Chong Qing 183W",
        "data": "abr/2026",
        "usd_fob": 43924.93,
        "cambio": 5.85,
        "numerario_rs": 58050.00,
        "devolucao_rs": 1095.02,
        "complementos_rs": 0,
        "observacao": "Primeiro embarque da série ST25311 (parte A). DI 26/0564654-7. Fatura Osvaldo 1000013015.",
        "pix_roque": "jhouroque@gmail.com",
    }
    out = "/sessions/beautiful-loving-tesla/mnt/outputs/02_IMPORTACAO/_cobrancas/COBRANCA_ST25311A_Mariane.pdf"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    gerar_cobranca_pdf(dados, out)
    print(f"OK: {out}")
