#Los bucles son sentencias controladas que nos permiten iterar los elementos iterables, Los elementos iterables son los que tienen un valor por el cual ejecutarse

animales = ["perro","gato","Loro","elefante"]
numeros = [52,16,22,55]

#Recorriendo la lista ANIMALES
for animal in animales:
    print(f"Ahora la variable animal es igual a: {animal}")
    
#Recorriendo la lista NUMEROS multiplicando la lista por 10
for numero in numeros:
    print(f"El numero es: {numero*10}")
    
#Iterando dos listas del mismo tamaño al mismo tiempo    
for numero,animal in zip(animales,numeros):
    print(f"Recorriendo lista 1: {numero}")
    print(f"Recorriendo lista 2: {animal}")
    
#Forma no optima de recorrer una lista con su indice
for num in range(10): #Si solo le paso un numero va a ir de 0 hasta la cantidad dada
    print(num)
    
#Forma correcta de recorrer una lista con su indice usando ELSE
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"El indice es: {indice} y el valor es: {valor}")
else:
    print("El bucle termino") #Siempre se muestra una vez al final del bucle, se haya ejecutado o no
    

#TODO LO ANTERIOR FUNCIONA CON LISTAS TANTO COMO CON TUPLAS


