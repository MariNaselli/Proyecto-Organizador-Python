# Organizador de Archivos Inteligente (Híbrido)

Este proyecto es un automatizador de archivos en **Python** que combina dos potentes funciones: limpia el desorden existente apenas arranca y luego se queda vigilando en tiempo real.

## ¿Qué hace este proyecto?
Este organizador funciona en dos fases:

1. **Limpieza Retroactiva:** Al ejecutarse, escanea la carpeta y organiza todos los archivos que ya estaban ahí.
2. **Vigilancia en Tiempo Real:** Utiliza la librería `watchdog` para "escuchar" la carpeta. Si descargas o creas un archivo nuevo, el script lo detecta y lo mueve en milisegundos.

### Características:
* **Cerebro Centralizado:** Lógica de clasificación unificada para evitar errores.
* **Manejo de Duplicados:** Evita sobrescribir archivos añadiendo contadores (ej: `nota_1.txt`).
* **Soporte de Extensiones:** 
    * **PDFs** -> `Mis_PDFs/`
    * **Imágenes** (.jpg, .png) -> `Mis_Imagenes/`
    * **Notas** (.txt) -> `Mis_Notas_Texto/`
    * **Otros** -> Carpeta para archivos no clasificados.

## Demostración

### Estado Inicial (Desorden)
*La carpeta llena de archivos sueltos (.pdf, .jpg, .txt).*

![Carpeta desordenada](antes.png)

### Después: 
*El script crea las carpetas correspondientes y mueve los archivos automáticamente.*

![Carpeta organizada](después.png)

## Tecnologías utilizadas
* **Python 3.13.6**
* **Watchdog Library** (Event handler del sistema de archivos)
* **OS & Shutil** (Gestión de rutas y movimiento de archivos)

## Cómo usarlo
1. Clona este repositorio.
2. Instala la dependencia necesaria: `pip install watchdog`.
3. Ejecuta `python organizador.py`.
4. El script dirá: `Iniciando limpieza...` y luego se quedará en modo `Esperando nuevos archivos...`.