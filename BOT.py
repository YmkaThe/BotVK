# -*- coding: utf-8 -*-
import requests
import vk_api
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
import time
from yandex_translate import YandexTranslate
import datetime
import re
import json
import random
## токен
vk_session = vk_api.VkApi(token = 'token')

## переводчик
url_tr = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
translate = YandexTranslate('TOKEN YANDEX.TRANSLATE')
## группа и т.д
longpoll = VkBotLongPoll(vk_session, ' ID GROUP ' ) 
vk = vk_session.get_api()
peer_id = индитификатор беседы, где будет бот
## сам код

mut = {} # словарь мученых
Privet = {1:'Доброго времени суток',2: 'Нихао',3:'Приуэт'}
start = 0
sa = 0
try:
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW :
            message = event.obj['message']
            text = message['text']
            members = vk.messages.getConversationMembers(
                        peer_id=peer_id,
                    )['items']
            k = 0
            members_ids = [member['member_id'] for member in members if member['member_id'] > 0]
            message = ' Оповестили людей'
            for member_id in members_ids:
                        k +=1
            if text.lower() =='!запуск':
                         if start == 0:
                          if event.message.from_id == mut:
                           vk.messages.send(
                                     random_id = get_random_id(),
                                     chat_id = event.chat_id,

                                     message = 'Вы были убиты. Ожидай-те, когда вас воскресят  \n'
                                        'Команда !воскресить',

                             )
                          else:
                           s = random.randint(1,3)
                           vk.messages.send(
                                      random_id = get_random_id(),
                                     chat_id = event.chat_id,

                                     message = Privet[s] + ', БОТ  готов к работе.\n'
                                     'Для работы введите /список',
                                        )
                           start = 1
                         elif start == 1:
                          vk.messages.send(
                                     random_id = get_random_id(),
                                     chat_id = event.chat_id,

                                     message = 'Бот уже запущен и готов к работе! \n'
                                     'Для просмотра списка команд, введите !список',

                                        )
            if start == 0:
                pass
            elif start == 1:
                for event in longpoll.listen():
                    if event.type == VkBotEventType.MESSAGE_NEW :
                        message = event.obj['message']
                        text = message['text']
                        members = vk.messages.getConversationMembers(
                                    peer_id=peer_id,
                                )['items']
                        k = 0
                        members_ids = [member['member_id'] for member in members if member['member_id'] > 0]
                        message = ' Оповестили людей'
                        for member_id in members_ids:
                                    k +=1
                        if text.lower() =='!запуск':
                         if start == 0:
                          if event.message.from_id == mut:
                           vk.messages.send(
                                     random_id = get_random_id(),
                                     chat_id = event.chat_id,

                                     message = 'Вы были убиты. Ожидай-те, когда вас воскресят  \n'
                                        'Команда !воскресить',

                             )
                          else:
                           s = random.randint(1,3)
                           vk.messages.send(
                                      random_id = get_random_id(),
                                     chat_id = event.chat_id,

                                     message = Privet[s] + ', БОТ  готов к работе.\n'
                                     'Для работы введите /список',
                                        )
                           start = 1
                         elif start == 1:
                          vk.messages.send(
                                     random_id = get_random_id(),
                                     chat_id = event.chat_id,

                                     message = 'Бот уже запущен и готов к работе! \n'
                                     'Для просмотра списка команд, введите !список',

                                        )
                        if text.lower() == '!объявление':
                            qw +=1
                            if event.message.from_id == mut:
                             vk.messages.send(
                                         random_id = get_random_id(),
                                         chat_id = event.chat_id,

                                         message = 'Вы были убиты. Ожидай-те, когда вас воскресят  \n'
                                            'Команда !воскресить',

                                 )
                            else:
                             print('lll')
                             def main():
                                members = vk.messages.getConversationMembers(
                                    peer_id=peer_id,
                                )['items']

                                members_ids = [member['member_id'] for member in members if member['member_id'] > 0]

                                message = ' Оповестили людей'
                                for member_id in members_ids:
                                    message += f'[id{member_id}|.]'
                                # 1- беседа с машей 2- беседа шараги 3- беседа с Ваней  ОБЯЗАТЕЛЬНО ПРАВА АДМИНА!!!!
                                vk.messages.send(
                                    peer_id=peer_id,
                                    message=message,
                                    random_id=get_random_id(),
                                )
                             if __name__ == '__main__':
                                main()
                 
                        if text.lower() == '!список':
                           for sa in mut:
                             if mut[sa] == event.message.from_id:
                              vk.messages.send(
                                         random_id = get_random_id(),
                                         chat_id = event.chat_id,

                                         message = 'Вы были убиты. Ожидай-те, когда вас воскресят  \n'
                                            'Команда !воскресить',

                                            )
                              break
                           else:
                             print('lll')
                             vk.messages.send(
                                 random_id = get_random_id(),
                                 chat_id = event.chat_id,

                                 message = '1) !список - вызывает список команд '
                                           '\n 2) !перевод - переводит текст.'
                                           '\n 3) !группа - говорит вам в какой группе вы находитесь.'
                                           '\n 4) !объявление - созывает всех в беседу.'
                                           '\n 5) !открепить - открепляет закрепленное сообщение'
                                           '\n 6) !смерть - убивает игрока.'
                                           '\n 7) !воскресить - воскресить  умерших(умершего)'
                                           '\n 8) !спать - бот уходит в режим сна(команды недоступны. Все умершие - воскресают)',
                                 )
                        if text.lower() == '!перевод':
                           for sa in mut:
                             if mut[sa] == event.message.from_id:
                              vk.messages.send(
                                         random_id = get_random_id(),
                                         chat_id = event.chat_id,

                                         message = 'Вы были убиты. Ожидай-те, когда вас воскресят  \n'
                                            'Команда !воскресить',

                                            )
                              break
                           else:
                             print('lll')
                             vk.messages.send( #Тоже самое, но для бесед
                                    random_id = get_random_id(),
                                    chat_id=event.chat_id,
                                    message='На какой язык? Указывать двумя буквами.\n Например: Русский - ru, Английский - en'
    	                    )

                             for event in longpoll.listen():
                                 if event.type == VkBotEventType.MESSAGE_NEW  and event.from_chat:
                                     if text.lower() == 'выход':
                                         break
                                     else:
                                          message = event.obj['message']
                                          text = message['text']
                                          trTo = text.lower() #Сохраняем текст в переменную

                                          vk.messages.send( #Тоже самое, но для бесед
                                                      random_id = get_random_id(),
                                                      chat_id=event.chat_id,
                                                      message='Введите фразу, которую надо перевести '
    	                                      )
                                          flag = 0 #Шаманский танец для выхода из 2-х циклов
                                          for event in longpoll.listen():
                                            if event.type == VkBotEventType.MESSAGE_NEW  and event.from_chat:
                                                if text.lower() == 'выход':
                                                    break
                                                else:
                                                     message = event.obj['message']
                                                     text = message['text']
                                                     trNormal = 1 #Колхозный флаг для ошибки
                                                     try: #Исключение, о них поговорим ниже
                                                         trFrom = translate.detect(text.lower()) #Определяем язык

                                                         trResult = translate.translate(text.lower(), trFrom + '-' + trTo) #Переводим
                                                     except Exception as e: #Если что-то пошло не так
                                                         trNormal = 0 #Пинаем флаг ошибки
                                                         print("Exception:", e) #Пишем в консоль
                                                         pass
                                                     if trNormal == 1: 

                                                             vk.messages.send( #Тоже самое, но для бесед
                                                                  random_id = get_random_id(),
                                                                 chat_id=event.chat_id,
                                                                 message='Вот перевод текста \n' + str(trResult['text'])
    		                                         )
                                                             flag = 1
                                                             break
                                                     if trNormal == 0:

                                                                 vk.messages.send( #Тоже самое, но для бесед
                                                                      random_id = get_random_id(),
                                                                     chat_id=event.chat_id,
                                                                     message='Неправильно введён язык'
    				                             )
                                                                 flag = 1
                                                                 break
                                     if flag == 1: 
                                                 break                        
                        if text.lower() == '!игры':
                           for sa in mut:
                             if mut[sa] == event.message.from_id:
                              vk.messages.send(
                                         random_id = get_random_id(),
                                         chat_id = event.chat_id,

                                         message = 'Вы были убиты. Ожидай-те, когда вас воскресят  \n'
                                            'Команда !воскресить',

                                            )
                              break
                           else:
                             print('lll')
                             vk.messages.send(
                                 random_id = get_random_id(),
                                 chat_id = event.chat_id,

                                 message = '1) камень-ножницы-бумага. ',
                                 )
                             for event in longpoll.listen():
                                if event.type == VkBotEventType.MESSAGE_NEW  and event.from_chat:
                                    message = event.obj['message']
                                    text = message['text']
                                    if text.lower() == '1':
                                      f = 1
                                      while f>0:
                                        one = 'камень',
                                        two = 'ножницы',
                                        three = 'бумага',
                                        vk.messages.send(
                                         random_id = get_random_id(),
                                         chat_id = event.chat_id,
                                         message = 'что выбираете?',
                                         )
                                        for event in longpoll.listen():
                                            if event.type == VkBotEventType.MESSAGE_NEW  and event.from_chat:
                                                message = event.obj['message']
                                                text = message['text']
                                                if text.lower() =='камень' or text.lower()== 'бумага' or text.lower() =='ножницы':
                                                    kod = random.randint(1,3)
                                                    if text.lower() == 'камень':
                                                            if kod == 1:
                                                              vk.messages.send(
                                                                 random_id = get_random_id(),
                                                                 chat_id = event.chat_id,
                                                                 message = 'ничья! \n'
                                                                           '\n Хотите повторить?',
                                                                 )
                                                              for event in longpoll.listen():
                                                                if event.type == VkBotEventType.MESSAGE_NEW  and event.from_chat:
                                                                    message = event.obj['message']
                                                                    text = message['text']
                                                                    if text.lower() == 'да':
                                                                        vk.messages.send(
                                                                         random_id = get_random_id(),
                                                                         chat_id = event.chat_id,
                                                                         message = 'что выбираете?',)
                                                                        f = 1
                                                                        break
                                                                    else:
                                                                        f = 0
                                                                        break
                                                            elif kod == 2:
                                                                vk.messages.send(
                                                                 random_id = get_random_id(),
                                                                 chat_id = event.chat_id,
                                                                 message = 'Победа! \n'
                                                                           '\n Хотите попробывать еще?',
                                                                 )
                                                                for event in longpoll.listen():
                                                                 if event.type == VkBotEventType.MESSAGE_NEW  and event.from_chat:
                                                                    message = event.obj['message']
                                                                    text = message['text']
                                                                    if text.lower() == 'да':
                                                                        vk.messages.send(
                                                                         random_id = get_random_id(),
                                                                         chat_id = event.chat_id,
                                                                         message = 'что выбираете?',)
                                                                        f = 1
                                                                        break
                                                                    else:
                                                                        f = 0
                                                                        break
                                                            elif kod == 3:
                                                                vk.messages.send(
                                                                 random_id = get_random_id(),
                                                                 chat_id = event.chat_id,
                                                                 message = 'Проиграли! \n'
                                                                            '\n Попробуем еще раз?',
                                                                 )
                                                                for event in longpoll.listen():
                                                                 if event.type == VkBotEventType.MESSAGE_NEW  and event.from_chat:
                                                                    message = event.obj['message']
                                                                    text = message['text']
                                                                    if text.lower() == 'да':
                                                                        vk.messages.send(
                                                                         random_id = get_random_id(),
                                                                         chat_id = event.chat_id,
                                                                         message = 'что выбираете?',)
                                                                        f = 1
                                                                        break
                                                                    else:
                                                                        f = 0
                                                                        break
                                                    if text.lower() == 'бумага':
                                                            if kod == 1:
                                                              vk.messages.send(
                                                                 random_id = get_random_id(),
                                                                 chat_id = event.chat_id,
                                                                 message = 'Победа!\n'
                                                                 '\n Еще раз?',
                                                                 )
                                                              for event in longpoll.listen():
                                                                 if event.type == VkBotEventType.MESSAGE_NEW  and event.from_chat:
                                                                    message = event.obj['message']
                                                                    text = message['text']
                                                                    if text.lower() == 'да':
                                                                        vk.messages.send(
                                                                         random_id = get_random_id(),
                                                                         chat_id = event.chat_id,
                                                                         message = 'что выбираете?',)
                                                                        f = 1
                                                                        break
                                                                    else:
                                                                        f = 0
                                                                        break
                                                            elif kod == 2:
                                                                vk.messages.send(
                                                                 random_id = get_random_id(),
                                                                 chat_id = event.chat_id,
                                                                 message = 'Проиграли! \n'
                                                                 '\n Еще раз?',
                                                                 )
                                                                for event in longpoll.listen():
                                                                 if event.type == VkBotEventType.MESSAGE_NEW  and event.from_chat:
                                                                    message = event.obj['message']
                                                                    text = message['text']
                                                                    if text.lower() == 'да':
                                                                        vk.messages.send(
                                                                         random_id = get_random_id(),
                                                                         chat_id = event.chat_id,
                                                                         message = 'что выбираете?',)
                                                                        f = 1
                                                                        break
                                                                    else:
                                                                        f = 0
                                                                        break
                                                            elif kod == 3:
                                                                vk.messages.send(
                                                                 random_id = get_random_id(),
                                                                 chat_id = event.chat_id,
                                                                 message = 'Ничья!\n'
                                                                 '\n Еще раз?',
                                                                 )
                                                                for event in longpoll.listen():
                                                                 if event.type == VkBotEventType.MESSAGE_NEW  and event.from_chat:
                                                                    message = event.obj['message']
                                                                    text = message['text']
                                                                    if text.lower() == 'да':
                                                                        vk.messages.send(
                                                                         random_id = get_random_id(),
                                                                         chat_id = event.chat_id,
                                                                         message = 'что выбираете?',)
                                                                        f = 1
                                                                        break
                                                                    else:
                                                                        f = 0
                                                                        break
                                                    if text.lower() == 'ножницы':
                                                            if kod == 1:
                                                              vk.messages.send(
                                                                 random_id = get_random_id(),
                                                                 chat_id = event.chat_id,
                                                                 message = 'Проиграли!\n'
                                                                 '\n Еще раз?',
                                                                 )
                                                              for event in longpoll.listen():
                                                                 if event.type == VkBotEventType.MESSAGE_NEW  and event.from_chat:
                                                                    message = event.obj['message']
                                                                    text = message['text']
                                                                    if text.lower() == 'да':
                                                                        vk.messages.send(
                                                                         random_id = get_random_id(),
                                                                         chat_id = event.chat_id,
                                                                         message = 'что выбираете?',)
                                                                        f = 1
                                                                        break
                                                                    else :
                                                                        f = 0
                                                                        break
                                                            elif kod == 2:
                                                                vk.messages.send(
                                                                 random_id = get_random_id(),
                                                                 chat_id = event.chat_id,
                                                                 message = 'Ничья!\n'
                                                                 '\n Еще раз?',
                                                                 )
                                                                for event in longpoll.listen():
                                                                 if event.type == VkBotEventType.MESSAGE_NEW  and event.from_chat:
                                                                    message = event.obj['message']
                                                                    text = message['text']
                                                                    if text.lower() == 'да':
                                                                        vk.messages.send(
                                                                         random_id = get_random_id(),
                                                                         chat_id = event.chat_id,
                                                                         message = 'что выбираете?',)
                                                                        f = 1
                                                                        break
                                                                    else:
                                                                        f = 0
                                                                        break
                                                            elif kod == 3:
                                                                vk.messages.send(
                                                                 random_id = get_random_id(),
                                                                 chat_id = event.chat_id,
                                                                 message = 'Победа!\n'
                                                                 '\n Еще раз?',
                                                                 )
                                                                for event in longpoll.listen():
                                                                 if event.type == VkBotEventType.MESSAGE_NEW  and event.from_chat:
                                                                    message = event.obj['message']
                                                                    text = message['text']
                                                                    if text.lower() == 'да':
                                                                        vk.messages.send(
                                                                         random_id = get_random_id(),
                                                                         chat_id = event.chat_id,
                                                                         message = 'что выбираете?',)
                                                                        f = 1
                                                                        break
                                                                    else:
                                                                        f = 0
                                                                        break
                                                else:
                                                    if f == 0 :
                                                        break
                                                    vk.messages.send(
                                                     random_id = get_random_id(),
                                                     chat_id = event.chat_id,
                                                     message = 'нет тут таких условий! давай по новой!',
                                                     )
                                                    f = 1
                                      break
                        if text.lower() == 'выстрел':
                            for sa in mut:
                             if mut[sa] == event.message.from_id:
                              vk.messages.send(
                                         random_id = get_random_id(),
                                         chat_id = event.chat_id,

                                         message = 'Вы были убиты. Ожидай-те, когда вас воскресят  \n'
                                            'Команда !воскресить',

                                            )
                              break
                            else:
                             print('lll')
                             def main():
                                members = vk.messages.getConversationMembers(
                                    peer_id=peer_id,
                                )['items']
                                k = 0
                                members_ids = [member['member_id'] for member in members if member['member_id'] > 0]

                                message = ' Оповестили людей'
                                for member_id in members_ids:
                                    k +=1


                                s = random.randint(0,k-1)
                                print(s)
                                print(members_ids[s])
                                ##############################
                                ids = event.message.from_id
                                user_get=vk.users.get(user_ids = (ids))
                                user_get=user_get[0]
                                ffirst_name=user_get['first_name']
                                flast_name=user_get['last_name']
                                ferst_full_name=ffirst_name+" "+flast_name

                                ##############################
                                id = members_ids[s]
                                user_get=vk.users.get(user_ids = (id))
                                user_get=user_get[0]
                                first_name=user_get['first_name']
                                last_name=user_get['last_name']
                                full_name=first_name+" "+last_name
                                ##############################
                                heals = {0:'убит', 1:'левую ногу',2:'правую ногу',3:'колено',4:'тело',5:'пах',6:'левую руку',7:'правую руку'}
                                if members_ids[s] == event.message.from_id:
                                    vk.messages.send(
                                         random_id = get_random_id(),
                                         chat_id = event.chat_id,

                                         message = ''+ full_name + ' рукожоп, выстрел попал в стрелявшего'
                                         )
                                else:
                                    fs = random.randint(0,7)
                                    print(fs)

                                    if fs == 0:
                                        vk.messages.send(
                                             random_id = get_random_id(),
                                             chat_id = event.chat_id,

                                             message = ''+ ferst_full_name + ' cделал(a) выстрел, убив  ' + f'[id{members_ids[s]}|'+full_name+']' + '&#128299; \n'

                                            ''+ ferst_full_name + 'у вас меткий глаз'
                                             )
                                        if members_ids[s] !=152953803:
                                         mut[0] = members_ids[s]
                                    if fs == 1 or fs == 2:
                                         if 1:
                                             g = heals[1]
                                         elif 2:
                                             g = heals[2]
                                         vk.messages.send(
                                             random_id = get_random_id(),
                                             chat_id = event.chat_id,

                                             message = '' +ferst_full_name+ ' cделал(a) выстрел, попав в '+ g + ' ' + f'[id{members_ids[s]}|'+full_name+']' + '&#128299; \n'

                                             'Можно было и лучше'
                                             )
                                    if fs == 3:
                                         vk.messages.send(
                                             random_id = get_random_id(),
                                             chat_id = event.chat_id,

                                             message = '' +ferst_full_name+ ' cделал(a) выстрел, попав в колено ' + f'[id{members_ids[s]}|'+full_name+']' + '&#128299; \n'

                                             ''+ferst_full_name+ ', а вы умеете мучить человека' + '&#128527;'
                                             )
                                    if fs == 4:
                                        vk.messages.send(
                                             random_id = get_random_id(),
                                             chat_id = event.chat_id,

                                             message = '' +ferst_full_name+ ' cделал(a) выстрел, попав в живот ' + f'[id{members_ids[s]}|'+full_name+']' + '&#128299; \n'

                                             'Это наверное больно....'
                                             )
                                    if fs == 5:
                                        vk.messages.send(
                                             random_id = get_random_id(),
                                             chat_id = event.chat_id,

                                             message = '' +ferst_full_name+ ' cделал(a) выстрел, попал в пах ' + f'[id{members_ids[s]}|'+full_name+']' + '&#128299; \n'

                                             '' + full_name + ' лешился своего наследия...'
                                             )
                                    if fs == 6 or fs==7:
                                         if 6:
                                             g = heals[6]
                                         elif 7:
                                             g = heals[7]
                                         vk.messages.send(
                                             random_id = get_random_id(),
                                             chat_id = event.chat_id,

                                             message = '' +ferst_full_name+ 'cделал(a) выстрел, попав в '+ g + ' ' + f'[id{members_ids[s]}|'+full_name+']' + '&#128299; \n'

                                             'Можно было и лучше'
                                             )
                             if __name__ == '__main__':
                              main() # подключить базу данных.
                        if text.lower() == '!открепить':
                            for sa in mut:
                             if mut[sa] == event.message.from_id:
                              vk.messages.send(
                                         random_id = get_random_id(),
                                         chat_id = event.chat_id,

                                         message = 'Вы были убиты. Ожидай-те, когда вас воскресят  \n'
                                            'Команда !воскресить',

                                            )
                              break
                            else:
                              peer_id = peer_id,

                              vk.messages.unpin(peer_id=peer_id, group_id = group_id')
                        if text.lower() == '!закреп':
                             pass
                        if text.lower() == '!смерть':
                            sa+=1
                            for sa in mut:
                             if mut[sa] == event.message.from_id:
                              vk.messages.send(
                                         random_id = get_random_id(),
                                         chat_id = event.chat_id,

                                         message = 'Вы были убиты. Ожидай-те, когда вас воскресят  \n'
                                            'Команда !воскресить',

                                            )
                              break
                            else:
                                            print('111')
                                            sa+=1
                                            ids = event.message.from_id
                                            user_get=vk.users.get(user_ids = (ids))
                                            user_get=user_get[0]
                                            ffirst_name=user_get['first_name']
                                            flast_name=user_get['last_name']
                                            ferst_full_name=ffirst_name+" "+flast_name
                                            vk.messages.send(
                                            random_id = get_random_id(),
                                            chat_id = event.chat_id,

                                            message = ''+ferst_full_name+ ', за вами уже выехали! ',
                                            attachment = 'photo-187153942_457239022'

                                            )

                                            if event.message.from_id != 152953803:
                                             mut[sa] = event.message.from_id
                                             print(mut)
                        if text.lower() == '!воскресить':
                            for sa in mut:
                             if mut[sa] == event.message.from_id:
                              vk.messages.send(
                                         random_id = get_random_id(),
                                         chat_id = event.chat_id,

                                         message = 'Вы были убиты. Ожидай-те, когда вас воскресят  \n'
                                            'Команда !воскресить',

                                            )
                              break
                            else:
                                    print('111')
                                    vk.messages.send(
                                         random_id = get_random_id(),
                                         chat_id = event.chat_id,

                                         message = 'Умершие! Восстаньте!'


                                 )
                                    mut.clear()
                        if text.lower() == '!спать':
                            for sa in mut:
                             if mut[sa] == event.message.from_id:
                              vk.messages.send(
                                         random_id = get_random_id(),
                                         chat_id = event.chat_id,

                                         message = 'Вы были убиты. Ожидай-те, когда вас воскресят  \n'
                                            'Команда !воскресить',

                                            )
                              break
                            else:
                                    print('111')
                                    vk.messages.send(
                                         random_id = get_random_id(),
                                         chat_id = event.chat_id,

                                         message = 'Я вас понял, прекращаю работу'


                                 )

                                    mut.clear()
                                    start = 0
                                    break

           
except requests.exceptions.ReadTimeout:
        print("\n Переподключение к серверам ВК \n")
        time.sleep(3)


