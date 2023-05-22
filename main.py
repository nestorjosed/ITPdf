import tkinter as tk
from tkinter import filedialog
from pdf_to_word import convert_pdf_to_word
from merge_pdf import merge_pdfs
from compress_pdf import compress_pdf
from word_to_pdf import convert_word_to_pdf
import ocr_handler

def main():
    root = tk.Tk()
    root.withdraw()

    # Pregunta al usuario qué acción realizar
    action = input("¿Qué acción deseas realizar? (w: convertir de Word a PDF, c: combinar PDF, p: comprimir PDF, r: convertir de PDF a Word, i: OCR): ")

    if action == "w":
        # Convertir de Word a PDF
        word_file = filedialog.askopenfilename(title="Seleccione el archivo de Word", filetypes=[("Archivos de Word", "*.docx")])
        if word_file:
            output_file = filedialog.asksaveasfilename(title="Guardar como PDF", filetypes=[("Archivo PDF", "*.pdf")], defaultextension=".pdf")
            convert_word_to_pdf(word_file, output_file)
    elif action == "c":
        # Combinar archivos PDF
        input_files = filedialog.askopenfilenames(title="Seleccione los archivos PDF para combinar", filetypes=[("Archivos PDF", "*.pdf")])
        input_files = root.tk.splitlist(input_files)
        if input_files:
            output_file = filedialog.asksaveasfilename(title="Guardar archivo combinado", filetypes=[("Archivo PDF", "*.pdf")], defaultextension=".pdf")
            merge_pdfs(input_files, output_file)
    elif action == "p":
        # Comprimir archivo PDF
        input_file = filedialog.askopenfilename(title="Seleccione el archivo PDF a comprimir", filetypes=[("Archivos PDF", "*.pdf")])
        if input_file:
            output_file = filedialog.asksaveasfilename(title="Guardar archivo comprimido", filetypes=[("Archivo PDF", "*.pdf")], defaultextension=".pdf")
            compress_pdf(input_file, output_file)
    elif action == "r":
        # Convertir de PDF a Word
        pdf_file = filedialog.askopenfilename(title="Seleccione el archivo PDF para convertir", filetypes=[("Archivos PDF", "*.pdf")])
        if pdf_file:
            output_file = filedialog.asksaveasfilename(title="Guardar como Word", filetypes=[("Archivos de Word", "*.docx")], defaultextension=".docx")
            convert_pdf_to_word(pdf_file, output_file)
    elif action == "i":
        # Realizar OCR en una imagen
        image_file = filedialog.askopenfilename(title="Seleccione la imagen para realizar OCR", filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg")])
        if image_file:
            output_format = input("¿En qué formato deseas guardar el texto resultante? (word, txt, clipboard): ")
            if output_format == "word":
                output_file = filedialog.asksaveasfilename(title="Guardar como Word", filetypes=[("Archivos de Word", "*.docx")], defaultextension=".docx")
                ocr_handler.perform_ocr_save_word(image_file, output_file)
            elif output_format == "txt":
                output_file = filedialog.asksaveasfilename(title="Guardar como TXT", filetypes=[("Archivo de texto", "*.txt")], defaultextension=".txt")
                ocr_handler.perform_ocr_save_txt(image_file, output_file)
            elif output_format == "clipboard":
                ocr_handler.perform_ocr_copy_to_clipboard(image_file)
            else:
                print("Formato de salida no válido. Elige 'word', 'txt' o 'clipboard'.")
    else:
        print("Acción no reconocida. Elige 'w' para convertir, 'c' para combinar, 'p' para comprimir, 'r' para convertir de PDF a Word o 'i' para OCR.")

if __name__ == "__main__":
    main()
