import spacy

# Cargar el modelo de lenguaje de spaCy
nlp = spacy.load("es_core_news_sm")

# MENU
fideos = 1500
carne = 2300
vino = 2000
agua = 600

# ORDENES
def ordenes():
    pedido = input("Hola, Mucho gusto, ¿qué le gustaría pedir? ")
    productos = []  # Lista para almacenar los productos del pedido

    # Realizar análisis sintáctico utilizando spaCy
    doc = nlp(pedido)

    # Verificar cada token en el análisis sintáctico
    for token in doc:
        if token.pos_ == "NOUN":
            productos.append(token.text)

    if len(productos) > 0:
        print("Su pedido es:", ", ".join(productos))
    else:
        print("Lo siento, no hemos entendido su pedido correctamente.")

ordenes()
