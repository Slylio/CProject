import random 
from time import sleep
import keyboard
import mouse

activate=False
while (True):
    if (keyboard.is_pressed('&')):
        print("épée")
        activate=True
    elif(keyboard.is_pressed('é') or keyboard.is_pressed('"') or keyboard.is_pressed('\'') or keyboard.is_pressed('(') or keyboard.is_pressed('-') or keyboard.is_pressed('è') or keyboard.is_pressed('x') or keyboard.is_pressed('c') or keyboard.is_pressed('c')):
        activate=False
        print("inventaire")

    if (activate and mouse.is_pressed('left')):
        mouse.click('left')
        sleep(random.randint(100,500))
        print("doubleclick")
    