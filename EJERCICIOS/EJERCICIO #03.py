#1 alumno es profesor, 1 alumno es asistente
#a)Pedir la edad de los compañeros que vinieron hoy a clase y ordenar los datos de menor a mayor


contador = 0

edades = []

while contador < 10:
    Cual_es_tu_edad = int(input("Cual es tu Edad? "))
    edades.append(Cual_es_tu_edad)
    contador += 1
    print(Cual_es_tu_edad)

def Mayor_a_Menor(edades):
    edades.sort()
    print(f"Las edades van de la siguiente forma: {edades}")

Mayor_a_Menor(edades)


#b)El mayor de la clase es el profesor y el menor es el asistente


contador = 0

edades = []

nombres = []


while contador < 4:
    pedir_Edad = int(input("Cual es tu Edad? "))
    pedir_Nombre = input("Cual es tu Nombre? ")
    edades.append(pedir_Edad)
    nombres.append(pedir_Nombre)
    contador += 1

def Elegir_Profesor(edades, nombres):
    menor_edad = sorted(edades)[0]  # Obtener la menor edad
    profesor_idx = edades.index(18) if 18 in edades else None
    asistente_idx = None

    if profesor_idx is None:
        asistentes_edades = [edad for edad in edades if edad != menor_edad]
        if asistentes_edades:
            asistente_idx = edades.index(sorted(asistentes_edades)[0])

    for i, nombre in enumerate(nombres):
        if i == profesor_idx:
            print(f"{nombre} es el Profesor porque es mayor de edad, tiene: {edades[i]}")
            print("-----------------------------------------")
        elif i == asistente_idx:
            print(f"{nombre} es el asistente del Profesor porque es menor de edad, tiene: {edades[i]}")
            print("-----------------------------------------")
        else:
            print(f"{nombre} no es ni el Profesor ni el asistente, van a prestar atencion")
            print("-----------------------------------------")

Elegir_Profesor(edades, nombres)

