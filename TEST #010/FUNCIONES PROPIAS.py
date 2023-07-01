#Creando una funcion
def Greeting ():
    print("Hola, como estas")
    
#Ejecutando una funcion simple
Greeting()

#Funcion usando parametros
def Greeting (nombre, sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "Mujer"
    elif (sexo == "hombre"):
        adjetivo = "Hombre"
    else: 
        adjetivo = "No lo se"
        
    print(f"Hola {nombre}, me identidfico como: {adjetivo}, Vos como estas??")
    
Greeting ("Susana","mujer")

#Crear una funcion que nos retorne Valores
def crear_contraseña_aleatoria (num):
    chars = "abcdefghijk"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num + 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña #La funcion en si puede haber sido bastante compleja pero lo importante es mostrar que hay que retornar valores
    
password = crear_contraseña_aleatoria(1)
frase = f"Tu nueva contraseña es: {password}"
print(frase)