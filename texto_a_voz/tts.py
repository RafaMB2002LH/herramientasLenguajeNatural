import pyttsx3

def muestra():
    print("Herramienta que convierte el texto a voz\n-------------------------------------------------'")
    while True:
        inp = input("Escriba el texto (0 para salir):\n\n")

        if inp == '0':
            print('\n-------------------------------------------------')
            break

        engine = pyttsx3.init()
        engine.setProperty('rate', 120)
        engine.setProperty('voice', 'spanish')
        engine.setProperty('volume', 1)
        print("-------------------------------------------------\nHablando...\n-------------------------------------------------")
        engine.say(inp)
        engine.runAndWait()