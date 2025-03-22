# Markdown a PDF Converter

Aplicación de escritorio para convertir archivos Markdown a PDF con estilos profesionales.

## Características

- Interfaz gráfica fácil de usar
- Estilos profesionales para el PDF generado
- Soporte para tablas, código y citas
- Numeración automática de páginas
- Encabezados y pies de página personalizados

## Requisitos previos

1. **Python 3.8 o superior**
   - Descarga e instala Python desde [python.org](https://www.python.org/downloads/)
   - Asegúrate de marcar la opción "Add Python to PATH" durante la instalación

2. **wkhtmltopdf**
   - Descarga wkhtmltopdf desde [wkhtmltopdf.org](https://wkhtmltopdf.org/downloads.html)
   - Instala en la ruta predeterminada: `C:\Program Files\wkhtmltopdf`
   - Asegúrate de que el ejecutable esté en: `C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe`

## Instalación

1. Clona o descarga este repositorio

2. Abre una terminal en la carpeta del proyecto

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Ejecuta la aplicación:
   ```bash
   python app.py
   ```

2. La interfaz gráfica se abrirá automáticamente

3. Haz clic en el botón "Seleccionar archivo Markdown"

4. Selecciona tu archivo .md

5. El PDF se generará automáticamente en la misma ubicación que el archivo Markdown

## Formato Markdown soportado

La aplicación soporta las siguientes características de Markdown:

- Encabezados (# h1, ## h2, etc.)
- Texto en **negrita** y *cursiva*
- Listas ordenadas y no ordenadas
- Enlaces e imágenes
- Tablas
- Bloques de código con resaltado
- Citas
- Líneas horizontales

## Ejemplo de uso

Para probar la aplicación, puedes crear un archivo `ejemplo.md` con el siguiente contenido:

```markdown
# Mi Documento

## Introducción
Este es un ejemplo de documento Markdown.

## Características
- Soporte para **negrita**
- Soporte para *cursiva*
- Soporte para `código`

## Tabla de ejemplo
| Columna 1 | Columna 2 |
|-----------|-----------|
| Celda 1   | Celda 2   |
| Celda 3   | Celda 4   |

## Código
```python
def hello_world():
    print("¡Hola, mundo!")
```

> Este es un ejemplo de una cita.

## Solución de problemas

1. **Error: No se encuentra wkhtmltopdf**
   - Verifica que wkhtmltopdf esté instalado en `C:\Program Files\wkhtmltopdf`
   - Asegúrate de que el ejecutable esté en la ruta correcta

2. **Error: No se pueden instalar las dependencias**
   - Verifica tu conexión a internet
   - Asegúrate de tener Python correctamente instalado
   - Intenta ejecutar pip con privilegios de administrador

3. **Error: El PDF no se genera**
   - Verifica que el archivo Markdown tenga extensión .md
   - Asegúrate de tener permisos de escritura en la carpeta

## Contribuir

Si encuentras algún error o tienes sugerencias de mejora, no dudes en crear un issue o enviar un pull request.
