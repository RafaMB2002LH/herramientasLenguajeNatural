import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

lemmatizer = WordNetLemmatizer()

def lemmatize_sentence(sentence):
    words = word_tokenize(sentence)
    lemmatized_words = [lemmatizer.lemmatize(word, pos='v') for word in words]
    lemmatized_sentence = ' '.join(lemmatized_words)
    return lemmatized_sentence

sentence = "I am running in the park"
lemmatized_sentence = lemmatize_sentence(sentence)

print(f'Oración original: {sentence}')
print(f'Oración lematizada: {lemmatized_sentence}')