import pytesseract
from pypdf import PdfWriter
from pytesseract import image_to_string
from tqdm import tqdm
import os
from time import sleep

imagesFolder = 'images/pages'
open('out.pdf', 'a').close()
open('out.txt', 'a').close()

fileCounter = 0
for entry in tqdm(os.scandir(imagesFolder), desc="Progression", total=len(os.listdir(imagesFolder))):
    sleep(0.05)
    filename = entry.path
    pdf = pytesseract.image_to_pdf_or_hocr(filename, extension='pdf', lang='fra', config='-c textonlypdf=0')
    with open('out.txt', 'a') as f:
        f.write(image_to_string(filename))  # pdf type is bytes by default
    with open('output/test' + str(fileCounter) + '.pdf', 'w+b') as f:
        f.write(pdf)  # pdf type is bytes by default
    fileCounter = fileCounter + 1

merger = PdfWriter()

for pdf in os.scandir('output'):
     merger.append(str(pdf.path))
     os.remove(pdf.path)

merger.write("out.pdf")
merger.close()