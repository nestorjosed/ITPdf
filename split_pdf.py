import wx
import fitz


class SplitPDFPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        self.pdf_path = ""
        self.page_list = []

        # Crear controles de interfaz
        self.file_picker = wx.FilePickerCtrl(self, message="Seleccione un archivo PDF", wildcard="Archivos PDF (*.pdf)|*.pdf")
        self.page_checklist = wx.CheckListBox(self, style=wx.LB_SINGLE)
        self.extract_button = wx.Button(self, label="Extraer páginas seleccionadas")

        # Agregar controles al sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.file_picker, 0, wx.EXPAND | wx.ALL, 10)
        sizer.Add(self.page_checklist, 1, wx.EXPAND | wx.ALL, 10)
        sizer.Add(self.extract_button, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        self.SetSizer(sizer)

        # Conectar eventos a los botones
        self.file_picker.Bind(wx.EVT_FILEPICKER_CHANGED, self.on_file_picker_changed)
        self.page_checklist.Bind(wx.EVT_CHECKLISTBOX, self.on_page_checked)
        self.extract_button.Bind(wx.EVT_BUTTON, self.on_extract_button)

    def on_file_picker_changed(self, event):
        self.pdf_path = self.file_picker.GetPath()
        self.load_pdf_pages()

    def load_pdf_pages(self):
        self.page_list = []
        self.page_checklist.Clear()

        # Cargar el archivo PDF y obtener la cantidad de páginas
        if self.pdf_path:
            doc = fitz.open(self.pdf_path)
            num_pages = doc.page_count

            # Agregar cada página a la lista de páginas
            for i in range(num_pages):
                self.page_list.append(i)
                self.page_checklist.Append(f"Página {i+1}")

    def on_page_checked(self, event):
        page_index = event.GetSelection()
        is_checked = self.page_checklist.IsChecked(page_index)

        if is_checked:
            self.page_checklist.SetString(page_index, f"Página {page_index+1} *")
        else:
            self.page_checklist.SetString(page_index, f"Página {page_index+1}")

    def on_extract_button(self, event):
        selected_pages = self.get_selected_pages()
        if selected_pages:
            output_path = self.show_save_dialog("Guardar páginas seleccionadas")
            if output_path:
                self.extract_pages(selected_pages, output_path)
        else:
            wx.MessageBox("No se ha seleccionado ninguna página.", "Aviso", wx.OK | wx.ICON_INFORMATION)

    def get_selected_pages(self):
        selected_pages = []
        for i in range(self.page_checklist.GetCount()):
            if self.page_checklist.IsChecked(i):
                selected_pages.append(i)
        return selected_pages

    def extract_pages(self, page_numbers, output_path):
        doc = fitz.open(self.pdf_path)
        output_doc = fitz.open()

        for page_num in page_numbers:
            page = doc.load_page(page_num)
            output_doc.insert_pdf(doc, from_page=page_num, to_page=page_num)

        output_doc.save(output_path)
        output_doc.close()

        wx.MessageBox("Páginas extraídas con éxito.", "Éxito", wx.OK | wx.ICON_INFORMATION)

    def show_save_dialog(self, message):
        dialog = wx.FileDialog(self, message=message, wildcard="Archivos PDF (*.pdf)|*.pdf",
                               style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if dialog.ShowModal() == wx.ID_OK:
            return dialog.GetPath()
        return None


class SplitPDFFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Dividir PDF")
        self.panel = SplitPDFPanel(self)


def run_split_pdf_app():
    app = wx.App()
    frame = SplitPDFFrame()
    frame.Show()
    app.MainLoop()


if __name__ == "__main__":
    run_split_pdf_app()
