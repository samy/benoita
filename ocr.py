import pytesseract
from pypdf import PdfWriter
from tqdm import tqdm
import os

imagesFolder = 'images/pages'
open('out.pdf', 'a').close()

fileCounter = 0
for entry in tqdm(os.scandir(imagesFolder), desc="Progression", total=len(os.listdir(imagesFolder))):
    filename = entry.path
    pdf = pytesseract.image_to_pdf_or_hocr(filename, extension='pdf', lang='fra')
    with open('output/test' + str(fileCounter) + '.pdf', 'w+b') as f:
        f.write(pdf)  # pdf type is bytes by default
    fileCounter = fileCounter + 1

merger = PdfWriter()

for pdf in os.scandir('output'):
     merger.append(str(pdf.path))
     os.remove(pdf.path)

merger.write("out.pdf")
merger.close()