from tkinter import Tk, filedialog

def select_word_file():
    root = Tk()
    root.withdraw()
    word_file = filedialog.askopenfilename(title="Seleccione el archivo de Word", filetypes=[("Archivos de Word", "*.docx")])
    return word_file

def select_pdf_files():
    root = Tk()
    root.withdraw()
    input_files = filedialog.askopenfilenames(title="Seleccione los archivos PDF", filetypes=[("Archivos PDF", "*.pdf")])
    input_files = root.tk.splitlist(input_files)
    return input_files

def select_pdf_file():
    root = Tk()
    root.withdraw()
    input_file = filedialog.askopenfilename(title="Seleccione el archivo PDF", filetypes=[("Archivos PDF", "*.pdf")])
    return input_file

def select_output_file():
    root = Tk()
    root.withdraw()
    output_file = filedialog.asksaveasfilename(title="Seleccione el archivo de salida")
    return output_file
