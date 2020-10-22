#!python3
import pyautogui as p
import time as t


#1. click the cookie
def cookieClicks():
    cookie = p.locateCenterOnScreen('cooke.png', confidence = 0.7)
    while True:
        for i in range(0,1000):
            p.click(cookie)
        break
#2.cycle through upgrades from buttom to top
def upgrades():
    #wizard
    p.moveTo(1195,787)
    if p.pixelMatchesColor(1195,787,(255,255,255)):
        for i in range(0,5):
            p.click(1195,787)
    t.sleep(1)
    #Temple
    p.moveTo(1201,721)
    if p.pixelMatchesColor(1201,721,(255,255,255)):
        for i in range(0,5):
            p.click(1201,721)
    t.sleep(1)
    #Bank
    p.moveTo(1197,663)
    if p.pixelMatchesColor(1197,663,(255,255,255)):
        for i in range(0,5):
            p.click(1197,663)
    t.sleep(1)
    #Factory
    p.moveTo(1196,598)
    if p.pixelMatchesColor(1196,598,(255,255,255)):
        for i in range(0,5):
            p.click(1196,598)
    t.sleep(1)
    #Mine
    p.moveTo(1200,530)
    if p.pixelMatchesColor(1199,525,(255,255,255)):
        for i in range(0,5):
            p.click(1199,525)
    t.sleep(1)
    #farm
    p.moveTo(1197,463)
    if p.pixelMatchesColor(1196,463,(255,255,255)):
        for i in range(0,5):
            p.click(1197,463)
    t.sleep(1)
    #grandma
    p.moveTo(1193,403)
    if p.pixelMatchesColor(1193,403,(255,255,255)):
        for i in range(0,5):
            p.click(1193,403)
    t.sleep(1)
    #cursor
    p.moveTo(1193,340)
    if p.pixelMatchesColor(1193,340,(255,255,255)):
        for i in range(0,5):
            p.click(1193,340)
    t.sleep(1)


#3.check the store button every minute
def store():
    store = p.locateCenterOnScreen('store.png', confidence=0.75)
    print
    p.click(store)
    p.move(-121,64)
    p.click(1151, 235)
    t.sleep(0.5)

def playGame():
    while True:
        cookieClicks()
        upgrades()
        cookieClicks()
        store()
        if p.position(1151,235):
            continue
        else:
            break
playGame()