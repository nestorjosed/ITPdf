import os
from docx2pdf import convert as docx2pdf_convert

def convert_word_to_pdf(input_file, output_file):
    try:
        docx2pdf_convert(input_file, output_file)
        print(f"Archivo convertido a PDF en {output_file}")
    except Exception as e:
        print(f"Error al convertir a PDF: {str(e)}")
