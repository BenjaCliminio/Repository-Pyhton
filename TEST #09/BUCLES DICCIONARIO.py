diccionario = {
    "Nombre" : 'Pepito',
    "Apellido" : 'Gomez',
    "Edad" : 22
}

#Recorriendo diccionario para obtener las claves
for key in diccionario:
    key
    print(f"la clave es: {key}")

#Recorriendo diccionario con items para obtener la clave y el valor
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"La Clave es: {key} y el valor es: {value}")
    
