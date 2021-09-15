from os import system, name
from time import sleep
import random

def cls():
    _ = system('cls')

while True:
    cls()
    print('Random Number Generator')
    print('')
    min = input('Minimum: ')
    max = input('Maximum: ')
    a = (random.randint(int(min),int(max)))
    b = 0
    cls()
    
    while a is not b:
        cls()
        while a - 10 > b:
            b = (b)+10
            if a is b:
                sleep(0.1)
        else:
            b = (b)+1
        print(b)

    cls
    print(a)
    if a is (69):
        sleep(1)
        print('Nice.')
        sleep(1)
    input("Press Enter to continue...")