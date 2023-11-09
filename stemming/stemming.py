from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize

# Añade esta línea para importar SnowballStemmer
stemmer = SnowballStemmer("spanish")

def lemmatize_sentence(sentence):
    words = word_tokenize(sentence, language='spanish')
    lemmatized_words = [stemmer.stem(word) for word in words]
    lemmatized_sentence = ' '.join(lemmatized_words)
    return lemmatized_sentence

def muestra():
    while True:

        sentence = input("Introduzca la oracion que desea hacer stemming (0 para volver al menu)\n")
        if sentence == '0':
            print('\n-------------------------------------------------')
            break

        lemmatized_sentence = lemmatize_sentence(sentence)

        print(f'-------------------------------------------------\nOración original: {sentence}')
        print(f'Oración con stemming: {lemmatized_sentence}\n-------------------------------------------------')
