from PyPDF2 import PdfReader
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# print(pytesseract.image_to_string(Image.open('download.jpg')))


# creating a pdf reader object
reader = PdfReader('perform.pdf')

# printing number of pages in pdf file
print(len(reader.pages))

# getting a specific page from the pdf file
for i in range(1):
    page = reader.pages[i]

    # extracting text from page
    text = page.extract_text()
    print(text)
    f = open("test.txt", "a+")
    f.write(text)
    f.close()
