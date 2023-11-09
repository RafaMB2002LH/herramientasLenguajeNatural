from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

lemmatizer = WordNetLemmatizer()

def lemmatize_sentence(sentence):
    words = word_tokenize(sentence)
    lemmatized_words = [lemmatizer.lemmatize(word, pos='v') for word in words]
    lemmatized_sentence = ' '.join(lemmatized_words)
    return lemmatized_sentence

def muestra():
    print('Programa que lematiza una oracion EN INGLES\n-------------------------------------------------')
    while True:
        
        sentence = input("Introduzca la oracion que desea lematizar (0 para volver al menu):\n")
        if sentence == '0':
            print('\n-------------------------------------------------')
            break
        lemmatized_sentence = lemmatize_sentence(sentence)

        print(f'-------------------------------------------------\nOración original: {sentence}')
        print(f'Oración lematizada: {lemmatized_sentence}\n-------------------------------------------------')
