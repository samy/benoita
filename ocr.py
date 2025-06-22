from PIL import Image

import pytesseract
from pytesseract import Output

filename = 'image_01.jpg'
img1 = np.array(Image.open(filename))
pdf = pytesseract.image_to_pdf_or_hocr(filename, extension='pdf', lang='fra')
with open('test.pdf', 'w+b') as f:
    f.write(pdf) # pdf type is bytes by default