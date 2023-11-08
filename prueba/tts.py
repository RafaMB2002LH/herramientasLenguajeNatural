import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 120)
engine.setProperty('voice', 'spanish')
engine.setProperty('volume', 1)
texto = input("Escriba el texto:\n")
engine.say(texto)
engine.runAndWait()