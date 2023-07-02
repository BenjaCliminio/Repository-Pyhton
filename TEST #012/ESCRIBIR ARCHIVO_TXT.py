with open("ARCHIVOS\\texto_de_pepito.txt","w",encoding = "UTF-8") as archivo:
    
    #Reescribe un archivo
    archivo.write("HOLAAaaa\n")
    
    #Agregando 2 lineas al archivo con writelines()
    archivo.writelines([" - Hola Como estas\n"," - Yo todo bien"])