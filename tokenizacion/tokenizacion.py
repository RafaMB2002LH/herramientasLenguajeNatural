from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

# Tokenizar a nivel de palabra
oracion = "Esta es una frase de ejemplo. Buenas tardes!"
tokens_oracion = word_tokenize(oracion)
print(tokens_oracion)
#tokenizar a nivel de oracion
print(sent_tokenize(oracion))
