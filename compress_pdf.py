import os
from PyPDF4 import PdfFileReader, PdfFileWriter

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
