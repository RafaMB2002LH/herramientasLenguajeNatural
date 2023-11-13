import nltk
from nltk.tokenize import word_tokenize

def muestra():
    print("Programa que hace el analis lexico de una oracion (en ingles)\n-------------------------------------------------")
    while True:
        inp = input("Escriba la oracion a analizar (0 para volver al menu):\n")

        if inp == '0':
            print('\n-------------------------------------------------')
            break

        text = word_tokenize(inp)
        print(f'-------------------------------------------------\nAnalisis lexico:\n{nltk.pos_tag(text)}\n-------------------------------------------------')