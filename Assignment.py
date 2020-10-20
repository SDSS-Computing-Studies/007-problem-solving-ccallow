#!python3

import pyautogui as p
import time as t

#p.mouseInfo()

cookie = p.locateCenterOnScreen('cooke.png')

print(cookie)

store = p.locateCenterOnScreen('store buttom.png')
print(store)

#1. click the cookie as fast as possible
while True:
    p.click(cookie) 
#2. cycle through upgrades from buttom to top every minute

#3. check the store button every minute