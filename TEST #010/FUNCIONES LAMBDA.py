#Es el equivalente a las funciones flechas de JavaScript, Lambda crea funciones anonimas que podemos almacenar en variables
multiplicar_por_dos = lambda x : x*2

print(multiplicar_por_dos(5)) #Las funciones lambda sirve cuando tenemos que hacer algo rapido y facil

numeros = [1,2,3,4,5,6,7,8,9]

def es_par (numeros):
    if (numeros%2==0):
        return True
    
numeros_pares = filter(es_par,numeros)

print(list(numeros_pares))