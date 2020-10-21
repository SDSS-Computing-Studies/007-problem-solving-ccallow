#!python3
import pyautogui as p
import time as t

curTime = t.time()
target = curTime+30

#p.mouseInfo()

cookie = p.locateCenterOnScreen('cooke.png')

print(cookie)

store = p.locateCenterOnScreen('store.png', confidence=0.75)
print(store)

#1. click the cookie as fast as possible
while True:
    p.click(cookie) 
    break
#2. cycle through upgrades from buttom to top every minute

#3. check the store button every minute