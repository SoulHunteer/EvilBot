import subprocess
import os
import time
import pyautogui
import random

with open("conf.txt", "r") as f:
    text = f.read()
    phone_number = text[:text.find(',')]


os.chdir("/home/noname/spymer")
list_dir = subprocess.Popen(['python3', 'spammer.py'])
time.sleep(1)


pyautogui.typewrite('1')
pyautogui.press('enter')
pyautogui.typewrite('1')
pyautogui.press('enter')
pyautogui.typewrite(phone_number)
pyautogui.press('enter')
pyautogui.typewrite('1')
pyautogui.press('enter')
list_dir.wait()