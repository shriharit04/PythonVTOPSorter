import time

import pyautogui
from time import sleep

class Windows:
    def SearchApp(name,self = "windows"):
        pyautogui.press('winleft')
        pyautogui.write(name)
        sleep(1)

        pyautogui.press('enter')

    def PreviousApp(self = "windows"):
        pyautogui.hotkey('alt','tab')

    def NextDestop(self = "windows"):
        pyautogui.hotkey('winleft', 'ctrl','right')

    def PrevDestop(self = "windows"):
        pyautogui.hotkey('winleft', 'ctrl','left')



class Browser:
    def __init__(self,BrowserName):
        self.name = BrowserName

    def SearchNew(self,url):
        pyautogui.hotkey("ctrl","t")
        sleep(1)
        pyautogui.typewrite(url)
        pyautogui.press("Enter")
        sleep(1)

    def CloseTab(self):
        pyautogui.hotkey('ctrl','w')

    def FindInPage(self,name):
        pyautogui.hotkey("ctrl","f")
        pyautogui.typewrite(name)


class mail:
    def __init__(self,seats):
        self.seats = seats


