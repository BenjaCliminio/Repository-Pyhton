#Crear conjunto con set()

conjunto = set(["Dato1","Dato2"])

print(conjunto)

#Teoria de conjuntos
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#Verificamos si es un subconjuno
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

#Verificamos si es un superconjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1

#Verificamos si hay algun numero en comun
resultado = conjunto2.isdisjoint(conjunto1)

print(resultado)