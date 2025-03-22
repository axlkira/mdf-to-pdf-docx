# Manual de Usuario - Conversor de Markdown a PDF/DOCX

## Índice
1. [Introducción](#introducción)
2. [Requisitos del Sistema](#requisitos-del-sistema)
3. [Instalación](#instalación)
4. [Uso de la Aplicación](#uso-de-la-aplicación)
5. [Solución de Problemas](#solución-de-problemas)
6. [Preguntas Frecuentes](#preguntas-frecuentes)

## Introducción

El Conversor de Markdown a PDF/DOCX es una aplicación de escritorio que permite convertir archivos en formato Markdown (.md) a documentos PDF o DOCX (Word) con un diseño profesional y elegante. Esta herramienta es ideal para:

- Estudiantes que necesitan entregar trabajos académicos
- Profesionales que crean documentación técnica
- Escritores que desean formatear sus textos
- Cualquier persona que trabaje con archivos Markdown y necesite convertirlos a formatos más ampliamente utilizados

La aplicación cuenta con una interfaz gráfica intuitiva que facilita el proceso de conversión con solo unos clics.

## Requisitos del Sistema

### Hardware
- Procesador: Intel Core i3 o equivalente (2 GHz o superior)
- Memoria RAM: 4 GB mínimo (8 GB recomendado)
- Espacio en disco: 200 MB de espacio libre
- Resolución de pantalla: 1280 x 720 o superior

### Software
- Sistema Operativo: Windows 10/11 (64 bits)
- Python 3.8 o superior
- Dependencias adicionales (se instalan automáticamente durante el proceso de instalación)

### Requisitos Adicionales
- Conexión a Internet (solo para la instalación)
- wkhtmltopdf instalado en el sistema (para la conversión a PDF)

## Instalación

### Paso 1: Instalar Python
Si no tiene Python instalado en su sistema:
1. Visite [python.org](https://www.python.org/downloads/)
2. Descargue la última versión de Python 3 para Windows
3. Ejecute el instalador y asegúrese de marcar la opción "Add Python to PATH"
4. Complete la instalación siguiendo las instrucciones del asistente

### Paso 2: Instalar wkhtmltopdf
Para la conversión a PDF, es necesario instalar wkhtmltopdf:
1. Visite [wkhtmltopdf.org](https://wkhtmltopdf.org/downloads.html)
2. Descargue la versión estable para Windows (64 bits)
3. Ejecute el instalador y siga las instrucciones
4. La ruta de instalación predeterminada es `C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe`

### Paso 3: Instalar la Aplicación
1. Descomprima el archivo ZIP del conversor en la ubicación deseada
2. Abra una ventana de línea de comandos (CMD o PowerShell)
3. Navegue hasta la carpeta donde descomprimió la aplicación:
   ```
   cd ruta\a\la\carpeta\del\conversor
   ```
4. Instale las dependencias requeridas:
   ```
   pip install -r requirements.txt
   ```

## Uso de la Aplicación

### Iniciar la Aplicación
1. Abra una ventana de línea de comandos (CMD o PowerShell)
2. Navegue hasta la carpeta de la aplicación:
   ```
   cd ruta\a\la\carpeta\del\conversor
   ```
3. Ejecute la aplicación:
   ```
   python app.py
   ```

### Convertir un Archivo Markdown a PDF
1. Inicie la aplicación como se describió anteriormente
2. Haga clic en el botón "Convertir a PDF"
3. En el explorador de archivos, seleccione el archivo Markdown (.md) que desea convertir
4. La aplicación procesará el archivo y generará un PDF con el mismo nombre en la misma ubicación
5. Si ya existe un archivo PDF con el mismo nombre, se le preguntará si desea sobrescribirlo

### Convertir un Archivo Markdown a DOCX (Word)
1. Inicie la aplicación como se describió anteriormente
2. Haga clic en el botón "Convertir a DOCX"
3. En el explorador de archivos, seleccione el archivo Markdown (.md) que desea convertir
4. La aplicación procesará el archivo y generará un documento DOCX con el mismo nombre en la misma ubicación
5. Si ya existe un archivo DOCX con el mismo nombre, se le preguntará si desea sobrescribirlo

### Características de los Documentos Generados

#### Documentos PDF
- Diseño profesional con márgenes adecuados
- Tipografía legible y atractiva
- Numeración de páginas en el pie de página
- Soporte para elementos Markdown como encabezados, listas, tablas, código, etc.

#### Documentos DOCX (Word)
- Formato estructurado con estilos de Word
- Encabezados jerárquicos correctamente formateados
- Soporte para listas ordenadas y no ordenadas
- Bloques de código con formato especial
- Atribución "Hecho por Alexander Muñoz Castro" al final del documento

## Solución de Problemas

### La aplicación no inicia
- Verifique que Python esté correctamente instalado ejecutando `python --version` en la línea de comandos
- Asegúrese de haber instalado todas las dependencias con `pip install -r requirements.txt`
- Compruebe que está ejecutando la aplicación desde la carpeta correcta

### Error en la conversión a PDF
- Verifique que wkhtmltopdf esté correctamente instalado
- Compruebe que la ruta a wkhtmltopdf en el código sea correcta (línea 263 en app.py)
- Asegúrese de que el archivo Markdown no contenga caracteres especiales no soportados

### Error en la conversión a DOCX
- Asegúrese de haber instalado la biblioteca python-docx con `pip install python-docx`
- Verifique que el archivo Markdown tenga una estructura válida
- Si el error persiste, intente simplificar el contenido del archivo Markdown

## Preguntas Frecuentes

### ¿Puedo convertir varios archivos a la vez?
Actualmente, la aplicación solo permite convertir un archivo a la vez. Para procesar múltiples archivos, deberá repetir el proceso para cada uno.

### ¿Qué elementos de Markdown son compatibles?
La aplicación soporta la mayoría de los elementos estándar de Markdown, incluyendo:
- Encabezados (# a ######)
- Énfasis (negrita, cursiva)
- Listas (ordenadas y no ordenadas)
- Enlaces
- Imágenes
- Bloques de código
- Tablas
- Citas

### ¿Puedo personalizar el estilo de los documentos generados?
La personalización del estilo requiere modificar el código fuente de la aplicación. Los estilos están definidos en las secciones correspondientes del archivo app.py.

### ¿La aplicación funciona en Mac o Linux?
La aplicación está diseñada principalmente para Windows, pero puede funcionar en Mac o Linux con algunas modificaciones, principalmente en la ruta de wkhtmltopdf.

---

Para más información o soporte, contacte al desarrollador.

*Aplicación desarrollada por Alexander Muñoz Castro*
