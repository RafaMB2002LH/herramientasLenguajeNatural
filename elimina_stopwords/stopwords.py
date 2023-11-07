import nltk
from nltk.corpus import stopwords

stopwords_espanol = stopwords.words('spanish')

def elimina_stopwords(texto):
    palabras = texto.split()

    palabras_filtradas =  []

    for palabra in palabras:
        if palabra.lower() not in stopwords_espanol:
            palabras_filtradas.append(palabra)

    texto_filtrado = ' '.join(palabras_filtradas)

    return texto_filtrado

def muestra():
    print('Programa que elimina las "stopwords" de un texto\n-------------------------------------------------')
    while True:
        texto = input('Escriba el texto a eliminar (0 para salir):\n')
        if texto == '0':
            print('\n-------------------------------------------------')
            break
        print(f'-------------------------------------------------\nAqui tiene su texto sin "stopwords":\n-------------------------------------------------\n{elimina_stopwords(texto)}\n-------------------------------------------------')
        