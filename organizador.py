import os
import shutil
import time


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


print("-- Organizador encendido --")

while True:

    archivos = os.listdir('.')
    print(archivos)

    for nombre_completo in archivos:

        if os.path.isdir(nombre_completo) or nombre_completo in ['organizador.py', 'README.md', '.gitignore']:
            continue
        nombre, extension = os.path.splitext(nombre_completo)
        extension = extension.lower()

        print(f"Archivo: {nombre} | Extensión: {extension}")

        if extension == '.pdf':
            mover_a_carpeta(nombre_completo, 'Mis_PDFs')

        elif extension == '.jpg' or extension == '.png':
            mover_a_carpeta(nombre_completo, 'Mis_Imagenes')

        elif extension == '.txt':
            mover_a_carpeta(nombre_completo, 'Mis_Notas_Texto')

        else:
            mover_a_carpeta(nombre_completo, 'Otros')

    # El programa cada 10 segundos revisa si hay archivos por organizar
    time.sleep(10)
