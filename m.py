import vk_api
from data1 import *
session = vk_api.VkApi(login_id, pass_id, token=a_token)
session.auth()
print(__name__)
sessions=session.get_api()
print (sessions)
vk_session = vk_api.VkApi(token=token)
session_api = vk_session.get_api()

def kuk(message, chunks, send_sticker_id, send_q1):  # , sticker_id=None,q1=None):
    print(send_sticker_id)
    print('Цикл рассылки сообщений')
    import random

    from def1 import send_message

    for i in chunks:
        try:
         session_api.messages.send(user_ids=i, title='✦N.R.X✦', message=message,
                             random_id=random.randint(-2147483648, +2147483648),
                               sticker_id=send_sticker_id, attachment=send_q1)

        except vk_api.exceptions.ApiError as vk_error:

               #logging.error("ОШИБКА ПРИ РАССЫЛКЕ СООБЩЕНИЙ {0} {1}".format(str(today),i) + str(vk_error))
               print (vk_error)




