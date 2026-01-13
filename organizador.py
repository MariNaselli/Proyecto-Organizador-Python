import os
import shutil

#Creamos una función para el proceso de preguntar si existe la carpeta, crearla y mover el archivo

def mover_a_carpeta (archivo, carpeta):
    if not os.path.exists(carpeta):
        os.mkdir(carpeta)
        print(f"Carpeta creada {carpeta}")
        
    shutil.move(archivo, carpeta)
    print(f"{archivo} --> {carpeta}")
    
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
        mover_a_carpeta(nombre_completo, 'Mis_PDFs')
        # carpeta_destino = 'Mis_PDFs' #Definimos nombre de la carpeta
        
        # if not os.path.exists(carpeta_destino): #Si la carpeta no existe la creamos
        #     os.mkdir(carpeta_destino)
        #     print(f"Carpeta {carpeta_destino} creada")
            
        # shutil.move(nombre_completo, carpeta_destino) #Movemos el archivo a esa carpeta
        # print(f"Moved: {nombre_completo} --> {carpeta_destino}")
    
    elif extension == '.jpg' or extension == '.png':
         mover_a_carpeta(nombre_completo, 'Mis_Imagenes')
    
    elif extension == '.txt':
         mover_a_carpeta(nombre_completo, 'Mis_Notas_Texto')
        
    else:
         mover_a_carpeta(nombre_completo, 'Otros')
    
