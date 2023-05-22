import pytesseract
from PIL import Image
from docx import Document
import pyperclip

def perform_ocr(image_file):
    """
    Realiza OCR en una imagen y devuelve el texto extraído.
    """
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(Image.open(image_file))
    return text

def perform_ocr_save_word(image_file, output_file):
    """
    Realiza OCR en una imagen y guarda el texto resultante en un archivo de Word (docx).
    """
    text = perform_ocr(image_file)

    doc = Document()
    doc.add_paragraph(text)
    doc.save(output_file)
    print("Texto guardado como Word.")

def perform_ocr_save_txt(image_file, output_file):
    """
    Realiza OCR en una imagen y guarda el texto resultante en un archivo de texto (txt).
    """
    text = perform_ocr(image_file)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)
    print("Texto guardado como TXT.")

def perform_ocr_copy_to_clipboard(image_file):
    """
    Realiza OCR en una imagen y copia el texto resultante al portapapeles.
    """
    text = perform_ocr(image_file)
    pyperclip.copy(text)
    print("Texto copiado al portapapeles.")
