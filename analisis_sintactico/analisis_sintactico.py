import spacy

def muestra():
    print("Programa que analiza sintacticamente una oracion\n-------------------------------------------------")
    while True:
        inp = input("Escriba la oracion a analizar (0 para volver al menu):\n\n")
        nlp = spacy.load("es_core_news_sm")
        doc = nlp(inp)

        print("-------------------------------------------------\nAnalisis sintactico:\n")
        for token in doc:
            print(f"Palabra: {token.text}, Parte de la oracion: {token.pos_}, Dependencia: {token.dep_}")
        print("\n-------------------------------------------------")
