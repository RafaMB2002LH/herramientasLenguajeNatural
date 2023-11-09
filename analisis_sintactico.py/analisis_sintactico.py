import spacy

nlp = spacy.load("es_core_news_sm")

sentence = "El gato negro saltó sobre la valla"

doc = nlp(sentence)

for token in doc:
    print(f"Palabra: {token.text}, Parte de la oracion: {token.pos_}, Dependencia: {token.dep_}")
