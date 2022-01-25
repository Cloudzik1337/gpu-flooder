
from random import randint
import colorama
import os
import threading
from threading import Lock


"""
github.com/Cloudzik1337  
github.com/Cloudzik1337  
github.com/Cloudzik1337  

Procesor Flooder based on os.urandom()
I don't recomend going higher than 500 threads it may freeze windows.
Im not responsible how u will use code

Feel free to edit code cuz its very easy
Please if u copy code u can add

"""



lock = Lock()
def save_print(*args, **kwargs):
  with lock:
    print(*args, **kwargs) # Part to avoid both threads printing in same line
os.system('cls')
colorama.init(autoreset=True) #Auto reset color after new line

def autro():
    print(colorama.Fore.GREEN + '''################################
#   github.com/Cloudzik1337    #
################################
# Welcome to processor flooder #
################################''')



autro()
threads_amount = input(colorama.Fore.YELLOW+'Enter amounts of threads $')


def work():
    while True:
        string = os.urandom(randint(432544, 43242342)).hex()  #Size of byte converted to hex
        save_print(colorama.Fore.LIGHTYELLOW_EX + 'Generated '+colorama.Fore.RED+str(len(string))+colorama.Fore.RESET+colorama.Fore.YELLOW+' long string')

for _ in range(int(threads_amount)):
    threading.Thread(target=work).start()
save_print('Activated', threading.active_count(), 'threads')