#!python3
import pyautogui as p
import time as t

curTime = t.time()

p.mouseInfo()




#1. click the cookie
def cookieClicks():
    cookie = p.locateCenterOnScreen('cooke.png', confidence = 0.8)
    print(cookie)
    while True:
        for i in range(0,100):
            p.click(cookie)
        break
#2.cycle through upgrades from buttom to top every minute
def upgrades():
    store = p.locateCenterOnScreen('store.png', confidence=0.75)
    print(store)

#Cursor (1249,329)
#Grandma (1249, 389)
#Farm (1249,449)
#Mine(1249, 519)
#Factory (1249, 589)
#Bank (1249, 659)
#Temple (1249, 709)

#3.check the store button every minute