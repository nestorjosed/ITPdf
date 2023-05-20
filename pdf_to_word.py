from pdf2docx import Converter

def convert_pdf_to_word(input_file, output_file):
    try:
        cv = Converter(input_file)
        cv.convert(output_file, start=0, end=None)
        cv.close()
        print(f"Archivo convertido a Word en {output_file}")
    except Exception as e:
        print(f"Error al convertir a Word: {str(e)}")
