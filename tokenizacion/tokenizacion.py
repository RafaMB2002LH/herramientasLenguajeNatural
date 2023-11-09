from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

def muestra():
    print('Herramienta que tokeniza una oracion\n-------------------------------------------------')
    while True:

        inp = input("Escriba la oracion a tokenizar (0 para volver al menu):\n")

        if inp == '0':
            print('\n-------------------------------------------------')
            break

        # Tokenizar a nivel de palabra
        print(f'-------------------------------------------------\nTokenizacion a nivel de palabra:\n{word_tokenize(inp)}')
        #tokenizar a nivel de oracion
        print(f'Tokenizacion a nivel de oracion:\n{sent_tokenize(inp)}\n-------------------------------------------------')
