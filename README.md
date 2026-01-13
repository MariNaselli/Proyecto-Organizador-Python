# Organizador de Archivos Inteligente

Automatización en Python diseñada para la clasificación de archivos y el monitoreo de carpetas en tiempo real.

# Funcionalidades

** Gestión Híbrida: Organiza los archivos presentes al iniciar el proceso y mantiene un monitoreo constante para nuevas incorporaciones.

** Infraestructura Dinámica: El script genera automáticamente las carpetas de destino si no se encuentran en el directorio.

**Integridad de Datos: Implementa un sistema de numeración para evitar la sobrescritura en caso de nombres duplicados (ej: archivo_1.pdf).

** Filtro de Exclusión: Protege el código fuente, la documentación y archivos de sistema para asegurar la estabilidad del entorno.

# Categorización

** Documentos PDF → Mis_PDFs/
** Imágenes (.jpg, .png) → Mis_Imagenes/
** Archivos de Texto (.txt) → Mis_Notas_Texto/
** Otros Formatos → Otros/

# Demostración

** Estado Inicial (Sin organizar)
*Vista de la carpeta antes de ejecutar el script.*

![Estado inicial](antes.png)

** Estado Final (Organización aplicada)
*Resultado tras la clasificación automática.*

![Estado final](despues.png)

# Tecnologías

** Python 3.13.6
** Watchdog Library (Gestión de eventos del sistema de archivos)
** OS & Shutil (Procesamiento de rutas y transferencia de datos)

# Uso

** Instalar dependencia: pip install watchdog
**Ejecutar: python organizador.py
