#!python3
import pyautogui as p
import time as t

curTime = t.time()

p.mouseInfo()

cookie = p.locateCenterOnScreen('cooke.png', confidence = 0.8)
print(cookie)

store = p.locateCenterOnScreen('store.png', confidence=0.75)
print(store)

#1. click the cookie
def cookieClicks():
    while True:
        for i in range(0,100):
            p.click(cookie)
        break
#2.cycle through upgrades from buttom to top every minute
def upgrades():


#3.check the store button every minute