import pytesseract
from PIL import Image

img = Image.open('c:\Users\Admin\Downloads\Untitled (5).png')

text = pytesseract.image_to_string(img)

print(text)