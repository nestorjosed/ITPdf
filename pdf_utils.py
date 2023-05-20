import os
from PyPDF4 import PdfFileMerger, PdfFileReader, PdfFileWriter
from pdf2docx import Converter

def convert_pdf_to_word(input_file, output_file):
    try:
        cv = Converter(input_file)
        cv.convert(output_file, start=0, end=None)
        cv.close()
        print(f"Archivo convertido a Word en {output_file}")
    except Exception as e:
        print(f"Error al convertir a Word: {str(e)}")

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

def compress_pdf(input_file, output_file, quality=75):
    try:
        pdf_writer = PdfFileWriter()
        pdf_reader = PdfFileReader(input_file)
        for page_num in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page_num)
            page.compressContentStreams()
            pdf_writer.addPage(page)

        with open(output_file, 'wb') as f:
            pdf_writer.write(f)
        
        print(f"Archivo PDF comprimido creado en {output_file}")
    except Exception as e:
        print(f"Error al comprimir archivo PDF: {str(e)}")
