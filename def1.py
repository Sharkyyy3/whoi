from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from datetime import date
import random
import pickle
import json
import requests
import vk_api
import time
from multiprocessing import Process

print(__name__)


def chk(a, b):
    return a % b and 0 or 1

def get_byid (sessions, message_ids, group_id = 177625749, preview_length = None, fields= None, extended = None ):
    sessions.messages.getById(message_ids=message_ids, preview_length=preview_length, extended=extended, fields=fields,group_id=group_id )

def sent_message(session_api, user_ids,  tit=None, message=None, keyboard=None, payload=None, sticker_id=None, q1=None):
    session_api.messages.send(user_ids=user_ids, title=tit, message=message, random_id=random.randint(-2147483648, +2147483648),
                              keyboard=keyboard, payload=payload, sticker_id=sticker_id, attachment=q1)

def sending_message(session_api, user_ids,  tit=None, message=None, sticker_id=None, q1=None):
    session_api.messages.send(user_ids=user_ids, title=tit, message=message, random_id=random.randint(-2147483648, +2147483648),
                               sticker_id=sticker_id, attachment=q1)








def send_message(sessions, peer_id, tit=None, message=None, keyboard=None, payload=None, sticker_id=None, q1=None, dont_parse_links=1):
    sessions.messages.send(peer_id=peer_id, title=tit, message=message, random_id=random.randint(-2147483648, +2147483648),
                              keyboard=keyboard, payload=payload, sticker_id=sticker_id, attachment=q1, dont_parse_links=dont_parse_links)



def typing(time,session_api, user_id, id_talker,type_typing):
    session_api.messages.setActivity(user_id=user_id, type=type_typing,
                                                          peer_id=id_talker,
                                                          group_id=179410262)
    time.sleep(1)



def create_keyboard(response, item, in_chat, perk, number, var):
   #try:

    keyboard = VkKeyboard(one_time=True)


    if (response == 'стоп' and in_chat == 1) or response == 'новый':

       keyboard.add_button("👍🏻", color=VkKeyboardColor.POSITIVE, payload='')
       keyboard.add_button("👎🏻", color=VkKeyboardColor.NEGATIVE, payload='')
    elif (response == 'зонк 🎲' or response == 'зонк') and in_chat == 1 or (var ==  'zonk0'):
        keyboard.add_button("Да 👍🏻", color=VkKeyboardColor.POSITIVE, payload='')
        keyboard.add_button("Нет 👎🏻", color=VkKeyboardColor.NEGATIVE, payload='')
    elif (response == 'да 👍🏻' or response == 'да') and in_chat ==3:

        c_5, c_10, c_15, c_30 = calc_color_zonk (item)
        keyboard.add_button("5💎", color=c_5, payload='')
        keyboard.add_button("10💎", color=c_10, payload='')
        keyboard.add_button("15💎", color=c_15, payload='')
        keyboard.add_button("30💎", color=c_30, payload='')
        keyboard.add_line()
        keyboard.add_button("Выйти", color=VkKeyboardColor.NEGATIVE, payload='')

    if response == 'ктоя?' and in_chat == 1:
        keyboard.add_button("Да", color=VkKeyboardColor.POSITIVE, payload='')
        keyboard.add_button("Нет", color=VkKeyboardColor.NEGATIVE, payload='')

    elif response == 'helper' and var == 'helper':
        keyboard.add_button("Поиск 🔍", color=VkKeyboardColor.POSITIVE, payload='')
        keyboard.add_line()
        keyboard.add_button("Меню", color=VkKeyboardColor.DEFAULT, payload='')



    elif response == 'ктоя?' and in_chat == 0:
        keyboard.add_button("Да", color=VkKeyboardColor.POSITIVE, payload='')
        keyboard.add_button("Нет", color=VkKeyboardColor.NEGATIVE, payload='')


    if number > 9 and (response == 'еще' or response == 'еще 🎲') and in_chat == 3:
        keyboard.add_button("Хватит ✅", color=VkKeyboardColor.NEGATIVE, payload='')
        keyboard.add_line()
        keyboard.add_button("Перекинуть ♻", color=VkKeyboardColor.PRIMARY, payload='')

    if number == 9 and (response == 'еще' or response == 'еще 🎲') and in_chat == 3:
        keyboard.add_button("Хватит ✅", color=VkKeyboardColor.NEGATIVE, payload='')

    if var == 'exit_game':
        keyboard.add_button("Выйти", color=VkKeyboardColor.NEGATIVE, payload='')



    elif number < 9 and (response == 'еще' or response == 'еще 🎲') and in_chat == 3:
        keyboard.add_button("Еще 🎲", color=VkKeyboardColor.POSITIVE, payload='')
        keyboard.add_button("Хватит ✅", color=VkKeyboardColor.NEGATIVE, payload='')


    elif ((response == '5💎' or response == '10💎' or response == '15💎' or response == '30💎')  and in_chat == 3) or var=='except':
        keyboard.add_button("Еще 🎲", color=VkKeyboardColor.POSITIVE, payload='')
        keyboard.add_button("Хватит ✅", color=VkKeyboardColor.NEGATIVE, payload='')


    elif (response == 'выйти') and in_chat == 3:
        return keyboard.get_empty_keyboard()
    elif (response == 'перекинуть' or response == 'перекинуть ♻') and in_chat == 3:
        keyboard.add_button("Хватит ✅", color=VkKeyboardColor.NEGATIVE, payload='')
    elif (response == 'выбрать голос' or response == 'выбрать голос 🗣' or response == "выбрать другой") and  in_chat == 1 and var == 0:
        keyboard.add_button("NRX", color=VkKeyboardColor.POSITIVE, payload='')
        keyboard.add_button("Борис", color=VkKeyboardColor.POSITIVE, payload='')
        keyboard.add_button("Оксана", color=VkKeyboardColor.POSITIVE, payload='')
        keyboard.add_button("Джейн", color=VkKeyboardColor.POSITIVE, payload='')
        keyboard.add_line()
        keyboard.add_button("Колян", color=VkKeyboardColor.POSITIVE, payload='')
        keyboard.add_button("Артем", color=VkKeyboardColor.POSITIVE, payload='')
        keyboard.add_button("Таня", color=VkKeyboardColor.POSITIVE, payload='')
        keyboard.add_button("Элис", color=VkKeyboardColor.POSITIVE, payload='')
        keyboard.add_line()
        keyboard.add_button("Назад", color=VkKeyboardColor.DEFAULT, payload='')

    elif (response == 'выбрать голос' or response == 'выбрать голос 🗣' or response == "выбрать другой") and in_chat == 1 and var != 0:
        keyboard.add_button("NRX", color=VkKeyboardColor.POSITIVE, payload='')
        keyboard.add_button("Борис", color=VkKeyboardColor.POSITIVE, payload='')
        keyboard.add_button("Оксана", color=VkKeyboardColor.POSITIVE, payload='')
        keyboard.add_button("Джейн", color=VkKeyboardColor.POSITIVE, payload='')
        keyboard.add_line()
        keyboard.add_button("Колян", color=VkKeyboardColor.POSITIVE, payload='')
        keyboard.add_button("Артем", color=VkKeyboardColor.POSITIVE, payload='')
        keyboard.add_button("Таня", color=VkKeyboardColor.POSITIVE, payload='')
        keyboard.add_button("Элис", color=VkKeyboardColor.POSITIVE, payload='')
        keyboard.add_line()
        keyboard.add_button("Убрать голос", color=VkKeyboardColor.NEGATIVE, payload='')
        keyboard.add_button("Назад", color=VkKeyboardColor.DEFAULT, payload='')

    elif var == 'voices' and in_chat == 1:
        keyboard.add_button("Выбрать другой", color=VkKeyboardColor.DEFAULT, payload='')
        keyboard.add_button("Убрать голос", color=VkKeyboardColor.NEGATIVE, payload='')


    elif perk == 0:
        if (((response == '👍🏻' or response == '👎🏻') or ((response == 'меню' or response == 'начать' or response == 'стоп' or response == 'назад') and in_chat != 1)) and var == 'negativ' and var != 'spam'):
            keyboard.add_button("Поиск 🔍", color=VkKeyboardColor.POSITIVE, payload='')
            keyboard.add_line()
            keyboard.add_button("М", color=VkKeyboardColor.NEGATIVE, payload='')
            keyboard.add_button("Беседа 👯‍♀", color=VkKeyboardColor.NEGATIVE, payload='')
            keyboard.add_button("Ж", color=VkKeyboardColor.NEGATIVE, payload='')
            keyboard.add_line()
            keyboard.add_button("Вип 👑", color=VkKeyboardColor.PRIMARY, payload='')
            keyboard.add_button("Профиль 👾", color=VkKeyboardColor.PRIMARY, payload='')
        elif (response =='👍🏻' or response =='👎🏻')  or ((response == 'меню' or response == 'начать' or response =='стоп' or response == 'назад') and in_chat !=1 and var != 'spam'):
            keyboard.add_button("Поиск 🔍", color=VkKeyboardColor.POSITIVE, payload='')
            keyboard.add_line()
            keyboard.add_button("М", color=VkKeyboardColor.DEFAULT, payload='')
            keyboard.add_button("Беседа 👯‍♀", color=VkKeyboardColor.NEGATIVE, payload='')
            keyboard.add_button("Ж", color=VkKeyboardColor.DEFAULT, payload='')
            keyboard.add_line()
            keyboard.add_button("Вип 👑", color=VkKeyboardColor.PRIMARY, payload='')
            keyboard.add_button("Профиль 👾", color=VkKeyboardColor.PRIMARY, payload='')

        elif (response == 'меню' or response == 'назад') and in_chat == 1:
            c_treat, c_city, c_age, c_photo, c_link = calc_y(item, 'keyboard')
            keyboard.add_button("City 🌆", color=VkKeyboardColor.NEGATIVE, payload='')
            keyboard.add_button("Age 👶🏻", color=VkKeyboardColor.NEGATIVE, payload='')
            keyboard.add_button("Photo 📸", color=VkKeyboardColor.NEGATIVE, payload='')
            keyboard.add_button("Link 📎", color=VkKeyboardColor.NEGATIVE, payload='')
            keyboard.add_line()
            keyboard.add_button("Выбрать голос 🗣", color=VkKeyboardColor.NEGATIVE, payload='')
            keyboard.add_line()
            keyboard.add_button("Зонк 🎲", color=VkKeyboardColor.PRIMARY, payload='')
            keyboard.add_button("Угостить 🍬", color=c_treat, payload='')


        elif (response == 'беседа' or response == 'беседа 👯‍♀') and in_chat == 0:
            keyboard.add_button("Вип 👑", color=VkKeyboardColor.PRIMARY, payload='')
            keyboard.add_button("Назад", color=VkKeyboardColor.DEFAULT, payload='')



    elif perk > 0:

        if (response =='👍🏻' or response =='👎🏻')  or ((response == 'меню' or response == 'начать' or response =='стоп' or response == 'назад') and in_chat !=1 and var != 'spam'):
            keyboard.add_button("Поиск 🔍", color=VkKeyboardColor.POSITIVE, payload='')
            keyboard.add_line()
            keyboard.add_button("М", color=VkKeyboardColor.POSITIVE, payload='')
            keyboard.add_button("Беседа 👯‍♀", color=VkKeyboardColor.POSITIVE, payload='')
            keyboard.add_button("Ж", color=VkKeyboardColor.POSITIVE, payload='')
            keyboard.add_line()
            keyboard.add_button("Вип 👑", color=VkKeyboardColor.PRIMARY, payload='')
            keyboard.add_button("Профиль 👾", color=VkKeyboardColor.PRIMARY, payload='')

        elif (response == 'меню' or response == 'назад') and in_chat == 1:

            c_treat, c_city, c_age, c_photo, c_link =calc_y(item,'keyboard')

            keyboard.add_button("City 🌆", color=c_city, payload='')
            keyboard.add_button("Age 👶🏻", color=c_age, payload='')
            keyboard.add_button("Photo 📸", color=c_photo, payload='')
            keyboard.add_button("Link 📎", color=c_link, payload='')
            keyboard.add_line()
            keyboard.add_button("Выбрать голос 🗣", color=VkKeyboardColor.POSITIVE, payload='')
            keyboard.add_line()
            keyboard.add_button("Зонк 🎲", color=VkKeyboardColor.PRIMARY, payload='')
            keyboard.add_button("Угостить 🍬", color=c_treat, payload='')




    if (response == 'вип' or response == 'вип 👑') and in_chat !=0:
        keyboard.add_button("!код", color=VkKeyboardColor.POSITIVE, payload='')

    elif (response =='профиль' or response =='профиль 👾' or response =='!реп') and in_chat ==0:
        keyboard.add_button("Назад", color=VkKeyboardColor.DEFAULT, payload='')



    elif (response == '!админ' or response =='!назад') and var == 1:
        keyboard.add_button("!вип+", color=VkKeyboardColor.POSITIVE, payload='')
        keyboard.add_button("!вип-", color=VkKeyboardColor.NEGATIVE, payload='')
        keyboard.add_line()
        keyboard.add_button("!алмазы+", color=VkKeyboardColor.POSITIVE, payload='')
        keyboard.add_button("!алмазы-", color=VkKeyboardColor.NEGATIVE, payload='')
        keyboard.add_line()
        keyboard.add_button("!реп+", color=VkKeyboardColor.POSITIVE, payload='')
        keyboard.add_button("!реп-", color=VkKeyboardColor.NEGATIVE, payload='')
        keyboard.add_line()
        keyboard.add_button("!стата", color=VkKeyboardColor.POSITIVE, payload='')
        keyboard.add_button("!рассылка", color=VkKeyboardColor.PRIMARY, payload='')
        keyboard.add_button("!офф", color=VkKeyboardColor.NEGATIVE, payload='')
        keyboard.add_button("!удалить", color=VkKeyboardColor.NEGATIVE, payload='')
        keyboard.add_line()
        keyboard.add_button("!очистить очередь", color=VkKeyboardColor.NEGATIVE, payload='')
        keyboard.add_line()
        keyboard.add_button("меню", color=VkKeyboardColor.DEFAULT, payload='')
        keyboard.add_button("♻", color=VkKeyboardColor.DEFAULT, payload='')

    elif (response == '!админ' or response =='!назад') and var == 0:
        keyboard.add_button("!вип+", color=VkKeyboardColor.POSITIVE, payload='')
        keyboard.add_button("!вип-", color=VkKeyboardColor.NEGATIVE, payload='')
        keyboard.add_line()
        keyboard.add_button("!алмазы+", color=VkKeyboardColor.POSITIVE, payload='')
        keyboard.add_button("!алмазы-", color=VkKeyboardColor.NEGATIVE, payload='')
        keyboard.add_line()
        keyboard.add_button("!реп+", color=VkKeyboardColor.POSITIVE, payload='')
        keyboard.add_button("!реп-", color=VkKeyboardColor.NEGATIVE, payload='')
        keyboard.add_line()
        keyboard.add_button("!стата", color=VkKeyboardColor.POSITIVE, payload='')
        keyboard.add_button("!рассылка", color=VkKeyboardColor.PRIMARY, payload='')
        keyboard.add_button("!он", color=VkKeyboardColor.POSITIVE, payload='')
        keyboard.add_button("!удалить", color=VkKeyboardColor.NEGATIVE, payload='')
        keyboard.add_line()
        keyboard.add_button("меню", color=VkKeyboardColor.DEFAULT, payload='')

    elif response == '!он':
        keyboard.add_button("Да", color=VkKeyboardColor.POSITIVE, payload='')
        keyboard.add_button("Нет", color=VkKeyboardColor.NEGATIVE, payload='')


    elif var == 'id':
        keyboard.add_button("106545709", color=VkKeyboardColor.DEFAULT, payload='')
        keyboard.add_button("523486418", color=VkKeyboardColor.DEFAULT, payload='')
        keyboard.add_button("425268753", color=VkKeyboardColor.DEFAULT, payload='')






    elif (response == 'вип' or response == 'вип 👑') and in_chat ==0:
        keyboard.add_button("!код", color=VkKeyboardColor.POSITIVE, payload='')
        keyboard.add_button("Назад", color=VkKeyboardColor.DEFAULT, payload='')

    elif response == '!стата' or response =="⬅" or response =="➡" or var == 'stata2':
        keyboard.add_button("!найти", color=VkKeyboardColor.DEFAULT, payload='')
        keyboard.add_line()
        keyboard.add_button("⬅", color=VkKeyboardColor.DEFAULT, payload='')
        keyboard.add_button("➡", color=VkKeyboardColor.DEFAULT, payload='')
        keyboard.add_line()
        keyboard.add_button("!назад", color=VkKeyboardColor.DEFAULT, payload='')

    elif var == 'spam':
        keyboard.add_button("в меню", color=VkKeyboardColor.DEFAULT, payload='')
        keyboard.add_button("в чате", color=VkKeyboardColor.DEFAULT, payload='')
        keyboard.add_button("в беседе", color=VkKeyboardColor.DEFAULT, payload='')
        keyboard.add_button("в зонке", color=VkKeyboardColor.DEFAULT, payload='')
        keyboard.add_line()
        keyboard.add_button("пропавшим", color=VkKeyboardColor.DEFAULT, payload='')
        keyboard.add_button("випам", color=VkKeyboardColor.PRIMARY, payload='')
        keyboard.add_button("без вип", color=VkKeyboardColor.DEFAULT, payload='')
        keyboard.add_line()
        keyboard.add_button("всем", color=VkKeyboardColor.POSITIVE, payload='')

    elif var == 'er' and in_chat !=3:
        keyboard.add_button("Меню", color=VkKeyboardColor.DEFAULT, payload='')
    elif var == 'er' and in_chat == 3:
        return keyboard.get_empty_keyboard()

    elif (response == 'угостить 🍬' or response == 'угостить') and in_chat ==1:
        keyboard.add_button("🍺", color=VkKeyboardColor.POSITIVE, payload='')
        keyboard.add_button("🍸", color=VkKeyboardColor.POSITIVE, payload='')
        keyboard.add_button("🍹", color=VkKeyboardColor.POSITIVE, payload='')
        keyboard.add_button("🥃", color=VkKeyboardColor.POSITIVE, payload='')
        keyboard.add_line()
        keyboard.add_button("🍼", color=VkKeyboardColor.NEGATIVE, payload='')
        keyboard.add_button("💩", color=VkKeyboardColor.NEGATIVE, payload='')






    elif response == 'закрыть':
        #print('закрываем клаву')
        return keyboard.get_empty_keyboard()

    keyboard = keyboard.get_keyboard()
    return keyboard
   #except:
       #keyboard = VkKeyboard(one_time=True)
       #return keyboard.get_empty_keyboard()

#таймаут
def mon_choise(q,session_api, bot, mon, item):

    #q = load_obj('dict_users')
    found = q[item]['id_talker']
    keyboard = VkKeyboard(one_time=True)

    mon_item = mon - q[item]['timeout']
    mon_talker = mon - q[found]['timeout']

    #ИСКЛЮЧАЮТ МЕНЯ
    if (mon_item > 2000 and mon_talker <2000) or mon_item <= 0:

            send_message(session_api, peer_id=item, tit=bot,
                         message='Вы были исключены за бездействие!\nИгра окончена!😕',
                         keyboard=keyboard.get_empty_keyboard())
            send_message(session_api, peer_id=found, tit=bot,
                         message='Ваш собеседник исключен за бездействие!😕\nИгра окончена!😕',
                         keyboard=keyboard.get_empty_keyboard())
            if q[found]['bet'] != 0:
                q[found]['diamonds'] += q[found]['bet']

                send_message(session_api, peer_id=found, tit=bot,
                             message='Ваша ставка аннулирована\n+{}💎'.format(
                                 q[found]['bet']))

            res = 1
            save_obj(obj=q, name='dict_users')

    #ИСКЛЮЧАЮТ МОЕГО СОБЕСЕДНИКА
    elif (mon_talker > 2000 and mon_item < 2000)  or mon_talker <= 0:

            send_message(session_api, peer_id=item, tit=bot,
                         message='Ваш собеседник исключен за бездействие!😕\nИгра окончена!😕',
                         keyboard=keyboard.get_empty_keyboard())
            send_message(session_api, peer_id=found, tit=bot,
                         message='Вы были исключены за бездействие!\nИгра окончена!😕',
                         keyboard=keyboard.get_empty_keyboard())
            if q[item]['bet'] != 0:
                q[item]['diamonds'] += q[item]['bet']

                send_message(session_api, peer_id=item, tit=bot,
                             message='Ваша ставка аннулирована\n+{}💎'.format(q[item]['bet']))

            res = 2
            save_obj(obj=q, name='dict_users')
    #ИСКЛЮЧАЕТ ОБОИХ
    elif (mon_item > 2000 and mon_talker > 2000) or (mon_item <= 0 and mon_talker <= 0):

            send_message(session_api, peer_id=item, tit=bot,
                         message='Вы были исключены за бездействие!\nИгра окончена!😕',
                         keyboard=keyboard.get_empty_keyboard())
            send_message(session_api, peer_id=found, tit=bot,
                         message='Вы были исключены за бездействие!\nИгра окончена!😕',
                         keyboard=keyboard.get_empty_keyboard())

            res = 3
            save_obj(obj=q, name='dict_users')
    else:
            res = 0

    if res != 0:
            q[item]['game_room'] = 0
            q[item]['bet'] = 0
            q[item]['number'] = 0
            q[item]['in_chat'] = 1

            q[found]['game_room'] = 0
            q[found]['bet'] = 0
            q[found]['number'] = 0
            q[found]['in_chat'] = 1

            q[found]['timeout'] = 0
            q[item]['timeout'] = 0

            q[item]['cod'] = 0
            q[found]['cod'] = 0
            save_obj(obj=q, name='dict_users')



def calc_color_zonk (item):
    q = load_obj('dict_users')
    if q[item]['diamonds'] >=5:
       color_5 = VkKeyboardColor.DEFAULT
    else:
        color_5 = VkKeyboardColor.NEGATIVE

    if q[item]['diamonds'] >=10:
       color_10 = VkKeyboardColor.DEFAULT
    else:
       color_10 = VkKeyboardColor.NEGATIVE

    if q[item]['diamonds'] >=15:
       color_15 = VkKeyboardColor.DEFAULT
    else:
       color_15 = VkKeyboardColor.NEGATIVE

    if q[item]['diamonds'] >=30:
       color_30 = VkKeyboardColor.DEFAULT
    else:
       color_30 = VkKeyboardColor.NEGATIVE
    return color_5, color_10, color_15, color_30

def calc_y (item,xxx):
    q = load_obj('dict_users')
    if q[item]['diamonds'] >= 1:
        color_treat = VkKeyboardColor.DEFAULT
        price_treat = '-1💎'
    else:
        color_treat = VkKeyboardColor.NEGATIVE
        price_treat = '🚫'

    if q[item]['diamonds'] >=2:
       color_city = VkKeyboardColor.DEFAULT
       price_city = '-2💎'
    else:
        color_city = VkKeyboardColor.NEGATIVE
        price_city = '🚫'
    if q[item]['diamonds'] >=5:
       color_age = VkKeyboardColor.DEFAULT
       price_age = '-5💎'
    else:
       color_age = VkKeyboardColor.NEGATIVE
       price_age = '🚫'
    if q[item]['diamonds'] >= 10:
       color_photo = VkKeyboardColor.DEFAULT
       price_photo = '-10💎'
    else:
       color_photo = VkKeyboardColor.NEGATIVE
       price_photo = '🚫'
    if q[item]['diamonds'] >= 50:
       color_link = VkKeyboardColor.DEFAULT
       price_link = '-50💎'

    else:
       color_link = VkKeyboardColor.NEGATIVE
       price_link = '🚫'


    if xxx == 'keyboard':
        return color_treat, color_city, color_age, color_photo, color_link
    if xxx == 'chat':
        return price_treat, price_city, price_age, price_photo, price_link




def time_out_mes (mon):
    q = load_obj('dict_users')
    #mon_item = mon - q[item]['timeout']
    #zxc = [i for i in q if q[i]['perk'] > 0]
    for i in q:
        mon_items=mon - q[i]['timeout']
        out= 120 - int(mon_items)
        #print(out)

def save_obj(obj, name ):
    try:
        with open('obj/'+ name + '.pkl', 'wb') as f:
            pickle.dump(obj, f, 0)
    except EOFError as e:
        print(e)

def load_obj(name ):
    try:
        with open('obj/' + name + '.pkl', 'rb') as f:
            return pickle.load(f)
    except EOFError as e:
        print(e)
#скинованные кубики или нет
def choices_photo (choices = None,id_talker =None,item = None):
    photo_id =''
    q = load_obj('dict_users')
    if q[id_talker]['perk'] > 0 or q[item]['perk'] > 0:
        perk =1
    else:
        perk = 0
    if perk == 0:
        if choices == 1:
            photo_id = 'photo-179410262_456239245'
        elif choices == 2:
            photo_id = 'photo-179410262_456239246'
        elif choices == 3:
            photo_id = 'photo-179410262_456239247'
        elif choices == 4:
            photo_id = 'photo-179410262_456239248'
        elif choices == 5:
            photo_id = 'photo-179410262_456239249'
        elif choices == 6:
            photo_id = 'photo-179410262_456239250'
    else:
        if choices == 1:
            photo_id = 'photo-179410262_456239239'
        elif choices == 2:
            photo_id = 'photo-179410262_456239240'
        elif choices == 3:
            photo_id = 'photo-179410262_456239241'
        elif choices == 4:
            photo_id = 'photo-179410262_456239242'
        elif choices == 5:
            photo_id = 'photo-179410262_456239243'
        elif choices == 6:
            photo_id = 'photo-179410262_456239244'

    return photo_id

def yers(age):
    yers = ''
    if age <= 3 or age ==21 or age ==31 or age ==41 or age ==51:
        yers = 'год'
    elif (age >= 5 and age <= 20) or (age >=25 and age <= 30) or (age >=35 and age <= 40) or (age >=45 and age <= 50):
        yers = 'лет'
    elif age == 4 or (age >=22 and age <=24) or (age >=32 and age <=34) or (age >=42 and age <=44):
        yers = 'годa'
    else:
        yers = ''
    return yers
def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def end_perk (date,item):
    q = load_obj('dict_users')
    left = q[item]['perk_date'] - date
    if left <= 0:
        end = 1
    else:
        end = 0
        left = ((left //60)//60)#//24)#сколько часов осталось до конца

    return end, left

def rt (id_talker=None):
    q = load_obj('dict_users')
    reputation_talker =''
    if q[id_talker]['rep_points'] < 0:
       reputation_talker = '👣'
       q[id_talker]['rep'] = -1
    if q[id_talker]['rep_points'] >= 0:
       reputation_talker = '⭐'
       q[id_talker]['rep'] = 0
    if q[id_talker]['rep_points'] >= 2000:
       reputation_talker = '⭐⭐'
       q[id_talker]['rep'] = 1
    if q[id_talker]['rep_points'] >= 5000:
       reputation_talker = '⭐⭐⭐'
       q[id_talker]['rep'] = 2
    if q[id_talker]['rep_points'] >= 10000:
       reputation_talker = '⭐⭐⭐⭐'
       q[id_talker]['rep'] = 3
    if q[id_talker]['rep_points'] >= 20000:
       reputation_talker = '⭐⭐⭐⭐⭐'
       q[id_talker]['rep'] = 4
    save_obj(obj=q, name='dict_users')
    return reputation_talker

def bets (response=None):
    bbb =0
    aaa = 0
    if response == '5💎' or str(response) == '5':
        bbb = 5
        aaa = 1
    if response == '10💎' or str(response) == '10':
        bbb = 10
        aaa = 2
    if response == '15💎' or str(response) == '15':
        bbb = 15
        aaa = 3
    if response == '30💎' or str(response) == '30':
        bbb = 30
        aaa = 6
    return bbb, aaa

def r (rep_points=None, item=None):
    q = load_obj('dict_users')
    reputation = ''
    next_level = 0
    if rep_points < 0:
        q[item]['rep'] = -1
        reputation = '👣'  # 'Изгой👣'
        next_level = 0 - q[item]['rep_points']

    if rep_points >= 0:
        q[item]['rep'] = 0
        reputation = '⭐'  # 'Интроверт🙊'
        next_level = 2000 - q[item]['rep_points']

    if rep_points >= 2000:
        q[item]['rep'] = 1
        reputation = '⭐⭐'  # 'Любитель поболтать🗣'
        next_level = 5000 - q[item]['rep_points']

    if rep_points >= 5000:
        q[item]['rep'] = 2
        reputation = '⭐⭐⭐'  # 'Интересный собеседник🔥'
        next_level = 10000 - q[item]['rep_points']

    if rep_points >= 10000:
        q[item]['rep'] = 3
        reputation = '⭐⭐⭐⭐'  # 'Завсегдатай чата🚀'
        next_level = 20000 - q[item]['rep_points']

    if rep_points >= 20000:
        q[item]['rep'] = 4
        reputation = '⭐⭐⭐⭐⭐'  # 'Смотритель чата🐩'
        next_level = 0

    save_obj(obj=q, name='dict_users')

    #print(q[item]['rep'])

    return reputation, next_level

def smile_score(number):
    c ='✅'
    if number <9:
        c = '✅'
    elif number == 9:
        c = '🎯'
    elif number >9:
        c= '❌'
    return c

def calc_x (coef):
    c=2
    if coef >=3:
        c = 3
    if coef >=6:
        c = 4
    if coef >=12:
        c = 5

    return c
def voice (session_api, event,response,voices):
    #ключи и значения передающиеся в гет
    field = {'key': '22fe10e2-aa2f-4a58-a934-54f2c1c4d908', 'text': response, 'fornat': 'wav', 'lang': 'ru-RU',
             'emotion': 'neutral', 'speaker': voices, 'robot': '1'} #'smoky' 'evil'

    r = requests.get('https://tts.voicetech.yandex.net/generate', params=field)

    with open('voice.ogg', 'wb') as out_stream:
        req = requests.get(r.url, stream=True)
        for chunk in req.iter_content(1024):
            out_stream.write(chunk)

    afile = session_api.docs.getMessagesUploadServer(type='audio_message', peer_id=event.object.peer_id)
    upload_url = afile['upload_url']
    resp = requests.post(upload_url, files={'file': open('voice.ogg', 'rb')})
    result = json.loads(resp.text)
    file = result['file']

    #print(result)

    doc = session_api.docs.save(file=file, title='Voice message')['audio_message']
    id = doc['id']
    owner_id = doc['owner_id']

    #print(doc)
    #print('Голосовое сообщение отправителя: {0} и его файл ID: {1}'.format(owner_id, id))

    q2 = ['doc' + str(owner_id) + '_' + str(id)]
    return q2

def what_v (voices):
    golos = ''
    if voices == 'smoky':
        golos = 'NRX'
    elif voices == 'levitan':
        golos = 'Борис'
    elif voices == 'oksana':
        golos = 'Оксана'
    elif voices == 'jane':
        golos = 'Джейн'
    elif voices == 'kolya':
        golos = 'Колян'
    elif voices == 'dude':
        golos = 'Артем'
    elif voices == 'tanya':
        golos = 'Таня'
    elif voices == 'tatyana_abramova':
        golos = 'Элис'
    return golos





def open_menu (session_api,response,item, bot, var):
    q = load_obj('dict_users')
    try:
        if q[item]['perk'] > 0:
            sent_message(session_api, user_ids=item, tit=bot,
                         message='Репутация: {0} Баланс: 💎{1}\n\nПоиск - для поиска собеседника👌🏻'
                                 '\nМ - для поиска парня 🙎‍♂\nБеседа - для поиска беседы 👪\nЖ - для поиска девушки 🙎‍♀\n'.format(
                             rt(item), q[item]['diamonds']),
                         keyboard=create_keyboard(response, item, q[item]['in_chat'], q[item]['perk'], q[item]['number'], var))

        elif (q[item]['rep_points'] < 0 or q[item]['diamonds'] <3) and q[item]['perk'] ==0:
            sent_message(session_api, user_ids=item, tit=bot,
                         message='Репутация: {0} Баланс: 💎{1}\n\nПоиск - для поиска собеседника👌🏻'
                                 '\nМ - 🙎‍♂ для поиска парня 🚫\nБеседа - для поиска беседы 🚫\nЖ - 🙎‍♀ для поиска девушки 🚫\n'.format(
                             rt(item), q[item]['diamonds']),
                         keyboard=create_keyboard(response, item, q[item]['in_chat'], q[item]['perk'], q[item]['number'],
                                                  'negativ'))


        else:
            sent_message(session_api, user_ids=item, tit=bot,
                         message='Репутация: {0} Баланс: 💎{1}\n\nПоиск - для поиска собеседника👌🏻'
                                 '\nМ - 🙎‍♂ для поиска парня -3💎\nБеседа - для поиска беседы 🚫\nЖ - 🙎‍♀ для поиска девушки -3💎\n'.format(
                             rt(item), q[item]['diamonds']),
                         keyboard=create_keyboard(response, item, q[item]['in_chat'], q[item]['perk'], q[item]['number'], var))

    except:
        for ite in item:
            if q[ite]['perk'] > 0:
                sent_message(session_api, user_ids=ite, tit=bot,
                             message='Репутация: {0} Баланс: 💎{1}\n\nПоиск - для поиска собеседника👌🏻'
                                     '\nМ - для поиска парня 🙎‍♂\nБеседа - для поиска беседы 👪\nЖ - для поиска девушки🙎‍♀\n'.format(
                                 rt(ite), q[ite]['diamonds']), keyboard=create_keyboard(response, item, q[ite]['in_chat'], q[ite]['perk'], q[ite]['number'], var))

            elif (q[ite]['rep_points'] < 0 or q[ite]['diamonds'] <3) and q[ite]['perk'] ==0:
                sent_message(session_api, user_ids=ite, tit=bot,
                             message='Репутация: {0} Баланс: 💎{1}\n\nПоиск - для поиска собеседника👌🏻'
                                     '\nМ - 🙎‍♂ для поиска парня 🚫\nБеседа - для поиска беседы 🚫\nЖ - 🙎‍♀ для поиска девушки 🚫\n'.format(
                                 rt(ite), q[ite]['diamonds']),
                             keyboard=create_keyboard(response, item, q[ite]['in_chat'], q[ite]['perk'], q[ite]['number'],
                                                      'negativ'))
            else:
                sent_message(session_api, user_ids=ite, tit=bot,
                             message='Репутация: {0} Баланс: 💎{1}\n\nПоиск - для поиска собеседника👌🏻'
                                     '\nМ - 🙎‍♂ для поиска парня -3💎\nБеседа - для поиска беседы 🚫\nЖ - 🙎‍♀ для поиска девушки -3💎\n'.format(
                                 rt(ite), q[ite]['diamonds']), keyboard=create_keyboard(response, item, q[ite]['in_chat'], q[ite]['perk'], q[ite]['number'], var))


def open_admin(session_api,status_bot,bot, code14, code31, diamonds150, gold_vip, duhs, item, in_chat, perk, number, dat):
    q = load_obj('dict_users')
    q[item]['cod'] = 'admin'
    save_obj(obj=q, name='dict_users')
    # те кто в чате
    chat0 = [i for i in q if q[i]['in_chat'] == 0]
    chat1 = [i for i in q if q[i]['in_chat'] == 1]
    chat2 = [i for i in q if q[i]['in_chat'] == 2]
    chat3 = [i for i in q if q[i]['in_chat'] == 3]
    perk1 = [i for i in q if q[i]['perk'] == 1]
    perk0 = [i for i in q if q[i]['perk'] == 0]
    try:
      missing = [i for i in q if  dat > q[i]['last_activity'] + 259200] #в dat записан текущий тайм.тайм()
    except:
        print('исключение')
        for i in q:
            q[i]['last_activity'] = dat
            save_obj(obj=q, name='dict_users')
        missing = [i for i in q if  dat > q[i]['last_activity'] + 259200]
    if status_bot == 1:
        bo = '✅ Бот работает ✅'
    else:
        bo = '⛔ Бот остановлен ⛔'

    try:
       deleted_items = load_obj('deleted_items')
    except:
        deleted_items = []
        print('ОШИБКА: Список не существует')
    send_message(session_api, peer_id=106545709, tit=bot,
                 message='{10}\n'
                         '\n👥 в меню: {0}'
                         '\n👥 в чатах: {1}'
                         '\n👥 в беседах: {2}'
                         '\n👥 в Зонке: {3}'
                         '\n👥 пассивы: {11}'
                         '\n👥 VIP 👑 : {4}'
                         '\n👥 БЕЗ VIP: {12}'
                         '\n👥 подключено к БД: {9}'
                         '\n👥 удалены из duhs: {13}'
                         '\n\n🔑 Количество VIP 👑  подписок на 2 недели: {5}'
                         '\n🔑Количество VIP 👑  подписок на месяц: {6}'
                         '\n🔑Количество кодов на 150💎: {7}'
                         '\n🔑Количество gold vip 👑 кодов: {8}'.format(len(chat0), len(chat1), len(chat2), len(chat3),
                                                                     len(perk1), len(code14), len(code31),
                                                                     len(diamonds150), len(gold_vip), len(duhs), bo, len(missing),len(perk0), len(deleted_items)),
                 keyboard=create_keyboard('!админ', item, in_chat, perk, number, status_bot))


def close_voices (item):
    q = load_obj('dict_users')
    q[item]['cod'] = 0
    save_obj(obj=q, name='dict_users')



def hi_chat (session_api, q, event,bot,item, user_inf):
    #q = load_obj('dict_users')
    chat1 = [i for i in q if q[i]['in_chat'] == 1]
    chat2 = [i for i in q if q[i]['in_chat'] == 2]
    chat3 = [i for i in q if q[i]['in_chat'] == 3]
    calc_u = len(chat1) + len(chat2) + len(chat3) + random.randint(99, 111)
    if item == 106545709:
       calc_u = len(chat1) + len(chat2) + len(chat3)

    #user_inf = session_api.users.get(user_ids=event.obj.from_id,
    #                                 fields='sex')

    if user_inf == 1:#[0]['sex']
        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                     message='Мадам🙋, вы добавлены в очередь поиска собеседника 👫'
                             '\nИщем собеседника 🕵' + ' \nСейчас 👥 в чате: ' + str(calc_u))
    elif user_inf != 1:
        send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                     message='Месье🙋‍♂, вы добавлены в очередь поиска собеседника 👫'
                             '\nИщем собеседника 🕵' + ' \nСейчас 👥 в чате: ' + str(calc_u))

#def generators (session_api, q, os, logging, today, dat,mon,bot,var, newsletter):



def attachments (session_api, bot, event,requests, q1, len_buf, item):
    if 'geo' in event.obj:
        #print('гео')

        send_message(session_api, peer_id=event.obj.from_id, tit=bot,
                     message='К сожалению я не умею присылать гео 😢')

    fwd = event.obj.fwd_messages
    # УЗНАЕМ ТИП ПРИКРЕПЛЕНИЯ В GET MESSAGES
    get_messages = session_api.messages.getById(message_ids=event.obj.id, group_id=179410262)

    get_messages_atta = get_messages['items'][0]['attachments']
    #print(get_messages_atta)
    if get_messages_atta != []:
        type_atta = []
        for element in get_messages_atta:
            type_atta.append(str(element['type']))
            #print(type_atta)

    else:
        type_atta = []

    # ЕСЛИ В ЧАТЕ ПРИКРЕПИЛИ СТИКЕР ОТПРАВЛЯЕМ ЕГО
    if 'sticker' in type_atta:
        sticker_id = (get_messages_atta[0]['sticker']['sticker_id'])
        #print("стикер id " + str(sticker_id))
    else:
        sticker_id = 0

    # ЕСЛИ В ЧАТЕ ПРИКРЕПИЛИ ГОЛОСОВУХУ ОТПРАВЛЯЕМ
    if 'audio_message' in type_atta:

        #print(get_messages_atta[0]['audio_message']['owner_id'])
        #print(get_messages_atta[0]['audio_message']['id'])
        #print(str(type_atta['id']))

        with open('audio.ogg', 'wb') as out_stream:
            req = requests.get(get_messages_atta[0]['audio_message']['link_ogg'], stream=True)
            for chunk in req.iter_content(1024):
                out_stream.write(chunk)

        afile = session_api.docs.getMessagesUploadServer(type='audio_message', peer_id=event.object.peer_id)
        upload_url = afile['upload_url']
        resp = requests.post(upload_url, files={'file': open('audio.ogg', 'rb')})
        result = json.loads(resp.text)
        file = result['file']

        #print(result)

        doc = session_api.docs.save(file=file, title='Voice message')['audio_message']
        id = doc['id']
        owner_id = doc['owner_id']

        #print(doc)
        #print('Голосовое сообщение отправителя: {0} и его файл ID: {1}'.format(owner_id, id))

        q1 = ['doc' + str(owner_id) + '_' + str(id)]
        #q1 = ['doc' + str(get_messages_atta[0]['audio_message']['owner_id']) + '_' + str(get_messages_atta[0]['audio_message']['id'])]
        type_typing = 'audiomessage'
        # print(q1)
    # elif 'photo' in type_atta:
    # a = session_api.photos.getMessagesUploadServer(peer_id=event.object.peer_id)
    # b = requests.post(a['upload_url'], files={'photo': open('1.jpg', 'rb')})
    # result = json.loads(b.text)
    # server = result['server']
    # hash = result ['hash']
    # print (hash)
    # photo = result['photo']
    # print (photo)
    # print(result)
    # c = session_api.photos.saveMessagesPhoto(photo=photo, server=server, hash=hash)
    # print(c)
    # owner_id = c[0]['owner_id']
    # id = c[0]['id']
    # q1 = 'photo{}_{}'.format(str(c['owner_id']),str(c['id']))
    # q1 = ['photo' + str(owner_id) + '_' + str(id)]
    elif 'wall' in type_atta and item == 106545709:
        try:
            type_typing = 'typing'

           #print(get_messages_atta[0]['wall']['to_id'])
            #print(get_messages_atta[0]['wall']['id'])

            q1 = 'wall'+ str(get_messages_atta[0]['wall']['to_id']) +'_' + str(get_messages_atta[0]['wall']['id'])

            #print(q1)
        except:

            q1=0
            send_message(session_api, peer_id=event.obj.from_id, tit=bot,
                         message='К сожалению я не могу это отправить 😢')

    # ЕСЛИ ПРИКРЕПЛЕНИЕ НЕ СТИКЕР И ТИП ПРЕКРЕПЛЕНИЯ НЕ ПУСТОЙ ТО ДЕЛАЕМ ПЕРЕБОР ВЛОЖЕННЫХ ДОКОВ
    elif 'sticker' not in type_atta and type_atta != []:  # ) and 'audio' or 'video' or 'doc' or 'photo' in type_atta:
        buf = []
        type_typing = 'typing'

       # print('пошел перебор вложенных документов')
        for element in get_messages_atta:
            if element['type'] == 'graffiti':
                try:
                    buf.append(
                        'doc' + str(element['graffiti']['owner_id']) + '_' + str(element['graffiti']['id']) + '_' + str(
                            element['graffiti']['access_key']))
                except:
                    buf.append('doc' + str(element['graffiti']['owner_id']) + '_' + str(element['graffiti']['id']))

            elif element['type'] == 'audio':
                buf.append('audio' + str(element['audio']['owner_id']) + '_' + str(element['audio']['id']))
            elif element['type'] == 'video':
                try:
                    buf.append(
                        'video' + str(element['video']['owner_id']) + '_' + str(element['video']['id']) + '_' + str(
                            element['video']['access_key']))
                    print('в видео есть ключ')
                except:
                    print('в видео нет ключа')
                    buf.append('video' + str(element['video']['owner_id']) + '_' + str(
                        element['video']['id']))

            # ЕСЛИ ТИП ФОТО ПРОБУЕМ ПЕРЕБРАТЬ ВСЕ ЭЛЕМЕНТЫ ФОТО СНАЧАЛА С КЛЮЧОМ, ЕСЛИ КЛЮЧА НЕТ, ТО БЕЗ НЕГО
            elif element['type'] == 'photo':
                try:
                    buf.append('photo' + str(element['photo']['owner_id']) + '_' + str(
                        element['photo']['id']) + '_' + str(element['photo']['access_key']))
                    print('в фото есть ключ')
                except:
                    print('в фото нет ключа')
                    buf.append('photo' + str(element['photo']['owner_id']) + '_' + str(element['photo']['id']))

            elif element['type'] == 'doc':
                try:
                    buf.append('doc' + str(element['doc']['owner_id']) + '_' + str(element['doc']['id']) + '_' + str(
                        element['doc']['access_key']))
                    print('в доках есть ключ')
                except:
                    print('в доках нет ключа')
                    buf.append('doc' + str(element['doc']['owner_id']) + '_' + str(element['doc']['id']))

            # ЕСЛИ КАКОЕ ТО НЕИЗВЕСТНОЕ ВЛОЖЕНИЕ
            else:
                send_message(session_api, peer_id=event.obj.from_id, tit=bot,
                             message='К сожалению я не могу это отправить 😢')

        if buf != []:
            q1 = ','.join(buf)
            len_buf = (len(buf))
            #print('Нашел вложения: ' + str(buf))

    else:

        q1 = 0
        type_typing = 'typing'


    return q1, fwd, len_buf, type_typing, sticker_id

def wall_com(session_api, owner_id=None, massage=None, id = None, at = None):
    session_api.wall.createComment(owner_id=owner_id, post_id = 486, from_group=1, message =massage, reply_to_comment=id, attachments = at)


def weel_choise(session_api, sessions, weel,item, t, os, q):
        user_inf = session_api.users.get(user_ids=item,
                                         fields='sex')
        hide = 0
        try:
         wall_search = sessions.wall.search(owner_id =item, query = '#nrx,#whoi', count = 100)
         #print(wall_search)
        except:
            hide = 1

        za_repost =''

        a = ''  # ОБРАЩЕНИЕ К ДАМЕ
        if ((user_inf[0]['sex'])) == 1:#ЕСЛИ ПИШЕТ БАБА
            a = 'a'



        if os.path.exists("obj\\weel.pkl"):
            weel = load_obj('weel')

        if os.path.exists("obj\\dict_users.pkl"):
            q = load_obj('dict_users')

        try:

         if item in weel:
             if hide == 0:
              if wall_search['items'] != [] : #ЕСЛИ РЕПОСТ СДЕЛАН
                 if 'time_post' in weel[item]: #ЕСЛИ ДО ЭТОГО БЫЛ СДЕЛАН РЕПОСТ
                     result = t-weel[item]['time_post']#время сейчас - время сделанного репоста = сколько часов назад сделали репост
                     #print(result)

                     if result >= 10000 and weel[item]['time_post'] !=wall_search['items'][0]['date']: #если прощло 12 часов и появился новый пост
                         weel[item]['ticket'] += 3
                         weel[item]['time_post'] = wall_search['items'][0]['date']
                         za_repost = '\nУра! Ты получил{0} +3🎟 билета за репост, так держать!'.format(a)
                         print('Подходит под условия последняя запись')
                 else: #ПЕРВЫЙ РЕПОСТ ПОЛЬЗОВАТЕЛЯ
                     weel[item]['time_post'] = wall_search['items'][0]['date']
                     weel[item]['ticket'] += 3
                     za_repost = '\nТы получил{0} +3🎟 билета за репост, так держать!'.format(a)



             if t >= weel[item]['time'] + 43200:
                 weel[item]['ticket'] += 3
                 weel[item]['time'] = t
                 za_repost = '\nЕжедневное вознаграждение +3🎟 билета!'
             save_obj(obj=weel, name='weel')


         elif item not in weel:
             weel[item] = {'ticket': 3, 'time': t}

             save_obj(obj=weel, name='weel')

        except KeyError:
            weel[item] = {'ticket': 3, 'time': t}
            save_obj(obj=weel, name='weel')



        if weel[item]['ticket'] >=1:

            weel[item]['ticket'] -= 1
            save_obj(obj=weel, name='weel')



            balance = '{1}\nОсталось: {0}🎟'.format(str(weel[item]['ticket']),za_repost) #НАПОМИНАНИЕ О БАЛАНСЕ

            if weel[item]['ticket'] == 1:
                b1 ='\nОстался последний 🎟 билет, крутани еще разок, уверен, тебе повезет 😎'
                b2 ='\nОстался 1🎟 билет'
                b = [b1,b2]
                balance = random.choice(b)



            first_name = (str(user_inf[0]['first_name']))

            choices = random.randint(0, 155)
            print(choices)


            if choices >= 0 and choices <=9:
                photo_id = 'photo-179410262_457240417' #250RP
                msg = 'Ого ты выйграл{0} +250⭐ очков репутации на свой счет, так держать!😉{1}'.format(a,balance)
                q[item]['rep_points'] +=250
                save_obj(obj=q, name='dict_users')
                q = load_obj('dict_users')

            elif choices >= 10 and choices <=20:
                photo_id = 'photo-179410262_457240418' #0
                msg = 'Упс😒...не повезло в этот раз, повезет в следующий 👍🏻{0}'.format(balance)


            elif choices == 21:
                photo_id = 'photo-179410262_457240419' #500RP
                msg ='Ура! +500⭐ очков репутации на твой счет!🥳{0}'.format(balance)
                q[item]['rep_points'] += 500
                save_obj(obj=q, name='dict_users')
                q = load_obj('dict_users')


            elif choices >= 22 and choices <= 30:
                photo_id = 'photo-179410262_457240420' #0
                msg = 'Вот это ты крутанул{0}!😃 Но, в этот раз тебе не повезло😒{1}'.format(a,balance)


            elif choices == 31:
                photo_id = 'photo-179410262_457240421' #1000RP
                msg = 'Воу! +1000⭐ очков репутации на твой счет завезли!🤗{0}'.format(balance)
                q[item]['rep_points'] += 1000
                save_obj(obj=q, name='dict_users')
                q = load_obj('dict_users')

            elif choices >= 32 and choices <= 40:
                photo_id = 'photo-179410262_457240422' #0
                msg = 'Ура!😃 А, нет, не ура🤔, повезет в следующий раз 👍{0}'.format(balance)


            elif choices == 41:
                photo_id = 'photo-179410262_457240423' #100A!!!
                msg = 'Бам🤜🏻💥 сектор приз на барабане! +100💎 алмазов на твой счет!🙀{0}'.format(balance)
                q[item]['diamonds'] += 100
                save_obj(obj=q, name='dict_users')
                q = load_obj('dict_users')


            elif choices >= 42 and choices <= 50:
                photo_id = 'photo-179410262_457240424' #0
                msg = 'Ой, сектор 0 на барабане!😖{0}'.format(balance)


            elif choices == 51:
                photo_id = 'photo-179410262_457240425'  # 150A!!!
                msg = 'Вот это ты крутанул{0}!😃 Целая гора алмазов теперь твоя!🙈 +150💎 алмазов на твой счет🤑{1}'.format(a,balance)
                q[item]['diamonds'] += 150
                save_obj(obj=q, name='dict_users')
                q = load_obj('dict_users')


            elif choices >= 52 and choices <= 60:
                photo_id = 'photo-179410262_457240426'  # 0
                msg = '{0}, повезет в следующий раз👻{1}'.format(first_name,balance)


            elif choices == 61:
                photo_id = 'photo-179410262_457240427'  # 500RP
                msg = '{0}, поздравляю!🐶 Ты выйграл{2} +500⭐ очков репутации!{1}'.format(first_name,balance,a)
                q[item]['rep_points'] += 500
                save_obj(obj=q, name='dict_users')
                q = load_obj('dict_users')



            elif choices >= 62 and choices <= 70:
                photo_id = 'photo-179410262_457240459'  # 0
                msg = 'Вот это да!😱 Ты выйграл{0} целую гору ничего!😂{1}'.format(a,balance)


            elif choices == 71:
                photo_id = 'photo-179410262_457240429'  # 1750RP
                msg = 'Огошеньки мои!🙀 Ты выйграл{1} +1750⭐ очков репутации🤩{0}'.format(balance,a)
                q[item]['rep_points'] += 1750
                save_obj(obj=q, name='dict_users')
                q = load_obj('dict_users')


            elif choices >= 72 and choices <= 80:
                photo_id = 'photo-179410262_457240430'  # 0
                msg = 'Сектор "Пусто" на барабане!{0}'.format(balance)


            elif choices == 81:
                photo_id = 'photo-179410262_457240431'  # 50A!!
                msg = 'Такс, что тут у нас...ого😃 ты выйграл{0} +50💎 алмазов на твой счет🤑{1}'.format(a,balance)
                q[item]['diamonds'] += 50
                save_obj(obj=q, name='dict_users')
                q = load_obj('dict_users')


            elif choices >= 82 and choices <= 90:
                photo_id = 'photo-179410262_457240432' #0
                msg = 'Упс, сектор 0 на барабане, повезет в другой раз😉{0}'.format(balance)


            elif choices == 91:
                photo_id = 'photo-179410262_457240433' # 3D!!!
                msg = '🎉Ура! {0}, ты выйграл{1} супер приз! VIP 👑 подписку на 3 дня! Поздравляю🎊{2}'.format(first_name,a,balance)
                if q[item]['perk'] == 0:
                    q[item]['perk'] = 1
                    q[item]['perk_time'] = t
                    q[item]['perk_date'] = t + 259200
                    save_obj(obj=q, name='dict_users')
                    q = load_obj('dict_users')

                elif q[item]['perk'] > 1:
                    q[item]['perk'] = 1
                    q[item]['perk_date'] += 259200
                    save_obj(obj=q, name='dict_users')
                    q = load_obj('dict_users')


            elif choices >= 92 and choices <= 100:
                photo_id = 'photo-179410262_457240434' #0
                msg = 'Пусто😒{0}'.format(balance)


            elif choices == 101:
                photo_id = 'photo-179410262_457240443'  # 2000RP!
                msg = '🎉+2000⭐ очков репутации!🤩 Поздравляю!🎊{0}'.format(balance)
                q[item]['rep_points'] += 2000
                save_obj(obj=q, name='dict_users')
                q = load_obj('dict_users')


            elif choices >= 102 and choices <= 110:
                photo_id = 'photo-179410262_457240444'  # 0
                msg = 'Сектор "Пусто"😒{0}'.format(balance)


            elif choices == 111:
                photo_id = 'photo-179410262_457240445'  # 10A!
                msg = 'Как мощно ты крутанул{0} +10💎 алмазов на твой счет🤑{1}'.format(a,balance)
                q[item]['diamonds'] += 10
                save_obj(obj=q, name='dict_users')
                q = load_obj('dict_users')

            elif choices >= 112 and choices <= 120:
                photo_id = 'photo-179410262_457240446'  # 0
                msg = 'Урааа!!! Ой, нет, не ура, я ошибся.😶 Повезет в другой раз🤥{0}'.format(balance)


            elif choices == 121:
                photo_id = 'photo-179410262_457240447'  # 7B!
                weel[item]['ticket'] += 7
                balance = '{1}\nОсталось: {0}🎟'.format(str(weel[item]['ticket']), za_repost)
                save_obj(obj=weel, name='weel')
                msg = 'Вау! +7🎟 билетов! Давай крути еще!🔁{0}'.format(balance)




            elif choices >= 122 and choices <= 130:
                photo_id = 'photo-179410262_457240448'  # 0
                msg = 'Сорян, сектор "Пусто" на барабане{0}'.format(balance)



            elif choices == 131:
                photo_id = 'photo-179410262_457240449'  # 1D!!
                msg = '🎉Ура! {0}, ты выйграл{1} приз! VIP 👑 подписку на 1 день! Поздравляю🎊{2}'.format(first_name,a,balance)

                if q[item]['perk'] == 0:
                    q[item]['perk'] = 1
                    q[item]['perk_time'] = t
                    q[item]['perk_date'] = t + 86400
                    save_obj(obj=q, name='dict_users')
                    q = load_obj('dict_users')

                elif q[item]['perk'] > 1:
                    q[item]['perk'] = 1
                    q[item]['perk_date'] += 86400
                    save_obj(obj=q, name='dict_users')
                    q = load_obj('dict_users')



            elif choices >= 132 and choices <= 155:
                photo_id = 'photo-179410262_457240450'  # 0
                msg = 'Пусто😥{0}'.format(balance)

            save_obj(obj=q, name='dict_users')


            #print(photo_id)


        else:

            photo_id = ''
            m1 = 'У тебя не хватает билетов 🎟 чтобы крутануть колесо, приходи завтра!👻'
            m2 = 'Не хватает билетов🎟, чтобы крутануть колесо?🧐\n Ты можешь сделать репост этой записи (не чаще 1 раза в 12 часов) и получить +3🎟 бонусных билета😎\nP.S. Профиль должен быть открыт😉'
            m =[m1,m2]
            msg = random.choice(m)


        return photo_id, msg



def bonus_vip(bot, session_api, i):
    try:
        time.sleep(0)
        send_message(session_api, peer_id=i, tit=bot,
                     message='Ваш VIP статус истекает сегодня 😒\nНо у нас для вас есть специальное предложение! 😃\nПродли VIP 👑 подписку на месяц сейчас и получи +150💎 на свой счет совершенно бесплатно! 🤩 \nВип - купить вип')
    except Exception as err:
        print('Ошибка при отправке сообения, бонусов: ' + str(err))

def send_end_vip(i, bot,session_api):
    try:
            send_message(session_api, peer_id=i, tit=bot,
                         message='', sticker_id='9131')
            time.sleep(0)
            send_message(session_api, peer_id=i, tit=bot,
                         message='Действие вашего VIP статуса истекло😐\nВип - купить вип')
    except Exception as err:
        print('Ошибка при отправке сообения, о завершении вип статуса: ' + str(err))

def helper (sessions, session_api, result, search_helper1, bot, search_helper2,logging ):
    user_inf = sessions.users.get(user_ids=result,
                                     fields='sex')

    random_message = ['Кажется,☺ кое-кто не прочь с тобой поболтать 💬',
                      'Кое-кто,😈 хочет с тобой поговорить 😇', 'Кое-кто, очень хочет с тобой пообщаться 💬',
                      'Сейчас самый пик 💥 активности в чатах! Жми "Поиск"',
                      'С тобой хотят поболтать😑 Жмякай кнопку "Поиск"👇🏻']

    #print(user_inf)
    time.sleep(0)
    if len(search_helper1) > 2:

        if user_inf[0]['sex'] == 1:
            try:

               send_message(session_api, peer_id=result, tit=bot,
                             message=random.choice(random_message),
                             keyboard=create_keyboard('helper', result, 0, 0, 0, 'helper'))



            except  vk_api.exceptions.ApiError as vk_error:
                print('ОШИБКА: 901 УДАЛЯЕМ ПОЛЬЗОВАТЕЛЯ')
                print(vk_error)
                if '901' in str(vk_error):
                     delete(result, session_api)



    elif len(search_helper2) > 2:

        if user_inf[0]['sex'] == 2:
            try:

                send_message(session_api, peer_id=result, tit=bot,
                             message=random.choice(random_message),
                             keyboard=create_keyboard('helper', result, 0, 0, 0, 'helper'))




            except  vk_api.exceptions.ApiError as vk_error:
                print('ОШИБКА: 901 УДАЛЯЕМ ПОЛЬЗОВАТЕЛЯ')
                print(vk_error)
                if '901' in str(vk_error):
                    delete(result, session_api)


def delete (result, session_api):
    app_del_el = []

    inf = ''
    convers = load_obj('convers')
    duhs = load_obj('list_duhs')
    q = load_obj('dict_users')
    que = load_obj('que')
    all_list = load_obj('all_list')
    third_list = load_obj('third_list')
    deleted_items = load_obj('deleted_items')
    bot = '✦N.R.X✦'

    #for element in sent:


    if result in duhs:
                err = 1
                duhs.remove(result)  # удаляем из duhs
                save_obj(obj=duhs, name='list_duhs')
                print('Удален из duhs helperom')
                if result not in deleted_items:
                    app_del_el.append(result)  # список id которые запретили отправку сообщений
                    deleted_items.append(result)  # добавляем в список удаленных пользователей
                    save_obj(obj=deleted_items, name='deleted_items')

                que = [name for name in que if
                       result not in name['user']]  # удаляет пользователя из очереди поиска по критериям
                save_obj(obj=que, name='que')
                print('Удален из QUE')
                #print(que)

                i = result
                item = result
                try:
                    f = q[i]['id_talker']
                    found = q[i]['id_talker']

                    if (q[i]['in_chat'] == 1 or q[i]['in_chat'] == 3):  # and #q[f]['id_talker'] == i:
                        try:
                            send_message(session_api, peer_id=f, tit=bot,
                                         message='Диалог #{0} закончен 👫\nПонравился собеседник?'.format(
                                             q[f]['id_convers']),
                                         keyboard=create_keyboard('стоп', f, 1, q[f]['perk'], 0, 0))
                            if q[f]['bet'] != 0:
                                q[f]['diamonds'] += q[f]['bet']
                                send_message(session_api, peer_id=f, tit=bot,
                                             message='+{}💎'.format(str(q[f]['bet'])))

                        except vk_api.exceptions.ApiError as vk_error: #888
                            print(vk_error)
                        try:
                            q[f]['id_convers'] = 0
                            q[f]['in_chat'] = 0
                            q[f]['voices'] = 0

                            q[f]['bet'] = 0
                            q[f]['game_room'] = 0
                            q[f]['number'] = 0
                            q[f]['timeout'] = 0

                            q[f]['cod'] = 0
                        except:
                            pass

                    elif q[item]['in_chat'] == 2:
                        if len(q[item]['id_talker']) == 2:

                            for i in q[item]['id_talker']:
                                q[item]['id_talker'] = [i for i in q[i]['id_talker'] if i != item]
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
                except KeyError as keyerr:
                    print(keyerr)
                q[i]['id_convers'] = 0
                q[i]['id_talker'] = 0
                q[i]['in_chat'] = 0

                q[i]['voices'] = 0
                q[i]['cod'] = 0

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
    else:
                err = 0
                #print('Пользователя нет в duhs, он уже удален'.format(app_del_el))

    if err == 1:
                inf = '\nБыл добавлен в список блокированных пользователей: {0}'.format(app_del_el)

                #print('-1 пользователь {0}'.format(inf))
                #send_message(session_api, peer_id=106545709, tit=bot,
                 #            message='Рассылка прошла успешно! {0}'.format(inf))


def otv(session_api,event,group_id,bot, monotonic, mon):


    keyboard = VkKeyboard(one_time=True)
    print('Ответ на сообщение не найден')

    time.sleep(0)
    user_inf, first_name, last_name, last_and_first_name = user_information (session_api, event)
    if session_api.groups.isMember(group_id=group_id,
                                   user_id=event.obj.peer_id):
        try:
            print('Пользователь: {0} есть в группе!'.format(last_and_first_name))
        except:
            pass
        u_m_11 = '❌ {0} такой команды не существует! ❌\nСовет: Чем чаще вы выигрываете в игре Зонк 🎲 тем быстее растет ваш уровень репутации!'.format(last_and_first_name)
        u_m_12 = '❌ {0} такой команды не существует! ❌\nСовет: Самые активные участники диалога или беседы получают 💎'.format(last_and_first_name)
    else:
        try:
            print('Пользователь: {0} нет в группе!'.format(last_and_first_name))
        except:
            pass
        if user_inf == 1:

            u_m_11 = '❌ {0} такой команды не существует! ❌\nТак, {0} ты почему еще не подписана на нас?🤔'.format(first_name)
            u_m_12 = '❌ {0} такой команды не существует! ❌\n{0}, мы уже так долго вместе, а ты до сих пор не подписана на нас😒'.format(
                first_name)

        else:
            u_m_11 = '❌ {0} такой команды не существует! ❌\nТак, {0} ты почему еще не подписан на нас?🤔'.format(first_name)
            u_m_12 = '❌ {0} такой команды не существует! ❌\n{0}, мы уже так долго вместе, а ты до сих пор не подписан на нас😒'.format(first_name)

    u_m_0 = '❌ {0} такой команды не существует! ❌\nСовет: Чем выше 🔝 ваша репутация ⭐⭐⭐⭐⭐ тем  больше 💎 за общение вы получаете!'.format(first_name)
    u_m_1 = '❌ {0} такой команды не существует! ❌\nСовет: Меню - чтобы узнать все доступные команды'.format(first_name)
    u_m_2 = '❌ {0} такой команды не существует! ❌\nСовет: Меню - чтобы узнать все доступные команды'.format(first_name)
    u_m_4 = '❌ {0} такой команды не существует! ❌\nСовет: Оценивая собеседника кнопкой 👍🏻 вы повышаете его репутацию, а кнопкой 👎🏻 понижаете'.format(first_name)
    u_m_5 = '❌ {0} такой команды не существует! ❌\nСовет: С VIP 👑 статусом ваша репутация растет гораздо быстрее!'.format(first_name)
    u_m_6 = '❌ {0} такой команды не существует! ❌\nСовет: С VIP 👑 статусом вы получите новый скин для игры в Зонк 🎲'.format(first_name)
    u_m_7 = '❌ {0} такой команды не существует! ❌\nСовет: Пользователи с отрицательной 👣 репутацией имееют ограничения на некоторые функции чата!'.format(first_name)
    u_m_8 = '❌ {0} такой команды не существует! ❌\nСовет: Чем выше 🔝 ваша репутация, ⭐⭐⭐⭐⭐ тем  больше очков репутации за 👍🏻 получит собеседник!'.format(first_name)
    u_m_9 = '❌ {0} такой команды не существует! ❌\nСовет: Чем выше 🔝 ваша серия побед 🏆, тем больше ваш выигрыш в игре Зонк 🎲'.format(first_name)
    u_m_10 ='❌ {0} такой команды не существует! ❌\nСовет: Нажми "Угостить 🍬", когда находишься в диалоге'.format(first_name)
    # if u_m_10
    if user_inf == 1:

        u_m_3 = '❌ {0} такой команды не существует! ❌\nПсс... {0} у меня есть для тебя персональное предложение 😑' \
                '\nНапиши: Вип'.format(
            first_name)
    else:
        u_m_3 = '❌ {0} такой команды не существует! ❌\n{0}, хочешь получить доступ к приватным функциям анонимного чата?😑' \
                '\nНапиши: Вип'.format(
            first_name)

    u_message = [u_m_0, u_m_1, u_m_2, u_m_3, u_m_4, u_m_5, u_m_6, u_m_7, u_m_8, u_m_9, u_m_10, u_m_11, u_m_12]
    u_message = random.choice(u_message)


    if u_message == u_m_5 or u_message == u_m_3 or u_message == u_m_6:
        keyboard.add_button("Вип 👑", color=VkKeyboardColor.PRIMARY, payload='')
        keyboard.add_line()

    keyboard.add_button("Меню", color=VkKeyboardColor.DEFAULT, payload='')
    keyboard.add_button("Сообщить об ошибке", color=VkKeyboardColor.DEFAULT, payload='')
    keyboard = keyboard.get_keyboard()

    send_message(session_api, peer_id=event.obj.peer_id, tit=bot,
                 message=u_message, keyboard=keyboard)
    mon_3 = monotonic()
    print(mon_3 - mon)

def user_information (session_api, event):
    user_inf = session_api.users.get(user_ids=event.obj.from_id,
                                     fields='sex')

    first_name = (str(user_inf[0]['first_name']))
    last_name = (str(user_inf[0]['last_name']))
    last_and_first_name = str(first_name) + ' ' + str(last_name)
    user_inf = user_inf[0]['sex']
    return user_inf, first_name, last_name, last_and_first_name

def treat (q, session_api, response, item, bot, found, threading, tit):
    if response == "🍺":
        response = 'Вам поставили 🍺'

        send_message(session_api, peer_id=item, tit=bot,
                     message='Вы поставили собеседнику 🍺')
        send_message(session_api, peer_id=item, tit=bot,
                     message='-1💎')


        q[item]['diamonds'] -= 1
        q[found]['rep_points'] += 15

    if response == "🍸":
        response = 'Вас угостили 🍸'
        send_message(session_api, peer_id=item, tit=bot,
                     message='Вы угостили собеседника 🍸')
        send_message(session_api, peer_id=item, tit=bot,
                     message='-1💎')

        q[item]['diamonds'] -= 1
        q[found]['rep_points'] += 30

    if response == "🍹":
        response = 'Вас угостили вкусным 🍹'
        send_message(session_api, peer_id=item, tit=bot,
                     message='Вы угостили собеседника 🍹')
        send_message(session_api, peer_id=item, tit=bot,
                     message='-1💎')

        q[item]['diamonds'] -= 1
        q[found]['rep_points'] += 60

    if response == "🥃":
        response = 'Вас угостили дорогим 🥃'
        send_message(session_api, peer_id=item, tit=bot,
                     message='Вы угостили собеседника 🥃')
        send_message(session_api, peer_id=item, tit=bot,
                     message='-1💎')

        q[item]['diamonds'] -= 1
        q[found]['rep_points'] += 120

    if response == "🍼":
        response = 'Вас попоили из 🍼'
        send_message(session_api, peer_id=item, tit=bot,
                     message='Вы попоили собеседника из 🍼')
        send_message(session_api, peer_id=item, tit=bot,
                     message='-1💎')

        q[item]['diamonds'] -= 1
        q[found]['rep_points'] -= 15

    if response == "💩":
        response = 'В вас кинули 💩'
        send_message(session_api, peer_id=item, tit=bot,
                     message='Вы кинули в собеседника 💩')
        send_message(session_api, peer_id=item, tit=bot,
                     message='-1💎')

        q[item]['diamonds'] -= 1
        q[found]['rep_points'] -= 120
    #send_message(session_api, peer_id=found, tit=bot,
    #             message=response)
    t_smg = threading.Thread(target=send_message, name='thread_smg', args=(session_api, found, tit, response))
    t_smg.start()
    print('Cтартанул поток {}'.format(t_smg.name))
    save_obj(obj=q, name='dict_users')
    q = load_obj('dict_users')


def random_bonus(q, threading, bot,session_api, rep, item, event):
    global give_rep
    global pick_rep
    if rep == 0:
        give_rep = 15
        pick_rep = 5
        if random.randint(1, 45) == 1:
            q[item]['diamonds'] += 1

            save_obj(obj=q, name='dict_users')
            t_send = threading.Thread(target=send_message, name='bonus_send',
                                      args=(session_api, event.obj.peer_id, bot, '+1💎'))
            t_send.start()
            print('Cтартанул поток {}'.format(t_send.name))

    elif rep == 1:
        give_rep = 30
        pick_rep = 10
        if random.randint(1, 40) == 1:
            q[item]['diamonds'] += 1

            save_obj(obj=q, name='dict_users')
            t_send = threading.Thread(target=send_message, name='bonus_send',
                                      args=(session_api, event.obj.peer_id, bot, '+1💎'))
            t_send.start()
            print('Cтартанул поток {}'.format(t_send.name))
    elif rep == 2:
        give_rep = 60
        pick_rep = 20
        if random.randint(1, 35) == 1:
            q[item]['diamonds'] += 1

            save_obj(obj=q, name='dict_users')
            t_send = threading.Thread(target=send_message, name='bonus_send',
                                      args=(session_api, event.obj.peer_id, bot, '+1💎'))
            t_send.start()
            print('Cтартанул поток {}'.format(t_send.name))
    elif rep == 3:
        give_rep = 120
        pick_rep = 40
        if random.randint(1, 30) == 1:
            q[item]['diamonds'] += 1
            diamonds = q[item]['diamonds']
            save_obj(obj=q, name='dict_users')
            t_send = threading.Thread(target=send_message, name='bonus_send',
                                      args=(session_api, event.obj.peer_id, bot, '+1💎'))
            t_send.start()
            print('Cтартанул поток {}'.format(t_send.name))
    elif rep == 4:
        give_rep = 240
        pick_rep = 80
        if random.randint(1, 15) == 1:
            q[item]['diamonds'] += 1

            save_obj(obj=q, name='dict_users')
            t_send = threading.Thread(target=send_message, name='bonus_send',
                                      args=(session_api, event.obj.peer_id, bot, '+1💎'))
            t_send.start()
            print('Cтартанул поток {}'.format(t_send.name))
    return give_rep, pick_rep