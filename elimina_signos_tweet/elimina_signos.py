import re

def quita_puntuacion(tweet):

    tweet= tweet.lower()
    tweet = re.sub(r'[^\w\s]','', tweet)

    return tweet

def muestra():
    print('Programa que elimina los signos de un texto (como un tweet)\n-------------------------------------------------')
    while True:
        tweet = input('Escriba el texto (0 para volver al menu):\n')
        if tweet == '0':
            print('\n-------------------------------------------------')
            break
        print(f'-------------------------------------------------\nEste es tu texto limpio:\n--------------------------------------\n{quita_puntuacion(tweet)}\n-------------------------------------------------')
        