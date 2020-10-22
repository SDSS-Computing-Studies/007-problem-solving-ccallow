#!python3
import pyautogui as p
import time as t

curTime = t.time()

p.mouseInfo()

store = p.locateCenterOnScreen('store.png', confidence=0.75)
print(store)


#1. click the cookie
def cookieClicks():
    cookie = p.locateCenterOnScreen('cooke.png', confidence = 0.8)
    print(cookie)
    while True:
        for i in range(0,100):
            p.click(cookie)
        break
#2.cycle through upgrades from buttom to top
def upgrades():
    #farm
    p.moveTo(1197,463)
    if p.pixelMatchesColor(1196,463,(255,255,255)):
        for i in range(0,5):
            p.click(1197,463)
    t.sleep(2)
    #grandma
    p.moveTo(1193,403)
    if p.pixelMatchesColor(1193,403,(255,255,255)):
        for i in range(0,5):
            p.click(1193,403)
    t.sleep(2)
    #cursor
    p.moveTo(1193,340)
    if p.pixelMatchesColor(1193,340,(255,255,255)):
        for i in range(0,5):
            p.click(1193,340)
    t.sleep(2)

#Farm (1195,454)
#Mine(1201, 519)
#Factory (1196,582)
#Bank (1197,663)
#Temple (1201,721)
#white (#FFFFFF)

#3.check the store button every minute
#leftupgrade(1150,215)
#rightupgrade(1391,221)
#blueLight(#0F2835)
#blueDark(#050F14)

def playGame():
    cookieClicks()
    upgrades()
    print("Finished!")


playGame()