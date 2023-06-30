#While es una bucle al igual que For, pero a diferencia de For el bucle While se va a ejecutar siempre que una condicion sea verdadera de manera infinita (por ejemplo si un numero es menor a 5 y es True se va a ejecutar)

contador = 0

while contador < 16: #El numero que pongamos a aca va a ser la cantidad de veces que el bucle se repita (en este caso se va a ejecutar del 0 al 16)
    print(contador)
    contador += 1 #Si no estuviera esta linea de codigo el bucle seria al infinito
print("El while llego a su fin")

