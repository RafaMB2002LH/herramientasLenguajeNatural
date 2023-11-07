import requests
from bs4 import BeautifulSoup
from langdetect import detect

def getweblanguage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup=BeautifulSoup(response.content, 'html.parser')

        #Eliminar html, script, estilos, etc.
        for script in soup(['script','style']):
            script.extract()
        
        #Obtenemos texto limpio
        text = soup.get_text()
        #Detectamos el idioma
        lenguage = detect(text)

        return lenguage

    except requests.exceptions.RequestException as e:
        print(f"Error al obtener pagina: {e}")
    except Exception as e:
        print(f"Error no esperado: {e}")

def muestra():
    print('Programa que detecta el idioma de una pagina\n-------------------------------------------------')
    while True:
        url = input("Escriba la url de la pagina a detectar (0 para volver al menu):\n")
        if url == '0':
            print('\n-------------------------------------------------')
            break
        idioma = getweblanguage(url)
        print(f'-------------------------------------------------\nEl idioma de la pagina es: {idioma}\n-------------------------------------------------')

    

