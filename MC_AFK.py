import time
import multiprocessing
import keyboard
import pyautogui as pg
import os

### variables

c = False
b = 5
a = False
kilof = 0
count = 0
mined = 0

def mine():
    global kilof, b
    a = True
    b = 5

    for x in range(6):
        print('Mining in:',b,'s')
        time.sleep(1)
        b -= 1
        os.system('cls')
        c = True
    while c == True:
        pg.mouseDown()

        if keyboard.is_pressed('esc'):
            pg.mouseUp()
            c = False

def timer():
    global count,c, mined

    c = True

    time.sleep(6)

    while c == True:
        time.sleep(count)
        mined += 1
        print(mined)
        

def mine_set():
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
        a = True 

mine_set()

p1 = multiprocessing.Process(target=mine)
p2 = multiprocessing.Process(target=timer)

if __name__ == '__main__':
    p1.start()
    p2.start()
    print('asd')