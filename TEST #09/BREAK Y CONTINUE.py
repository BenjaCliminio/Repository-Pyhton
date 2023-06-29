frutas = ["Granada","Banana","Frutilla","Pera","Durazno"]

#Evitamos que se coma una fruta con la sentencia continue
for fruta in frutas:
    if fruta == "Granada":
        continue
    print(f"Me comi una: {fruta}")
    
#Evitar que el bucle siga ejecutandose
for fruta in frutas:
    if fruta == "Frutilla":
        break
    print(f"Me voy a  comer una: {fruta}")