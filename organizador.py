import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def mover_a_carpeta(archivo, carpeta):
    if not os.path.exists(carpeta):
        os.mkdir(carpeta)

    ruta_destino = os.path.join(carpeta, archivo)
    contador = 1

    while os.path.exists(ruta_destino):
        nombre, extension = os.path.splitext(archivo)
        nuevo_nombre = f"{nombre}_{contador}{extension}"
        ruta_destino = os.path.join(carpeta, nuevo_nombre)
        contador += 1

    shutil.move(archivo, ruta_destino)
    print(f"{archivo} --> {ruta_destino}")


def clasificar_y_organizar(archivo):
    nombre, extension = os.path.splitext(archivo)

    extension = extension.lower()

    if extension == '.pdf':
        mover_a_carpeta(archivo, 'Mis_PDFs')

    elif extension == '.jpg' or extension == '.png':
        mover_a_carpeta(archivo, 'Mis_Imagenes')
    elif extension == '.txt':
        mover_a_carpeta(archivo, 'Mis_Notas_Texto')
    else:
        mover_a_carpeta(archivo, 'Otros')


def limpiar_archivos():
    print("Iniciando limpieza de archivos existentes")
    archivos = os.listdir('.')

    for nombre_completo in archivos:
        if os.path.isdir(nombre_completo) or nombre_completo in ['organizador.py', 'README.md', '.gitignore', 'antes.png', 'despues.png']:
            continue

        clasificar_y_organizar(nombre_completo)


class OrganizadorHandler (FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        nombre_archivo = os.path.basename(event.src_path)
        time.sleep(1)

        clasificar_y_organizar(nombre_archivo)


if __name__ == "__main__":
    limpiar_archivos()

    event_handler = OrganizadorHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)

    observer.start()
    print("Esperando archivos nuevos... ")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("Programa Apagado")

    observer.join()
