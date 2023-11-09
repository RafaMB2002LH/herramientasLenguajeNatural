import nltk
from nltk.tokenize import word_tokenize

text = word_tokenize("And from now on this will be completely different")
print(nltk.pos_tag(text))