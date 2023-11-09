import detecta_idioma_web.detecta_idioma as diw
import elimina_signos_tweet.elimina_signos as est
import elimina_stopwords.stopwords as es
import lematizacion.lematizacion_english as lematizacion

if __name__=='__main__':
    #Menu
    while True:
        print('Elija la herramienta que quiere utilizar:\n- 1 --> Detector de idioma de una web\n- 2 --> Eliminador de signos de un texto\n- 3 --> Eliminador de "stopwords" de un texto\n- 4 --> Lematizacion\n- 5 --> Stemming\n- 6 --> Tokenizacion\n- 7 --> Analisis lexico\n- 8 --> Analisis sintactico\n- 9 --> Analisis semantico\n- 10 -> Texto a voz\n- 11 -> Salir')
        opc = input('Escriba la opcion de programa que quiere utilizar: ')
        print('\n-------------------------------------------------')

        if opc == '1':
            diw.muestra()
        elif opc == '2':
            est.muestra()
        elif opc == '3':
            es.muestra()
        elif opc == '4':
            lematizacion.muestra()
        elif opc == '5':
            print("En proceso")
        elif opc == '6':
            print("En proceso")
        elif opc == '7':
            print("En proceso")
        elif opc == '8':
            print("En proceso")
        elif opc == '9':
            print("En proceso")
        elif opc == '10':
            print("En proceso")
        elif opc == '11':
            print("En proceso")
        elif opc == '12':
            break
        else:
            print('Opcion no valida, escriba una opcion de programa valida')

    