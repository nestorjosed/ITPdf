import tkinter as tk
from tkinter import filedialog
from pdf_to_word import convert_pdf_to_word
from merge_pdf import merge_pdfs
from compress_pdf import compress_pdf
from word_to_pdf import convert_word_to_pdf

def main():
    root = tk.Tk()
    root.withdraw()

    # Pregunta al usuario qué acción realizar
    action = input("¿Qué acción deseas realizar? (w: convertir de Word a PDF, c: combinar PDF, p: comprimir PDF, r: convertir de PDF a Word): ")

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
    else:
        print("Acción no reconocida. Elige 'w' para convertir, 'c' para combinar, 'p' para comprimir o 'r' para convertir de PDF a Word.")

if __name__ == "__main__":
    main()
