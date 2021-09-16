from os import system
from time import sleep
import random

# define cls command
def cls():
    _ = system('cls')


# main loop
try:
    while True:
        while True:
            cls()
            print('Random Number Generator\n')
            try:
                #ask for min and max integer, filter negative numbers and strings 
                min = int(input('Minimum: '))
                if(min >= 0):
                    try:
                        max = int(input('Maximum: '))
                        if(max >= 0):
                            if(min <= max):
                                break
                            else:
                                print("The minimum value is langer than the max value!")
                                sleep(1)
                        else:
                            print("Please enter a positive integer.")
                            sleep(1)
                    except ValueError:
                        print("That is not an integer.")
                        sleep(1)
                else:
                    print("Please enter a positive integer")
                    sleep(1)
            except ValueError:
                print("That is not an integer.")
                sleep(1)

        # define random integer from min to max
        rand_int = (random.randint(int(min),int(max)))
        cut = 0
        x = ""
        cls()

        # cut every digit from rand_int after third number and store amount of cut numbers
        if(len(str(rand_int)) > 3):
            cut = len(str(rand_int)) - 3
            rand_int_cut = int(str(rand_int)[:-cut])
        else:
            rand_int_cut = rand_int

        # insert random number from 1 to 9 for every cut number
        for i in range(rand_int_cut):
            x = ""
            for not_used in range(cut):
                x += str(random.randint(1, 9))
            print(str(i) + str(x), end='\r')
            sleep(0.01)

        # print final value and pause
        print(rand_int)
        input("Press Enter to continue...")

# catch KeyboardInterrupt and print exit text
except KeyboardInterrupt:
    cls()
    print("\33[34mThsnks for using RndNmbrGen\33[0m")