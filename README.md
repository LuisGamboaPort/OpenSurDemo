
# Descripción

Este repositorio contiene el proyecto de demostración de pruebas automatizas de UI de OpenSur  . 

# **Instrucciones de Configuración**

# Configuración de Python

Puedes correr este demo desde cualquier sistema operativo: Windows, macOS, Linux, etc.

Este demo requiere Python 3.8 o superior. Puedes descargar la última versión de Python desde Python.org.

Este demo también requiere pipenv. Para instalar pipenv, ejecuta pip install pipenv desde la línea de comandos.

También necesitarás un editor/IDE de Python de tu elección. Buenas opciones incluyen PyCharm y Visual Studio Code.

También necesitarás Git para copiar este código de proyecto.

# Configuración de Selenium WebDriver

Para pruebas de interfaz de usuario web, necesitarás instalar las últimas versiones de Google Chrome. Puedes usar otros navegadores con Selenium WebDriver, pero el demo utilizará Chrome.

También necesitarás instalar las últimas versiones de los ejecutables de WebDriver es decir ChromeDriver para Chrome. Cada caso de prueba lanzará el ejecutable de WebDriver para su navegador objetivo. El ejecutable de WebDriver actuará como un proxy entre la automatización de pruebas y la instancia del navegador. Por favor, utiliza las últimas versiones tanto de los navegadores como de los ejecutables de WebDriver. Las versiones antiguas pueden ser incompatibles entre sí.

ChromeDriver  debe estar instalado en la ruta del sistema.

# **Configuración de WebDriver para Windows**

Para instalar ChromeDriver en Windows:

Crea una carpeta llamada `C:\Selenium`.
Mueve los ejecutables a esta carpeta.
Agrega esta carpeta a la variable de entorno Path. (Consulta Cómo agregar a la variable de entorno PATH de Windows.)
Configuración de WebDriver para *NIX

# Para instalar ChromeDriver en Linux, macOS y otras variantes de UNIX, 

Muévelos al directorio `/usr/local/bin/:`

`$ mv /ruta/a/ChromeDriver /usr/local/bin`

Este directorio ya debería estar incluido en la ruta del sistema. Para solucionar problemas, consulta:

Cómo establecer la ruta en macOS
Cómo establecer la ruta en Linux
Prueba de Configuración de WebDriver
Para verificar la configuración correcta en cualquier sistema operativo, simplemente intenta ejecutarlos desde la terminal:

`$ ChromeDriver`

Puede que veas o no algún resultado. Solo verifica que puedas ejecutarlos sin errores. Utiliza `Ctrl-C` para detenerlos.

# Configuración del Proyecto

Clona este repositorio.
Ejecuta `cd xxxxxx.py` para ingresar al proyecto.
Ejecuta `pipenv install` para instalar las dependencias.
Ejecuta `pipenv run python -m pytest` para verificar que el marco pueda ejecutar pruebas.
Crea una rama para tus cambios de código. (Consulta Ramificación del Repositorio abajo.)

# Solución de Problemas de Configuración del Proyecto

Actualiza Python a las últimas versiones. Lo siguiente funciona frecuentemente para mí:
Python 3.12 (`python --version`)
pip buscar (`pip --version`)
pipenv añadir (`pipenv --version`)
Ejecuta pipenv update desde el directorio del proyecto.
Si las actualizaciones no funcionan, intenta forzar la instalación del paquete:

Ejecuta `pipenv install pytest` desde el directorio del proyecto.
Si estos pasos no funcionan en tu proyecto, entonces intenta correr sin pipenv:

Instala los paquetes de Python directamente usando `pip`.
Ejecuta las pruebas directamente usando `python -m pytest`.

# Ramificación del Repositorio

por añadir