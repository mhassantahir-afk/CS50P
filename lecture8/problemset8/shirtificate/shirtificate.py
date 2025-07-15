from fpdf import FPDF

class PDFmanipulator(FPDF):
    def pdfCR(self, name):
        self.image("shirtificate.png", 'C', 50)

        self.cell(26.5, 5)

        self.cell(text="CS50 Shirtificate", center=True)

        self.set_text_color(255, 255, 255)

        self.cell(26.5, 200, text=name, align="C", center=True)


pdf = PDFmanipulator()
pdf.add_page()
pdf.set_font("Times", size=40)
pdf.pdfCR(input("Name: "))
pdf.output("shirtificate.pdf")



