import os 
from fpdf import FPDF

pdf = FPDF("P", "mm", "A4")
pdf.add_page()
pdf.set_font("Times", "", 25)

texto = "Coronavirus - Dias Atuais\n\nAtualmente estamos vivenciando uma das piores épocas já vivenciadas, e no município Brasileiro de Itapetininga do estado de São Paulo, na Região Sudeste do país não é diferente. Foram confirmados cerca de 17.632 casos e 559 mortes até agora.\nTanto homens como mulheres vêm sendo vítimas dessa doença e a faixa etária está bastante dividida.\nApesar de outros municípios estarem mais prejudicados, Itapetininga vem conseguindo controlar as mortes.\nEntretanto, se as pessoas não se colocarem no lugar do proximo, mais vidas serão tiradas."

pdf.multi_cell(w=0, h=8, txt=texto, align="C")

pdf.image(name="img_01.png", x=85, y=125, w=127)

pdf.output("relatorio.pdf")

print("Sim, o PDF foi criado!")
os.system("pause")