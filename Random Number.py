from os import system
from time import sleep
import random

def cls():
    _ = system('cls')

while True:
    while True:
        cls()
        print('Random Number Generator\n')
        try:
            min = int(input('Minimum: '))
            if(min >= 0):
                try:
                    max = int(input('Maximum: '))
                    if(max >= 0):
                        if(min <= max):
                            break
                        else:
                            print("min is langer than max")
                            sleep(1)
                    else:
                        print("Please enter a positiv integer")
                        sleep(1)
                except ValueError:
                    print("That is not an integer.")
                    sleep(1)
            else:
                print("Please enter a positiv integer")
                sleep(1)
        except ValueError:
            print("That is not an integer.")
            sleep(1)


    rand_int = (random.randint(int(min),int(max)))
    cut = 0
    x = ""
    cls()
    
    if(len(str(rand_int)) > 4):
        cut = len(str(rand_int)) - 4
        rand_int_cut = int(str(rand_int)[:-cut])
    else:
        rand_int_cut = rand_int

    for i in range(rand_int_cut):
        x = ""
        for not_used in range(cut):
            x += str(random.randint(1, 9))
        print(str(i) + str(x), end='\r')
        sleep(0.01)

    print(rand_int)
    input("Press Enter to continue...")