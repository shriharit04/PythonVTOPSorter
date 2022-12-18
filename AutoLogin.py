import datetime, pyautogui
import sys
import time
from time import sleep
import AutomationFunctions
from AutomationFunctions import *


def ButtonClick(img):
    BtnLocation = pyautogui.locateCenterOnScreen(r"VPics/" + img, confidence=0.7)
    pyautogui.click(BtnLocation)
    sleep(1)


def TodayDate():
    file = open("LatestDate.txt", "r")
    a = str(datetime.date.today())
    DateLast = file.read()
    DateToday = "-".join(a.split("-")[::-1])


vtopUrl = ("https://vtop.vit.ac.in/vtop/content")

acad = ()
Windows.PreviousApp()
'''sleep((1))
browser =Browser("opera")
browser.SearchNew(vtopUrl)
sleep(3)
ButtonClick("StudentPic.png")'''

# pyautogui.click("StudentPic.png")
sleep(10)

# todo : picture location

# pyautogui.click("Academics.png")
pyautogui.click(106, 199)
sleep(1)
ButtonClick("Academics.png")
sleep(2)
ButtonClick("CoursePage.png")
sleep(2)
pyautogui.click(1500, 1000)
sleep(1)

ButtonClick("img.png")
sleep(0.5)
for i in range(2):
    pyautogui.hotkey('down')
    pyautogui.hotkey('enter')
    sleep(0.3)
    pyautogui.hotkey('tab')
    sleep(0.3)
SubjectCount = 9

pyautogui.hotkey()

# todo:automation library filtering
