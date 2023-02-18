import os

#Ruta del directorio
path = 'C:\\Users\\Alejandro\\Downloads\\Historico_recibos\\'

#Lista vacía para almacenar archivos
files = []

#Utilizamos os.walk para recorrer la ruta
for ruta, directorio, archivo in os.walk(path):
   for file in archivo:
       if file.endswith('.txt') and file.startswith('REC_03'):
           files.append(os.path.join(ruta,file))

#Creamos el archivo a partir de los archivos encontrados
with open('unido.txt', 'w') as file:
   for f in files:
       with open(f, 'r') as archivo:
           file.write(archivo.read() + '\n')