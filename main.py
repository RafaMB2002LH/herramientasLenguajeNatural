import detecta_idioma_web.detecta_idioma as diw
import elimina_signos_tweet.elimina_signos as est
import elimina_stopwords.stopwords as es
import lematizacion.lematizacion_english as lematizacion
import stemming.stemming as stemming
import tokenizacion.tokenizacion as tokenizacion
import analisis_lexico.analisis_lexico as alex
import analisis_sintactico.analisis_sintactico as asin
import analisis_semantico.analisis_semantico as asem
import texto_a_voz.tts as tts

if __name__=='__main__':
    #Menu
    while True:
        print('Elija la herramienta que quiere utilizar:\n- 0 --> Salir\n- 1 --> Detector de idioma de una web\n- 2 --> Eliminador de signos de un texto\n- 3 --> Eliminador de "stopwords" de un texto\n- 4 --> Lematizacion\n- 5 --> Stemming\n- 6 --> Tokenizacion\n- 7 --> Analisis lexico\n- 8 --> Analisis sintactico\n- 9 --> Analisis semantico\n- 10 -> Texto a voz')
        opc = input('Escriba la opcion de herramienta que quiere utilizar: ')
        print('\n-------------------------------------------------')

        if opc =='0':
            break
        elif opc == '1':
            diw.muestra()
        elif opc == '2':
            est.muestra()
        elif opc == '3':
            es.muestra()
        elif opc == '4':
            lematizacion.muestra()
        elif opc == '5':
            stemming.muestra()
        elif opc == '6':
            tokenizacion.muestra()
        elif opc == '7':
            alex.muestra()
        elif opc == '8':
            asin.muestra()
        elif opc == '9':
            asem.muestra()
        elif opc == '10':
            tts.muestra()
        else:
            print('Opcion no valida, escriba una opcion de herramienta valida')

    