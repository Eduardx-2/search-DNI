#EDUARDX-2
import requests
from bs4 import BeautifulSoup
import random
from colorama import Fore, init
#----colors----------#
init()
lwh = Fore.LIGHTWHITE_EX
v = Fore.LIGHTGREEN_EX
y = Fore.YELLOW
cyan = Fore.CYAN
mg = Fore.MAGENTA
reset = Fore.RESET

class SendRequest():

    def __init__(self):
        self.URL = "https://dniperu.online/buscador/ejemplo_ajax_proceso.php"
        self.AGENT_RANDOM = ['Mozilla/5.0 (iPad; CPU OS 13_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/107.0 Mobile/15E148 Safari/605.1.15',
                            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                            'Mozilla/5.0 (Android 13; Mobile; LG-M255; rv:107.0) Gecko/107.0 Firefox/107.0',
                            'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
                            'Mozilla/5.0 (X11; Linux i686; rv:107.0) Gecko/20100101 Firefox/107.0',
                            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
                            'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0) Gecko/20100101 Firefox/73.0',
                            'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',]
 

    def urlRequest(self):
        nombre = str(input(f"{cyan}NOMBRE {mg}>>> {lwh}")).split()
        apellido = str(input(f"{cyan}APELLIDO {mg}>>> {lwh}")).split()
        headers_session = {
          "User-Agent": random.choice(self.AGENT_RANDOM),
          "Content-Type": "application/x-www-form-urlencoded"
        }
        try:

          if len(nombre) == 1 and len(apellido) == 2:
            dataEncode = f"APE_PAT={apellido[0]}&APE_MAT={apellido[1]}&NOMBRES={nombre[0]}"
            request = requests.post(self.URL, headers=headers_session, data=dataEncode)
          elif len(nombre) == 2 and len(apellido) == 2:
            dataEncode = f"APE_PAT={apellido[0]}&APE_MAT={apellido[1]}&NOMBRES={nombre[0]}+{nombre[1]}"
            request = requests.post(self.URL, headers=headers_session, data=dataEncode)
          elif len(nombre) == 0 or len(apellido) == 0:
               print(y+"USTED NO INGRESO NADA")
               return inicio.urlRequest()

        except Exception as e:
          print(str(e))
          exit()

        response_r = BeautifulSoup(request.content, "html.parser")

        if request.status_code == 200:
           if 'COSTO : UN CAFÉ' in response_r.find_all('b')[0].text:
              print(y+"NO SE ENCONTRARON DATOS") 
           else:
              try:
                for content in response_r.find_all('b')[0:5]:
                    print(v+content.text)
              except:
                 print(reset+"OCURRIO UN ERROR")
        else:
           print("STATUS => [%d]" % (request.status_code))

inicio = SendRequest()
inicio.urlRequest()
