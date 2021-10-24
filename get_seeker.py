import subprocess
import os
import vk_api
import time
import pyautogui
import random
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType



def get_config (whats) :
	os.chdir("/home/noname/config_bot")
	do_config = open('config.txt', 'r')
	from_id = do_config.read()
	print(from_id)
	do_config.close()
	if whats == 'from_id' :
		return from_id
	elif whats == 'chat_id' :
		return 1

os.chdir("/home/noname/seeker")
list_dir = subprocess.Popen(['python3', 'seeker.py', '-t','manual'])
time.sleep(1)

vk_session = vk_api.VkApi(token='d44cc9cfb8d2062dc3603550f6fb6f7b75e76efc0727db80afcf2b4cdd570816b1aa83fcd2cd580a9636d')
longpoll_bot = VkBotLongPoll(vk_session, 168924289)
vk = vk_session.get_api()





pyautogui.typewrite('3')
pyautogui.press('enter')
pyautogui.typewrite('Test')
pyautogui.press('enter')
pyautogui.typewrite('Test')
pyautogui.press('enter')
pyautogui.typewrite('/home/noname/Pictures/Screenshot_2021-02-24_02_48_32.png')
pyautogui.press('enter')
pyautogui.typewrite('1')
pyautogui.press('enter')
pyautogui.typewrite('1')
pyautogui.press('enter')
list_dir.wait()








