import os
import shutil

archivos = os.listdir('.') # solicitamos lista de archivos en esta misma carpeta
print(archivos)

for nombre_completo in archivos:
    
    if os.path.isdir(nombre_completo) or nombre_completo in ['organizador.py', 'README.md', '.gitignore']:
        continue
    nombre, extension = os.path.splitext(nombre_completo)
    extension = extension.lower()
    #la herramienta os.path.splitext separa el nombre de la extensión. Busca el último punto de derecha a izquierda.
    print(f"Archivo: {nombre} | Extensión: {extension}")
    
    if extension == '.pdf':
        carpeta_destino = 'Mis_PDFs' #Definimos nombre de la carpeta
        
        if not os.path.exists(carpeta_destino): #Si la carpeta no existe la creamos
            os.mkdir(carpeta_destino)
            print(f"Carpeta {carpeta_destino} creada")
            
        shutil.move(nombre_completo, carpeta_destino) #Movemos el archivo a esa carpeta
        print(f"Moved: {nombre_completo} --> {carpeta_destino}")
    
    elif extension == '.jpg' or extension == '.png':
        print(f"{nombre_completo} es una IMAGEN")
    
    elif extension == '.txt':
        print(f"{nombre_completo} es una NOTA DE TEXTO")
        
    else:
        print(f"{nombre_completo} es OTROS")
    
