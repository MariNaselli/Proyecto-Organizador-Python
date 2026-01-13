# Organizador de Archivos en Tiempo Real (Watchdog)

Este proyecto es un script de **Python** que vigila una carpeta específica y organiza automáticamente los archivos nuevos según su extensión. 

## ¿Qué hace este proyecto?
El script utiliza la librería `watchdog` para detectar eventos de creación de archivos. No necesita ser ejecutado repetidamente; una vez encendido, se queda "escuchando" y actúa al instante.

### Características:
* **Automatización total:** Detecta archivos nuevos en milisegundos.
* **Manejo de duplicados:** Si un archivo ya existe, le añade un contador (ej: `foto_1.jpg`) para no sobrescribir nada.
* **Clasificación inteligente:** Separa PDFs, Imágenes y Notas de texto en carpetas independientes.

## Demostración
> **[Capturas de pantalla"]**

### Estado Inicial (Desorden)
*La carpeta llena de archivos sueltos (.pdf, .jpg, .txt).*
![Carpeta desordenada](antes.png)

### Después: 
*El script crea las carpetas correspondientes y mueve los archivos automáticamente.*

## Tecnologías utilizadas
* **Python 3.13.6**
* **Watchdog Library** (para la vigilancia de eventos del sistema)
* **Shutil & OS** (para la manipulación de archivos y rutas)

## Cómo usarlo
1. Clona este repositorio.
2. Instala la dependencia necesaria: `pip install watchdog`.
3. Ejecuta `python organizador.py`.
4. ¡Empieza a descargar o mover archivos a la carpeta y mira cómo se organizan solos!