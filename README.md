# Proyecto ITPdf

Herramienta Python para operaciones con archivos PDF y Word, con una interfaz gráfica basada en wxPython.

## Descripción

El Proyecto ITPdf es una aplicación que permite realizar diversas operaciones con archivos PDF y Word de manera sencilla y eficiente. Esta versión incluye una interfaz gráfica desarrollada utilizando la biblioteca wxPython, lo que proporciona una experiencia accesible y amigable para el usuario.

## Clonar el Repositorio

Para clonar el repositorio, utiliza el siguiente comando:

git clone [https://github.com/nestorjosed/ITPdf.git]


## Uso

Para utilizar el Proyecto ITPdf, sigue los siguientes pasos:

1. Ejecuta el archivo principal `main.py`.
2. Se mostrará una interfaz gráfica con diferentes acciones disponibles.
3. Selecciona la acción deseada haciendo clic en el botón correspondiente (Convertir de Word a PDF, Combinar PDF, Comprimir PDF, Convertir de PDF a Word, OCR).
4. Sigue las instrucciones en pantalla y utiliza los cuadros de diálogo para seleccionar los archivos de entrada y salida según sea necesario.
5. La aplicación realizará la acción seleccionada y generará el archivo resultante.

## Accesos Rápidos

- Acción para convertir de Word a PDF: Haz clic en el botón "Convertir de Word a PDF".
- Acción para combinar archivos PDF: Haz clic en el botón "Combinar PDF".
- Acción para comprimir archivo PDF: Haz clic en el botón "Comprimir PDF".
- Acción para convertir de PDF a Word: Haz clic en el botón "Convertir de PDF a Word".
- Acción para realizar OCR en una imagen: Haz clic en el botón "OCR".

## Diálogos de Archivos

Durante el uso de la aplicación, se mostrarán cuadros de diálogo de archivos para seleccionar los archivos de entrada y salida. Estos cuadros de diálogo permiten navegar y seleccionar los archivos correspondientes de manera intuitiva.

## Funciones del Proyecto ITPdf

El programa del Proyecto ITPdf cuenta con varias funciones que permiten realizar distintas operaciones con archivos PDF y Word. A continuación, se explica cada función y cómo funciona:

1. `convert_word_to_pdf(word_file, output_file)`: Esta función convierte un archivo de Word a formato PDF. Recibe la ruta del archivo de Word de entrada (`word_file`) y la ruta de salida para el archivo PDF resultante (`output_file`). Utiliza la librería `python-docx` para leer el contenido del archivo de Word y la librería `PyPDF4` para generar el archivo PDF.

2. `merge_pdfs(input_files, output_file)`: Esta función combina varios archivos PDF en uno solo. Recibe una lista de rutas de archivos PDF de entrada (`input_files`) y la ruta de salida para el archivo PDF combinado (`output_file`). Utiliza la librería `PyPDF4` para realizar la combinación de los archivos PDF.

3. `compress_pdf(input_file, output_file)`: Esta función comprime un archivo PDF. Recibe la ruta del archivo PDF de entrada (`input_file`) y la ruta de salida para el archivo PDF comprimido (`output_file`). Utiliza la librería `PyPDF4` para reducir el tamaño del archivo PDF sin perder la calidad del contenido.

4. `convert_pdf_to_word(pdf_file, output_file)`: Esta función convierte un archivo PDF a formato Word (docx). Recibe la ruta del archivo PDF de entrada (`pdf_file`) y la ruta de salida para el archivo de Word resultante (`output_file`). Utiliza la librería `pdf2docx` para extraer el texto del PDF y generar el archivo de Word.

5. `perform_ocr(image_file)`: Esta función realiza reconocimiento óptico de caracteres (OCR) en una imagen y devuelve el texto extraído. Recibe la ruta de la imagen (`image_file`). Utiliza la librería `pytesseract` en combinación con la librería `PIL` (Python Imaging Library) para realizar el OCR.

## Resultados

Los resultados de cada función dependen de la operación realizada. Por ejemplo, al convertir de Word a PDF, se generará un archivo PDF que representa el contenido del archivo de Word. Al combinar archivos PDF, se generará un nuevo archivo PDF que contiene todas las páginas de los archivos de entrada. Al comprimir un PDF, se generará un nuevo archivo PDF con un tamaño reducido. Al convertir de PDF a Word, se generará un archivo de Word con el texto extraído del archivo PDF. Al realizar OCR en una imagen, se obtendrá el texto extraído de la imagen.

## Descargo de Responsabilidad

El Proyecto ITPdf se proporciona tal cual, sin garantías de ningún tipo, expresas o implícitas. El uso de esta aplicación es bajo tu propio riesgo. No nos hacemos responsables de ningún daño o pérdida causados por el uso de esta aplicación.

## Contacto

Para cualquier consulta o comentario, puedes contactarme a través de las siguientes vías:

- Twitter: [@nestorjosedf](https://twitter.com/nestorjosedf)
- Correo electrónico: androidnjdb@gmail.com

Esperamos que el Proyecto ITPdf sea útil en tus tareas relacionadas con archivos PDF y Word. Si tienes alguna pregunta adicional, no dudes en preguntar.
