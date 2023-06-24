cadena1 = "alfajor,tazaa"
cadena2 = f"Bienvenido {cadena1}"

#Convierte a mayuscula
mayusc = cadena1.upper()

#Convierte a minuscula
minusc = cadena1.lower()

#Primera letra Mayuscula
primer_letra_mayusc = cadena1.capitalize()

#Buscamos una cadena dentro de otra cadena #Me devuelve el indice donde esta la cadena, si la cadena no esta devuelve -1
busqueda_find = cadena1.find("p")

busqueda_indice = cadena1.index("")
#La diferencia entre FIND y INDEX es que si en FIND no se encuentra la cadena devuelve -1 y en INDEX devuelve un error

#si es numero devuelve TRUE, sino devuelve FALSE

es_numero = cadena1.isnumeric()

#Devuelve la cantidad de coincidencias dentro de una cadena

contar_coincidencias = cadena1.count("a")  

#Devuelve cuantos caracteres tiene una cadena

contar_caracteres = len(cadena1)  

#Verificamos si una cadena empieza con otra cadena dada, si es asi devuelve True
 
empieza_con = cadena1.startswith("a")

#Verificamos si una cadena termina con otra cadena dada, si es asi devuelve True

termina_con = cadena1.endswith("aa")

#Remplaza un pedazo de la cadena dada, por otra, primero se escribe la palabra que quiero reemplazar y despues por la que lo quiero reemplazar("tazaa", "tazon")

cadena_nueva = cadena1.replace("tazaa", "tazon")

#Separar cadenas con la cadena que le pasemos, y devuelve una lista con las cadena separadas

cadena_separada = cadena1.split(",")

print(cadena_separada)
