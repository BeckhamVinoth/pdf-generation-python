from fpdf import FPDF
import pandas as pd

df = pd.read_csv('topics.csv')

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

for index, data in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(254, 0, 0)
    pdf.cell(w=0, h=12, txt=data['Topic'], align='L', ln=1)
    pdf.line(10, 22, 200, 22)

    # footer
    pdf.ln(265)
    pdf.set_font(family='Times', style='I', size=8)
    pdf.set_text_color(255, 127, 127)
    pdf.cell(w=0, h=10, txt=data['Topic'], align='R', ln=1)

    for i in range(data['Pages']-1):
        pdf.add_page()

        # footer
        pdf.ln(277)
        pdf.set_font(family='Times', style='I', size=8)
        pdf.set_text_color(255, 127, 127)
        pdf.cell(w=0, h=10, txt=data['Topic'], align='R', ln=1)

pdf.output('output.pdf')

