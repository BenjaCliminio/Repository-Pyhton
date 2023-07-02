with open("ARCHIVOS\\texto_de_pepito.txt","a",encoding = "UTF-8") as archivo:
    archivo.write("\n")
    
    #Usando un bucle for range() para agregar una linea mas de una vez
    for i in range(5):
        archivo.write(" - linea 1 ")