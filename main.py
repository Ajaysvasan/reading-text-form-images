from pytesseract import pytesseract
from PIL import Image
import enum

class OS(enum.Enum):
    windows = 1

class languages(enum.Enum):
    ENG = 'eng'

class ImageReader:
    def __init__(self,os:OS):
        if os==OS.windows:
            windows = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
            pytesseract.tesseract_cmd = windows
            print("on windows")
    
    def extract(self,file,lang):
        img = Image.open(file)
        text = pytesseract.image_to_string(img,lang=lang)
        return text

ir = ImageReader(OS.windows)
text = ir.extract('text.png',lang='eng')
print(text)