import sys
sys.path.insert(0, '../')
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from def1 import random_bonus,  helper, send_end_vip, bets, sent_message, send_message, create_keyboard, mon_choise, save_obj, load_obj, choices_photo, yers, calculate_age, end_perk, rt, r, calc_x, smile_score, voice, open_menu, close_voices, hi_chat, calc_y, typing, what_v, open_admin, attachments, sending_message, wall_com, weel_choise, bonus_vip, otv, user_information, treat
import vk_api
from datetime import datetime
import random
from data1 import *
import logging
import os
import requests
import json
import time
import threading
from time import monotonic
#os.system('chcp 65001')
from multiprocessing import Process
import multiprocessing
from m import kuk



logging.basicConfig(filename="eror.log", level=logging.ERROR)

#session = vk_api.VkApi(login_id, pass_id)
session = vk_api.VkApi(login_id, pass_id, token=a_token)
session.auth()

sessions=session.get_api()
print (sessions)

vk_session = vk_api.VkApi(token=token)
session_api = vk_session.get_api()

#longpoll = VkLongPoll(session) #VkBotLongPoll(vk_session, group_id)
longpoll = VkBotLongPoll(vk_session, group_id)


#узнаем какой сегодня день
today = datetime.strftime(datetime.now(), "%X %d.%m.%Y")

print('Главное Меню: ' + __name__)

if __name__ == '__main__': #если процесс основной
    #id_like=list(filter(lambda likes_r: likes_r['items'] == event.obj.from_id, [likes_r for likes_r in sessions.likes.getList(items=event.obj.from_id)]
 multiprocessing.freeze_support()
 print(multiprocessing.freeze_support())
 print('Если основной проц: ' + __name__)

    #проверка на наличие БД файлов
 if os.path.exists("obj\\dict_users.pkl") and os.path.exists("obj\\list_duhs.pkl"):

                    q = load_obj('dict_users')
                    duhs = load_obj('list_duhs')


                    print("БД успешно загружена")
                    '''if item == 106545709:
                        print('*' * 80)
                        print(q)
                        print(duhs)

                        print('*' * 80)'''

 elif os.path.exists ("obj"):
                    print ("Директория obj найдена будут созданны новые базы")
 else:
                     path = "obj"

                     try:
                        os.mkdir(path)
                        print("Директория {0} НЕ найдена, но была успешно создана директория {0}".format(path))
                     except OSError:
                        print("Создать директорию {0} не удалось".format(path))
                        logging.error("Создать директорию {0} не удалось".format(path))

                # ЕСЛИ В ДИРЕКТОРИИ OBJ ПРИСУТСТВУЕТ ФАЙЛ convers.pkl ТО ЗАГРУЖАЕМ ФАЙЛ
 if os.path.exists("obj\\zonk.pkl"):
                        zonk = load_obj('zonk')

 if os.path.exists("obj\\newsletter.pkl"):
                    newsletter = load_obj('newsletter')


 if os.path.exists("obj\\convers.pkl"):
                        convers = load_obj('convers')
                        #print('Количество диалоговов ' + str(convers))

 if os.path.exists("obj\\deleted_items.pkl"):
                    deleted_items = load_obj('deleted_items')

                # ЕСЛИ В ДИРЕКТОРИИ OBJ ПРИСУТСТВУЕТ ФАЙЛ que.pkl ТО ЗАГРУЖАЕМ ФАЙЛ
 if os.path.exists("obj\\que.pkl"):
                        que = load_obj('que')
                        #print("БД очередь успешно загружена")
 if os.path.exists("obj\\all_list.pkl"):
                        all_list = load_obj('all_list')
                        #print("БД весь список очереди пользователей загружен")
 if os.path.exists("obj\\third_list.pkl"):
                        third_list = load_obj('third_list')
                        #print("БД втроем загруженна")
 if os.path.exists("obj\\status_bot.pkl"):
                status_bot = load_obj('status_bot')

 if os.path.exists("obj\\code14.txt"):
                    with open("obj\\code14.txt", "r") as file: #столбец с кодами загружен
                        code14 = [line.rstrip() for line in file]
 if os.path.exists("obj\\code31.txt"):
                    with open("obj\\code31.txt", "r") as file:  # столбец с кодами загружен
                        code31 = [line.rstrip() for line in file]
 if os.path.exists("obj\\diamonds150.txt"):
                    with open("obj\\diamonds150.txt", "r") as file:  # столбец с кодами загружен
                        diamonds150 = [line.rstrip() for line in file]
 if os.path.exists("obj\\gold_vip.txt"):
                    with open("obj\\gold_vip.txt", "r") as file:  # столбец с кодами загружен
                        gold_vip = [line.rstrip() for line in file]
 while True:

  try: #1
    #ttm = time_out_mes(monotonic())
    # event not in longpoll.listen():

    try:
        convers = load_obj('convers')
        duhs = load_obj('list_duhs')
        q = load_obj('dict_users')
        que = load_obj('que')
        all_list = load_obj('all_list')
        third_list = load_obj('third_list')
        deleted_items = load_obj('deleted_items')
    except:
        print("НЕ ЗАГРУЖЕННА БД")
    for event in longpoll.listen():

        # ЕСЛИ ТИП ИВЕНТА == ВСТУПЛЕНИЕ В ГРУППУ ТО

        if event.type == VkBotEventType.GROUP_JOIN:
         print('_' * 80)
         try:

            user_inf = sessions.users.get(user_id=event.obj.user_id, fields='sex')
            ffirst_name = (str(user_inf[0]['first_name']))

            j_m_1 = '{0}, добро пожаловать в анонимный чат🤗'.format(ffirst_name)
            j_m_2 = '{0}, ты как раз вовремя, сотни пользователей хотят общаться с тобой прямо сейчас😈'.format(ffirst_name)
            join_message = [j_m_1, j_m_2]
            try:
                send_message(session_api, peer_id=event.obj.user_id, tit=bot,
                            message=(random.choice(join_message)))
            except:
                print("НЕ МОГУ ОТПРАВИТЬ ВСТУПИТЕЛЬНОЕ СООБЩЕНИЕ!")
            print("Пользователь успешно вступил в группу")

         except:

             user_inf = sessions.users.get(user_id=event.obj.user_id, fields='sex')
             ffirst_name = (str(user_inf[0]['first_name']))
             print('НЕИЗВЕСТНАЯ ОШИБКА ПРИ ВСТУПЛЕНИИ В ГРУППУ')
             logging.error("НЕИЗВЕСТНАЯ ОШИБКА ПРИ ВСТУПЛЕНИИ В ГРУППУ ПОЛЬЗОВАТЕЛЯ {0} С ID: {1} ".format(ffirst_name,event.obj.user_id)+str(today))

         print('_' * 80)
        # ЕСЛИ ТИП ИВЕНТА == ВЫШЕЛ ИЗ ГРУППЫ

        if event.type == VkBotEventType.GROUP_LEAVE:
         print('_' * 80)
         try:

            user_inf = sessions.users.get(user_id=event.obj.user_id, fields='sex')
            ffirst_name = (str(user_inf[0]['first_name']))

            #print(user_inf)
            #print(ffirst_name)

            l_m_1 = '{0}, ну куда-же ты 🙄 '.format(ffirst_name)
            l_m_2 = 'Прощай {0}, если будет скучно, пиши нам 🤗'.format(ffirst_name)
            leave_message = [l_m_1, l_m_2]

            try:
                send_message(session_api, peer_id=event.obj.user_id, tit=bot,
                             message=(random.choice(leave_message)))
            except:
                print("НЕ МОГУ ПОПРАЩАТЬСЯ С ПОЛЬЗОВАТЕЛЕМ!")
            print("Пользователь успешно покинул группу")
         except:
             user_inf = sessions.users.get(user_id=event.obj.user_id, fields='sex')
             ffirst_name = (str(user_inf[0]['first_name']))
             print('НЕИЗВЕСТНАЯ ОШИБКА ПРИ ВЫХОДЕ ИЗ ГРУППЫ!')
             logging.error("НЕИЗВЕСТНАЯ ОШИБКА ПРИ ВЫХОДЕ ИЗ ГРУППЫ ПОЛЬЗОВАТЕЛЯ {0} С ID: {1} ".format(ffirst_name,event.obj.user_id) + str(today))

         print('_' * 80)
        # ЕСЛИ ТИП ИВЕНТА == ЗАПРЕТИТЬ СООБЩЕНИЯ ОТ ГУППЫ #3

        if event.type == VkBotEventType.MESSAGE_DENY:
           #print(event)
           print('_' * 80)
           try:
            item = event.obj.user_id
            print('Блок сообщений')

            print (item)



            ### DUHS - Всего написавших пользователей
            if os.path.exists("obj\\list_duhs.pkl"):
                duhs = load_obj('list_duhs')
                print ('Найден duhs')
                if item in duhs:

                    duhs.remove(event.obj.user_id) #удаляем пользователя из бд
                    save_obj(obj=duhs, name='list_duhs')
                    print('Удален из duhs')
                    if item not in deleted_items:
                        deleted_items.append(item)  # добавляем в список удаленных пользователей
                        save_obj(obj=deleted_items, name='deleted_items')

            ### Q - ПОЛНЫЙ СЛОВАРЬ ДАННЫХ О ПОЛЬЗОВАТЕЛЕ
            if os.path.exists("obj\\dict_users.pkl"):
                q = load_obj('dict_users')

                if item in q:
                    #если он был в диалоге
                    if q[item]['in_chat'] == 1 or q[item]['in_chat'] == 3:
                        found = q[item]['id_talker']
                        try:
                          send_message(session_api, peer_id=found, tit=bot,
                                    message='Диалог #{0} закончен 👫\nПонравился собеседник?'.format(
                                         q[item]['id_convers']),
                                    keyboard=create_keyboard('стоп', found, 1, q[found]['perk'], 0, 0))
                          if q[found]['bet'] != 0:
                              q[found]['diamonds'] += q[found]['bet']
                              send_message(session_api, peer_id=found, tit=bot,
                                           message='+{}💎'.format(str(q[found]['bet'])))
                              save_obj(obj=q, name='dict_users')
                        except:
                            pass
                        try:
                            q[found]['id_convers'] = 0
                            q[found]['in_chat'] = 0
                            q[found]['voices'] = 0

                            q[found]['bet'] = 0
                            q[found]['game_room'] = 0
                            q[found]['number'] = 0
                            q[found]['timeout'] = 0

                            q[found]['cod'] = 0
                            save_obj(obj=q, name='dict_users')
                        except:
                            pass

                    elif q[item]['in_chat'] == 2:
                        if len(q[item]['id_talker']) == 2:

                            for i in q[item]['id_talker']:
                                q[i]['id_talker'] = [i for i in q[i]['id_talker'] if i != item]
                                save_obj(obj=q, name='dict_users')
                                try:
                                    send_message(session_api, peer_id=i, tit=bot,
                                                 message='Один из собеседников покинул беседу!\nКоличество человек в беседе: 2')
                                except:
                                    print('ОШИБКА: Не могу отправить сообщение f при удалении')
                        else:
                            try:
                                found = q[item]['id_talker'][0]
                                fof = 0
                            except Exception as err:
                                print('ОШИБКА fof: Не могу отправить сообщение f при удалении' + str(err))
                                fof = 1

                            if fof == 0:
                                try:
                                    send_message(session_api, peer_id=found, tit=bot,
                                                 message='Беседа #{0} закончена 👫'.format(q[found]['id_convers']))
                                    open_menu(session_api, 'меню', found, bot, 0)
                                except:
                                    print('ОШИБКА: Не могу отправить сообщение f при удалении')

                                try:
                                    q[found]['in_chat'] = 0
                                    q[found]['id_talker'] = 0
                                    q[found]['id_convers'] = 0
                                    save_obj(obj=q, name='dict_users')
                                except:
                                    print('ОШИБКА: Не могу отправить сообщение f при удалении')



                    q[item]['id_convers'] = 0
                    q[item]['id_talker'] = 0
                    q[item]['in_chat'] = 0  # СОЗДАЕМ СЛОВАРЬ В СЛОВАРЕ С ДАННЫМИ ID БЕСЕДЫ

                    q[item]['voices'] = 0
                    q[item]['cod'] = 0
                    q[item]['last_activity'] = time.time()

                    q[item]['bet'] = 0
                    q[item]['game_room'] = 0
                    q[item]['number'] = 0
                    q[item]['timeout'] = 0
                    save_obj(obj=q, name='dict_users')
                    print('Очищен в q')


            ### QUE - список пользователей в очереди ожидания по критериям
            if os.path.exists("obj\\que.pkl"):
                que = load_obj('que')

                print(que)
                que = [name for name in que if event.obj.user_id not in name['user']]  # удаляет пользователя из очереди поиска по критериям
                save_obj(obj=que, name='que')
                print('Удален из QUE')
                print(que)


            ### ALL_LIST - всего пользователей ожидают
            if os.path.exists("obj\\all_list.pkl"):
                all_list = load_obj('all_list')
                if event.obj.user_id in all_list:
                    print('Удален из ALL_LIST')
                    all_list.remove(event.obj.user_id)  # удаляем из общего списка
                    save_obj(obj=all_list, name='all_list')
                    #### CONVERS - КОЛИЧЕСТВО ДИАЛОГОВ
                    if os.path.exists("obj\\convers.pkl"):
                        convers = load_obj('convers')

                        convers -= 1  # уменьшаем количество диалогов
                        save_obj(obj=convers, name='convers')

            ### THIRD_LIST - ожидание беседы
            if os.path.exists("obj\\third_list.pkl"):
                third_list = load_obj('third_list')
                if event.obj.user_id in third_list:
                    print('Удален из THIRD_LIST')
                    third_list.remove(event.obj.user_id) #удаляем из ждущих в беседе
                    save_obj(obj=third_list, name='third_list')

           except:
               print('ОШИБКА ПРИ БЛОКИРОВКИ СООБЩЕНИЙ ПОЛЬЗОВАТЕЛЕМ')
               logging.error("ОШИБКА ПРИ БЛОКИРОВКИ СООБЩЕНИЙ ПОЛЬЗОВАТЕЛЕМ {0}".format(str(today)))
           print('_' * 80)

        # ЕСОИ ТИП ИВЕНТА == РАЗРЕШИТЬ СООБЩЕНИЯ ОТ ГРУППЫ
        if event.type == VkBotEventType.MESSAGE_ALLOW:
            print('_' * 80)
            item = event.obj.user_id
            print('Разблок сообщений')

            print(item)
            if os.path.exists("obj\\deleted_items.pkl"):
                deleted_items = load_obj('deleted_items')

                if item in deleted_items:

                    deleted_items.remove(item) #удаляем пользователя из deleted_items
                    save_obj(obj=deleted_items, name='deleted_items')
                    print('Удален из deleted_items')

            print('_' * 80)


        #ЕСЛИ ТИП ИВЕНТА == НОВОМУ СООБЩЕНИЮ ТО
        if event.type == VkBotEventType.MESSAGE_NEW:
         #try: #2
            print('_' * 80)
            print(event.obj.peer_id)



            if event.obj.peer_id != 106545709 and event.obj.peer_id != 523486418 and status_bot == 0:
                send_message(session_api, peer_id=event.obj.from_id, tit=bot,
                             message='⚠Ведутся техническе работы!⚠ Пожалуйста подождите!⏳')
                time.sleep(10)
                break
            mon = monotonic()
            dat = time.time()
            start_mon = time.monotonic()


            date_now = datetime.fromtimestamp(dat).strftime("%d.%m.%y %H:%M")
            print ('Время сейчас: ' + str(time.time()) +' | ' +str(date_now))

            #print (event.obj.id)


            print('|' * 80)



              # Записать в переменную response - event.obj.text.lower


                #ДЛЯ СООБЩЕНИЙ ИЗ СООБЩЕСТВА
            if event.obj.peer_id == event.obj.from_id:


                mon_z = monotonic()
                print(mon_z - mon)

                item = event.obj.from_id  # id пользователя
                response = event.obj.text.lower()
                otvet = 0

                #print(code14)
                #print('Количество VIP подписок на 2 недели: {0}' .format(len(code14)))
                #print('Количество VIP подписок на месяц: {0}'.format(len(code31)))
                #print('Количество кодов на 150 алмазов: {0}'.format(len(diamonds150)))


             # ЕСЛИ ID ПОЛЬЗОВАТЕЛЯ НЕТ В СПИСКЕ DUHS ТОГДА ДОБАВИТЬ ЭТО ID К НЕМУ
                if item not in q: #item not in duhs and
                    hi = 0
                    q[item] = {'id_convers': 0, 'id_talker': 0, 'in_chat':0} #СОЗДАЕМ СЛОВАРЬ В СЛОВАРЕ С ДАННЫМИ ID БЕСЕДЫ
                    q[item]['perk'] = 0
                    q[item]['perk_time'] = 0
                    q[item]['perk_date'] = 0
                    q[item]['rep'] = 0
                    q[item]['rep_points'] = 0
                    q[item]['diamonds'] = 10
                    q[item]['voices'] = 0
                    q[item]['cod'] = 0
                    q[item]['reg_date'] = time.time()
                    q[item]['last_activity'] = time.time()

                    q[item]['bet'] = 0
                    q[item]['game_room'] = 0
                    q[item]['number'] = 0
                    q[item]['timeout'] = 0

                    zonk[item] = {'win':0}
                    zonk[item]['lose'] = 0
                    zonk[item]['draw'] = 0

                    zonk[item]['coef'] = 0
                    save_obj(obj=zonk, name='zonk')
                    duhs.append(item)
                    save_obj(obj=duhs, name='list_duhs')

                    id_convers = q[item]['id_convers']

                    id_talker = q[item]['id_talker']
                    in_chat = q[item]['in_chat']
                    in_chat_v = in_chat
                    perk =q[item]['perk']
                    perk_time = q[item]['perk_time']
                    perk_date = q[item]['perk_date']
                    rep = q[item]['rep']
                    rep_points = q[item]['rep_points']
                    diamonds = q[item]['diamonds']
                    voices = q[item]['voices']
                    cod = q[item]['cod']
                    reg_date = q[item]['reg_date']
                    last_activity = q[item]['last_activity']

                    save_obj(obj=q, name='dict_users')

                    bet = q[item]['bet']
                    game_room =q[item]['game_room']
                    number = q[item]['number']
                    timeout = q[item]['timeout']

                    win = zonk[item]['win']
                    lose = zonk[item]['lose']
                    draw = zonk[item]['draw']

                    coef = zonk[item]['coef']


                    # rp - репутация в звездочках, nl - осталось очков до след уровня
                    rp, nl = r(q[item]['rep_points'], item)

                elif item in q:
                    if item not in duhs:
                        duhs.append(item)
                        save_obj(obj=duhs, name='list_duhs')
                        send_message(session_api, peer_id=item, tit=bot,
                                     message='Спасибо что снова с нами 🤗')

                    hi =1
                    found = q[item]['id_talker']
                    # rp - репутация в звездочках, nl - осталось очков до след уровня
                    if q[item]['in_chat'] == 3  and q[item]['cod'] == 0 and q[found]['cod'] == 0:
                        mon_choise(q,session_api, bot, mon, item)
                        q = load_obj('dict_users')
                    id_convers = q[item]['id_convers']

                    id_talker = q[item]['id_talker']

                    in_chat = q[item]['in_chat']
                    in_chat_v=in_chat
                    perk = q[item]['perk']
                    perk_time = q[item]['perk_time']
                    perk_date = q[item]['perk_date']
                    rep = q[item]['rep']
                    rep_points = q[item]['rep_points']
                    diamonds = q[item]['diamonds']

                    try:
                     voices = q[item]['voices']
                    except:
                     q[item]['voices'] = 0
                     voices = q[item]['voices']

                    try:
                     cod = q[item]['cod']
                    except:
                     q[item]['cod'] = 0
                     cod = q[item]['cod']

                    try:
                     bet = q[item]['bet']
                    except:
                     q[item]['bet'] = 0
                     bet = q[item]['bet']

                    try:
                     reg_date = q[item]['reg_date']
                     q[item]['last_activity'] = time.time()
                     last_activity = q[item]['last_activity']
                    except:
                     q[item]['reg_date'] = time.time()
                     reg_date = q[item]['reg_date']
                     q[item]['last_activity'] = time.time()
                     last_activity = q[item]['last_activity']

                    try:
                     game_room = q[item]['game_room']
                    except:
                     q[item]['game_room'] = 0
                     game_room = q[item]['game_room']

                    try:
                     number = q[item]['number']
                    except:
                     q[item]['number'] = 0
                     number = q[item]['number']

                    try:
                     timeout = q[item]['timeout']
                    except:
                     q[item]['timeout'] = 0
                     timeout = q[item]['timeout']

                    try:
                     win = zonk[item]['win']
                    except:
                     zonk[item] = {'win': 0}
                     win = zonk[item]['win']

                    try:
                     lose = zonk[item]['lose']
                    except:
                     zonk[item]['lose'] = 0
                     lose = zonk[item]['lose']

                    try:
                     draw = zonk[item]['draw']
                    except:
                     zonk[item]['draw'] = 0
                     draw = zonk[item]['draw']

                    try:
                     coef = zonk[item]['coef']
                    except:
                     zonk[item]['coef'] = 0
                     coef = zonk[item]['coef']

                    save_obj(obj=zonk, name='zonk')
                    save_obj(obj=q, name='dict_users')

                    rp, nl = r(q[item]['rep_points'], item)
                    #проверка на таймауты в игре зонк
                    if q[item]['in_chat'] == 3  and q[item]['cod'] == 0 and q[found]['cod'] == 0:
                        mon_choise(q, session_api, bot, mon, item)
                        q = load_obj('dict_users')
                    #print("Пользователь есть в БД")

                #print(q[item]['perk'])
                #подсчет количества написавших боту пользователей
                count = len(q)

                print(q[item]['cod'])

                keyboard = create_keyboard(response, item, in_chat, perk, number, var)
                #q1, fwd, len_buf, type_typing, sticker_id = attachments(session_api, bot, event, requests, q1, len_buf)

                #send_message(session_api, peer_id=106545709, tit=bot,
                #             message='',q1='wall-179410262_486')
                if q[item]['in_chat'] == 1 or q[item]['in_chat'] == 2 or q[item]['cod'] == 'admin' or admin == 'spam' or q[item]['cod'] == 'err':
                    #t_v = threading.Thread(target=attachments, name='thread_v', args=(session_api, bot, event,requests, q1, len_buf, item))
                    #t_v.start()
                    #print('Cтартанул поток {}'.format(t_v.name))
                    #pool = ThreadPool(processes=1)

                    #async_result = pool.apply_async(attachments, (session_api, bot, event,requests, q1, len_buf, item))  # tuple of args for foo

                    #q1, fwd, len_buf, type_typing, sticker_id= async_result.get()

                    #print(sticker_id)
                    q1, fwd, len_buf, type_typing, sticker_id = attachments (session_api, bot, event,requests, q1, len_buf, item)



                #добавляем спам фильтр
                spam_filter = [name for name in list_responses if name in response]


                if (response == response1 and q[item]['cod'] != 'admin' and item1 == item and q1 == 0 and  sticker_id ==0 ) and in_chat !=3:
                    print('Пауза')
                    #time.sleep(1)

                    if (((response == response1 and response == response2) or (len(response) == len(response1) and len(response) == len(response2))) and item1 == item and item2 == item and q1 == 0 and  sticker_id ==0):
                        print('Защита от спама, отключение')
                        print('_' * 80 + str(today))
                        send_message(session_api, peer_id=item, tit=bot,
                                     message='Слишком много однотипных запросов. Попробуйте позже!')

                        break

                    response2 = response
                    item2 = item


                else:

                    response1 = response
                    item1 = item

                #mon_1 = monotonic()
                #print(mon_1 - mon)
                if spam_filter != []:
                    bbb =['http', '.ru' , '.com', '.net', 'vk.com', '@']
                    bbb = [i for i in bbb if i in str(response) and (in_chat ==1 or in_chat ==2)]
                    if len(bbb) != 0:
                         send_message(session_api, peer_id=item, tit=bot,
                                     message='Вам запрещенно отправлять ссылки!')
                         print ('Найдена спам ссылка')

                         print('_' + '_' * 71 + '{:>.3f}'.format(time.monotonic() - start_mon))
                         break

                #ГЕНЕРАТОР СПИСКОВ
                # zxc список VIP пользователей

                zonk_time_out = [i for i in q if q[i]['in_chat'] == 3]
                mon_3 = monotonic()
                print(mon_3 - mon)
                zxc = [i for i in q if q[i]['perk'] > 0]
                   # список левл апов
                congr = [i for i in q if
                            (q[i]['rep_points'] >= 2000 and q[i]['rep'] == 0) or (
                                    q[i]['rep_points'] >= 5000 and q[i]['rep'] == 1) or (
                                    q[i]['rep_points'] == 10000 and q[i]['rep'] == 2) or (
                                    q[i]['rep_points'] == 20000 and q[i]['rep'] == 3)]
                # ТЕ КТО В ЧАТЕ И НЕТ АКТИВНОСТИ 3 ДНЯ

                timeout_chat1 = [i for i in q if q[i]['in_chat'] == 1 and dat > q[i]['last_activity'] + 86400]
                timeout_chat2 = [i for i in q if q[i]['in_chat'] == 2 and i not in third_list and dat > q[i]['last_activity'] + 43200]
                timeout_chat3 = [i for i in q if q[i]['in_chat'] == 3 and dat > q[i]['last_activity'] + 43200]

                search_helper1 = [name for person in que for name, attr in person['user'].items() if
                                 attr['search'] == 1]
                search_helper2 = [name for person in que for name, attr in person['user'].items() if
                                  attr['search'] == 2]

                if len(timeout_chat2) > 0:
                       print('Таймаут2' + str(timeout_chat2))
                       for n in timeout_chat2:
                           if dat > q[n]['last_activity'] + 43200:
                               try:
                                   # если собеседников 3
                                   if len(q[n]['id_talker']) == 2:
                                       try:
                                           send_message(session_api, peer_id=n, tit=bot,
                                                        message='Вы были исключены из беседы #{0} 👫 за бездействие!'.format(
                                                            q[n]['id_convers']))
                                           open_menu(session_api, 'меню', n, bot, var)
                                       except:
                                           print('ОШИБКА: Не могу отправить сообщение f таймаут2')
                                       for i in q[n]['id_talker']:
                                           q[i]['id_talker'] = [i for i in q[i]['id_talker'] if i != n]
                                           save_obj(obj=q, name='dict_users')
                                           try:
                                              send_message(session_api, peer_id=i, tit=bot,
                                                        message='Один из собеседников покинул беседу!\nКоличество человек в беседе: 2')

                                           except:
                                               print('ОШИБКА: Не могу отправить сообщение f таймаут2')

                                       try:
                                           q[n]['in_chat'] = 0
                                           q[n]['id_talker'] = 0
                                           q[n]['id_convers'] = 0
                                           save_obj(obj=q, name='dict_users')
                                       except:
                                           print('ОШИБКА: Не могу отправить сообщение f таймаут2')

                                   else:
                                     try:
                                        found = q[n]['id_talker'][0]
                                        fof = 0
                                     except Exception as err:
                                        print('ОШИБКА fof: Не могу отправить сообщение f таймаут2' + str(err))
                                        fof = 1

                                     if fof == 0:
                                       try:
                                           send_message(session_api, peer_id=found, tit=bot,
                                                        message='Вы были исключены из беседы #{0} 👫 за бездействие!'.format(q[found]['id_convers']))
                                           open_menu(session_api, 'меню', found, bot, var)
                                       except:
                                           print('ОШИБКА: Не могу отправить сообщение f таймаут2')
                                       try:
                                           send_message(session_api, peer_id=n, tit=bot,
                                                        message='Вы были исключены из беседы #{0} 👫 за бездействие!'.format(q[n]['id_convers']))
                                           open_menu(session_api, 'меню', n, bot, var)
                                       except:
                                           print('ОШИБКА: Не могу отправить сообщение f таймаут2')

                                       try:
                                           q[found]['in_chat'] = 0
                                           q[found]['id_talker'] = 0
                                           q[found]['id_convers'] = 0
                                           save_obj(obj=q, name='dict_users')
                                       except:
                                           print('ОШИБКА: Не могу отправить сообщение f таймаут2')
                                       try:
                                           q[n]['in_chat'] = 0
                                           q[n]['id_talker'] = 0
                                           q[n]['id_convers'] = 0
                                           save_obj(obj=q, name='dict_users')
                                       except:
                                           pass
                               except Exception as err:
                                   print('ОШИБКА: Не могу отправить сообщение f таймаут2' + str(err))
                                   logging.error("ОШИБКА: Не могу отправить сообщение f таймаут2: {0} ".format(err) + str(today))


                if len(timeout_chat1) > 0:
                       print('Таймаут1' + str(timeout_chat1))
                       for i in q:

                           if dat > q[i]['last_activity'] + 86400 and q[i]['in_chat'] == 1:  # 86400:
                             try:
                                f = q[i]['id_talker']
                                ff=1
                             except:
                                ff=0
                                print('Ошибка timeot1')

                             if ff==1 and dat > q[f]['last_activity'] + 86400 and q[f]['in_chat'] == 1:
                               try:
                                   #print('Не могу отправить сообщение i об исключении в timeout_chat1:' + str(f))
                                   send_message(session_api, peer_id=i, tit=bot,
                                                message='Вы были исключены из диалога #{0} за бездействие 👫\nПонравился собеседник?'.format(
                                                    q[i]['id_convers']),
                                                keyboard=create_keyboard('стоп', i, q[i]['in_chat'], q[i]['perk'], 0,
                                                                         var))
                               except:
                                   print('Не могу отправить сообщение i об исключении в timeout_chat1:' + str(i))

                               try:
                                   q[i]['id_convers'] = 0
                                   q[i]['in_chat'] = 0
                                   q[i]['voices'] = 0
                                   save_obj(obj=q, name='dict_users')
                               except:
                                   print('Не могу обновить данные для i в q в генераторе timeout_chat1')


                               try:

                                   #print('Не могу отправить сообщение i об исключении в timeout_chat1:' + str(f))
                                   send_message(session_api, peer_id=f, tit=bot,
                                                message='Вы были исключены из диалога #{0} за бездействие 👫\nПонравился собеседник?'.format(
                                                    q[f]['id_convers']),
                                                keyboard=create_keyboard('стоп', f, q[f]['in_chat'], q[f]['perk'], 0,
                                                                         var))
                               except:
                                   print('Не могу отправить сообщение i об исключении в timeout_chat1:' + str(f))

                               try:
                                   q[f]['id_convers'] = 0
                                   q[f]['in_chat'] = 0
                                   q[f]['voices'] = 0
                                   save_obj(obj=q, name='dict_users')
                               except:
                                   print('Не могу обновить данные для f в q в генераторе timeout_chat1')

                if len(timeout_chat3) > 0:
                    print('Таймаут3' + str(timeout_chat3))
                    keyboard = VkKeyboard(one_time=True)
                    for i in q:

                        if dat > q[i]['last_activity'] + 43200 and q[i]['in_chat'] == 3:  # 86400:
                            f = q[i]['id_talker']


                            try:
                                q[i]['game_room'] = 0
                                q[i]['number'] = 0
                                q[i]['in_chat'] = 1
                                q[i]['timeout'] = 0
                                q[i]['cod'] = 0
                                if q[i]['bet'] != 0:
                                    q[i]['diamonds'] += q[i]['bet']
                                    send_message(session_api, peer_id=i, tit=bot,
                                                 message='+{}💎'.format(q[i]['bet']))
                                q[i]['bet'] = 0
                                save_obj(obj=q, name='dict_users')
                            except:
                                print('Не могу обновить данные для i в q в генераторе timeout_chat3')


                            try:
                                send_message(session_api, peer_id=i, tit=bot,
                                             message='Вы были исключены за бездействие!\nИгра окончена!😕',
                                             keyboard=keyboard.get_empty_keyboard())
                            except:
                                print('Не могу отправить i сообщение об исключении в timeout_chat3:' + str(i))


                            try:
                                q[f]['game_room'] = 0
                                q[f]['number'] = 0
                                q[f]['in_chat'] = 1
                                q[f]['timeout'] = 0
                                q[f]['cod'] = 0
                                if q[f]['bet'] != 0:
                                    q[f]['diamonds'] += q[f]['bet']
                                    send_message(session_api, peer_id=f, tit=bot,
                                                 message='+{}💎'.format(q[f]['bet']))
                                q[f]['bet'] = 0
                                save_obj(obj=q, name='dict_users')

                            except:
                                print('Не могу обновить данные для f в q в генераторе timeout_chat3')

                            try:
                                send_message(session_api, peer_id=f, tit=bot,
                                         message='Вы были исключены за бездействие!\nИгра окончена!😕',
                                         keyboard=keyboard.get_empty_keyboard())
                            except:
                                print('Не могу отправить f сообщение:' + str(f))

                if len(zonk_time_out) != 0:
                       keyboard = VkKeyboard(one_time=True)
                       for i in zonk_time_out:
                           t = mon - q[i]['timeout']
                           m = 180 - int(t)
                           if (m == 60 or m == 30 or m == 15) and q[q[i]['id_talker']]['cod'] == 'endzonk':
                               send_message(session_api, peer_id=i, tit=bot,
                                            message='Вы будите исключены за бездействие, через {} секунд'.format(
                                                str(m)))
                           elif m <= 0 and q[q[i]['id_talker']]['cod'] == 'endzonk':


                               send_message(session_api, peer_id=i, tit=bot,
                                            message='Вы были исключены за бездействие!\nИгра окончена!',
                                            keyboard=keyboard.get_empty_keyboard())
                               send_message(session_api, peer_id=q[i]['id_talker'], tit=bot,
                                            message='Ваш собеседник исключен за бездействие!😔\nИгра окончена!😕',
                                            keyboard=keyboard.get_empty_keyboard())
                               if q[q[i]['id_talker']]['bet'] != 0:
                                   q[q[i]['id_talker']]['diamonds'] += q[q[i]['id_talker']]['bet']

                                   send_message(session_api, peer_id=q[i]['id_talker'], tit=bot,
                                                message='Ваша ставка аннулирована\n+{}💎'.format(
                                                    q[q[i]['id_talker']]['bet']))

                               q[i]['game_room'] = 0
                               q[i]['bet'] = 0
                               q[i]['number'] = 0
                               q[i]['in_chat'] = 1

                               q[q[i]['id_talker']]['game_room'] = 0
                               q[q[i]['id_talker']]['bet'] = 0
                               q[q[i]['id_talker']]['number'] = 0
                               q[q[i]['id_talker']]['in_chat'] = 1

                               q[q[i]['id_talker']]['timeout'] = 0
                               q[i]['timeout'] = 0

                               q[i]['cod'] = 0
                               q[q[i]['id_talker']]['cod'] = 0
                               save_obj(obj=q, name='dict_users')

                if len(congr) != 0:
                       print('Повысили свою репутацию' + str(congr))
                       deadpool = [9110, 9111, 9127]
                       for i in congr:
                           print(q[i]['rep_points'])
                           print(i)
                           # if (q[i]['rep_points'] >=2000 and q[i]['rep'] == 0) or (q[i]['rep_points'] >=5000 and q[i]['rep'] == 1) or (q[i]['rep_points'] >=10000 and q[i]['rep'] == 2) or (q[i]['rep_points'] >=20000 and q[i]['rep'] == 3):
                           rp_congr, nl_congr = r(q[i]['rep_points'], i)
                           q = load_obj('dict_users')
                           send_message(session_api, peer_id=i, tit=bot,
                                        message='🎉 Вы достигли репутации: {}'.format(rp_congr))
                           send_message(session_api, peer_id=i, tit=bot, message='', sticker_id=random.choice(deadpool))

                x = []
                # print(zxc)
                if len(zxc) != 0:
                       #test_newsler = newsletter
                       for i in zxc:
                           end, left = end_perk(dat, i)
                           cxz = {i: [left, q[i]['perk_date']]}
                           x.append(cxz)

                           if end == 1: #рассылка окончания Вип
                               q[i]['perk'] = 0
                               q[i]['perk_time'] = 0
                               # снят вип автоматически
                               q[i]['perk_date'] = 1
                               q[i]['voices'] = 0
                               if i in newsletter:
                                   newsletter.remove(i)
                                   save_obj(obj=newsletter, name='newsletter')
                               save_obj(obj=q, name='dict_users')
                               #send_end_vip(i, bot, session_api)
                               t_v = threading.Thread(target=send_end_vip, name='thread_v',args=(i, bot, session_api))
                               t_v.start()
                               print('Cтартанул поток {}'.format(t_v.name))

                           elif end !=1 and left < 24.0 and i not in newsletter: #рассылка бонусов
                                   # print(left)

                                   print(i)

                                   newsletter.append(i)

                                   t_x = threading.Thread(target=bonus_vip, name='thread_x',
                                                          args=(bot, session_api, i))
                                   t_x.start()
                                   print('Cтартанул поток {}'.format(t_x.name))

                                   save_obj(obj=newsletter, name='newsletter')

                           #if len(test_newsler) < len(newsletter):
                            #   print('РАССЫЛКА УВЕДОМЛЕНИЙ О БОНУСАХ ЗАВЕРШИНА')




                if len(search_helper1) > 2 or len(search_helper2) > 2:
                    q_helper = [i for i in q if q[i]['in_chat'] == 0 and dat > q[i]['last_activity'] + 43200 and q[i]['cod'] == 0]
                    #print('helper' + str(q_helper))
                    if len(q_helper) > 1:

                        result = random.choice(q_helper)

                        print('Была last_act: ' + str(q[result]['last_activity']))
                        q[result]['last_activity'] = time.time()
                        save_obj(obj=q, name='dict_users')
                        print('Стала last_act: ' + str(q[result]['last_activity']))
                        #print(result)

                        #if random.randint(1, 2) == 1:
                        t_h = threading.Thread(target=helper, name='thread_h',
                                                   args=(sessions, session_api, result, search_helper1, bot, search_helper2,logging ))
                        t_h.start()
                        print('Cтартанул поток {}'.format(t_h.name))




                #print(newsletter)
                print('ГЕНЕРАТОР СПИСКОВ РАБОТАЕТ')

                q = load_obj('dict_users')


                #РАСЧЕТ СЛУЧАЙНОЙ НАГРАДЫ #ТОЛЬКО ДЛЯ ТЕХ КТО ОБЩАЕТСЯ В ЧАТЕ
                if q[item]['in_chat'] !=0 and spam_filter == []:
                    g_rep, p_rep = random_bonus(q, threading, bot,session_api, rep, item, event)

                    q = load_obj('dict_users')
                    diamonds = q[item]['diamonds']

                    #БОНУСНАЯ НАДБАВКА
                    if rep_points == 19 or rep_points == 199 or rep_points == 1999 or rep_points == 19999:
                        q[item]['diamonds'] += 1
                        diamonds = q[item]['diamonds']
                        save_obj(obj=q, name='dict_users')

                #узнаем статус пользователя
                if q[item]['perk'] == 0:
                    tit = talker
                    info = '-3💎'


                elif q[item]['perk'] > 0:
                    tit = vip
                    info = '✅'

                print('Что в q1: ' + str(q1))
                print('Что в sticker_id:' + str(sticker_id))
                print('Кто находиться в очереди на поиск: ' + str(que))
                print('Кто находиться в all_list' + str(all_list))
                print('Кто находиться в third_list' + str(third_list))
                print('-' * 80)
                if item == 106545709:

                    if (response == '!админ' or response == '!назад' or response == '♻'):# and event.obj.peer_id == 106545709:

                        admin = 1
                        #ФУНКЦИЯ ОТКРЫТИЯ АДМИНКИ
                        open_admin(session_api,status_bot,bot, code14, code31, diamonds150, gold_vip, duhs, item, in_chat, perk, number, dat)
                        q = load_obj('dict_users')
                        print('Admin' + '_' * 71 + '{:>.3f}'.format(time.monotonic() - start_mon))
                        break

                    elif response == '!офф' and q[item]['cod'] == 'admin' and item == 106545709:


                        status_bot = 0
                        save_obj(obj=status_bot, name='status_bot')

                        open_admin(session_api,status_bot,bot, code14, code31, diamonds150, gold_vip, duhs, item, in_chat, perk, number, dat)
                        q = load_obj('dict_users')
                        print('Admin' + '_' * 71 + '{:>.3f}'.format(time.monotonic() - start_mon))
                        break

                    elif response == '!он' and q[item]['cod'] == 'admin' and item == 106545709:

                        status_bot = 1
                        save_obj(obj=status_bot, name='status_bot')
                        q[item]['cod'] = 'status_bot'
                        save_obj(obj=q, name='dict_users')
                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='Бот запущен ✅\nОтправвить сообщение о работоспособности бота?',keyboard =create_keyboard(response, item, in_chat, perk, number, var))

                        print('Admin' + '_' * 71 + '{:>.3f}'.format(time.monotonic() - start_mon))
                        break

                    elif (response == 'да' or response == 'нет') and q[item]['cod'] == 'status_bot' and item == 106545709:

                        if response == 'да':
                            for i in duhs:
                                try:

                                    send_message(session_api, peer_id=i, tit=bot,
                                                 message='Технические работы завершены! Анонимный чат работает в штатном режиме!😉')
                                except:
                                    # ЕСЛИ НЕ УДАЕТСЯ ОТПРАВИТЬ РАССЫЛКУ ПОЛЬЗОВАТЕЛЮ, ОН ОЧИЩАЕТСЯ И ДОБАВЛЯЕТСЯ В СПИСОК УДАЛЕННЫХ ПОЛЬЗОВАТЕЛЕЙ
                                    if i in duhs:
                                        duhs.remove(i)  # удаляем из duhs
                                        save_obj(obj=duhs, name='list_duhs')
                                        print('Удален из duhs')
                                        if i not in deleted_items:
                                            deleted_items.append(i)  # добавляем в список удаленных пользователей
                                            save_obj(obj=deleted_items, name='deleted_items')

                                        que = [name for name in que if i not in name[
                                            'user']]  # удаляет пользователя из очереди поиска по критериям
                                        save_obj(obj=que, name='que')
                                        print('Удален из QUE')
                                        print(que)
                                        f = q[i]['id_talker']
                                        if q[i]['in_chat'] == 1 and q[f]['id_talker'] == i:

                                            try:
                                                send_message(session_api, peer_id=f, tit=bot,
                                                             message='Диалог #{0} закончен 👫\nПонравился собеседник?'.format(
                                                                 q[item]['id_convers']),
                                                             keyboard=create_keyboard('стоп', f, 1, q[f]['perk'], 0, 0))
                                            except:
                                                pass
                                            try:
                                                q[f]['id_convers'] = 0
                                                q[f]['in_chat'] = 0
                                                q[f]['voices'] = 0
                                            except:
                                                pass
                                        q[i]['id_convers'] = 0
                                        q[i]['id_talker'] = 0
                                        q[i]['in_chat'] = 0

                                        q[i]['voices'] = 0
                                        q[i]['cod'] = 0
                                        q[i]['last_activity'] = time.time()

                                        q[i]['bet'] = 0
                                        q[i]['game_room'] = 0
                                        q[i]['number'] = 0
                                        q[i]['timeout'] = 0
                                        save_obj(obj=q, name='dict_users')

                                        if i in all_list:
                                            print('Удален из ALL_LIST')
                                            all_list.remove(i)  # удаляем из общего списка
                                            save_obj(obj=all_list, name='all_list')
                                            #### CONVERS - КОЛИЧЕСТВО ДИАЛОГОВ
                                            convers -= 1  # уменьшаем количество диалогов
                                            save_obj(obj=convers, name='convers')

                                        if i in third_list:
                                            print('Удален из THIRD_LIST')
                                            third_list.remove(i)  # удаляем из ждущих в беседе
                                            save_obj(obj=third_list, name='third_list')
                                    continue


                        open_admin(session_api,status_bot,bot, code14, code31, diamonds150, gold_vip, duhs, item, in_chat, perk, number, dat)
                        q = load_obj('dict_users')
                        print('Admin' + '_' * 71 + '{:>.3f}'.format(time.monotonic() - start_mon))
                        break

                    elif response == '!рассылка' and admin == 1 and event.obj.peer_id == 106545709:

                        admin = 'spam'
                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='Введите текст сообщения для рассылки')
                        print('Admin' + '_' * 71 + '{:>.3f}'.format(time.monotonic() - start_mon))
                        break

                    elif admin == 'spam' and event.obj.peer_id == 106545709:
                        otvet = 1
                        admin = 'spam1'
                        send = event.obj.text
                        send_q1=q1
                        send_sticker_id=sticker_id
                        #print('Стикер: '+ str(sticker_id))
                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='Выберите пользователей для рассылки сообщений или введите id вручную', keyboard=create_keyboard(response, item, in_chat, perk, number, 'spam'))
                        print('Admin' + '_' * 71 + '{:>.3f}'.format(time.monotonic() - start_mon))
                        response = ''
                        break

                    elif admin == 'spam1' and event.obj.peer_id == 106545709: #4

                        # писали боту находятся в меню
                        chat0 = [i for i in q if q[i]['in_chat'] == 0]
                        # сейчас в чате
                        chat1 = [i for i in q if q[i]['in_chat'] == 1]
                        # сейчас в беседе
                        chat2 = [i for i in q if q[i]['in_chat'] == 2]
                        # сейчас в зонке
                        chat3 = [i for i in q if q[i]['in_chat'] == 3]
                        # вип пользователи
                        perk1 = [i for i in q if q[i]['perk'] == 1]
                        # не писали более 3 дней
                        missing = [i for i in q if  dat > q[i]['last_activity'] + 259200]
                        #без вип
                        perk0 = [i for i in q if q[i]['perk'] == 0]
                        l=''
                        if response == 'в меню':
                           l = chat0
                        elif response == 'в чате':
                           l = chat1

                        elif response == 'в беседе':
                           l = chat2
                        elif response == 'в зонке':
                           l = chat3
                        elif response == 'випам':
                            l = perk1
                        elif response == 'всем':
                            l = duhs
                        elif response == 'пропавшим':
                            l = missing
                        elif response == 'без вип':
                            l = perk0
                        if l =='':
                            l=event.obj.text
                            if ',' in l:
                                k = l.split(',')
                                l = [int(x) for x in k]
                        #try: #5
                        if l != '':


                            chunk_len = 2
                            chunks = [l[x:x + chunk_len] for x in range(0, len(l), chunk_len)]

                            p_func1 = Process(target=kuk, args=(send, chunks, send_sticker_id, send_q1))
                            p_func1.start()
                            print('Старт процесса1')
                            p_func1.join()
                            #t = threading.Thread(target=test_multiprocessing, args = (send, chunks, send_sticker_id, send_q1))
                            #t.start()


                            print('Бот вышел из цикла потоков')

                            open_admin(session_api, status_bot, bot, code14, code31, diamonds150, gold_vip, duhs, item,
                                       in_chat,
                                       perk, number, dat)

                        send = ''
                        admin = 0
                        response = ''

                        q1 = 0
                        # send_q1 = 0
                        #send_sticker_id = 0
                        sticker_id = 0
                        otvet = 1

                    elif response == '!del' and q[item]['cod'] == 'admin' and event.obj.peer_id == 106545709:
                        send_message(session_api, peer_id=106545709, tit=bot,
                                     message='Введите ID пользователя для полного удпления из БД')
                    elif response == '!очистить очередь' and q[item]['cod'] == 'admin':

                        que = []  # список пользователей в очереди ожидания
                        save_obj(obj=que, name='que')

                        all_list = [] #общий список очереди
                        save_obj(obj=all_list, name='all_list')

                        third_list = []  # беседа
                        save_obj(obj=third_list, name='third_list')

                        send_message(session_api, peer_id=106545709, tit=bot,
                                     message='Списки очередей: que, all_list, third_list. Очищены!')
                        print('Admin' + '_' * 71 + '{:>.3f}'.format(time.monotonic() - start_mon))
                        break

                    elif response == '!2' and q[item]['cod'] == 'admin':

                        inc2 = [i for i in q if q[i]['in_chat'] == 2]
                        send_message(session_api, peer_id=106545709, tit=bot,
                                     message=inc2)
                        if len(inc2) !=0:
                            for n in inc2:

                                q[n]['id_convers'] = 0
                                q[n]['in_chat'] = 0
                                q[n]['voices'] = 0
                                q[n]['id_talker'] = 0

                                q[n]['bet'] = 0
                                q[n]['game_room'] = 0
                                q[n]['number'] = 0
                                q[n]['timeout'] = 0

                                q[n]['cod'] = 0
                                save_obj(obj=q, name='dict_users')
                        print('Admin' + '_' * 71 + '{:>.3f}'.format(time.monotonic() - start_mon))
                        break
                    #УДАЛЕНИЕ ПОЛЬЗОВАТЕЛЕЙ КОТОРЫЕ ЗАБЛОКИРОВАЛИ СООБЩЕНИЯ И ДАВНО НЕ БЫЛИ В СИСТЕМЕ
                    elif response == '!удалить' and q[item]['cod'] == 'admin' and len(deleted_items) != 0 and event.obj.peer_id == 106545709: #6

                        di_list = [] #Временный список
                        how_many_de = [] #Количество удаленных пользователей
                        how_many_re = []
                        for i in q:
                            if i not in duhs and i not in deleted_items:
                                deleted_items.append(i)
                                save_obj(obj=deleted_items, name='deleted_items')
                                send_message(session_api, peer_id=106545709, tit=bot,
                                             message='Добавлен в список на исключение: @id{0}({0})'.format(i))
                                #continue

                        for i in deleted_items:
                            try:
                             if i in q and q[i]['perk'] == 0 and i not in duhs and dat > q[i]['last_activity'] + 60:

                                del q[i]
                                save_obj(obj=q, name='dict_users')
                                del zonk[i]
                                save_obj(obj=zonk, name='zonk')

                                how_many_de.append('@id{0}({0})'.format(i))

                                #send_message(session_api, peer_id=106545709, tit=bot,
                                #        message='Удален в q и zonk: @id{0}({0})'.format(i))



                             elif i in duhs and i not in q:
                                 duhs.remove(i)
                                 save_obj(obj=duhs, name='list_duhs')
                                 how_many_re.append('@id{0}({0})'.format(i))
                                 #send_message(session_api, peer_id=106545709, tit=bot,
                                 #             message='Восстановлен: @id{0}({0})'.format(i))
                             elif i not in duhs and i not in q:
                                 how_many_re.append('@id{0}({0})'.format(i))
                             else:

                                 send_message(session_api, peer_id=106545709, tit=bot,
                                              message='Не удален, активен: @id{0}({0})'.format(i))
                                 di_list.append(i)


                            except Exception as ert:
                                print(ert)
                                di_list.append(i)
                                send_message(session_api, peer_id=106545709, tit=bot,
                                             message='Ошибка при удалении: @id{0}({0})'.format(i))
                        try:
                          send_message(session_api, peer_id=106545709, tit=bot,
                                     message='Удалено: {0}\nВосстановлено: {1}'.format(how_many_de,how_many_re))
                        except Exception as err:
                            print('ОШИБКА В УДАЛЕНИИ'+ str(err))
                        deleted_items = di_list
                        save_obj(obj=deleted_items, name='deleted_items')
                        open_admin(session_api, status_bot, bot, code14, code31, diamonds150, gold_vip, duhs, item, in_chat,
                                   perk, number, dat)
                        q = load_obj('dict_users')
                        print('Admin' + '_' * 71 + '{:>.3f}'.format(time.monotonic() - start_mon))
                        break

                    elif response == '!удалить' and q[item]['cod'] == 'admin' and len(
                            deleted_items) == 0 and event.obj.peer_id == 106545709:

                        send_message(session_api, peer_id=106545709, tit=bot,
                                     message='Список пользователей под удаление пуст')
                        open_admin(session_api, status_bot, bot, code14, code31, diamonds150, gold_vip, duhs, item, in_chat,
                                   perk, number, dat)
                        q = load_obj('dict_users')
                        print('Admin' + '_' * 71 + '{:>.3f}'.format(time.monotonic() - start_mon))
                        break

                    elif response == '!стата' and admin == 1 and event.obj.peer_id == 106545709:

                        user_inf = session_api.users.get(user_ids=event.obj.from_id,
                                                         fields='sex')

                        first_name = (str(user_inf[0]['first_name']))
                        last_name = (str(user_inf[0]['last_name']))
                        last_and_first_name = str(first_name) + ' ' + str(last_name)

                        admin ='stata'
                        q[item]['cod'] = 'admin'
                        save_obj(obj=q, name='dict_users')

                        link = '@id{0} ({1})'.format(item, last_and_first_name)
                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='{0}(Пользователь) c ID: {1}'
                                             '\n| perk: {2} | rep: {3} | rep_points {4} | diamonds: {5} | voices: {6} | cod: {7} | in chat: {8} | id_convers: {9} | id_talker: {10}'.format(link, item,q[item]['perk'], q[item]['rep'], q[item]['rep_points'],  q[item]['diamonds'], q[item]['voices'], q[item]['cod'], q[item]['in_chat'], q[item]['id_convers'], q[item]['id_talker']),keyboard=create_keyboard(response, item, in_chat, perk, number, var))
                        print('Admin' + '_' * 71 + '{:>.3f}'.format(time.monotonic() - start_mon))
                        break


                    elif response == '⬅' and (admin == 'stata' or admin == 'stata1') and event.obj.peer_id == 106545709:

                        if admin == 'stata':
                            iaq = 0
                        try:
                            if admin == 'stata1':
                                iaq -= 1
                                print('Кто духс' + str(duhs[iaq]))
                        except:
                             iaq = 0
                             print('Кто духс' + str(duhs[iaq]))

                        iaq_name = list(filter(lambda name: name['id'] == duhs[iaq], [name for name in
                                                                                         session_api.messages.getConversationMembers(
                                                                                             peer_id=duhs[iaq],
                                                                                             fields='profiles')[
                                                                                             'profiles']]))[0]

                        last_and_first_n = str(iaq_name['first_name']) + ' ' + str(iaq_name['last_name'])
                        link = '@id{0} ({1})'.format(duhs[iaq], last_and_first_n)
                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='{0}(Пользователь) c ID: {1}'
                                             '\n| perk: {2} | rep: {3} | rep_points {4} | diamonds: {5} | voices: {6} | cod: {7} | in chat: {8} | id_convers: {9} | id_talker: {10} #{11}'.format(
                                         link, duhs[iaq], q[duhs[iaq]]['perk'], q[duhs[iaq]]['rep'], q[duhs[iaq]]['rep_points'],
                                         q[duhs[iaq]]['diamonds'], q[duhs[iaq]]['voices'], q[duhs[iaq]]['cod'], q[duhs[iaq]]['in_chat'],
                                         q[duhs[iaq]]['id_convers'], q[duhs[iaq]]['id_talker'], iaq),
                                     keyboard=create_keyboard(response, duhs[iaq], in_chat, perk, number, var))
                        admin = 'stata1'
                        print('Admin' + '_' * 71 + '{:>.3f}'.format(time.monotonic() - start_mon))
                        break
                    elif response == '➡' and (admin == 'stata' or admin == 'stata1') and event.obj.peer_id == 106545709:

                        if admin == 'stata':
                            iaq = 1
                        try:
                          if admin == 'stata1':
                                    iaq += 1
                                    print('Кто духс' + str(duhs[iaq]))
                        except:
                            iaq = 0
                            print('Кто духс' + str(duhs[iaq]))

                        iaq_name = list(filter(lambda name: name['id'] == duhs[iaq], [name for name in
                                                                                      session_api.messages.getConversationMembers(
                                                                                          peer_id=duhs[iaq],
                                                                                          fields='profiles')[
                                                                                          'profiles']]))[0]

                        last_and_first_n = str(iaq_name['first_name']) + ' ' + str(iaq_name['last_name'])
                        link = '@id{0} ({1})'.format(duhs[iaq], last_and_first_n)
                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='{0}(Пользователь) c ID: {1}'
                                             '\n| perk: {2} | rep: {3} | rep_points: {4} | diamonds: {5} | voices: {6} | cod: {7} | in chat: {8} | id_convers: {9} | id_talker: {10} #{11}'.format(
                                         link, duhs[iaq], q[duhs[iaq]]['perk'], q[duhs[iaq]]['rep'],
                                         q[duhs[iaq]]['rep_points'],
                                         q[duhs[iaq]]['diamonds'], q[duhs[iaq]]['voices'], q[duhs[iaq]]['cod'],
                                         q[duhs[iaq]]['in_chat'],
                                         q[duhs[iaq]]['id_convers'], q[duhs[iaq]]['id_talker'], iaq),
                                     keyboard=create_keyboard(response, duhs[iaq], in_chat, perk, number, var))
                        admin = 'stata1'
                        print('Admin' + '_' * 71 + '{:>.3f}'.format(time.monotonic() - start_mon))
                        break

                    elif response == '!найти' and q[item]['cod'] == 'admin' and event.obj.peer_id == 106545709:
                        admin ='stata2'
                        #print(admin)
                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='Введите ID')
                        print('Admin' + '_' * 71 + '{:>.3f}'.format(time.monotonic() - start_mon))
                        break

                    elif admin =='stata2' and q[item]['cod'] == 'admin'and event.obj.peer_id == 106545709:

                        save_obj(obj=q, name='dict_users')
                        try:
                            if int(response) in duhs:

                                iaq_name = list(filter(lambda name: name['id'] == int(response), [name for name in
                                                                                              session_api.messages.getConversationMembers(
                                                                                                  peer_id=int(response),
                                                                                                  fields='profiles')[
                                                                                                  'profiles']]))[0]

                                last_and_first_n = str(iaq_name['first_name']) + ' ' + str(iaq_name['last_name'])
                                link = '@id{0} ({1})'.format(int(response), last_and_first_n)
                                item = int(response)
                                send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                             message='{0}(Пользователь) c ID: {1}'
                                                     '\n| perk: {2} | rep: {3} | rep_points: {4} | diamonds: {5} | voices: {6} | cod: {7} | in chat: {8} | id_convers: {9} | id_talker: {10}'.format(
                                                 link, str(item), q[item]['perk'], q[item]['rep'], q[item]['rep_points'],
                                                 q[item]['diamonds'], q[item]['voices'], q[item]['cod'], q[item]['in_chat'],
                                                 q[item]['id_convers'], q[item]['id_talker']),
                                             keyboard=create_keyboard(response, item, in_chat, perk, number, admin))
                            else:

                                send_message(session_api, peer_id=106545709, tit=bot,
                                             message='Нет в DUHS',
                                             keyboard=create_keyboard('!стата', item, in_chat, perk, number, admin))
                        except:

                            send_message(session_api, peer_id=106545709, tit=bot,
                                         message='Вы ввели неверный ID',keyboard=create_keyboard('!стата', item, in_chat, perk, number, admin))
                        admin = 'stata'
                        print('Admin' + '_' * 71 + '{:>.3f}'.format(time.monotonic() - start_mon))
                        break

                    elif response == '!алмазы+' and admin == 1 and event.obj.peer_id == 106545709:

                        admin = 'lot'#переменная переключатель
                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='Введите количество 💎')
                        print('Admin' + '_' * 71 + '{:>.3f}'.format(time.monotonic() - start_mon))
                        break

                    elif response == '!реп+' and admin == 1 and event.obj.peer_id == 106545709:

                        admin = 'rep+'#переменная переключатель
                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='Введите ID', keyboard=create_keyboard(response, item, in_chat, perk, number, 'id'))
                        print('Admin' + '_' * 71 + '{:>.3f}'.format(time.monotonic() - start_mon))
                        break

                    elif response == '!реп-' and admin == 1 and event.obj.peer_id == 106545709:

                        admin = 'rep-'#переменная переключатель
                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='Введите ID', keyboard=create_keyboard(response, item, in_chat, perk, number, 'id'))
                        print('Admin' + '_' * 71 + '{:>.3f}'.format(time.monotonic() - start_mon))
                        break

                    elif (admin == 'rep-' or admin == 'rep+') and event.obj.peer_id == 106545709:


                        try:
                            iaq_name = list(filter(lambda name: name['id'] == int(response), [name for name in
                                                                                              session_api.messages.getConversationMembers(
                                                                                                  peer_id=int(response),
                                                                                                  fields='profiles')[
                                                                                                  'profiles']]))[0]

                            last_and_first_n = str(iaq_name['first_name']) + ' ' + str(iaq_name['last_name'])
                            id_user = int(response)



                            link = '@id{0} ({1})'.format(id_user, last_and_first_n)
                            send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                         message='{2}(Пользователь) c ID: {3}\nРепутация: {0}{1}\nВведите количество очков'.format(rt (id_talker=id_user),q[id_user]['rep_points'],link, str(id_user)))

                            if admin == 'rep-':
                                admin = 'col-'

                            if admin == 'rep+':
                                admin = 'col+'
                        except:
                            send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                         message='Вы ввели неверный ID',
                                         keyboard=create_keyboard('!админ', item, in_chat, perk, number, var))
                            admin = 1


                        #print(admin)
                        print('Admin' + '_' * 71 + '{:>.3f}'.format(time.monotonic() - start_mon))
                        break

                    elif (admin == 'col-' or admin =='col+') and event.obj.peer_id == 106545709:#19

                        col = int(response)
                        try:
                            if admin == 'col-':
                                q[id_user]['rep_points'] -=col
                                save_obj(obj=q, name='dict_users')

                            elif admin == 'col+':
                                q[id_user]['rep_points'] += col
                                save_obj(obj=q, name='dict_users')
                        except:
                            send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                         message='Ошибка ввода!',
                                         keyboard=create_keyboard('!админ', item, in_chat, perk, number, var))
                            admin = 1
                        link = '@id{0}'.format(id_user)
                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='{2}(Пользователь) c ID: {3}\nРепутация: {0} Кол. очков репутации: {1}'.format(
                                         rt(id_talker=id_user), q[id_user]['rep_points'],link, str(id_user)),keyboard=create_keyboard('!админ', item, in_chat, perk, number, var))

                        admin = 1
                        print('Admin' + '_' * 71 + '{:>.3f}'.format(time.monotonic() - start_mon))
                        break

                    elif response == '!алмазы-' and admin == 1 and event.obj.peer_id == 106545709:

                        admin = 'id-'  # переменная переключатель

                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                         message='Введите ID пользователя чтобы обнулить 💎', keyboard=create_keyboard(response, item, in_chat, perk, number, 'id'))
                        print('Admin' + '_' * 71 + '{:>.3f}'.format(time.monotonic() - start_mon))
                        break

                    elif admin == 'lot' and event.obj.peer_id == 106545709:

                        try:
                            lot = int(response)
                            admin = 'id+'#переменная переключатель

                            send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                         message='Теперь введите ID пользователя, для добавления 💎', keyboard=create_keyboard(response, item, in_chat, perk, number, 'id'))
                        except:
                            send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                         message='Неверный формат, укажите количество 💎 одной цифрой')
                        print('Admin' + '_' * 71 + '{:>.3f}'.format(time.monotonic() - start_mon))
                        break

                    elif (admin == 'id+' or admin == 'id-') and event.obj.peer_id == 106545709:

                        q[item]['cod'] = 0
                        save_obj(obj=q, name='dict_users')

                        if admin == 'id+':
                            admin = 1
                            try:
                                if int(response) in duhs:
                                    id_user = int(response)
                                    iaq_name = list(filter(lambda name: name['id'] == id_user, [name for name in
                                                                                                      session_api.messages.getConversationMembers(
                                                                                                          peer_id=id_user,
                                                                                                          fields='profiles')[
                                                                                                          'profiles']]))[0]

                                    last_and_first_n = str(iaq_name['first_name']) + ' ' + str(iaq_name['last_name'])


                                    link = '@id{0} ({1})'.format(int(response), last_and_first_n)
                                    q[int(response)]['diamonds'] += lot
                                    diamonds = q[int(response)]['diamonds']
                                    save_obj(obj=q, name='dict_users')
                                    send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                                 message='{0}(Пользователь) : {1} получил  +{2}💎\n'.format(link,str(response),str(lot)))
                                    send_message(session_api, peer_id=int(response), tit=bot,
                                                 message='+{}💎'.format(str(lot)))
                                elif int(response) not in duhs:
                                    send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                                 message='Такого ID нет в общем списке')
                            except:
                                send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                             message='Вы ввели неверный ID')
                        elif admin == 'id-':
                            otvet = 1
                            admin = 1
                            try:
                                if int(response) in duhs:
                                    id_user = int(response)
                                    iaq_name = list(filter(lambda name: name['id'] == id_user, [name for name in
                                                                                                session_api.messages.getConversationMembers(
                                                                                                    peer_id=id_user,
                                                                                                    fields='profiles')[
                                                                                                    'profiles']]))[0]

                                    last_and_first_n = str(iaq_name['first_name']) + ' ' + str(iaq_name['last_name'])

                                    link = '@id{0} ({1})'.format(int(response), last_and_first_n)

                                    diam = q[int(response)]['diamonds']
                                    q[int(response)]['diamonds'] = 0
                                    diamonds = q[int(response)]['diamonds']
                                    save_obj(obj=q, name='dict_users')
                                    send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                                 message='Баланс {0}(Пользователя): {1} = {2}💎\n'.format(link, str(
                                                     response), str(q[int(response)]['diamonds'])))
                                    if diam > 0:
                                        send_message(session_api, peer_id=int(response), tit=bot,
                                                     message='-{}💎'.format(diam))
                                elif int(response) not in duhs:
                                    send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                                 message='Такого ID нет в общем списке')
                            except:
                                send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                             message='Вы ввели неверный ID')

                        print('Admin' + '_' * 71 + '{:>.3f}'.format(time.monotonic() - start_mon))
                        break


                    elif response == '!вип+'  and admin == 1 and event.obj.peer_id == 106545709:

                        admin = 2
                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='Введите количество дней цифрой')
                        print('Admin' + '_' * 71 + '{:>.3f}'.format(time.monotonic() - start_mon))
                        break

                    elif admin == 2 and event.obj.peer_id == 106545709:

                        try:
                            days = (((int(response) * 24) * 60) * 60)
                            admin = 3
                            print (days)
                            send_message(session_api, peer_id=event.obj.peer_id, tit=bot, message='Теперь введите ID пользователя, для добавления ВИП статуса',keyboard=create_keyboard(response, item, in_chat, perk, number, 'id'))
                        except:
                            send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                         message='Неверный формат, укажите количество дней одной цифрой')
                        print('Admin' + '_' * 71 + '{:>.3f}'.format(time.monotonic() - start_mon))
                        break

                    elif admin == 3 and event.obj.peer_id == 106545709:


                       admin = 1
                       q[item]['cod'] = 0
                       save_obj(obj=q, name='dict_users')
                       try:

                        if int(response) in q:

                            id_user = int(response)
                            iaq_name = list(filter(lambda name: name['id'] == id_user, [name for name in
                                                                                        session_api.messages.getConversationMembers(
                                                                                            peer_id=id_user,
                                                                                            fields='profiles')[
                                                                                            'profiles']]))[0]

                            last_and_first_n = str(iaq_name['first_name']) + ' ' + str(iaq_name['last_name'])

                            link = '@id{0} ({1})'.format(id_user, last_and_first_n)

                            q[int(response)]['perk'] = 1

                            if q[int(response)]['perk_time'] == 0:
                               q[int(response)]['perk_time'] = time.time()
                               q[int(response)]['perk_date'] = time.time() + days

                            else:
                              #print('продливаем вип статус пользователю: ' + response)
                              q[int(response)]['perk_date'] += days


                            date_perk = datetime.fromtimestamp(q[int(response)]['perk_date']).strftime("%d.%m.%y %H:%M")
                            #print(date_perk)
                            save_obj(obj=q, name='dict_users')
                            send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                         message='{0}(Пользователь) c ID: {1} получил  ВИП 👑 статус до {2}'.format(link,str(response), str(date_perk)))
                            send_message(session_api, peer_id=int(response), tit=bot,
                                         message='🎊{0}, вам активировали ВИП 👑 статус до {1}🎊'.format(iaq_name['first_name'],str(date_perk)))
                        elif int(response) not in q:
                            send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                         message='Такого ID нет в общем списке')
                       except:
                           send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                        message='Вы ввели неверный ID')
                       print('Admin' + '_' * 71 + '{:>.3f}'.format(time.monotonic() - start_mon))
                       break

                    elif response == 'репа':

                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='Репутация собеседника: {} {} '.format(rt(id_talker=id_talker),id_talker))
                        print('Admin' + '_' * 71 + '{:>.3f}'.format(time.monotonic() - start_mon))
                        break


                    elif response == '!вип-' and admin == 1 and event.obj.peer_id == 106545709:

                        admin = 4

                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='Введите ID пользователя, для  снятия ВИП статуса',keyboard=create_keyboard(response, item, in_chat, perk, number, 'id'))
                        print('Admin' + '_' * 71 + '{:>.3f}'.format(time.monotonic() - start_mon))
                        break

                    elif admin == 4 and event.obj.peer_id == 106545709:

                        admin = 1
                        q[item]['cod'] = 0
                        save_obj(obj=q, name='dict_users')
                        try:
                         if int(response) in q:

                            id_user = int(response)
                            iaq_name = list(filter(lambda name: name['id'] == id_user, [name for name in
                                                                                        session_api.messages.getConversationMembers(
                                                                                            peer_id=id_user,
                                                                                            fields='profiles')[
                                                                                            'profiles']]))[0]

                            last_and_first_n = str(iaq_name['first_name']) + ' ' + str(iaq_name['last_name'])

                            link = '@id{0} ({1})'.format(id_user, last_and_first_n)

                            send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                         message='{0}(Пользователь) c ID: {1} утратил ВИП статус'.format(link,
                                                                                                         str(response)))

                            if q[id_user]['perk'] == 1:
                                send_message(session_api, peer_id=id_user, tit=bot,
                                             message='{0}, вы утратили 😐 ВИП статус 👑'.format(str(iaq_name['first_name'])))
                                if id_user in newsletter:
                                    newsletter.remove(id_user)
                                    save_obj(obj=newsletter, name='newsletter')

                            q[int(response)]['perk'] = 0
                            q[int(response)]['perk_time'] = 0
                            # 2 сняли вип вручную
                            q[int(response)]['perk_date'] = 2
                            q[int(response)]['voices'] = 0
                            save_obj(obj=q, name='dict_users')

                         elif int(response) not in q:
                            send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                         message='Такого ID нет в общем списке')
                        except:
                            send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                         message='Вы ввели неверный ID')
                        print('Admin' + '_' * 71 + '{:>.3f}'.format(time.monotonic() - start_mon))
                        break

                # НЕ ПЕРЕСЫЛАЕТ СООБЩЕНИЯ
                if fwd !=[]:

                    print('Пользователь пытается переслать сообщение ')# + str(fwd))
                    send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                 message='Я не могу переслать твое сообщение, иначе оно не будет анонимным 🕵‍♀')
                    print('_' * 80)
                    fwd = []
                    break


                #print("Успешно")



                # нет реакций если пользователь в поиске
                if response != 'стоп' and item in all_list and in_chat == 0 and response not in list_admin and (q[item]['cod'] != 'admin' or (q[item]['cod'] == 'admin' and (response == 'меню' or otvet == 0))):

                    otvet = 1
                    q[item]['cod'] = 0
                    save_obj(obj=q, name='dict_users')

                    send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                 message='Жди, мы еще ищем тебе собеседника 🔎\nНапиши: Стоп чтобы остановить поиск ⛔')
                    print('Пользователь пытается запросить повторный поиск находясь в поиске' + str(que))
                elif response == 'сообщить об ошибке' and q[item]['in_chat'] == 0:
                    otvet = 1
                    q[item]['cod'] = 'err'
                    save_obj(obj=q, name='dict_users')
                    send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                 message='Опишите вашу проблему одним сообщением и прикрепите скриншот ошибки')

                elif q[item]['cod'] == 'err':
                    otvet = 1
                    q[item]['cod'] = 0
                    save_obj(obj=q, name='dict_users')

                    user_inf, first_name, last_name, last_and_first_name = user_information (session_api, event)

                    link = '@id{0} ({1})'.format(item, last_and_first_name)
                    send_message(session_api, peer_id=106545709, tit=bot,
                                 message='Сообщение от: {0} \n {1}'.format(link, response), sticker_id=sticker_id, q1=q1)

                    logging.error("{0} {1} сообщил об ошибке: {2}".format(today,link,response))
                    send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                 message='Сообщение отправлено!')
                elif in_chat == 0 and response == 'начать':

                      otvet = 1
                      if hi == 0:
                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='Привет! Это анонимный чат "КТО Я" 👻')

                      #t_open_m = threading.Thread(target=open_menu, name='thread_open_m',
                      #                              args=(session_api, response, item, bot, var))
                      #t_open_m.start()
                      #print('Cтартанул поток {}'.format(t_open_m.name))
                      open_menu(session_api, 'меню', item, bot, var)


                elif in_chat == 0  and response == '👍🏻' or response == '👎🏻':
                        otvet = 1

                        g_rep, p_rep = random_bonus(q, threading, bot, session_api, rep, item, event)
                        #print(g_rep)
                        if id_talker != 0:
                            try:
                                found = q[item]['id_talker']

                                if response == '👍🏻':
                                    q[found]['rep_points'] += g_rep
                                    q[item]['rep_points'] += 3

                                elif response == '👎🏻':
                                    q[found]['rep_points'] -= p_rep
                                    q[item]['rep_points'] += 3

                                save_obj(obj=q, name='dict_users')

                            except:
                                print('Не удалось поставить оценку пользователю!')

                        open_menu(session_api, 'меню', item, bot, var)
                        q[item]['id_talker'] = 0
                        save_obj(obj=q, name='dict_users')

                elif (response == 'вип' or response == 'вип 👑') and in_chat != 3:
                    otvet = 1
                    if perk > 0:
                        date_perk = datetime.fromtimestamp(q[item]['perk_date']).strftime("%d.%m.%y %H:%M")
                        start_perk = datetime.fromtimestamp(q[item]['perk_time']).strftime("%d.%m.%y %H:%M")
                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='Дата активации VIP 👑 ✅{0}\n У вас действует VIP 👑 до ➡{1}\n\nКупить VIP на 2 недели 👉🏻 https://vk.cc/9k4puf\nКупить VIP на месяц 👉🏻 https://vk.cc/9wZSKH'
                                             '\nКупить 150💎 👉🏻 https://vk.cc/9zEfRw'
                                             '\nКупить 🔥GOLD VIP🔥 👉🏻 https://vk.cc/9EJR2L\n\n!код - ввести код для получения 💎 или VIP 👑' .format(start_perk,date_perk), keyboard=create_keyboard(response, item, in_chat, perk, number, var))
                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='', sticker_id='9109')
                    if perk == 0:

                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='С VIP 👑 статусом вам будут доступны:'
                                             '\n\n1⃣ Обмен фото без ограничений'
                                             '\n2⃣ Поиск по полу без ограничений'
                                             '\n3⃣ Беседы'
                                             '\n4⃣ Буст очков репутации'
                                             '\n5⃣ Дополнительные функции чата'
                                             '\n\nКупить VIP на 2 недели 👉🏻 https://vk.cc/9k4puf'#Вы можете приобрести цифровой код VIP статуса на 2 недели по этой ссылке👉🏻 https://vk.cc/9k4puf
                                             '\nКупить VIP на месяц 👉🏻 https://vk.cc/9wZSKH'#https://vk.cc/9eZTEU'
                                             '\nКупить 150💎 👉🏻 https://vk.cc/9zEfRw'
                                             '\nКупить 🔥GOLD VIP🔥 👉🏻 https://vk.cc/9EJR2L'
                                             '\n\nУже есть цифровой код VIP статуса? \n▶Пиши: !код',keyboard=create_keyboard(response, item, in_chat, perk, number, var))


                elif response == '!код' and in_chat != 3:
                    print(datetime.now())
                    otvet = 1
                    q[item]['cod'] = item #переменная переключатель
                    save_obj(obj=q, name='dict_users')
                    send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                 message='Введите код, для получения VIP👑 или 💎')

                elif cod == event.obj.peer_id:
                    otvet = 1
                    q[item]['cod'] = 0 #переменная переключатель
                    keyboard = VkKeyboard(one_time=True)
                    save_obj(obj=q, name='dict_users')
                    keyboard.add_button("Меню", color=VkKeyboardColor.DEFAULT, payload='')
                    if in_chat == 0:
                        keyboard = keyboard.get_keyboard()
                    else:
                        keyboard=keyboard.get_empty_keyboard()

                    try:
                        if event.obj.text in code14 and perk ==0:
                          code14.remove(event.obj.text)
                          with open("obj\\code14.txt", "w") as file: #перезаписывает файл code14 без введенного кода
                              file.writelines("%s\n" % line for line in code14)
                          q[item]['perk'] = 1
                          q[item]['perk_time'] = time.time()
                          q[item]['perk_date'] = time.time() + 1209600
                          save_obj(obj=q, name='dict_users')

                          date_perk = datetime.fromtimestamp(q[item]['perk_date']).strftime("%d.%m.%y %H:%M")
                          send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='Поздравляем!🎉 Вы успешно ✅ активировали VIP👑 подписку на 2 недели\nВаша подписка действительна до ➡{0}'.format(date_perk),keyboard=keyboard)

                        elif event.obj.text in code14 and perk > 0:

                            code14.remove(event.obj.text)
                            with open("obj\\code14.txt", "w") as file: #перезаписывает файл code14 без введенного кода
                                file.writelines("%s\n" % line for line in code14)
                            q[item]['perk'] = 1
                            q[item]['perk_date'] += 1209600
                            save_obj(obj=q, name='dict_users')

                            date_perk = datetime.fromtimestamp(q[item]['perk_date']).strftime("%d.%m.%y %H:%M")
                            send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='Поздравляем!🎉 Вы успешно ✅ продлили VIP👑 подписку на 2 недели, спасибо что остаетесь с нами🤗\nВаша подписка действительна до ➡{0}'.format(date_perk),keyboard=keyboard)

                        elif event.obj.text in code31 and perk ==0:

                            code31.remove(event.obj.text)
                            with open("obj\\code31.txt", "w") as file:  # перезаписывает файл code31 без введенного кода
                                file.writelines("%s\n" % line for line in code31)
                            q[item]['perk'] = 1
                            q[item]['perk_time'] = time.time()
                            q[item]['perk_date'] = time.time() + 2678400
                            save_obj(obj=q, name='dict_users')

                            date_perk = datetime.fromtimestamp(q[item]['perk_date']).strftime("%d.%m.%y %H:%M")
                            send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                         message='Поздравляем!🎉 Вы успешно ✅ активировали VIP👑 подписку на месяц\nВаша подписка действительна до ➡{0}'.format(
                                             date_perk),keyboard=keyboard)
                        elif event.obj.text in code31 and perk > 0:

                            code31.remove(event.obj.text)
                            with open("obj\\code31.txt", "w") as file:  # перезаписывает файл code31 без введенного кода
                                file.writelines("%s\n" % line for line in code31)
                            q[item]['perk'] = 1
                            q[item]['diamonds'] += 150
                            q[item]['perk_date'] += 2678400
                            save_obj(obj=q, name='dict_users')

                            date_perk = datetime.fromtimestamp(q[item]['perk_date']).strftime("%d.%m.%y %H:%M")
                            send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                         message='+150💎')
                            send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                         message='Поздравляем!🎉 Вы успешно ✅ продлили VIP👑 подписку на месяц, спасибо что остаетесь с нами🤗\nВаша подписка действительна до ➡{0}'.format(
                                             date_perk),keyboard=keyboard)

                        elif event.obj.text in diamonds150:

                            diamonds150.remove(event.obj.text)
                            with open("obj\\diamonds150.txt", "w") as file:  # перезаписывает файл diamonds150 без введенного кода
                                file.writelines("%s\n" % line for line in diamonds150)

                            q[item]['diamonds'] += 150

                            save_obj(obj=q, name='dict_users')

                            send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                         message='+150💎')
                            send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                         message='Спасибо за покупку!',keyboard=keyboard)

                        elif event.obj.text in gold_vip and perk == 0:

                            gold_vip.remove(event.obj.text)
                            with open("obj\\gold_vip.txt", "w") as file:  # перезаписывает файл code31 без введенного кода
                                file.writelines("%s\n" % line for line in gold_vip)
                            q[item]['perk'] = 1
                            q[item]['perk_time'] = time.time()
                            q[item]['perk_date'] = time.time() + 8035200
                            q[item]['diamonds'] += 1500
                            save_obj(obj=q, name='dict_users')

                            date_perk = datetime.fromtimestamp(q[item]['perk_date']).strftime("%d.%m.%y %H:%M")
                            send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                         message='+1500💎')
                            send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                         message='Поздравляем!🎉 Вы успешно ✅ активировали VIP👑 подписку на 3 месяца\nВаша подписка действительна до ➡{0}'.format(
                                             date_perk), keyboard=keyboard)
                        elif event.obj.text in gold_vip and perk > 0:

                            gold_vip.remove(event.obj.text)
                            with open("obj\\gold_vip.txt", "w") as file:  # перезаписывает файл code31 без введенного кода
                                file.writelines("%s\n" % line for line in gold_vip)
                            q[item]['perk'] = 1
                            q[item]['perk_date'] += 8035200
                            q[item]['diamonds'] += 1500
                            save_obj(obj=q, name='dict_users')

                            date_perk = datetime.fromtimestamp(q[item]['perk_date']).strftime("%d.%m.%y %H:%M")
                            send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                         message='+1500💎')
                            send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                         message='Поздравляем!🎉 Вы успешно ✅ продлили VIP👑 подписку на 3 месяца, спасибо что остаетесь с нами🤗\nВаша подписка действительна до ➡{0}'.format(
                                             date_perk), keyboard=keyboard)


                        else:
                            send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                         message='Данный код невалиден!')
                    except:
                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                   message='Ошибка при вводе кода!')
                #КОГДА ПОЛЬЗОВАТЕЛЬ ЗАВЕРШИЛ ЧАТ И ID_TALKER НЕ ПУСТОЙ ТО ОН МОЖЕТ ПОСТАВИТЬ ЕМУ ОЦЕНКУ


                elif (response == 'меню' or response == 'назад') and q[item]['in_chat'] == 1:

                    otvet = 1
                    q[item]['cod'] = 0
                    save_obj(obj=q, name='dict_users')
                    c_treat, p_city, p_age, p_photo, p_link = calc_y(item, 'chat')
                    if q[item]['voices'] == str(voices):
                        what_voices = '\nОзвучивает сообщения: {}'.format(what_v(voices))
                    else:
                        what_voices = ''

                    if q[item]['perk'] >0:
                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message= 'Репутация: {0} Баланс: 💎{1}\n\nCity 🌆 - узнать город собеседника {2}\nAge 👶🏻 - узнать возраст собеседника {3}' 
                                              '\nPhoto 📸 - получить фото собеседника {4}'
                                              '\nLink 📎 - получить ссылку на профиль собеседника {5}\n{6}\n\nВыбрать голос -  озвучивание 🔊 сообщений ✉\n\nУгостить 🍬 {7}'.format(rt(item),q[item]['diamonds'],p_city, p_age, p_photo, p_link, what_voices,c_treat), keyboard=create_keyboard(response, item, in_chat, perk, number, var))
                    else:
                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='Репутация: {0} Баланс: 💎{1}\n\nCity 🌆 - узнать город собеседника 🚫\nAge 👶🏻 - узнать возраст собеседника 🚫'
                                             '\nPhoto 📸 - получить фото собеседника 🚫'
                                             '\nLink 📎 - получить ссылку на профиль собеседника 🚫\n\nВыбрать голос -  озвучивание 🔊 сообщений 🚫\n\nУгостить 🍬 {2}'.format(rt(item),q[item]['diamonds'],c_treat), keyboard=create_keyboard(response, item, in_chat, perk, number, var))
                    if response == 'назад':
                        close_voices(item)


                elif (response == 'выбрать голос 🗣' or response == 'выбрать голос' or response == "выбрать другой") and in_chat ==1 and perk > 0:
                    otvet = 1

                    q[item]['cod'] = 'voices'
                    save_obj(obj=q, name='dict_users')

                    if q[item]['voices'] == str(voices):
                        what_voices = '\nВыбран голос: {}\n\n'.format(what_v(voices))
                    else:
                        what_voices = ''
                    send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                 message='{0}Выберите голос 🗣 для озвучивания вашего текста.'
                                         '\n⚠Внимание⚠ После выбора голоса, собеседнику будут отправляться ТОЛЬКО голосовые сообщения!'.format(what_voices), keyboard=create_keyboard(response, item, in_chat, perk, number, var=q[item]['voices']))

                elif (response == 'выбрать голос 🗣' or response == 'выбрать голос' or response == "выбрать другой") and in_chat == 1 and perk == 0:
                    send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                 message='Доступ к этой функции есть только у VIP 👑'
                                         '\nВип - узнать подробности')



                elif response in list_voices and in_chat == 1 and perk > 0 and q[item]['cod'] == 'voices':
                    otvet=1
                    q[item]['cod'] = 0
                    if response == 'nrx' :
                        q[item]['voices'] = 'smoky'
                        try:
                            send_message(session_api, peer_id=item, tit=bot,
                                             message='Вы выбрали голос "NRX"',
                                             q1=voice(session_api, event, 'Саап я N R X', 'smoky'),keyboard=create_keyboard(response, item, in_chat, perk, number, var='voices'))
                        except:
                            print('ОШИБКА: Не удается озвучить сообщение ')
                            send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                             message='Озвучить сообщение не удалось 😒')

                    elif response =='борис':
                        q[item]['voices'] = 'levitan'
                        try:
                            send_message(session_api, peer_id=item, tit=bot,
                                             message='Вы выбрали голос "Борис"',
                                             q1=voice(session_api, event, 'И снова здравствуйте!', 'levitan'),keyboard=create_keyboard(response, item, in_chat, perk, number, var='voices'))
                        except:
                            print('ОШИБКА: Не удается озвучить сообщение ')
                            send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                             message='Озвучить сообщение не удалось 😒')
                    elif response == 'оксана':
                        q[item]['voices'] ='oksana'
                        try:
                            send_message(session_api, peer_id=item, tit=bot,
                                             message='Вы выбрали голос "Оксана"',
                                             q1=voice(session_api, event, 'Хочешь меня?', 'oksana'),keyboard=create_keyboard(response, item, in_chat, perk, number, var='voices'))
                        except:
                            print('ОШИБКА: Не удается озвучить сообщение ')
                            send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                             message='Озвучить сообщение не удалось 😒')
                    elif response == 'джейн':
                        q[item]['voices'] = 'jane'
                        try:
                            send_message(session_api, peer_id=item, tit=bot,
                                         message='Вы выбрали голос "Джейн"',
                                         q1=voice(session_api, event, 'Привет, я Джейн', 'jane'),keyboard=create_keyboard('другой', item, in_chat, perk, number, var='voices'))
                        except:
                            print('ОШИБКА: Не удается озвучить сообщение ')
                            send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                         message='Озвучить сообщение не удалось 😒')
                    elif response == 'колян':
                        q[item]['voices'] = 'kolya'
                        try:
                            send_message(session_api, peer_id=item, tit=bot,
                                         message='Вы выбрали голос "Колян"',
                                         q1=voice(session_api, event, 'Чиии, даааа???', 'kolya'),keyboard=create_keyboard(response, item, in_chat, perk, number, var='voices'))
                        except:
                            print('ОШИБКА: Не удается озвучить сообщение ')
                            send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                         message='Озвучить сообщение не удалось 😒')
                    elif response == 'артем':
                        q[item]['voices'] = 'dude'
                        try:
                            send_message(session_api, peer_id=item, tit=bot,
                                         message='Вы выбрали голос "Артем"',
                                         q1=voice(session_api, event, 'Займи косарь?', 'dude'),keyboard=create_keyboard(response, item, in_chat, perk, number, var='voices'))
                        except:
                            print('ОШИБКА: Не удается озвучить сообщение ')
                            send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                         message='Озвучить сообщение не удалось 😒')
                    elif response == 'таня':
                        q[item]['voices'] = 'tanya'
                        try:
                            send_message(session_api, peer_id=item, tit=bot,
                                         message='Вы выбрали голос "Таня"',
                                         q1=voice(session_api, event, 'Давай с тобой устроим бой!', 'tanya'),keyboard=create_keyboard(response, item, in_chat, perk, number, var='voices'))
                        except:
                            print('ОШИБКА: Не удается озвучить сообщение ')
                            send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                         message='Озвучить сообщение не удалось 😒')
                    elif response == 'элис':
                        q[item]['voices'] = 'tatyana_abramova'
                        try:
                            send_message(session_api, peer_id=item, tit=bot,
                                         message='Вы выбрали голос "Элис"',
                                         q1=voice(session_api, event, 'До меня дошел стишок, съешь дружочек пирожок!', 'tatyana_abramova'),keyboard=create_keyboard(response, item, in_chat, perk, number, var='voices'))
                        except:
                            print('ОШИБКА: Не удается озвучить сообщение ')
                            send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                         message='Озвучить сообщение не удалось 😒')

                    voices = q[item]['voices']
                    save_obj(obj=q, name='dict_users')


                elif response == 'убрать голос' and q[item]['voices'] == str(voices):
                    otvet = 1
                    q[item]['voices'] = 0
                    send_message(session_api, peer_id=item, tit=bot, message='Вы отключили озвучивание 🔇 сообщений ✉')
                    voices = q[item]['voices']
                    save_obj(obj=q, name='dict_users')

                elif response == 'назад' and in_chat == 1:
                    close_voices(item)

                elif (response == 'угостить 🍬' or response == 'угостить') and q[item]['diamonds'] >=1 and in_chat == 1:
                    q[item]['cod'] = 'treat'

                    save_obj(obj=q, name='dict_users')

                    send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                 message='🍺🍸🍹🥃 - для 👍🏻 собеседника, 🍼💩 - для 👎🏻 собеседника.',
                                 keyboard=create_keyboard(response, item, in_chat, perk, number, var))

                elif (response == 'угостить 🍬' or response == 'угостить') and q[item]['diamonds'] < 1 and in_chat == 1:
                    send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                 message='Не хватает 1💎 для выполнения этой команды ☹')




                elif response == '"ктоя?"' or response == '"ктоя"'  or response == 'ктоя' or response == 'котя?' or response == '"котя"' or response == '"котя?"' or response == 'котя':
                    otvet = 1
                    send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                 message='Некорректно введен промокод!', keyboard = create_keyboard(response, item, in_chat, perk, number, 'er'))
                    response = ''


                #если не действует вип или вип был снят автоматически
                elif response =='ктоя?' and q[item]['perk_date'] !=1 and q[item]['perk'] ==0 and in_chat !=3:
                    otvet = 1


                    q[item]['perk'] = 1
                    q[item]['perk_time'] = time.time()
                    q[item]['perk_date'] = time.time() + 259200
                    q[item]['diamonds'] +=30
                    q[item]['cod'] = 'bonus'
                    save_obj(obj=q, name='dict_users')
                    date_perk = datetime.fromtimestamp(q[item]['perk_date']).strftime("%d.%m.%y %H:%M")
                    send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                 message='+30💎')
                    send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                message='🥳 Поздравляем!🎉\n Вы ✅ активировали бонусную VIP👑 подписку на 3 дня\nВаша подписка действительна до ➡{0}\nХочешь получить еще 50💎?😑'.format(date_perk), keyboard=create_keyboard(response, item, in_chat, perk, number, var))

                elif response == 'да' and q[item]['cod'] == 'bonus':
                    otvet = 1
                    q[item]['cod'] = 0
                    save_obj(obj=q, name='dict_users')
                    send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                 message='Сделай репост вот этой 👉🏻 https://vk.cc/9HG790 записи у себя на стене и получи еще 50💎😑. Как все сделаешь не забудь отправить кодовое слово "аноним" (вводить без ковычек)\n\n P.S Твой профиль обязательно должен быть открыт чтобы я мог проверить результат👌')


                elif response == 'нет' and q[item]['cod'] == 'bonus':
                    otvet = 1
                    q[item]['cod'] = 0
                    save_obj(obj=q, name='dict_users')
                    if in_chat == 0:
                        open_menu(session_api, 'меню', item, bot, var)
                    response = ''
                elif response == "аноним":
                  #print(response)
                  likes_r = sessions.likes.getList(type='post', owner_id='-179410262', item_id='15',
                                                     page_url='https://vk.com/douknowwhoi?w=wall-179410262_15',
                                                     filter='copies', count='1000')
                  #print(likes_r)
                  if item in likes_r['items']:
                    otvet = 1
                    repost = []
                    if os.path.exists("obj\\repost.pkl"):

                        repost = load_obj('repost')
                        if item in repost:
                            send_message(session_api, peer_id=item, tit=bot,
                                         message='Вы уже получали 💎 за репост')
                            if in_chat == 0:
                                open_menu(session_api, 'меню', item, bot, var)

                        else:
                            repost.append(item)
                            save_obj(obj=repost, name='repost')
                            q[item]['diamonds'] += 50
                            save_obj(obj=q, name='dict_users')
                            send_message(session_api, peer_id=item, tit=bot,
                                         message='+50💎')
                            if in_chat == 0:
                                open_menu(session_api, 'меню', item, bot, var)
                  elif item not in likes_r['items']:
                        otvet = 1
                        send_message(session_api, peer_id=item, tit=bot,
                                     message='Вы  еще не сделали репост этой записи 👉🏻 https://vk.cc/9HG790')
                        if in_chat == 0:
                            open_menu(session_api, 'меню', item, bot, var)



                # если не действует вип или вип был снят автоматически
                elif response == 'ктоя?' and q[item]['perk_date'] == 1 and in_chat !=3:
                    otvet = 1
                    send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                 message='Промокод действителен только для новых пользователей')
                    if in_chat == 0:
                        open_menu(session_api, 'меню', item, bot, var)

                elif response == 'ктоя?' and q[item]['perk'] == 1 and in_chat !=3:
                    otvet = 1
                    send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                 message='Промокод действителен только для пользователей без VIP 👑')
                    if in_chat == 0:
                        open_menu(session_api, 'меню', item, bot, var)


                #отправляет город собеседника
                elif (response == 'city 🌆' or response == 'city') and q[item]['diamonds'] >= 2 and id_talker != 0 and in_chat == 1 and perk > 0:
                    otvet = 1
                    user_inform = sessions.users.get(user_id=id_talker,
                                                     fields='bdate, photo_id, verified, sex, bdate, city, country, home_town, has_photo, photo_50, photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, online, domain, has_mobile, contacts, site, education, universities, schools, status, last_seen, followers_count, common_count, occupation, nickname, relatives, relation, personal, connections, exports, activities, interests, music, movies, tv, books, games, about, quotes, can_post, can_see_all_posts, can_see_audio, can_write_private_message, can_send_friend_request, is_favorite, is_hidden_from_feed, timezone, screen_name, maiden_name, crop_photo, is_friend, friend_status, career, military, blacklisted, blacklisted_by_me')
                    #print(user_inform)
                    try:
                      send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                   message='Город собеседника: ' + str(user_inform[0]['city']['title']))
                      send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                 message='-2💎')
                      q[item]['diamonds'] -= 2
                      diamonds = q[item]['diamonds']
                      save_obj(obj=q, name='dict_users')
                    except:
                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='Город собеседника не указан ☹')
                elif (response == 'age 👶🏻' or response == 'age') and q[item]['diamonds'] >= 5 and id_talker != 0 and in_chat == 1 and perk > 0:
                    otvet = 1
                    user_inform = sessions.users.get(user_id=id_talker,
                                                     fields='bdate, photo_id, verified, sex, bdate, city, country, home_town, has_photo, photo_50, photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, online, domain, has_mobile, contacts, site, education, universities, schools, status, last_seen, followers_count, common_count, occupation, nickname, relatives, relation, personal, connections, exports, activities, interests, music, movies, tv, books, games, about, quotes, can_post, can_see_all_posts, can_see_audio, can_write_private_message, can_send_friend_request, is_favorite, is_hidden_from_feed, timezone, screen_name, maiden_name, crop_photo, is_friend, friend_status, career, military, blacklisted, blacklisted_by_me')




                    try:
                      date_of_birth = datetime.strptime(user_inform[0]['bdate'], "%d.%m.%Y")

                      age = calculate_age(date_of_birth)
                      send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                   message='Возраст собеседника: ' + str(age) + ' ' + str(yers(age))) #str(user_inform[0]['bdate']))
                      send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                 message='-5💎')
                      q[item]['diamonds'] -= 5
                      diamonds = q[item]['diamonds']
                      save_obj(obj=q, name='dict_users')
                    except:
                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='Год рождения собеседника не указан ☹')



                # отправляет фото собеседника!!!!!!!!!!!!!!!
                elif (response == 'photo 📸' or response == 'photo') and q[item]['diamonds'] >=10 and id_talker !=0 and in_chat == 1 and perk > 0:
                     otvet = 1
                     user_inform = sessions.users.get(user_id=id_talker,
                                                     fields='photo_max,photo_id')
                     #print(user_inform)
                     try:

                        #print('что в юзер секс' + str(user_inform))
                        photo_id ='photo' + str(user_inform[0]['photo_id'])

                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='Твой собеседник🗣', q1=photo_id)
                     except:
                          with open('1.jpg', 'wb') as out_stream:
                              req = requests.get(user_inform[0]['photo_max'], stream=True)
                              for chunk in req.iter_content(1024):
                                  out_stream.write(chunk)
                          a = session_api.photos.getMessagesUploadServer(peer_id=event.object.peer_id)
                          b = requests.post(a['upload_url'], files={'photo': open('1.jpg', 'rb')})
                          result = json.loads(b.text)
                          server = result['server']
                          hash = result ['hash']
                          photo = result['photo']
                          c = session_api.photos.saveMessagesPhoto(photo=photo, server=server, hash=hash)
                          owner_id = c[0]['owner_id']
                          id = c[0]['id']
                          q1 = ['photo' + str(owner_id) + '_' + str(id)]
                          send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                       message='Твой собеседник', q1=q1)
                          q1=0

                     send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                   message='-10💎')
                     q[item]['diamonds'] -= 10
                     diamonds = q[item]['diamonds']
                     save_obj(obj=q, name='dict_users')

                #ОТПРАВЛЯЕТ ССЫЛКУ СОБЕСЕДНИКА
                elif (response == 'link 📎' or response == 'link') and q[item]['diamonds'] >=50 and id_talker !=0 and in_chat == 1 and perk > 0:
                    otvet = 1
                    link_talker = '@id' + str(id_talker) + '(Твой собеседник)'
                    send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                 message=link_talker)
                    send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                 message='-50💎')
                    q[item]['diamonds'] -= 50
                    diamonds = q[item]['diamonds']
                    if q[found]['perk'] == 1:
                        send_message(session_api, peer_id=found, tit=bot,
                                     message='Собеседник получил  {0}(ссылку) 📎 на ваш профиль 📃'.format(('@id' + str(id_talker))))
                    save_obj(obj=q, name='dict_users')

                elif (response == 'photo 📸' or response == 'link 📎' or response == 'city 🌆' or response == 'age 👶🏻' or response == 'photo' or response == 'link' or response == 'city' or response == 'age') and id_talker != 0 and in_chat == 1:
                    otvet = 1
                    if perk ==0:
                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='Доступ к приватным функциям есть только у VIP 👑\nВип - узнать подробности')
                    elif perk >0:

                        mmm =''
                        if response == 'photo 📸' or response == 'photo':
                            mmm = 10 - q[item]['diamonds']
                        elif response == 'link 📎' or response == 'link':
                            mmm = 50 - q[item]['diamonds']
                        elif response == 'city 🌆' or response == 'city':
                            mmm = 2 - q[item]['diamonds']
                        elif response == 'age 👶🏻' or response == 'age':
                            mmm = 5 - q[item]['diamonds']

                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='Не хватает {}💎 для выполнения этой команды ☹'.format(mmm))

                elif (response == 'зонк 🎲' or response == 'зонк')  and id_talker != 0 and in_chat == 1 and cod != 'zonk1' and q[found]['diamonds'] >=5 and q[item]['diamonds'] >=5:
                     otvet = 1
                     print('Поступило предложение сыграть в зонк')


                     q[item]['cod'] = 'zonk1' #ждем ответа
                     q[found]['cod'] = 'zonk0'#переменная переключатель #согласен на предложение?
                     send_message(session_api, peer_id=item, tit=bot,
                                  message='Приглашение отправлено 🎲')
                     send_message(session_api, peer_id=id_talker, tit=bot,
                                  message='Собеседник предлагает сыграть в Зонк 🎲, вы согласны?', keyboard=create_keyboard(response, item, in_chat, perk, number, var))

                     q[found]['in_chat'] = 3
                     q[item]['in_chat'] = 3
                     in_chat = q[item]['in_chat']

                     save_obj(obj=q, name='dict_users')

                elif ((response == 'зонк 🎲' or response == 'зонк') and id_talker != 0 and in_chat == 1 and cod != 'zonk1' and (q[found]['diamonds'] < 5 or q[item]['diamonds'] < 5)):

                    if q[item]['diamonds'] < 5:
                        send_message(session_api, peer_id=item, tit=bot,
                                 message='У вас недостаточно 💎 для игры в Зонк ☹')
                    elif q[found]['diamonds'] < 5:
                        send_message(session_api, peer_id=item, tit=bot,
                                     message='У вашего собеседника недостаточно 💎 для игры в Зонк ☹')


                # ответ на предложение сыграть в игру ЗОНК
                elif (response == 'да 👍🏻' or response == 'да') and id_talker !=0 and in_chat == 3 and cod == 'zonk0':
                    otvet = 1

                    q[item]['game_room'] = q[item]['id_convers']
                    q[found]['game_room'] = q[item]['game_room']
                    game_room = q[item]['game_room']


                    send_message(session_api, peer_id=q[item]['id_talker'], tit=bot,
                                 message='Собеседник принял приглашение!\nДелайте ваши ставки!\nВаш баланс: 💎{0}\nСерия побед : 🏆{2}\nМножитель ставки: ✖{1}'.format(q[q[item]['id_talker']]['diamonds'],calc_x (zonk[q[item]['id_talker']]['coef']), zonk[q[item]['id_talker']]['coef']), keyboard=create_keyboard('да', q[item]['id_talker'] , in_chat, perk, number, var))

                    q[item]['cod'] = 'zonk2'  # переменная переключатель
                    q[found]['cod'] = 'zonk2'
                    save_obj(obj=q, name='dict_users')
                    send_message(session_api, peer_id=item, tit=bot,
                                 message='Делайте ваши ставки!\nВаш баланс: 💎{0}\nСерия побед : 🏆{2}\nМножитель ставки: ✖{1}'.format(q[item]['diamonds'],calc_x (coef),zonk[item]['coef']), keyboard=create_keyboard('да', item, in_chat, perk, number, var))
                #ответ на предложение сыграть в игру ЗОНК
                elif (response == 'нет 👎🏻' or response == 'нет') and id_talker != 0 and in_chat == 3 and cod == 'zonk0':
                    otvet = 1
                    q[item]['cod'] = 0
                    q[found]['cod'] = 0

                    q[found]['in_chat'] = 1

                    q[item]['in_chat'] = 1
                    in_chat = q[item]['in_chat']
                    save_obj(obj=q, name='dict_users')

                    send_message(session_api, peer_id=q[item]['id_talker'], tit=bot,
                                 message='Собеседник отказался от игры!')


                elif (response == '5💎' or response == '10💎' or response == '15💎' or response == '30💎' or response in list_bets) and q[item]['in_chat'] == 3 and (q[item]['cod'] == 'zonk2' or q[found]['cod'] == 'zonk2'):
                    otvet = 1
                    bets1, aaa = bets(response=event.obj.text)

                    q[item]['cod'] = 0

                    if q[item]['diamonds'] >= bets1:
                        q[item]['diamonds'] -= bets1
                        diamonds = q[item]['diamonds']
                        q[item]['bet'] += bets1
                        bet = q[item]['bet']
                        send_message(session_api, peer_id=item, tit=bot,
                                     message='-{}💎'.format(str(bets1)))
                        send_message(session_api, peer_id=q[item]['id_talker'], tit=bot,
                                     message='Собеседник делает ставку {}💎'.format(str(bets1)))

                        save_obj(obj=q, name='dict_users')

                    else:
                        keyboard = VkKeyboard(one_time=True)

                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='У вас недостаточно 💎 для выполнения этого действия ☹')
                        send_message(session_api, peer_id=q[item]['id_talker'], tit=bot,
                                     message='У вашего собеседника недостаточно 💎 для игры в Зонк ☹', keyboard = keyboard.get_empty_keyboard())

                        q[item]['game_room'] = 0
                        q[item]['in_chat'] = 1
                        q[item]['cod'] = 0

                        q[q[item]['id_talker']]['game_room'] = 0
                        q[q[item]['id_talker']]['in_chat'] = 1
                        q[q[item]['id_talker']]['diamonds'] += q[q[item]['id_talker']]['bet']
                        q[q[item]['id_talker']]['cod'] = 0

                        if q[q[item]['id_talker']]['bet'] != 0:
                            send_message(session_api, peer_id=q[item]['id_talker'], tit=bot,
                                         message='Ваша ставка аннулирована\n+{}💎'.format(
                                             q[q[item]['id_talker']]['bet']))
                        q[q[item]['id_talker']]['bet'] = 0


                        save_obj(obj=q, name='dict_users')

                    if q[item]['bet'] != 0 and q[q[item]['id_talker']]['bet'] != 0:


                        players = [item, q[item]['id_talker']]

                        sent_message(session_api, user_ids=players, tit=bot,
                                     message='Ставки сделанны! \nВаша цель набать 9 очков!')#\n\nЕще - кинуть еще 1 кубик\nХватит - закончить набор очков\nВыйти - закончить игру')
                        choices1 = random.randint(1, 6)
                        q[item]['number'] = choices1

                        choices2 = random.randint(1, 6)
                        q[q[item]['id_talker']]['number'] = choices2

                        q[item]['timeout'] = monotonic()
                        q[found]['timeout'] = monotonic()

                        save_obj(obj=q, name='dict_users')

                        send_message(session_api, peer_id=item, tit=bot,
                                     message='', q1=choices_photo(choices=choices1,id_talker=q[item]['id_talker'],item=item))

                        send_message(session_api, peer_id=item, tit=bot,
                                     message=#'На кубике выпадает число: {0}'
                                             '\n{2} Ваш счет: {0}\n📢 Счет собеседника: {1}'.format(q[item]['number'],q[q[item]['id_talker']]['number'], smile_score(number) ), keyboard=create_keyboard(response, item, in_chat, perk, number, var='except'))

                        send_message(session_api, peer_id=q[item]['id_talker'], tit=bot,
                                     message='', q1=choices_photo(choices=choices2,id_talker=q[item]['id_talker'],item=item))
                        send_message(session_api, peer_id=q[item]['id_talker'], tit=bot,
                                     message=#'На кубике выпадает число: {0}'
                                             '\n{2} Ваш счет: {1}\n📢 Счет собеседника: {0}'.format(q[item]['number'],q[q[item]['id_talker']]['number'], smile_score(q[found]['number'])), keyboard=create_keyboard(response, item, in_chat, perk, number, var='except'))


                elif (response == 'еще' or response == 'еще 🎲') and q[item]['in_chat'] == 3 and q[item]['game_room'] != -1 and q[item]['cod'] ==0:
                    otvet = 1

                    q[item]['timeout'] = monotonic()
                    save_obj(obj=q, name='dict_users')
                    if q[item]['number'] < 9:

                        choices = random.randint(1, 6)
                        q[item]['number'] += choices
                        number = q[item]['number']

                        send_message(session_api, peer_id=item, tit=bot,
                                     message='',q1=choices_photo(choices=choices,id_talker=q[item]['id_talker'],item=item))
                        send_message(session_api, peer_id=item, tit=bot,
                                     message=#'На кубике выпадает число: {0}'
                                             '{1} Ваш счет: {0}'.format(q[item]['number'],smile_score(number)),keyboard=create_keyboard(response, item,in_chat,perk,number, var))
                        send_message(session_api, peer_id=q[item]['id_talker'], tit=bot,
                                     message='📢 Счет собеседника:{0}'.format(q[item]['number'])) #Собеседник подбрасывает кубик! \n


                        save_obj(obj=q, name='dict_users')

                        if q[item]['number'] > 9:
                            #print('что в number ' + str(number))
                            send_message(session_api, peer_id=item, tit=bot,
                                         message='Вы набрали больше 9 очков, хотите перекинуть последний бросок кубика? -1💎' ,keyboard=create_keyboard(response, item,in_chat,perk,number, var))
                            q[item]['game_room'] = choices

                            save_obj(obj=q, name='dict_users')

                    elif q[item]['number'] > 9 and q[q[item]['id_talker']]['number'] <=9:
                        keyboard = VkKeyboard(one_time=True)
                        send_message(session_api, peer_id=item, tit=bot,
                                     message='Вы проиграли!😕', keyboard=keyboard.get_empty_keyboard())
                        send_message(session_api, peer_id=q[item]['id_talker'], tit=bot,
                                     message='Вы выйграли!\n+{}💎'.format(q[q[item]['id_talker']]['bet'] * calc_x (zonk[q[item]['id_talker']]['coef'])),
                                     keyboard=keyboard.get_empty_keyboard())

                        q[item]['game_room'] = 0
                        q[item]['bet'] = 0
                        q[item]['number'] = 0
                        q[item]['in_chat'] = 1
                        zonk[item]['coef'] = 0
                        zonk[item]['lose'] +=1

                        q[q[item]['id_talker']]['game_room'] = 0
                        q[q[item]['id_talker']]['diamonds'] += (q[q[item]['id_talker']]['bet'] * calc_x (zonk[q[item]['id_talker']]['coef']))
                        q[q[item]['id_talker']]['rep_points'] += (q[q[item]['id_talker']]['bet'] * calc_x(zonk[q[item]['id_talker']]['coef']))
                        q[q[item]['id_talker']]['bet'] = 0
                        q[q[item]['id_talker']]['number'] = 0
                        q[q[item]['id_talker']]['in_chat'] = 1

                        zonk[q[item]['id_talker']]['coef'] += 1
                        zonk[q[item]['id_talker']]['win'] +=1

                        q[q[item]['id_talker']]['timeout'] = 0
                        q[item]['timeout'] = 0

                        save_obj(obj=q, name='dict_users')
                        save_obj(obj=zonk, name='zonk')


                    elif q[item]['number'] == 9:

                        send_message(session_api, peer_id=item, tit=bot,
                                     message='Поздравляем! 🎉\n{2} Ваш счет: {0}'
                                             '\n📢 Счет собеседника: {1}'.format(q[item]['number'],q[q[item]['id_talker']]['number'],smile_score(number)),keyboard=create_keyboard(response, item,in_chat,perk,number, var))



                elif (response == 'перекинуть' or response == 'перекинуть ♻') and q[item]['in_chat'] == 3  and q[item]['number'] > 9 and q[item]['game_room'] != -1 and q[item]['cod'] ==0:

                    if q[item]['diamonds'] >= 1:
                        otvet = 1


                        q[item]['timeout'] = monotonic()

                        q[item]['diamonds'] -=1
                        send_message(session_api, peer_id=item, tit=bot,
                                     message='-1💎')
                        q[item]['number'] -= q[item]['game_room']
                        diamonds = q[item]['diamonds']

                        choices = random.randint(1, 6)
                        q[item]['number'] += choices
                        number = q[item]['number']
                        if number >9:
                            keyboard = VkKeyboard(one_time=True)
                            keyboard = keyboard.get_empty_keyboard()

                        send_message(session_api, peer_id=item, tit=bot,
                                     message='', q1=choices_photo(choices=choices,id_talker=q[item]['id_talker'],item=item))
                        send_message(session_api, peer_id=item, tit=bot,
                                     message=#'На кубике выпадает число: {0}'
                                             '{2} Ваш счет: {0}\n📢 Счет собеседника:{1}'.format(q[item]['number'],q[q[item]['id_talker']]['number'],smile_score(number)),keyboard=create_keyboard(response, item, in_chat, perk, number, var))
                        send_message(session_api, peer_id=q[item]['id_talker'], tit=bot,
                                     message='Собеседник перекинул последний бросок кубика! \n📢 Счет собеседника:{0}'.format(
                                         q[item]['number']))
                        q[item]['game_room'] = -1
                        save_obj(obj=q, name='dict_users')
                        save_obj(obj=zonk, name='zonk')


                        if q[item]['number'] > 9 and q[q[item]['id_talker']]['number'] <=9:

                            keyboard = VkKeyboard(one_time=True)
                            send_message(session_api, peer_id=item, tit=bot,
                                         message='Вы проиграли!😕', keyboard=keyboard.get_empty_keyboard())
                            send_message(session_api, peer_id=q[item]['id_talker'], tit=bot,
                                         message='Вы выйграли!\n+{}💎'.format(q[q[item]['id_talker']]['bet'] * calc_x (zonk[q[item]['id_talker']]['coef'])),
                                         keyboard=keyboard.get_empty_keyboard())

                            q[item]['game_room'] = 0
                            q[item]['bet'] = 0
                            q[item]['number'] = 0
                            q[item]['in_chat'] = 1
                            zonk[item]['coef'] = 0
                            zonk[item]['lose'] += 1

                            q[q[item]['id_talker']]['game_room'] = 0
                            q[q[item]['id_talker']]['diamonds'] += (q[q[item]['id_talker']]['bet'] * calc_x(zonk[q[item]['id_talker']]['coef']))
                            q[q[item]['id_talker']]['rep_points'] += (q[q[item]['id_talker']]['bet'] * calc_x(zonk[q[item]['id_talker']]['coef']))
                            q[q[item]['id_talker']]['bet'] = 0
                            q[q[item]['id_talker']]['number'] = 0
                            q[q[item]['id_talker']]['in_chat'] = 1

                            zonk[q[item]['id_talker']]['coef'] += 1
                            zonk[q[item]['id_talker']]['win'] += 1

                            q[q[item]['id_talker']]['timeout'] = 0
                            q[item]['timeout'] = 0
                            save_obj(obj=q, name='dict_users')
                            save_obj(obj=zonk, name='zonk')


                        elif q[item]['number'] > q[q[item]['id_talker']]['number'] and q[item]['number'] <=9 and q[q[item]['id_talker']]['number'] >9:
                            keyboard = VkKeyboard(one_time=True)
                            send_message(session_api, peer_id=item, tit=bot,
                                         message='Вы выйграли!\n+{}💎'.format(q[item]['bet'] * calc_x (coef)),keyboard=keyboard.get_empty_keyboard())
                            send_message(session_api, peer_id=q[item]['id_talker'], tit=bot,
                                         message='Вы проиграли!😕', keyboard=keyboard.get_empty_keyboard())

                            q[item]['game_room'] = 0
                            q[item]['diamonds'] += (q[item]['bet'] * calc_x (coef))
                            q[item]['rep_points'] += (q[item]['bet'] * calc_x(coef))
                            q[item]['bet'] = 0
                            q[item]['number'] = 0
                            q[item]['in_chat'] = 1

                            zonk[item]['coef'] += 1
                            zonk[item]['win'] += 1

                            q[q[item]['id_talker']]['game_room'] = 0
                            q[q[item]['id_talker']]['bet'] = 0
                            q[q[item]['id_talker']]['number'] = 0
                            q[q[item]['id_talker']]['in_chat'] = 1

                            zonk[q[item]['id_talker']]['coef'] = 0
                            zonk[q[item]['id_talker']]['lose'] += 1

                            q[q[item]['id_talker']]['timeout'] = 0
                            q[item]['timeout'] = 0
                            save_obj(obj=q, name='dict_users')
                            save_obj(obj=zonk, name='zonk')

                        elif q[item]['number'] > 9 and q[q[item]['id_talker']]['number'] >9:
                            keyboard = VkKeyboard(one_time=True)
                            send_message(session_api, peer_id=item, tit=bot,
                                         message='Вы проиграли!😕', keyboard=keyboard.get_empty_keyboard())
                            send_message(session_api, peer_id=q[item]['id_talker'], tit=bot,
                                         message='Вы проиграли!😕' ,keyboard=keyboard.get_empty_keyboard())

                            q[item]['game_room'] = 0
                            q[item]['bet'] = 0
                            q[item]['number'] = 0
                            q[item]['in_chat'] = 1

                            zonk[item]['coef'] = 0
                            zonk[item]['lose'] += 1

                            q[q[item]['id_talker']]['game_room'] = 0
                            q[q[item]['id_talker']]['bet'] = 0
                            q[q[item]['id_talker']]['number'] = 0
                            q[q[item]['id_talker']]['in_chat'] = 1

                            zonk[q[item]['id_talker']]['coef'] = 0
                            zonk[q[item]['id_talker']]['lose'] += 1

                            q[q[item]['id_talker']]['timeout'] = 0
                            q[item]['timeout'] = 0
                            save_obj(obj=q, name='dict_users')
                            save_obj(obj=zonk, name='zonk')

                    else:
                        send_message(session_api, peer_id=item, tit=bot,
                                     message="У вас недостаточно 💎", keyboard=keyboard)


                elif ((response  == 'хватит' or response  == 'хватит ✅' or response == 'перекинуть' or response == 'перекинуть ♻' or response == 'еще' or response == 'еще 🎲' ) and q[item]['in_chat'] == 3 and q[item]['cod'] == 0) or (q[item]['cod'] == 'endzonk'):  #and q[q[item]['id_talker']]['game_room'] == q[item]['id_convers']
                   try:
                    otvet = 1
                    keyboard = VkKeyboard(one_time=True)
                    q[item]['timeout'] = monotonic()
                    q[item]['game_room'] = -1

                    if q[item]['cod'] != 'endzonk':
                        send_message(session_api, peer_id=q[item]['id_talker'], tit=bot,
                                     message='{2} Ваш счет: {1}'
                                             '\n📢 Счет собеседника: {0}\nСобеседник закончил свой ход!'.format(
                                         q[item]['number'], q[q[item]['id_talker']]['number'], smile_score(q[found]['number'])))
                        if q[found]['cod'] == 'endzonk':
                            vvv = ''
                        else:
                            vvv = 'Ожидаем конца хода собеседника!'
                        send_message(session_api, peer_id=item, tit=bot,
                                     message='{2} Ваш счет: {0}'
                                             '\n📢 Счет собеседника: {1}\n{3}'.format(
                                         q[item]['number'], q[q[item]['id_talker']]['number'], smile_score(number),vvv),
                                     keyboard=keyboard.get_empty_keyboard())

                    else:
                        mon_talker = mon - q[found]['timeout']
                        kickoff = 120 - int(mon_talker)
                        if kickoff == 30 or kickoff == 15:
                            send_message(session_api, peer_id=q[item]['id_talker'], tit=bot,
                                        message='В течении {0} секунд вы будите исключены за бездействие!'.format(str(kickoff)))

                        mon_item = mon - q[item]['timeout']
                        kickoff1 = 120 - int(mon_item)

                        send_message(session_api, peer_id=item, tit=bot,
                                     message='{2} Ваш счет: {0}'
                                             '\n📢 Счет собеседника: {1}'
                                             '\nПротивник будет исключен за бездействие в течении {3} секунд!'.format(
                                         q[item]['number'], q[q[item]['id_talker']]['number'], smile_score(number),
                                         kickoff),
                                     keyboard=keyboard.get_empty_keyboard())

                    q[item]['cod'] = 'endzonk'
                    if (q[item]['game_room'] == -1 and q[q[item]['id_talker']]['game_room'] == -1) or q[q[item]['id_talker']]['number']>=9 or q[item]['number']>9:
                        q[item]['cod'] = 0
                        q[found]['cod'] = 0

                        save_obj(obj=q, name='dict_users')
                        if (q[item]['number'] > q[q[item]['id_talker']]['number'] and q[item]['number'] <=9) or (q[item]['number'] <=9 and q[q[item]['id_talker']]['number']>9):
                            send_message(session_api, peer_id=item, tit=bot,
                                         message='Вы выйграли!\n+{}💎'.format(q[item]['bet'] * calc_x (coef)),keyboard=keyboard.get_empty_keyboard())
                            send_message(session_api, peer_id=q[item]['id_talker'], tit=bot,
                                         message='Вы проиграли!😕',keyboard=keyboard.get_empty_keyboard())

                            q[item]['game_room'] = 0
                            q[item]['diamonds'] += (q[item]['bet'] * calc_x (coef))
                            q[item]['rep_points'] += (q[item]['bet'] * calc_x(coef))
                            q[item]['bet'] = 0
                            q[item]['number'] = 0
                            q[item]['in_chat'] = 1

                            zonk[item]['coef'] += 1
                            zonk[item]['win'] += 1

                            q[q[item]['id_talker']]['game_room'] = 0
                            q[q[item]['id_talker']]['bet'] = 0
                            q[q[item]['id_talker']]['number'] = 0
                            q[q[item]['id_talker']]['in_chat'] = 1

                            zonk[q[item]['id_talker']]['coef'] = 0
                            zonk[q[item]['id_talker']]['lose'] += 1

                            q[q[item]['id_talker']]['timeout'] = 0
                            q[item]['timeout'] = 0
                            save_obj(obj=q, name='dict_users')
                            save_obj(obj=zonk, name='zonk')


                        elif (q[item]['number'] < q[q[item]['id_talker']]['number'] and q[q[item]['id_talker']]['number'] <=9) or (q[q[item]['id_talker']]['number'] <=9 and q[item]['number']>9):
                            send_message(session_api, peer_id=item, tit=bot,
                                         message='Вы проиграли!😕',keyboard=keyboard.get_empty_keyboard())
                            send_message(session_api, peer_id=q[item]['id_talker'], tit=bot,
                                         message='Вы выйграли!\n+{}💎'.format(q[q[item]['id_talker']]['bet'] * calc_x (zonk[q[item]['id_talker']]['coef'])), keyboard=keyboard.get_empty_keyboard())

                            q[item]['game_room'] = 0
                            q[item]['bet'] = 0
                            q[item]['number'] = 0
                            q[item]['in_chat'] = 1

                            zonk[item]['coef'] = 0
                            zonk[item]['lose'] += 1

                            q[q[item]['id_talker']]['game_room'] = 0
                            q[q[item]['id_talker']]['diamonds'] += (q[q[item]['id_talker']]['bet'] * calc_x (zonk[q[item]['id_talker']]['coef']))
                            q[q[item]['id_talker']]['rep_points'] += (q[q[item]['id_talker']]['bet'] * calc_x(zonk[q[item]['id_talker']]['coef']))
                            q[q[item]['id_talker']]['bet'] = 0
                            q[q[item]['id_talker']]['number'] = 0
                            q[q[item]['id_talker']]['in_chat'] = 1

                            zonk[q[item]['id_talker']]['coef'] += 1
                            zonk[q[item]['id_talker']]['win'] += 1

                            q[q[item]['id_talker']]['timeout'] = 0
                            q[item]['timeout'] = 0
                            save_obj(obj=q, name='dict_users')
                            save_obj(obj=zonk, name='zonk')


                        elif q[item]['number'] == q[q[item]['id_talker']]['number'] and q[item]['number']<=9:

                            bets1, aaa = bets(response=q[item]['bet'])
                            send_message(session_api, peer_id=item, tit=bot,
                                         message='Ничья!\n+{}💎'.format(q[item]['bet'] + aaa),keyboard=keyboard.get_empty_keyboard())

                            q[item]['game_room'] = 0
                            q[item]['diamonds'] += (q[item]['bet'] + aaa)
                            q[item]['bet'] = 0
                            q[item]['number'] = 0
                            q[item]['in_chat'] = 1

                            zonk[item]['draw'] += 1

                            game_room = q[item]['game_room']
                            bet = q[item]['bet']
                            number = q[item]['number']
                            in_chat = q[item]['in_chat']

                            bets1, aaa = bets(response=q[q[item]['id_talker']]['bet'])
                            send_message(session_api, peer_id=q[item]['id_talker'], tit=bot,
                                         message='Ничья!\n+{}💎'.format(q[q[item]['id_talker']]['bet'] + aaa),
                                         keyboard=keyboard.get_empty_keyboard())

                            q[q[item]['id_talker']]['game_room'] = 0
                            q[q[item]['id_talker']]['diamonds'] += (q[q[item]['id_talker']]['bet'] + aaa)
                            q[q[item]['id_talker']]['bet'] = 0
                            q[q[item]['id_talker']]['number'] = 0
                            q[q[item]['id_talker']]['in_chat'] = 1

                            zonk[q[item]['id_talker']]['draw'] += 1

                            q[q[item]['id_talker']]['timeout'] = 0
                            q[item]['timeout'] = 0
                            save_obj(obj=q, name='dict_users')
                            save_obj(obj=zonk, name='zonk')

                        else:
                            send_message(session_api, peer_id=item, tit=bot,
                                         message='Вы проиграли!😕',keyboard=keyboard.get_empty_keyboard())
                            send_message(session_api, peer_id=q[item]['id_talker'], tit=bot,
                                         message='Вы проиграли!😕',keyboard=keyboard.get_empty_keyboard())

                            q[item]['game_room'] = 0
                            q[item]['bet'] = 0
                            q[item]['number'] = 0
                            q[item]['in_chat'] = 1

                            zonk[item]['coef'] = 0
                            zonk[item]['lose'] += 1

                            game_room = q[item]['game_room']
                            bet = q[item]['bet']
                            number = q[item]['number']
                            in_chat = q[item]['in_chat']

                            q[q[item]['id_talker']]['game_room'] = 0
                            q[q[item]['id_talker']]['bet'] = 0
                            q[q[item]['id_talker']]['number'] = 0
                            q[q[item]['id_talker']]['in_chat'] = 1

                            zonk[q[item]['id_talker']]['coef'] = 0
                            zonk[q[item]['id_talker']]['lose'] += 1

                            q[q[item]['id_talker']]['timeout'] = 0
                            q[item]['timeout'] = 0
                            save_obj(obj=q, name='dict_users')
                            save_obj(obj=zonk, name='zonk')


                    save_obj(obj=q, name='dict_users')

                   except:
                     print('ОШИБКА в endzonk')

                elif response == "выйти" and q[item]['in_chat'] == 3 and q[item]['number'] ==0:
                    otvet = 1

                    send_message(session_api, peer_id=item, tit=bot,
                                 message='Ва вышли из игры Зонк 🎲.', keyboard=create_keyboard(response, item, in_chat, perk, number, var))

                    send_message(session_api, peer_id=q[item]['id_talker'], tit=bot,
                                 message='Ваш собеседник отказался от игры в Зонк ☹', keyboard=create_keyboard(response, item, in_chat, perk, number, var))

                    q[item]['game_room'] = 0
                    q[item]['bet'] = 0
                    q[item]['number'] = 0
                    q[item]['in_chat'] = 1
                    q[item]['cod'] = 0

                    q[q[item]['id_talker']]['game_room'] = 0
                    q[q[item]['id_talker']]['diamonds'] += q[q[item]['id_talker']]['bet']
                    q[found]['cod'] = 0


                    if q[q[item]['id_talker']]['bet'] !=0:
                      send_message(session_api, peer_id=q[item]['id_talker'], tit=bot,
                                   message='Ваша ставка аннулирована\n+{}💎'.format(q[q[item]['id_talker']]['bet']), keyboard=create_keyboard(response, item, in_chat, perk, number, var))

                    q[q[item]['id_talker']]['bet'] = 0
                    q[q[item]['id_talker']]['number'] = 0
                    q[q[item]['id_talker']]['in_chat'] = 1

                    save_obj(obj=q, name='dict_users')



                elif response == "выйти" and q[item]['in_chat'] == 3 and q[item]['number'] !=0:
                    otvet = 1
                    send_message(session_api, peer_id=item, tit=bot,
                                 message='Сейчас вы не можете выйти из игры!')



                #ГЛУШИТ ДИАЛОГ ЕСЛИ ПОЛЬЗОВАТЕЛЬ В ЧАТЕ
                elif response == 'стоп' and in_chat == 1:

                  otvet = 1
                  found = q[item]['id_talker']

                  send_message(session_api, peer_id=item, tit=bot,
                               message='Диалог #{0} закончен 👫\nПонравился собеседник?'.format(q[item]['id_convers']), keyboard=create_keyboard(response, item, in_chat, perk, number, var))
                  try:
                     send_message(session_api, peer_id=found, tit=bot,
                               message='Диалог #{0} закончен 👫\nПонравился собеседник?'.format(q[item]['id_convers']),
                               keyboard=create_keyboard(response, item, in_chat, perk, number, var))
                  except:
                      pass

                  try:
                      q[item]['id_convers'] = 0
                      q[item]['in_chat'] = 0
                      q[item]['voices'] = 0
                      save_obj(obj=q, name='dict_users')

                      q[found]['in_chat'] = 0
                      q[found]['voices'] = 0
                      q[found]['id_convers'] = 0
                  except:
                      print('Ошибка в стопе chat1')

                  save_obj(obj=q, name='dict_users')

                elif response == 'стоп' and in_chat == 2 and item in third_list:#777
                    otvet = 1
                    third_list.remove(item)

                    try:
                        send_message(session_api, peer_id=third_list, tit=bot,
                                     message='Один из собеседников покинул беседу!\nКоличество человек в беседе: 1')
                    except Exception as err:
                        print('Ошибка при остановки беседы ' + str(err))
                        logging.error('Ошибка при остановки беседы ' + str(err))

                    send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                 message='Вы вышли из беседы 👫')
                    open_menu (session_api,'меню',item, bot, var)
                    q[item]['in_chat'] = 0
                    save_obj(obj=q, name='dict_users')
                    save_obj(obj=third_list, name='third_list')


                elif response == 'стоп' and in_chat == 2 and item not in third_list:
                 #try:
                  otvet = 1
                  #если собеседников трое
                  print(q[item]['id_talker'])
                  if len(q[item]['id_talker']) == 2:
                      for i in q[item]['id_talker']:
                          q[i]['id_talker'] = [i for i in q[i]['id_talker'] if i != item]
                          save_obj(obj=q, name='dict_users')
                          send_message(session_api, peer_id=i, tit=bot,
                                       message='Один из собеседников покинул беседу!\nКоличество человек в беседе: 2')


                      send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                   message='Вы вышли из беседы #{0} 👫'.format(q[item]['id_convers']))
                      open_menu (session_api,'меню',item, bot, var)

                      q[item]['in_chat'] = 0
                      q[item]['id_talker'] = 0
                      q[item]['id_convers'] = 0

                      save_obj(obj=q, name='dict_users')

                  else:

                      found = q[item]['id_talker'][0]

                      send_message(session_api, peer_id=found, tit=bot,
                                   message='Беседа #{0} закончена 👫'.format(q[item]['id_convers']))
                      open_menu(session_api, 'меню', found, bot, var)
                      send_message(session_api, peer_id=item, tit=bot,
                                   message='Беседа #{0} закончена 👫'.format(q[item]['id_convers']))
                      open_menu (session_api,'меню',item, bot, var)

                      q[found]['in_chat'] = 0
                      q[found]['id_talker'] = 0
                      q[found]['id_convers'] = 0
                      q[item]['in_chat'] = 0
                      q[item]['id_talker'] = 0
                      q[item]['id_convers'] = 0

                      save_obj(obj=q, name='dict_users')
                 #except:



                # ГЛУШИТ ДИАЛОГ ЕСЛИ ПОЛЬЗОВАТЕЛЬ В ЧАТЕ И СРАЗУ ИЩЕТ НОВОГО СОБЕСЕДНИКА
                elif response == 'новый' and in_chat == 1:
                    user_inf, first_name, last_name, last_and_first_name = user_information (session_api, event)
                    otvet = 1
                    found = q[item]['id_talker']

                    send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                 message='Диалог #{0} закончен 👫'.format(
                                     q[item]['id_convers']))
                    send_message(session_api, peer_id=found, tit=bot,
                                 message='Диалог #{0} закончен 👫\nПонравился собеседник?'.format(
                                     q[found]['id_convers']), keyboard=create_keyboard('стоп', found, 1, perk, number, var))
                    q[item]['id_convers'] = 0
                    q[item]['id_talker'] = 0
                    q[item]['in_chat'] = 0
                    q[found]['in_chat'] = 0
                    # q[found]['id_talker'] = 0
                    q[found]['id_convers'] = 0

                    search0 = [name for person in que for name, attr in person['user'].items() if
                                 attr['search'] == 0]
                    if len(search0) !=0:
                        general_search = search0
                        print('Пользователей найдено по по условию search0:0 = ' + str(search0))

                    elif user_inf == 1 and len(search0) ==0:
                        search1 = [name for person in que for name, attr in person['user'].items() if
                                  attr['search'] == 1]
                        general_search = search1
                        print('Пользователей найдено по по условию search:1 = ' + str(search1))
                    elif user_inf == 2 and len(search0) ==0:
                        search2 = [name for person in que for name, attr in person['user'].items() if
                                   attr['search'] == 2]
                        general_search = search2
                        print('Пользователей найдено по по условию search:2 = ' + str(search2))
                    else:
                        general_search = 0


                    if len(general_search) !=0:
                        #print('Cписок для выбора по параметру search:0 ' + str(search0))
                        found = (
                            random.choice(general_search))  # выбираем случайного пользователя из списка по параметру search
                        general_search.remove(found)  # кого нашли удаляем из списка ожидания
                        all_list.remove(found)
                        que = [name for name in que if found not in name['user']]

                        save_obj(obj=que, name='que')
                        save_obj(obj=all_list, name='all_list')
                        print('что в que ' + str(que))
                        print('С кем будет общатьсся ' + str(found))
                        print('#{0} диалога'.format(str(q[found]['id_convers'])))
                        q[item]['id_convers'] = q[found]['id_convers']
                        q[item]['in_chat'] = 1
                        q[found]['in_chat'] = 1

                        q[item]['id_talker'] = found
                        q[found]['id_talker'] = item

                        print('Собеседник ' + str(q[item]['id_talker']) + ' = ' + str(q[found]['id_talker']))

                        save_obj(obj=q, name='dict_users')

                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='Репутация собеседника: {0} \nПриятного общения! 😈\n\nСтоп - завершить текущий диалог ⛔\nНовый - завершить диалог и найти нового собеседника ♻\n{1}'.format(
                                         rt(id_talker=found),hack))
                        send_message(session_api, peer_id=found, tit=bot,
                                     message='Репутация собеседника: {0} \nПриятного общения! 😈\n\nСтоп - завершить текущий диалог ⛔\nНовый - завершить диалог и найти нового собеседника ♻\n{1}'.format(rp,hack))


                    else:

                        que.append({'user': {item: {'sex': user_inf,
                                                    'search': 0}}})  # добавляем в список ожидания пользователя

                        save_obj(obj=que, name='que')
                        all_list.append(item)
                        save_obj(obj=all_list, name='all_list')
                        print('В search:0 добавлен новый пользователь с ID: {0} = {1}' .format(item,que))
                        print('Так-же он был добавлен в all_list: ' + str(all_list))

                        convers += 1
                        save_obj(obj=convers, name='convers')

                        q[item]['id_convers'] = convers
                        save_obj(obj=q, name='dict_users')

                        #отправка сообщения о поиске собеседника
                        t_hi_chat = threading.Thread(target=hi_chat, name='thread_hi_chat',
                                               args=(session_api, q, event,bot,item, user_inf))
                        t_hi_chat.start()
                        print('Cтартанул поток {}'.format(t_hi_chat.name))
                        #hi_chat (session_api, q, event,bot,item, user_inf)
                        ###




                #НЕЛЬЗЯ ИСКАТЬ НОВОГО СОБЕСЕДНИКА ЧЕРЕЗ КОМАНДУ НОВЫЙ ЕСЛИ ПОЛЬЗОВАТЕЛЬ НЕ В ЧАТЕ
                elif (response == 'стоп' or response =='новый') and in_chat == 0 and item not in all_list:
                    otvet = 1
                    send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                 message='Ты не находишься в диалоге для выполнения этой команды 👫')
                    open_menu (session_api,'меню',item, bot, var)

                #ОСТАНАВЛИВАЕМ ПОИСК И УБИРАЕМ ИЗ ОЧЕРЕДИ
                elif (response == 'стоп' or response =='прервать') and in_chat == 0 and item in all_list:
                    otvet = 1
                    que = [name for name in que if item not in name['user']] #удаляет пользователя из очеди поиска
                    #print(keyboard)

                    send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                 message='Поиск собеседника 👫 остановлен ⛔')
                    open_menu (session_api,'меню',item, bot, var)
                    convers -= 1
                    save_obj(obj=convers, name='convers')

                    q[item]['id_convers'] = 0
                    save_obj(obj=q, name='dict_users')
                    all_list.remove(item)
                    save_obj(obj=all_list, name='all_list' )
                    save_obj(obj=que, name='que')

                    #print(que)


                #ПОМОЩЬ НЕ В ЧАТЕ
                elif (response == 'меню' or response == 'поиск' or response == 'м' or response == 'ж' or response == 'назад') and in_chat == 2:
                    otvet = 1
                    q[item]['cod'] = 0
                    save_obj(obj=q, name='dict_users')
                    send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                 message='Ты находишься в беседе 👫\nСтоп - выйти из беседы ⛔')
                elif (response == 'меню' or response == 'назад') and in_chat == 0:
                    otvet = 1
                    q[item]['cod'] = 0
                    save_obj(obj=q, name='dict_users')
                    #t_open_m = threading.Thread(target=open_menu, name='thread_open_m',
                    #                       args=(session_api,response,item, bot, var))
                    #t_open_m.start()
                    #print('Cтартанул поток {}'.format(t_open_m.name))
                    open_menu (session_api,'меню',item, bot, var)



                elif response == 'начать' and in_chat == 1:
                    otvet = 1
                    send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                 message='Ты находишься в диалоге 👫\n Напиши: Новый и мы найдем тебе нового собеседника ♻'
                                         '\nНапиши: Стоп чтобы закончить диалог с собеседником ⛔')

                elif (response == 'беседа' or response =='беседа 👯‍♀') and item in third_list and item not in all_list and in_chat ==2:  # and perk ==1: # and in_chat == 0:
                    otvet = 1
                    send_message(session_api, peer_id=item, tit=bot,
                                 message='Мы еще не подобрали вам собеседников😩\nСтоп - выйти из беседы ⛔')






                elif (response == 'беседа' or response =='беседа 👯‍♀') and in_chat == 0 and item not in third_list and item not in all_list and perk > 0:
                    otvet = 1
                    #ПЕРВЫЙ УЧАСТНИК БЕСЕДЫ
                    if len(third_list) == 0:

                        third_list.append(item)
                        save_obj(obj=third_list, name='third_list')
                        send_message(session_api, peer_id=item, tit=bot,
                                     message='Вы добавлены в беседу, ожидаем собеседников\nСтоп - выйти из беседы ⛔\nКоличество человек 👨‍💻 в беседе:1')
                        q[item]['in_chat'] = 2
                        q[item]['rep_points'] +=7
                        save_obj(obj=q, name='dict_users')
                    # ВТОРОЙ УЧАСТНИК БЕСЕДЫ
                    elif len(third_list) == 1:
                        third_list.append(item)
                        send_message(session_api, peer_id=item, tit=bot,
                                     message='Вы добавлены в беседу, ожидаем собеседника\nСтоп - выйти из беседы ⛔')
                        save_obj(obj=third_list, name='third_list')
                        sent_message(session_api, user_ids=third_list, tit=bot,
                                     message='Количество человек 👨‍💻 в беседе:2')
                        q[item]['in_chat'] = 2
                        q[item]['rep_points'] += 7
                        save_obj(obj=q, name='dict_users')
                        for i in third_list:
                            third_list = load_obj('third_list')
                            third_copy = third_list
                            third_copy.remove(i)
                            q[i]['id_talker'] = third_copy
                            print(q[i]['id_talker'])

                        save_obj(obj=q, name='dict_users')
                        third_list = load_obj('third_list')
                        q = load_obj('dict_users')


                    # ТРЕТИЙ УЧАСТНИК БЕСЕДЫ
                    elif len(third_list) == 2:
                        third_list.append(item)
                        save_obj(obj=third_list, name='third_list')
                        q[item]['in_chat'] = 2
                        q[item]['rep_points'] += 7
                        save_obj(obj=q, name='dict_users')
                        send_message(session_api, peer_id=item, tit=bot,
                                     message='Вы добавлены в беседу\nСтоп - выйти из беседы ⛔')
                        convers += 1
                        #ПЕРЕБИРАЕМ ВСЕХ УЧАСТНИКОВ В БЕСЕДЕ И ПРИСВАЕМ ЛИСТ БЕСЕДЫ
                        for i in third_list:
                            third_list = load_obj('third_list')
                            third_copy = third_list
                            third_copy.remove(i)

                            q[i]['id_talker'] = third_copy
                            print(q[i]['id_talker'])
                            q[i]['id_convers'] = convers

                        save_obj(obj=q, name='dict_users')
                        third_list = load_obj('third_list')


                        print(third_list)

                        save_obj(obj=convers, name='convers')

                        third_list = load_obj('third_list')
                        sent_message(session_api, user_ids=third_list, message='Количество человек 👨‍💻 в беседе:3\nПриятного общения!', tit=bot)

                        q = load_obj('dict_users')
                        third_list.clear()
                        save_obj(obj=third_list, name='third_list')



                #ПЕРВИЧНЫЙ ПОИСК СОБЕСЕДНИКа ПО ПОЛУ
                elif (response == 'м' or response == 'ж') and len(all_list) == 0 and  (perk > 0 or q[item]['diamonds'] >=3 and rep !=-1) and in_chat == 0 and item not in third_list:
                    otvet = 1
                    user_inf = session_api.users.get(user_ids=event.obj.from_id,
                                                     fields='sex,bdate,city,blacklisted,can_write_private_message')

                    if q[item]['diamonds'] >=3 and perk == 0:
                        q[item]['diamonds'] -= 3
                        diamonds = q[item]['diamonds']
                        save_obj(obj=q, name='dict_users')
                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='-3💎')




                    if response == 'м':
                       que.append({'user': {
                           item: {'sex': user_inf[0]['sex'], 'search': 2}}})  # добавляем в список ожидания пользователя
                       print('Пользователь добавлен в список ожидания по полу м' + str(que))
                       send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                    message='Вы добавлены в очередь поиска собеседника по полу 👫'
                                            '\nИщем 👱‍♂ собеседника 🕵')
                    elif response == 'ж' or response == 'ж 🙎‍♀':
                        que.append({'user': {
                            item: {'sex': user_inf[0]['sex'], 'search': 1}}})
                        print('Пользователь добавлен в список ожидания по полу ж' + str(que))
                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='Вы добавлены в очередь поиска собеседника по полу 👫'
                                             '\nИщем 👩‍🦱 собеседника 🕵')

                    save_obj(obj=que, name='que')
                    all_list.append(item)
                    save_obj(obj=all_list, name='all_list')
                    #print(que)
                    #print(all_list)

                    convers += 1
                    #+5 поинта за создание диалога поиска по полу
                    q[item]['rep_points'] +=5
                    q[item]['id_convers'] = convers
                    save_obj(obj=convers, name='convers')
                    save_obj(obj=q, name='dict_users')


                # ВТОРИЧНЫЙ ПОИСК СОБЕСЕДНИКА ПО ПОЛУ С ЭЛЕМЕНТАМИ ПЕРВИЧНОГО
                elif (response == 'м' or response == 'ж') and in_chat == 0 and len(all_list) != 0 and (perk > 0 or q[item]['diamonds'] >=3 and rep !=-1) and item not in all_list:
                    user_inf = session_api.users.get(user_ids=event.obj.from_id,
                                                     fields='sex,bdate,city,blacklisted,can_write_private_message')
                    otvet = 1
                    print('Очередь поиска' + str(que))
                    print('Кто в общем списке на поиск ' + str(all_list))
                    if q[item]['diamonds'] >=3 and perk == 0:
                        q[item]['diamonds'] -=3
                        diamonds = q[item]['diamonds']
                        save_obj(obj=q, name='dict_users')
                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='-3💎')

                    if response == 'м':
                       send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                    message='Вы добавлены в очередь поиска собеседника по полу 👫'
                                            '\nИщем 👱‍♂ собеседника 🕵')
                       search = [name for person in que for name, attr in person['user'].items() if (attr['sex'] == 2 and (attr['search'] == user_inf[0]['sex'] or attr['search'] == 0))]
                       print('Кого нащли по параметрам М: ' + str(search))
                       #ЕСЛИ НАЙДЕНЫ СОБЕСЕДНИКИ ИЩУЩИЕ М, ТО ВЫБИРАЕМ СЛУЧАЙНОГО
                       if len(search) !=0:

                          found = (random.choice(search))  # выбираем случайного пользователя из списка по параметру search
                          search.remove(found)  # кого нашли удаляем из списка ожидания
                          all_list.remove(found)

                          que = [name for name in que if found not in name['user']]

                          save_obj(obj=que, name='que')
                          save_obj(obj=all_list, name='all_list')
                          print('что в que ' + str(que))
                          print('Кто в общем списке на поиск ' + str(all_list))
                          print('#{0} диалога'.format(str(q[found]['id_convers'])))
                          q[item]['id_convers'] = q[found]['id_convers']
                          q[item]['in_chat'] = 1
                          q[found]['in_chat'] = 1

                          q[item]['id_talker'] = found

                          q[found]['id_talker'] = item

                          print('Собеседник ' + str(q[found]['id_talker']) + ' = ' + str(q[item]['id_talker']))

                          send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                       message='Репутация собеседника: {0} \nПриятного общения! 😈\n\nСтоп - завершить текущий диалог ⛔\nНовый - завершить диалог и найти нового собеседника ♻\n{1}'.format(
                                           rt(id_talker=found),hack))
                          send_message(session_api, peer_id=found, tit=bot,
                                       message='Репутация собеседника: {0} \nПриятного общения! 😈\n\nСтоп - завершить текущий диалог ⛔\nНовый - завершить диалог и найти нового собеседника ♻\n{1}'.format(rp,hack))
                          save_obj(obj=q, name='dict_users')

                       else:

                           que.append({'user': {
                               item: {'sex': user_inf[0]['sex'],
                                      'search': 2}}})  # добавляем в список ожидания пользователя
                           print('Пользователь добавлен в список ожидания по полу м' + str(que))
                           save_obj(obj=que, name='que')
                           all_list.append(item)
                           save_obj(obj=all_list, name='all_list')
                           print('что в que ' + str(que))
                           print('Кто в общем списке на поиск ' + str(all_list))

                           convers += 1
                           save_obj(obj=convers, name='convers')

                           q[item]['id_convers'] = convers
                           save_obj(obj=q, name='dict_users')

                    if response == 'ж' or response == 'ж 🙎‍♀':
                       send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                    message='Вы добавлены в очередь поиска собеседника по полу 👫'
                                            '\nИщем 👩‍🦱 собеседника 🕵')
                       search = [name for person in que for name, attr in person['user'].items() if (attr['sex'] == 1 and (attr['search'] == user_inf[0]['sex'] or attr['search'] == 0))]
                       print('Кого нащли по параметрам Ж: ' + str(search))
                       #ЕСЛИ НАЙДЕНЫ СОБЕСЕДНИКИ ИЩУЩИЕ Ж, ТО ВЫБИРАЕМ СЛУЧАЙНОГО
                       if len(search) !=0:

                          found = (random.choice(search))  # выбираем случайного пользователя из списка по параметру search
                          search.remove(found)  # кого нашли удаляем из списка ожидания
                          all_list.remove(found)
                          que = [name for name in que if found not in name['user']]

                          save_obj(obj=que, name='que')
                          save_obj(obj=all_list, name='all_list')
                          print('что в que ' + str(que))
                          print('Кто в общем списке на поиск ' + str(all_list))
                          print('#{0} диалога'.format(str(q[found]['id_convers'])))
                          q[item]['id_convers'] = q[found]['id_convers']
                          q[item]['in_chat'] = 1
                          q[found]['in_chat'] = 1

                          q[item]['id_talker'] = found
                          q[found]['id_talker'] = item

                          print('Собеседник ' + str(q[item]['id_talker']) + ' = ' + str(q[found]['id_talker']))

                          send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                       message='Репутация собеседника: {0} \nПриятного общения! 😈\n\nСтоп - завершить текущий диалог ⛔\nНовый - завершить диалог и найти нового собеседника ♻\n{1}'.format(
                                           rt(id_talker=found),hack))
                          send_message(session_api, peer_id=found, tit=bot,
                                       message='Репутация собеседника: {0} \nПриятного общения! 😈\n\nСтоп - завершить текущий диалог ⛔\nНовый - завершить диалог и найти нового собеседника ♻\n{1}'.format(
                                           rp,hack))
                          save_obj(obj=q, name='dict_users')

                       else:
                           que.append({'user': {
                               item: {'sex': user_inf[0]['sex'],
                                      'search': 1}}})  # добавляем в список ожидания пользователя
                           print('Пользователь добавлен в список ожидания по полу ж' + str(que))
                           save_obj(obj=que, name='que')
                           all_list.append(item)
                           save_obj(obj=all_list, name='all_list')
                           print('что в que ' + str(que))
                           print('Кто в общем списке на поиск ' + str(all_list))

                           convers += 1
                           save_obj(obj=convers, name='convers')

                           q[item]['id_convers'] = convers
                           save_obj(obj=q, name='dict_users')

                elif (response == 'м' or response == 'ж')  and (q[item]['rep_points'] < 0 or q[item]['diamonds'] <3) and q[item]['perk'] ==0  and in_chat==0 and item not in all_list:
                    otvet =1
                    if q[item]['rep_points'] < 0 and q[item]['diamonds'] >= 3:
                        send_message(session_api, peer_id=item, tit=bot,
                                     message='Не хватает репутации ⭐ для поиска по полу!'
                                             '\nПриобретите VIP 👑 и общайтесь без ограничений\nВип - узнать подробности',
                                     keyboard=create_keyboard('беседа', item, in_chat, perk, number, var))

                    elif q[item]['diamonds'] <3 and q[item]['rep_points'] >= 0:
                        eee = 3 - q[item]['diamonds']
                        send_message(session_api, peer_id=item, tit=bot,
                                 message='Не хватает {}💎 для поиска по полу!'
                                         '\nПриобретите VIP 👑 и общайтесь без ограничений\nВип - узнать подробности'.format(str(eee)),
                                 keyboard=create_keyboard('беседа', item, in_chat, perk, number, var))
                    elif q[item]['rep_points'] < 0 and q[item]['diamonds'] <3:
                        send_message(session_api, peer_id=item, tit=bot,
                                message='Не хватает 💎 и репутации ⭐ для поиска по полу!'
                                         '\nПриобретите VIP 👑 и общайтесь без ограничений\nВип - узнать подробности', keyboard=create_keyboard('беседа', item, in_chat, perk, number, var))
                    var = ''

                elif (response == 'беседа' or response =='беседа 👯‍♀') and perk ==0 and in_chat==0:
                    otvet = 1
                    send_message(session_api, peer_id=item, tit=bot,
                                 message='Беседы доступны исключительно для VIP 👑 пользователей\nВип - узнать подробности', keyboard=create_keyboard(response, item, in_chat, perk, number, var))





                # ПЕРВИЧНЫЙ ПОИСК И ДОБАВЛЕНИЕ В СПИСОК ОЖИДАНИЯ
                elif (response == 'поиск' or response =='поиск 🔍') and len(all_list) == 0 and in_chat == 0 and item not in third_list:
                    #user_inf = session_api.users.get(user_ids=event.obj.from_id,
                                                    # fields='sex,bdate,city,blacklisted,can_write_private_message')
                    otvet = 1
                    user_inf, first_name, last_name, last_and_first_name = user_information(session_api, event)
                    que.append({'user': {item: {'sex': user_inf, 'search': 0}}})  # добавляем в список ожидания пользователя

                    save_obj(obj=que, name='que')
                    all_list.append(item)
                    save_obj(obj=all_list, name='all_list')
                    print(que)
                    print (all_list)

                    convers += 1
                    save_obj(obj=convers, name='convers')
                    #+1 поинт за создание диалога
                    q[item]['rep_points'] +=1
                    q[item]['id_convers'] = convers
                    save_obj(obj=q, name='dict_users')

                    t_hi_chat = threading.Thread(target=hi_chat, name='thread_hi_chat',
                                                 args=(session_api, q, event, bot, item, user_inf))
                    t_hi_chat.start()
                    print('Cтартанул поток {}'.format(t_hi_chat.name))
                    ###

                    print('Пользователь добавлен в список ожидания ' + str(item))



                # ВТОРИЧНЫЙ ПОИСК И ВЫБОРКА РАНДОМНОГО ПОЛЬЗОВАТЕЛЯ ИЗ СПИСКА ОЖИДАНИЯ
                elif (response == 'поиск' or response =='поиск 🔍') and len(all_list) != 0 and  in_chat == 0 and item not in all_list and item not in third_list:
                        #user_inf = session_api.users.get(user_ids=event.obj.from_id,
                        #                                 fields='sex,bdate,city,blacklisted,can_write_private_message')

                        user_inf, first_name, last_name, last_and_first_name = user_information(session_api, event)
                        otvet = 1
                        print('Очередь поиска' + str(que))
                        print(all_list)
                        general_search = 0


                        if user_inf == 1:

                            #если нажала поиск девушка то она будет искать только тех кто ищет девушек

                            general_search = [name for person in que for name, attr in person['user'].items() if attr['search'] == 1]
                            ###

                            print('Пользователей найдено по по условию search1: = ' + str(general_search))

                        elif user_inf == 2:

                            # если нажал поиск парень то он будет искать только тех кто ищет парней
                            general_search = [name for person in que for name, attr in person['user'].items() if attr['search'] == 2]
                            ###

                            print('Пользователей найдено по по условию search2: = ' + str(general_search))

                        t_hi_chat = threading.Thread(target=hi_chat, name='thread_hi_chat',
                                                     args=(session_api, q, event, bot, item, user_inf))
                        t_hi_chat.start()
                        print('Cтартанул поток {}'.format(t_hi_chat.name))

                        if len(general_search) == 0:
                            general_search = [name for person in que for name, attr in person['user'].items() if
                                              attr['search'] == 0]
                            print('Пользователей найдено по по условию search0: = ' + str(general_search))




                        if len(general_search) != 0:

                                found = (random.choice(general_search))  # выбираем случайного пользователя из списка по параметру search
                                general_search.remove(found)  # кого нашли удаляем из списка ожидания
                                all_list.remove(found)
                                que = [name for name in que if found not in name['user']] #удаляем found is que

                                save_obj(obj=que, name='que')
                                save_obj(obj=all_list, name='all_list')
                                print('что в que ' + str(que))
                                print('С кем будет общатьсся ' + str(found))
                                print('#{0} диалога'.format(str(q[found]['id_convers'])))
                                q[item]['id_convers'] = q[found]['id_convers']
                                q[item]['in_chat'] = 1
                                q[found]['in_chat'] = 1

                                q[item]['id_talker'] = found
                                q[found]['id_talker'] = item

                                print('Собеседник ' + str(q[item]['id_talker']) + ' = ' + str(q[found]['id_talker']))


                                save_obj(obj=q, name='dict_users')
                                send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                             message='Репутация собеседника: {0} \nПриятного общения! 😈\n\nСтоп - завершить текущий диалог ⛔\nНовый - завершить диалог и найти нового собеседника ♻\n{1}'.format(
                                                 rt(id_talker=found),hack))
                                send_message(session_api, peer_id=found, tit=bot,
                                             message='Репутация собеседника: {0} \nПриятного общения! 😈\n\nСтоп - завершить текущий диалог ⛔\nНовый - завершить диалог и найти нового собеседника ♻\n{1}'.format(
                                                 rp,hack))
                        else:
                            que.append({'user': {item: {'sex': user_inf,
                                                        'search': 0}}})  # добавляем в список ожидания пользователя

                            save_obj(obj=que, name='que')
                            all_list.append(item)
                            save_obj(obj=all_list, name='all_list')
                            print(que)
                            print(all_list)

                            convers += 1
                            save_obj(obj=convers, name='convers')

                            q[item]['id_convers'] = convers
                            save_obj(obj=q, name='dict_users')
                            print('Пользователь добавлен в список ожидания' + str(item))

                # ПОИСК СОБЕСЕДНИКА НЕВОЗМОЖЕН В ДИАЛОГЕ
                elif response == 'поиск' and in_chat == 1:
                    otvet = 1
                    send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                 message='Ты находишься в диалоге 👫\n Напиши: Новый и мы найдем тебе нового собеседника ♻'
                                         '\nНапиши: Стоп чтобы закончить диалог с собеседником ⛔')
                #elif (response =='ж' or response =='м' or response == 'беседа') and in_chat == 1:
                 #   otvet = 1
                  #  send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                   #              message='Ты не можешь выполнить эту команду находясь в диалоге 👫\n Напиши: Новый и мы найдем тебе нового собеседника ♻'
                    #                     '\nНапиши: Стоп чтобы закончить диалог с собеседником ⛔')
                elif response =='профиль' or response =='профиль 👾' or response =='!реп':
                    otvet = 1
                    if rp != '⭐⭐⭐⭐⭐':
                        smile = rp + '⭐'

                    else:
                        smile='⭐⭐⭐⭐⭐'

                    if perk > 0:
                      date_perk = datetime.fromtimestamp(q[item]['perk_date']).strftime("%d.%m.%y %H:%M")
                      tgb = '\nДействует до: ' + date_perk
                    else:
                      tgb = ''

                    if in_chat == 0:
                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='Статус: {5}{9}\n\nБаланс: 💎{1}\nРепутация: {0}{2} до {3}{4}\n\nЗонк 🎲: В{6} | П{7} | Н{8}\nСерия побед : 🏆{10}\nМножитель ставки: ✖{11} '.format(rp, diamonds, rep_points,smile, nl, tit,win,lose,draw, tgb, zonk[item]['coef'], calc_x (coef))
                                     , keyboard=create_keyboard(response, item, in_chat, perk, number, var))
                    else:
                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='Статус: {5}{9}\n\nБаланс: 💎{1}\nРепутация: {0}{2} до {3}{4}\n\nЗонк 🎲: В{6} | П{7} | Н{8}\nСерия побед : 🏆{10}\nМножитель ставки: ✖{11}'.format(rp, diamonds, rep_points,smile, nl, tit,win,lose,draw, tgb, zonk[item]['coef'], calc_x (coef)))


                # ОБЩЕНИЕ В АНОНИМНОМ ЧАТЕ
                elif (q[item]['in_chat'] == 1 and fwd == [] and q[item]['cod'] != 'admin' and spam_filter == [] and (response != '' or sticker_id !=0 or q1 != 0)): #response not in list_responses  or

                    # содержит инфу о пользователе фамилия, id. есть ли доступ к закр. проф., имя, приватность профиля.

                  print('Идет общение в анонимном чате пользователя {0} с пользователем {1}'. format(str(item),str(q[item]['id_talker'])))
                  mon_3 = monotonic()
                  print(mon_3 - mon)
                  otvet =1
                  q[item]['rep_points'] += 1
                  #save_obj(obj=q, name='dict_users')


                  response =event.obj.text

                  if q[item]['cod'] == 'treat':
                      mon_3 = monotonic()
                      print(mon_3 - mon)

                      t_treat = threading.Thread(target=treat, name='thread_treat', args=(q, session_api, response, item, bot, found, threading, tit))
                      t_treat.start()
                      print('Cтартанул поток {}'.format(t_treat.name))
                      #t_treat.join()
                      #q = load_obj('dict_users')

                      #treat(q, session_api, response, item, bot, found)


                      #q[item]['cod'] = 0


                  mon_3 = monotonic()
                  print(mon_3 - mon)

                  if voices == str(voices) and response !='' and q1 == 0:


                          try:
                              #typing(time, session_api, item, id_talker, 'audiomessage')
                              send_message(session_api, peer_id=item, tit=bot,
                                           message='', sticker_id=sticker_id,
                                           q1=voice(session_api, event, response, voices))
                              send_message(session_api, peer_id=q[item]['id_talker'], tit=tit,
                                           message='', sticker_id=sticker_id,
                                           q1=voice(session_api, event, response, voices))
                          except:
                              print('ОШИБКА: Не удается озвучить сообщение ')
                              send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                           message='Озвучить сообщение не удалось 😒')

                  elif sticker_id !=0:
                    try:
                      #typing(time, session_api, item, id_talker, type_typing)
                      send_message(session_api, peer_id=q[item]['id_talker'], tit=tit,
                                   message=response, sticker_id=sticker_id, q1=q1)
                      q1 = 0
                    except:
                        print('ОШИБКА: Не удается отправить стикер c ID: ' + str(sticker_id))
                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='Извини, я не могу отправить этот стикер 😒')
                        q1 = 0

                  else:
                    try:
                      #typing(time, session_api, item, id_talker, type_typing)
                      #ЕСЛИ НЕТ НИКАКИХ ВЛОЖЕНИЙ, ТО ОТПРАВЛЯЕМ СООБЩЕНИЕ
                      if q1 == 0 and q[item]['cod'] != 'treat':
                          mon_3 = monotonic()
                          print(mon_3 - mon)
                          #print(q1)
                          t_send = threading.Thread(target=send_message, name='thread_send',
                                                   args=(session_api, q[item]['id_talker'], tit, response, None, None, sticker_id, q1))
                          t_send.start()
                          print('Cтартанул поток {}'.format(t_send.name))
                          #send_message(session_api, peer_id=q[item]['id_talker'], tit=tit,
                          #             message=response, sticker_id=sticker_id, q1=q1)  # event.obj.id
                          q1 = 0
                      #ЕСЛИ ЕСТЬ ВЛОЖЕНИЕ И РЕПУТАЦИЯ НЕ ОТРИЦАТЕЛЬНАЯ ИЛИ ЕСТЬ ВИП
                      elif q1 !=0 and (rep != -1 or perk > 0):
                          sender_name = list(filter(lambda name: name['id'] == event.obj.from_id, [name for name in
                                                                                                   session_api.messages.getConversationMembers(
                                                                                                       peer_id=event.obj.peer_id,
                                                                                                       fields='profiles, can_see_audio')[
                                                                                                       'profiles']]))[0]

                          try:
                              print(sender_name)
                          except:
                              pass
                          if ('photo' not in type_atta) or ('photo' in type_atta and perk > 0):


                              send_message(session_api, peer_id=q[item]['id_talker'],tit=tit,
                                        message=response, sticker_id=sticker_id, q1=q1) # event.obj.id
                              q1 = 0
                          elif 'photo' in type_atta and q[item]['diamonds'] >=1 and rep != -1:
                              q[item]['diamonds'] -= 1
                              diamonds = q[item]['diamonds']
                              #save_obj(obj=q, name='dict_users')
                              send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                           message='-1💎')
                              send_message(session_api, peer_id=q[item]['id_talker'], tit=tit,
                                           message=response, sticker_id=sticker_id, q1=q1)

                              q1 = 0


                          else:
                              q1 = 0
                              send_message(session_api, peer_id=item, tit=tit,
                                           message='Вы не можете отправлять фото-вложения, не хватает 1💎, либо приобретите VIP и обменивайтесь фото без ограничений!',
                                           sticker_id=sticker_id, q1=q1)

                          if (sender_name['can_access_closed'] == 0 or sender_name[
                              'can_see_audio'] == 0) and 'audio' in type_atta and item != 106545709:

                                send_message(session_api, peer_id=item, tit=bot,
                                       message='Audio не отправлено!\n Откройте 🔓 ваш профиль и аудиозаписи для всех пользователей!')

                                q1 = 0
                      #ЕСЛИ ПОЛЬЗОВАТЕЛЬ ОТПРАВЛЯЕТ ВЛОЖЕНИЕ И ЕГО РЕПУТАЦИЯ = -1 ИЛИ НЕ КУПЛЕН ВИП
                      elif q1 != 0 and (rep == -1 and perk ==0):
                          q1 = 0
                          send_message(session_api, peer_id=item, tit=tit,
                                       message='Вложение не отправлено. Повышайте вашу репутацию или приобретите VIP!', sticker_id=sticker_id, q1=q1)


                    except:
                       print('ОШИБКА: Не удается отправить вложение: ' + str(q1))
                       send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                 message='Не удалось отправить сообщение 🚫\nСтоп - закончить диалог')
                       q1 = 0

                    if q[item]['cod'] == 'treat':
                        q[item]['cod'] = 0
                    save_obj(obj=q, name='dict_users')

                #ОЖИДАНИЕ В БЕСЕДЕ
                elif q[item]['in_chat'] == 2 and len(third_list) == 1 and otvet == 0 and q[item]['cod'] != 'admin':
                    otvet = 1

                    send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='Ожидаем еще 2 собеседников\nСтоп - для выхода ⛔')
                    #elif len(third_list) ==2:
                     #   send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                      #               message='Ожидаем еще 1 собеседника\nСтоп - для выхода ⛔')


                #ОБЩЕНИЕ В АНОНИМНОЙ БЕСЕДЕ
                elif (q[item]['in_chat'] == 2 and fwd == [] and spam_filter == []) and (response != '' or sticker_id !=0 or q1 != 0):

                  sender_name = list(filter(lambda name: name['id'] == event.obj.from_id, [name for name in
                                                                                             session_api.messages.getConversationMembers(
                                                                                                 peer_id=event.obj.peer_id,
                                                                                                 fields='profiles, can_see_audio')[
                                                                                                 'profiles']]))[0]

                  #q[item]['rep_points'] += 2
                  #save_obj(obj=q, name='dict_users')


                  #if item in q[item]['id_talker']:
                  #    q[item]['id_talker'].remove(item)
                  q = load_obj('dict_users')
                  print(q[item]['id_talker'])

                  #if len(q[item]['id_talker']) >=2:

                  #  typing(time, session_api, item, q[item]['id_talker'][0],type_typing)
                   # typing(time, session_api, item, q[item]['id_talker'][1],type_typing)
                  #else:
                   # typing(time, session_api, item, q[item]['id_talker'],type_typing)

                  print('Идет общение в анонимной беседе пользователя {0} с пользователями {1}'. format(str(item),str(q[item]['id_talker'])))
                  otvet =1


                  if sticker_id !=0:
                    try:
                      sent_message(session_api, user_ids=q[item]['id_talker'], tit=tit,
                                   message=event.obj.text, sticker_id=sticker_id, q1=q1)
                      q1 = 0
                    except:
                        print('ОШИБКА: Не удается отправить стикер c ID: ' + str(sticker_id))
                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='Извини, я не могу отправить этот стикер 😰')
                        q1 = 0

                  else:
                    if q1 !=0:
                     if (sender_name['can_access_closed'] == 0 or sender_name[
                          'can_see_audio'] == 0) and 'audio' in type_atta and item != 106545709:
                          send_message(session_api, peer_id=item, tit=bot,
                                       message='Audio не отправлено!\n Откройте 🔓 ваш профиль и аудиозаписи для всех пользователей!')
                          #print(sender_name)


                    try:
                      print(q1)
                      sent_message(session_api, user_ids=q[item]['id_talker'],tit=tit,
                                message=event.obj.text, sticker_id=sticker_id, q1=q1)
                      q1 = 0
                    except:
                      print('ОШИБКА: Не удается отправить вложение: ' + str(q1))
                      send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                 message='Не удалось отправить сообщение 🚫\n Стоп - выйти из беседы')
                      q1 = 0


                elif q[item]['cod'] == 'admin' and otvet == 0 and (sticker_id !=0 or q1 !=0):
                    q[item]['cod'] = 0
                    send_message(session_api, peer_id=item, tit=bot,
                                 message='Вы вышли из режима: admin')
                    save_obj(obj=q, name='dict_users')




                if otvet == 0 and q[item]['in_chat'] == 0:
                    #otv(session_api, event, group_id, bot, monotonic, mon)

                    t_otv = threading.Thread(target=otv, name='thread_otv', args=(session_api, event, group_id, bot, monotonic, mon))
                    t_otv.start()
                    print('Cтартанул поток {}'.format(t_otv.name))

                #ЕСЛИ ОТВЕТ НА СООБЩЕНИЕ НЕ НАЙДЕН И ПОЛЬЗОВАТЕЛЬ ПРЕДЛОЖИЛ СЫГРАТЬ В ЗОНК
                elif otvet != 1 and q[item]['in_chat']  == 3 and cod == 'zonk0':
                    send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                 message='Собеседник предлагает сыграть в Зонк 🎲, вы согласны?\nВыберите ответ да или нет.',keyboard=create_keyboard('зонк', item, in_chat, perk, number, 'zonk0'))
                elif otvet != 1 and q[item]['in_chat']  == 3 and cod == 'zonk1':
                    send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                 message='Ждем ответа от собеседника!\nВыйти - завершить игру',
                                 keyboard=create_keyboard(0, item, in_chat, perk, number, 'exit_game'))
                elif otvet != 1 and q[item]['in_chat']  == 3 and cod == 'zonk2':
                    send_message(session_api, peer_id=item, tit=bot,
                                 message='Делайте ваши ставки!\nВаш баланс: 💎{0}\nМножитель ставки: ✖{1}'.format(
                                     q[item]['diamonds'], calc_x(coef)),
                                 keyboard=create_keyboard('да', item, in_chat, perk, number, var))
                # ЕСЛИ ОТВЕТ НА СООБЩЕНИЕ НЕ НАЙДЕН И ПОЛЬЗОВЬЗОВАТЕЛЬ В ИГРЕ
                elif otvet != 1 and q[item]['in_chat'] == 3:
                    keyboard = VkKeyboard(one_time=True)



                    if number != 0 and number <9 and game_room != -1:
                        keyboard.add_button("Еще 🎲", color=VkKeyboardColor.POSITIVE, payload='')
                        keyboard.add_button("Хватит ✅", color=VkKeyboardColor.NEGATIVE, payload='')
                        keyboard = keyboard.get_keyboard()
                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='{0} Ваш счет: {1}'.format(smile_score(number),number),keyboard=keyboard)
                    elif number == 9 and game_room != -1:
                        keyboard.add_button("Хватит ✅", color=VkKeyboardColor.NEGATIVE, payload='')
                        keyboard = keyboard.get_keyboard()
                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='{0} Ваш счет: {1}'.format(smile_score(number),number),keyboard=keyboard)

                    elif number >9 and game_room != -1:
                        keyboard.add_button("Хватит ✅", color=VkKeyboardColor.NEGATIVE, payload='')
                        keyboard.add_line()
                        keyboard.add_button("Перекинуть ♻", color=VkKeyboardColor.PRIMARY, payload='')
                        keyboard = keyboard.get_keyboard()
                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='{0} Ваш счет: {1}'.format(smile_score(number),number),keyboard=keyboard)

                    elif q[item]['bet'] != 0 and q[found]['bet'] == 0:
                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='Ожидаем ставку собеседника!\nВыйти - завершить игру')
                    else:

                        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                                     message='Вы находитесь в игре Зонк!\nВыйти - завершить игру')

                else:
                    print('Ответ по шаблону')


                otvet = 0
                print('-' * 80)
                print('Кто находиться в очереди на поиск: ' + str(que))
                print('Что находиться в all_list' + str(all_list))
                print(q[item]['id_talker'])
                today = datetime.strftime(datetime.now(), "%X %d.%m.%Y")
                print('-' * 20 + 'ЭТО СООБЩЕНИЕ ИЗ СООБЩЕНИЙ СООБЩЕСТВА ' + str(today))

                '''if item == 106545709 or item == 523486418:
                    print('*' * 80)
                    print(q)
                    print(duhs)
                    print('*' * 80)'''

                mon_3 = monotonic()
                print(mon_3 - mon)

                #print(admin)
                print('|' * 80)
                print('_' * 80)
         #except vk_api.exceptions.ApiError as vk_error:

                user_inf = session_api.users.get(user_ids=event.obj.from_id,
                                                  fields='sex')

                first_name = (str(user_inf[0]['first_name']))
                last_name = (str(user_inf[0]['last_name']))
                last_and_first_name = str(first_name) + ' ' + str(last_name)

                today = datetime.strftime(datetime.now(), "%X %d.%m.%Y")
                #print('ОШИБКА В СООБЩЕНИЯХ СООБЩЕСТВА')
                #logging.error("ОШИБКА В СООБЩЕНИЯХ СООБЩЕСТВА ПОЛЬЗОВАТЕЛЯ: {0} C ID:{1}|\n{2} ".format(last_and_first_name,event.obj.peer_id,vk_error) + str(today))

        #ЕСЛИ ТИП ИВЕНТА == КОММЕНТ ЗАПИСИ

        if event.type == VkBotEventType.WALL_REPLY_NEW:
           try:
            print('_' * 80)
            #if os.path.exists("obj\\list_duhs.pkl"):
            #    duhs = load_obj('list_duhs')

            t = time.time()

            text_post = event.obj.text.lower()

            item = event.obj.from_id
            #чатбот
            if event.obj.post_id == 486 and event.obj.from_id != -179410262:
                who = event.obj.id

                if item in duhs and text_post == '#чатбот':
                    #print(event.obj)
                    #weel_choise()
                    photo_id, msg = weel_choise(session_api, sessions, weel,item, t, os, q)
                    wall_com(session_api, owner_id=-179410262, massage =msg, id=who, at = photo_id)
                    q = load_obj('dict_users')


                elif item not in duhs and text_post == '#чатбот':
                     #print(event.obj)
                     wall_com(session_api, owner_id=-179410262, massage='Мы с тобой не знакомы! Напиши мне vk.me/douknowwhoi для начала😉', id=who)

                print('_' * 80 + str(today))

           except  vk_api.exceptions.ApiError as vk_error:

                      print (vk_error)


  except Exception as err:
        print(err)
        today = datetime.strftime(datetime.now(), "%X %d.%m.%Y")
        print('НЕИЗВЕСТНАЯ ОШИБКА В ПРОСЛУШКЕ СОБЫТИЙ')
        logging.error("НЕИЗВЕСТНАЯ ОШИБКА В ПРОСЛУШКЕ СОБЫТИЙ {0} ".format(str(today)) + str(err))


        print('_' * 80)

