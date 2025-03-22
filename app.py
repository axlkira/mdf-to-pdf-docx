import sys
import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, 
                            QWidget, QFileDialog, QLabel, QMessageBox)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QColor
import markdown2
import tempfile
import pdfkit

class MarkdownToPDFConverter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # Configuración de la ventana principal
        self.setWindowTitle('Markdown a PDF Converter')
        self.setGeometry(100, 100, 600, 400)
        
        # Widget central y layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Estilo para los widgets
        self.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-size: 14px;
                min-width: 200px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QLabel {
                font-size: 14px;
                color: #2c3e50;
                margin: 10px;
            }
        """)
        
        # Etiqueta de título
        title_label = QLabel('Conversor de Markdown a PDF')
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet('font-size: 24px; font-weight: bold; margin: 20px;')
        layout.addWidget(title_label)
        
        # Etiqueta de instrucciones
        instructions = QLabel('Selecciona un archivo Markdown (.md) para convertirlo a PDF')
        instructions.setAlignment(Qt.AlignCenter)
        layout.addWidget(instructions)
        
        # Botón para seleccionar archivo
        self.select_button = QPushButton('Seleccionar archivo Markdown')
        self.select_button.clicked.connect(self.select_file)
        layout.addWidget(self.select_button)
        
        # Etiqueta para mostrar el archivo seleccionado
        self.file_label = QLabel('Ningún archivo seleccionado')
        self.file_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.file_label)
        
        # Agregar espacio
        layout.addStretch()
        
        # Configurar colores de fondo
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor('#f5f6fa'))
        self.setPalette(palette)

    def select_file(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar archivo Markdown",
            "",
            "Markdown Files (*.md)"
        )
        
        if file_name:
            self.file_label.setText(f'Archivo seleccionado: {os.path.basename(file_name)}')
            self.convert_to_pdf(file_name)

    def convert_to_pdf(self, md_file):
        try:
            # Leer el contenido del archivo Markdown
            with open(md_file, 'r', encoding='utf-8') as file:
                md_content = file.read()
            
            # Convertir Markdown a HTML con extras
            html_content = markdown2.markdown(
                md_content,
                extras=[
                    'tables',
                    'fenced-code-blocks',
                    'header-ids',
                    'tag-friendly',
                    'break-on-newline'
                ]
            )
            
            # Estilos CSS mejorados con más espaciado y colores
            css_content = """
                body {
                    font-family: 'Arial', sans-serif;
                    line-height: 1.8;
                    color: #2c3e50;
                    max-width: 21cm;
                    margin: 0 auto;
                    padding: 2cm;
                    background-color: #ffffff;
                }
                h1, h2, h3, h4, h5, h6 {
                    margin-top: 2em;
                    margin-bottom: 1em;
                    page-break-after: avoid;
                }
                h1 {
                    color: #2c3e50;
                    font-size: 2.5em;
                    border-bottom: 3px solid #3498db;
                    padding-bottom: 0.5em;
                }
                h2 {
                    color: #34495e;
                    font-size: 2em;
                    border-bottom: 2px solid #95a5a6;
                    padding-bottom: 0.3em;
                }
                h3 {
                    color: #2980b9;
                    font-size: 1.5em;
                }
                p {
                    margin: 1.2em 0;
                    text-align: justify;
                    line-height: 1.8;
                }
                ul, ol {
                    padding-left: 2em;
                    margin: 1em 0;
                }
                li {
                    margin: 0.5em 0;
                    line-height: 1.6;
                }
                a {
                    color: #3498db;
                    text-decoration: none;
                }
                table {
                    width: 100%;
                    border-collapse: collapse;
                    margin: 2em 0;
                    page-break-inside: avoid;
                }
                th {
                    background-color: #3498db;
                    color: white;
                    font-weight: bold;
                    padding: 12px;
                    border: 1px solid #bdc3c7;
                }
                td {
                    padding: 12px;
                    border: 1px solid #bdc3c7;
                }
                tr:nth-child(even) {
                    background-color: #f8f9fa;
                }
                tr:hover {
                    background-color: #edf2f7;
                }
                code {
                    background-color: #f8f9fa;
                    color: #e74c3c;
                    padding: 0.2em 0.4em;
                    border-radius: 4px;
                    font-family: 'Courier New', monospace;
                    font-size: 0.9em;
                }
                pre {
                    background-color: #2c3e50;
                    color: #ecf0f1;
                    padding: 1em;
                    border-radius: 8px;
                    overflow-x: auto;
                    margin: 1.5em 0;
                    page-break-inside: avoid;
                }
                pre code {
                    background-color: transparent;
                    color: inherit;
                    padding: 0;
                    border-radius: 0;
                }
                blockquote {
                    border-left: 4px solid #3498db;
                    margin: 1.5em 0;
                    padding: 1em 1.5em;
                    background-color: #f8f9fa;
                    color: #34495e;
                    font-style: italic;
                    page-break-inside: avoid;
                }
                img {
                    max-width: 100%;
                    height: auto;
                    display: block;
                    margin: 2em auto;
                    page-break-inside: avoid;
                }
                hr {
                    border: none;
                    border-top: 2px solid #bdc3c7;
                    margin: 2em 0;
                }
                /* Ajustes para impresión */
                @media print {
                    body {
                        font-size: 12pt;
                    }
                    h1 {
                        font-size: 24pt;
                    }
                    h2 {
                        font-size: 20pt;
                    }
                    h3 {
                        font-size: 16pt;
                    }
                }
            """
            
            # Crear HTML completo con estilos incrustados
            full_html = f"""
                <!DOCTYPE html>
                <html>
                <head>
                    <meta charset="UTF-8">
                    <style>
                        {css_content}
                    </style>
                </head>
                <body>
                    {html_content}
                </body>
                </html>
            """
            
            # Crear archivo HTML temporal
            temp_html = tempfile.NamedTemporaryFile(delete=False, suffix='.html')
            temp_html.write(full_html.encode('utf-8'))
            temp_html.close()
            
            # Generar el nombre del archivo PDF
            pdf_file = os.path.splitext(md_file)[0] + '.pdf'
            
            # Verificar si el archivo PDF ya existe
            if os.path.exists(pdf_file):
                reply = QMessageBox.question(
                    self,
                    "Archivo existente",
                    f"El archivo {os.path.basename(pdf_file)} ya existe.\n¿Desea sobrescribirlo?",
                    QMessageBox.Yes | QMessageBox.No,
                    QMessageBox.No
                )
                
                if reply == QMessageBox.No:
                    QMessageBox.information(
                        self,
                        "Operación cancelada",
                        "La conversión ha sido cancelada."
                    )
                    return
            
            # Configuración de wkhtmltopdf
            config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
            
            # Opciones mejoradas para el PDF
            options = {
                'encoding': 'UTF-8',
                'margin-top': '25mm',
                'margin-right': '25mm',
                'margin-bottom': '25mm',
                'margin-left': '25mm',
                'page-size': 'A4',
                'enable-local-file-access': None,
                'header-font-size': '9',
                'header-spacing': '10',
                'footer-right': '[page] de [topage]',
                'footer-font-size': '9',
                'footer-spacing': '10',
                'enable-smart-shrinking': True,
                'zoom': '1.2'
            }
            
            # Convertir a PDF
            pdfkit.from_file(temp_html.name, pdf_file, configuration=config, options=options)
            
            # Eliminar archivo temporal
            os.unlink(temp_html.name)
            
            QMessageBox.information(
                self,
                "Éxito",
                f"PDF generado exitosamente:\n{pdf_file}"
            )
            
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Error al convertir el archivo:\n{str(e)}"
            )

def main():
    app = QApplication(sys.argv)
    converter = MarkdownToPDFConverter()
    converter.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
