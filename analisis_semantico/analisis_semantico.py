import nltk
from nltk.corpus import wordnet

palabra = 'hola'
synsets = wordnet.synsets(palabra)
# Utilizamos pos=wordnet.ADJ para buscar el synset de un adjetivo

if synsets:
    synset = synsets[0]  # Tomamos el primer synset si hay varios

    print(synset.definition())
    print(synset.examples())
else:
    print(f"No se encontraron synsets para '{palabra}' en WordNet")