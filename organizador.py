import os

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
        print(f"{nombre_completo} es un DOCUMENTO")
    
    elif extension == '.jpg' or extension == '.png':
        print(f"{nombre_completo} es una IMAGEN")
    
    elif extension == '.txt':
        print(f"{nombre_completo} es una NOTA DE TEXTO")
        
    else:
        print(f"{nombre_completo} es OTROS")
    
