#Crear diccionario con dict()
diccionario = dict(nombre="Pepito",apellido="Gomez")

#Las listas no pueden se claves y usamos frozenset para meter conjuntos
diccionario = {frozenset({"pepito","malo"}):"jajaja"}

#Creando diccionario con fromkeys() con dos parametros
diccionario = dict.fromkeys(["Nombre","Apellido"])

#Creando diccionario con fromkeys() cambiando el avalor por defecto a "No se" en vez de None
diccionario = dict.fromkeys(["Nombre","Apellido"],"No se")

print(diccionario)