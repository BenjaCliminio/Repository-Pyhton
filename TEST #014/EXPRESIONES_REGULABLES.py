import re

text = '''Hola Pepito. como estas. esta es la cadena. 1'''

#Haciendo una busqueda simple
resultado = re.findall("Hola",text)

#Haciendo una busqueda de digitios numericos del 0-9
resultado2 = re.findall(r"\d",text)

#Haciendo una busqueda y devolviendo todo menos los digitos numericos del 0-9
resultado3 = re.findall(r"\D",text)

#Haciendo una busqueda y devolviendo caracteres alfanumericos (a-z A-Z 0-9)
resultado4 = re.findall(r"\w",text)

#Haciendo una busqueda y devolviendo caracteres menos los alfanumericos (a-z A-Z 0-9)
resultado5 = re.findall(r"\W",text) #Devuelve una cadena vacia

#Haciendo una busqueda y devolviendo los espacio en blanco (espacios, tabs, saltos de linea)
resultado6 = re.findall(r"\s",text)

#Haciendo una busqueda y devolviendo todo menos los espacio en blanco (espacios, tabs, saltos de linea)
resultado7 = re.findall(r"\S",text)

#Haciendo una busqueda y devolviendo todo menos saltos en linea
resultado8 = re.findall(r".",text)

#Haciendo una busqueda y devolviendo los saltos en linea
resultado9 = re.findall(r"\n",text)

#\ Cancela los caracteres especiales, en este caso cancelando la funcion del . y buscando todos los . de la cadena
resultado10 = re.findall(r"\.",text)

#Busca el comienzo de una linea
resultado11 = re.findall(r"ʌ",text)


print(resultado11)