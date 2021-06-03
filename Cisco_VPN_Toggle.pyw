#Basic automation of connection to Cisco VPN
#Who: Fil Rondel
#What: Basic automation bot
#Why: Laziness

import pyautogui as pag

#To trigger failsafe move your mouse to the top left corner of your screen (x, y = 0, 0) 
pag.FAILSAFE = True

pag.press('win')
pag.write('Anyconnect')
pag.PAUSE = 0.5
pag.press('enter')
pag.PAUSE = 1.5

if pag.locateOnScreen(r'C:\Users\<Username>\cisco-vpn-automation\disconnect.png', confidence=0.9) != None:
    pag.press('enter')
    print("Disconnected")
    pag.keyDown('alt')
    pag.press('f4')
    pag.keyUp('alt')

else:
    pag.press('enter')
    pag.PAUSE = 0.5
    pag.write('ReplaceMeWithYourPassword')
    pag.PAUSE = 0.1
    pag.press('tab')
    pag.PAUSE = 0.1
    pag.write('push')
    pag.PAUSE = 0.5
    pag.press('enter')
