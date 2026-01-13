import os

archivos = os.listdir('.') # solicitamos lista de archivos en esta misma carpeta
print(archivos)

for nombre_completo in archivos:
    nombre, extension = os.path.splitext(nombre_completo)
    #la herramienta os.path.splitext separa el nombre de la extensión
    print(f"Archivo: {nombre} | Extensión: {extension}")
    
