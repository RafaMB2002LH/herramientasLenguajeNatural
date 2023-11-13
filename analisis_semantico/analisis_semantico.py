import nltk
from nltk.corpus import wordnet

def muestra():
    print("'Herramienta que analiza semanticamente una palabra (en ingles)\n-------------------------------------------------'")
    while True:

        inp = input("Escriba la palabra a analizar (0 para volver al menu):\n")

        if inp == '0':
            print('\n-------------------------------------------------')
            break

        synsets = wordnet.synsets(inp)
        # Utilizamos pos=wordnet.ADJ para buscar el synset de un adjetivo

        if synsets:
            synset = synsets[0]  # Tomamos el primer synset si hay varios

            print(f'-------------------------------------------------\nDefinicion:\n{synset.definition()}\n')
            print(f'Ejemplos:\n{synset.examples()}\n-------------------------------------------------')
        else:
            print(f"No se encontraron synsets para '{inp}' en WordNet")