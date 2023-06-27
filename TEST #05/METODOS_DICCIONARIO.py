diccionario = {
     #keys        valor
     "nombre" : 'pepito',
     #keys          valor
     "apellido" : 'gomez',
     #keys    valor
     "edad" : 23
}

#Mostrar las keys
claves = diccionario.keys()

#Accede a la propiedad de un elemento
#claves = diccionario.get()

#Elimina todos los elementos del diccionario
#claves = diccionario.clear()

#Elimina un elemento del del diccionario
#diccionario.pop("edad")

#Obteniendo unn elemento dict_items iterable. (Key | valor)
diccionario_iterable = diccionario.items()

print(diccionario_iterable)