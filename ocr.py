import shutil

import pytesseract
from pytesseract import image_to_string
from tqdm import tqdm
import os
from time import sleep

imagesFolder = 'images/pages'
outputFolder = 'output/'
open('out.pdf', 'a').close()
open('out.txt', 'a').close()

for entry in tqdm(os.scandir(imagesFolder), desc="Progression", total=len(os.listdir(imagesFolder))):
    if not str(entry.path).endswith(".jpg"):
        continue
    sleep(0.05)
    filename = entry.path
    pdf = pytesseract.image_to_pdf_or_hocr(filename, extension='hocr', lang='fra')
    with open('out.txt', 'a') as f:
        f.write(image_to_string(filename))  # pdf type is bytes by default
    with open(outputFolder + os.path.basename(str(entry.path)).replace('.jpg', '.hocr'), 'w+b') as f:
        f.write(pdf)  # pdf type is bytes by default
    shutil.copyfile(str(entry.path), outputFolder + os.path.basename(str(entry.path)))
