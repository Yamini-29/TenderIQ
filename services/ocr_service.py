import pytesseract
from PIL import Image
import fitz  # PyMuPDF


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text_from_file(file_path):
    text = ""

    # PDF
    if file_path.lower().endswith(".pdf"):
        doc = fitz.open(file_path)
        for page in doc:
            text += page.get_text()

    # TEXT FILE
    elif file_path.lower().endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

    # IMAGE
    else:
        img = Image.open(file_path)
        text = pytesseract.image_to_string(img)

    return text.strip()