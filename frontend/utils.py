from fpdf import FPDF


def dataframe_to_pdf(df, title="Expense Report"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Title
    pdf.set_font("Arial", style='B', size=14)
    pdf.multi_cell(200, 10, title, ln=True, align='C')
    pdf.ln(10)

    # Table header
    pdf.set_font("Arial", style='B', size=12)
    col_width = pdf.w / (len(df.columns) + 1)
    for col in df.columns:
        pdf.cell(col_width, 10, col, border=1)
    pdf.ln()

    # Table rows
    pdf.set_font("Arial", size=12)
    for _, row in df.iterrows():
        for value in row:
            pdf.cell(col_width, 10, str(value), border=1)
        pdf.ln()

    return pdf.output(dest='S')

