import csv #Nos permite leer archivos CSV

with open("ARCHIVOS\\datos.csv") as archivo:
    reader = csv.reader(archivo)
    for row in reader: #Lee fila por fila
        print(row)
    