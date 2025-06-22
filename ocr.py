import pytesseract
from pypdf import PdfWriter
import os

filename = 'image_01.jpg'
pdf = pytesseract.image_to_pdf_or_hocr(filename, extension='pdf', lang='fra')
open('test.pdf', 'a').close()
with open('test.pdf', 'w+b') as f:
    f.write(pdf) # pdf type is bytes by default
with open('test2.pdf', 'a+b') as f:
    f.write(pdf) # pdf type is bytes by default

merger = PdfWriter()

for pdf in ["test.pdf", "test2.pdf"]:
    merger.append(pdf)
    os.remove(pdf)

merger.write("out.pdf")
merger.close()