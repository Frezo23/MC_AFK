import time
import multiprocessing
import keyboard
import os

### variables

a = False
kilof = 0
count = 0

def mine():
    global kilof, a, count
    while a == False:
        try:
            kilof = int(input('Pick a pickaxe type: \n wooden -> 1 \n stone -> 2 \n golden -> 3 \n iron ->  4 \n diamond -> 5 \n netherite -> 6 \n --> '))

            if kilof == '1':
                print('mine')
                a = True
                count = 1.15

            elif kilof == '2':
                print('mine')
                a = True
                count = 0.6

            elif kilof == '3':
                print('mine')
                a = True
                count = 0.2

            elif kilof == '4':
                print('mine')
                a = True
                count = 0.4

            elif kilof == '5':
                print('mine')
                a = True
                count = 0.3

            elif kilof == '6':
                print('mine')
                a = True
                count = 0.25
            else:
                os.system('cls')
        except ValueError:
            print('Wrong value')
        os.system('cls') 
        


mine()

### running processes

# if __name__ == '__main__':
#     p1.start()
#     p2.start()
