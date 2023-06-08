import wx
from pdf_to_word import convert_pdf_to_word
from merge_pdf import merge_pdfs
from compress_pdf import compress_pdf
from word_to_pdf import convert_word_to_pdf
import ocr_handler
import threading

class MainFrame(wx.Frame):
    def __init__(self, parent):
        super(MainFrame, self).__init__(parent, title="ITPdf", size=(500, 400))
        panel = wx.Panel(self)
        
        # Crear controles de interfaz
        action_label = wx.StaticText(panel, label="¿Qué acción deseas realizar?")
        self.action_choice = wx.Choice(panel, choices=["Convertir de Word a PDF", "Combinar PDF", "Comprimir PDF", "Convertir de PDF a Word", "OCR"])
        
        self.word_to_pdf_button = wx.Button(panel, label="Convertir de Word a PDF")
        self.combine_pdf_button = wx.Button(panel, label="Combinar PDF")
        self.compress_pdf_button = wx.Button(panel, label="Comprimir PDF")
        self.pdf_to_word_button = wx.Button(panel, label="Convertir de PDF a Word")
        self.ocr_button = wx.Button(panel, label="OCR")
        
        # Barra de progreso
        self.progress_bar = wx.Gauge(panel, range=100, style=wx.GA_HORIZONTAL)
        
        # Botón de salir
        self.exit_button = wx.Button(panel, label="Salir")
        
        # Agregar controles al sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(action_label, 0, wx.ALL, 10)
        sizer.Add(self.action_choice, 0, wx.EXPAND | wx.ALL, 10)
        sizer.Add(self.word_to_pdf_button, 0, wx.EXPAND | wx.ALL, 10)
        sizer.Add(self.combine_pdf_button, 0, wx.EXPAND | wx.ALL, 10)
        sizer.Add(self.compress_pdf_button, 0, wx.EXPAND | wx.ALL, 10)
        sizer.Add(self.pdf_to_word_button, 0, wx.EXPAND | wx.ALL, 10)
        sizer.Add(self.ocr_button, 0, wx.EXPAND | wx.ALL, 10)
        sizer.Add(self.progress_bar, 0, wx.EXPAND | wx.ALL, 10)
        sizer.Add(self.exit_button, 0, wx.EXPAND | wx.ALL, 10)
        
        panel.SetSizer(sizer)
        
        # Conectar eventos a los botones
        self.word_to_pdf_button.Bind(wx.EVT_BUTTON, self.on_word_to_pdf_button)
        self.combine_pdf_button.Bind(wx.EVT_BUTTON, self.on_combine_pdf_button)
        self.compress_pdf_button.Bind(wx.EVT_BUTTON, self.on_compress_pdf_button)
        self.pdf_to_word_button.Bind(wx.EVT_BUTTON, self.on_pdf_to_word_button)
        self.ocr_button.Bind(wx.EVT_BUTTON, self.on_ocr_button)
        self.exit_button.Bind(wx.EVT_BUTTON, self.on_exit_button)
        
    def execute_in_thread(self, function):
        thread = threading.Thread(target=function)
        thread.start()
        
    def on_word_to_pdf_button(self, event):
        def convert_word_to_pdf_thread():
            word_file_dialog = wx.FileDialog(self, message="Seleccione el archivo de Word", wildcard="Archivos de Word (*.docx)|*.docx", style=wx.FD_OPEN)
            if word_file_dialog.ShowModal() == wx.ID_OK:
                word_file = word_file_dialog.GetPath()
                save_file_dialog = wx.FileDialog(self, message="Guardar como PDF", wildcard="Archivo PDF (*.pdf)|*.pdf", style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
                if save_file_dialog.ShowModal() == wx.ID_OK:
                    output_file = save_file_dialog.GetPath()
                    self.progress_bar.SetValue(0)  # Reiniciar la barra de progreso
                    self.progress_bar.Pulse()  # Mostrar la barra de progreso en movimiento
                    convert_word_to_pdf(word_file, output_file)
                    self.progress_bar.SetValue(100)  # Completar la barra de progreso

        self.execute_in_thread(convert_word_to_pdf_thread)
        
    def on_combine_pdf_button(self, event):
        def merge_pdfs_thread():
            pdf_files_dialog = wx.FileDialog(self, message="Seleccione los archivos PDF para combinar", wildcard="Archivos PDF (*.pdf)|*.pdf", style=wx.FD_OPEN | wx.FD_MULTIPLE)
            if pdf_files_dialog.ShowModal() == wx.ID_OK:
                pdf_files = pdf_files_dialog.GetPaths()
                save_file_dialog = wx.FileDialog(self, message="Guardar archivo combinado", wildcard="Archivo PDF (*.pdf)|*.pdf", style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
                if save_file_dialog.ShowModal() == wx.ID_OK:
                    output_file = save_file_dialog.GetPath()
                    self.progress_bar.SetValue(0)  # Reiniciar la barra de progreso
                    self.progress_bar.Pulse()  # Mostrar la barra de progreso en movimiento
                    merge_pdfs(pdf_files, output_file)
                    self.progress_bar.SetValue(100)  # Completar la barra de progreso
        
        self.execute_in_thread(merge_pdfs_thread)
        
    def on_compress_pdf_button(self, event):
        def compress_pdf_thread():
            pdf_file_dialog = wx.FileDialog(self, message="Seleccione el archivo PDF a comprimir", wildcard="Archivos PDF (*.pdf)|*.pdf", style=wx.FD_OPEN)
            if pdf_file_dialog.ShowModal() == wx.ID_OK:
                pdf_file = pdf_file_dialog.GetPath()
                save_file_dialog = wx.FileDialog(self, message="Guardar archivo comprimido", wildcard="Archivo PDF (*.pdf)|*.pdf", style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
                if save_file_dialog.ShowModal() == wx.ID_OK:
                    output_file = save_file_dialog.GetPath()
                    self.progress_bar.SetValue(0)  # Reiniciar la barra de progreso
                    self.progress_bar.Pulse()  # Mostrar la barra de progreso en movimiento
                    compress_pdf(pdf_file, output_file)
                    self.progress_bar.SetValue(100)  # Completar la barra de progreso
        
        self.execute_in_thread(compress_pdf_thread)
        
    def on_pdf_to_word_button(self, event):
        def convert_pdf_to_word_thread():
            pdf_file_dialog = wx.FileDialog(self, message="Seleccione el archivo PDF para convertir", wildcard="Archivos PDF (*.pdf)|*.pdf", style=wx.FD_OPEN)
            if pdf_file_dialog.ShowModal() == wx.ID_OK:
                pdf_file = pdf_file_dialog.GetPath()
                save_file_dialog = wx.FileDialog(self, message="Guardar como Word", wildcard="Archivos de Word (*.docx)|*.docx", style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
                if save_file_dialog.ShowModal() == wx.ID_OK:
                    output_file = save_file_dialog.GetPath()
                    self.progress_bar.SetValue(0)  # Reiniciar la barra de progreso
                    self.progress_bar.Pulse()  # Mostrar la barra de progreso en movimiento
                    convert_pdf_to_word(pdf_file, output_file)
                    self.progress_bar.SetValue(100)  # Completar la barra de progreso
        
        self.execute_in_thread(convert_pdf_to_word_thread)
        
    def on_ocr_button(self, event):
        def ocr_thread():
            image_file_dialog = wx.FileDialog(self, message="Seleccione la imagen para realizar OCR", wildcard="Archivos de imagen (*.png;*.jpg;*.jpeg)|*.png;*.jpg;*.jpeg", style=wx.FD_OPEN)
            if image_file_dialog.ShowModal() == wx.ID_OK:
                image_file = image_file_dialog.GetPath()
                output_format_dialog = wx.MessageDialog(self, message="¿En qué formato deseas guardar el texto resultante?", style=wx.YES_NO | wx.CANCEL | wx.ICON_QUESTION)
                output_format_dialog.SetYesNoLabels("&Word", "&TXT")
                response = output_format_dialog.ShowModal()
                if response == wx.ID_YES:
                    save_file_dialog = wx.FileDialog(self, message="Guardar como Word", wildcard="Archivos de Word (*.docx)|*.docx", style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
                    if save_file_dialog.ShowModal() == wx.ID_OK:
                        output_file = save_file_dialog.GetPath()
                        self.progress_bar.SetValue(0)  # Reiniciar la barra de progreso
                        self.progress_bar.Pulse()  # Mostrar la barra de progreso en movimiento
                        ocr_handler.perform_ocr_save_word(image_file, output_file)
                        self.progress_bar.SetValue(100)  # Completar la barra de progreso
                elif response == wx.ID_NO:
                    save_file_dialog = wx.FileDialog(self, message="Guardar como TXT", wildcard="Archivo de texto (*.txt)|*.txt", style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
                    if save_file_dialog.ShowModal() == wx.ID_OK:
                        output_file = save_file_dialog.GetPath()
                        self.progress_bar.SetValue(0)  # Reiniciar la barra de progreso
                        self.progress_bar.Pulse()  # Mostrar la barra de progreso en movimiento
                        ocr_handler.perform_ocr_save_txt(image_file, output_file)
                        self.progress_bar.SetValue(100)  # Completar la barra de progreso
        
        self.execute_in_thread(ocr_thread)
        
    def on_exit_button(self, event):
        self.Close()  # Cerrar la aplicación
    
    def execute_in_thread(self, target):
        import threading
        
        thread = threading.Thread(target=target)
        thread.start()
        
def main():
    app = wx.App()
    frame = MainFrame(None)
    frame.Show()
    app.MainLoop()

if __name__ == "__main__":
    main()
