#indices       0           1         2    3
lista = ["pepito","pepitoyt",True,1.98]
tupla = ("pepito","pepitoyt",True,1.98) #Son datos que no pueden ser cambiados
conjunto = {"pepito","pepitoyt",True,1.98,"pepitoyt"} #No puede haber datos duplicados y no se accede a elementos por su indice

#Esto es valido, Muestra "Maquinola"
lista[3] = "Maquinola"

#Esto no es valido
#tupla[3] = "Maquinola2"

#Creando un diccionario (dict)
diccionario = {
     'nombre' : "pepito",
     'canal' : "pepitoyt",
     'esta_emocionado' : True,
     'altura' : 1.98,
     'dato_duplicado' : "pepitoyt"
}

print(diccionario['altura'])

print(conjunto[0]) # -> NO SE PUEDE HACER