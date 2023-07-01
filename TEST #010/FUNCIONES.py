#Nos permite separar el programa en partes para poder ir modificando y llamar a la funcion en el lugar especifico, permite un codigo mas legible para poder depurar

#Encontrar el numero mayor de una lista
lista = [4,7,5,3,24]
numeros_mas_alto = max(lista)
print(numeros_mas_alto)

#Encontrar el numero mas bajo de una lista
numeros_mas_bajo = min(lista)
print(numeros_mas_bajo)

#Redondear a 6 decimales con round()
numero = round(12.4577,2)
print(numero)

#Retornar False -> 0, vacio, False, None / True -> distinto a 0, True, Cadena, Datos no vacio
resultado_bool = bool(None)
print(resultado_bool)

#Retorna True, si todos los valores son correctos
resultado_all = all([0,"true",[344,23]])
print(resultado_all)

#Suma todos los numeros de un iterable
numeros = [2,3,4,4,5]
suma_total = sum(numeros)
print(suma_total)

