#Un archivo es un contenedor de informacion que contiene un formato (.png es un formato de imagen) 

#Las barras inversas sirven para buscar en una carpeta el archivo con la extencion .txt que estemos buscando y el metodo open() abre nuestro archivo y el read() lee nuestro archivo
#Usando open() para abrir un archivo con una codificacion universal (UTF-8)
archivo = open("ARCHIVOS\\texto_de_pepito.txt",encoding = "UTF-8")

#Leer archivo completo
archivo = archivo.read()

#Leer una sola linea
linea = archivo.readline()

#Leer linea por linea
lineas = archivo.readlines()

#Cerrar archivo, pero siempre que cierre el archivo tengo que volver a hacer uso de open() para poder volver a leer el archivo 
archivo.close()




