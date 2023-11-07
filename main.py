import detecta_idioma_web.detecta_idioma as diw
import elimina_signos_tweet.elimina_signos as est
import elimina_stopwords.stopwords as es

if __name__=='__main__':
    while True:
        print('Elija la herramienta que quiere utilizar:\n- 1 --> Detector de idioma de una web\n- 2 --> Eliminador de signos de un texto\n- 3 --> Eliminador de "stopwords" de un texto\n- 4 --> Salir')
        opc = input('Escriba la opcion de programa que quiere utilizar: ')
        print('\n-------------------------------------------------')

        if opc == '1':
            diw.muestra()
        elif opc == '2':
            est.muestra()
        elif opc == '3':
            es.muestra()
        elif opc == '4':
            break
        else:
            print('Opcion no valida, escriba una opcion de programa valida')

    