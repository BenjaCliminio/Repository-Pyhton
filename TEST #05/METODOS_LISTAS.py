lista = list([1,67,99,54,67])

cantidad_elementos = len(lista)

#Agregando un elemento a la lista
lista.append("ajaja")

#Agregando un elemento a la lista con un indice especifico
lista.insert(2,"como estas")

#Agregando varios elementos a la lista
lista.extend([False,2030])

#Eliminando un elemento de la lista (por su indice)
lista.pop(2)

#Eliminando un elemento en la lista (por su valor)
lista.remove("ajaja")

#Elimina todos los elementos de la lista
#lista.clear()

#Ordenando los elementos de la lista (de forma ascendente)
lista.sort()

#Invierte los elementos de la lista
#lista.reverse()

#Verificamos si el elemento se encuentra en la lista
elemento_encontrado = lista.index(99)

print(elemento_encontrado)