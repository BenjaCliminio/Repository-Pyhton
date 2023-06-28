#Calcular las cantidad de palabras que dice una persona y decirle cuanto tardaria en decirlas y cuanto tardaria una persona que habla un 30% mas rapido y si esta persona dice mas de 120 palabras decirle que hable menos

#Pedirle la frase al usuario
frase = input("Decime una frase y calculo cuanto tardarias en decirla: ")

#Creando una lista donde van las palabras (se separa cada vez que hay un espacio en blanco)
palabras_separadas = frase.split(" ")

#Viendo la cantidad de palabras de la lista
cantidad_de_palabras = len(palabras_separadas)

#Si tarda mas de un minuto le decimos que hable menos
if cantidad_de_palabras > 120:
    print("Habla un poco menos")

#Calculamos cuanto tardaria en decirla la palabras y se lo decimos
print(f"Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo")
print(f"Pero una persona que habla mas rapido lo diria en: {cantidad_de_palabras * 100 // 2 *1.3 / 100} segundos en decirlo")

