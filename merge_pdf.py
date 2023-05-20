import os
from PyPDF4 import PdfFileMerger

def merge_pdfs(input_files, output_file):
    try:
        merger = PdfFileMerger()
        for pdf in input_files:
            merger.append(pdf)
        merger.write(output_file)
        merger.close()
        print(f"Archivos PDF combinados en {output_file}")
    except Exception as e:
        print(f"Error al combinar archivos PDF: {str(e)}")
