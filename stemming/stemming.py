import nltk
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize

# Añade esta línea para importar SnowballStemmer
stemmer = SnowballStemmer("spanish")

def lemmatize_sentence(sentence):
    words = word_tokenize(sentence, language='spanish')
    lemmatized_words = [stemmer.stem(word) for word in words]
    lemmatized_sentence = ' '.join(lemmatized_words)
    return lemmatized_sentence

sentence = "Estoy corriendo en el parque"
lemmatized_sentence = lemmatize_sentence(sentence)

print(f'Oración original: {sentence}')
print(f'Oración lematizada: {lemmatized_sentence}')
