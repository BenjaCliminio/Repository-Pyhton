#Esta es la forma mas optima para abrir y leer un archivo por que consume menos recursos, es mas rapido, es mas optimo

#Abriendo el archivo con with open
with open("ARCHIVOS\\texto_de_pepito.txt",encoding="UTF-8") as archivo:
    
    #Leemos el archivo
    contenido = archivo.read()
    
    #Mostramos el archivo
    print(contenido)