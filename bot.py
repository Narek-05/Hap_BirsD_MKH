import os

import telebot # Импортируем telebot
from telebot import types # для определения типов
from datetime import datetime, timedelta

token =  os.getenv('BOT_TOKEN')  # передаём значение переменной с кодом экземпляру бота
bot = telebot.TeleBot(token)
# Получение сегодняшней даты
today = datetime.now()
current_month = today.month
current_year = today.year

# Функция для расчета возраста
def calculate_age(birthdate):
    birthdate_dt = datetime.strptime(birthdate, "%Y-%m-%d")
    return current_year - birthdate_dt.year - ((today.month, today.day) < (birthdate_dt.month, birthdate_dt.day))

# token = ('код')
#bot = telebot.TeleBot(token)

people = [
    {"name": "Сурен", "surname": "Мхитарян", "birthdate": "1924-02-16"},
    {"name": "Феник", "surname": "Манукян (Мхитарян)", "birthdate": "1928-05-06"},

    {"name": "Лаура", "surname": "Мхитарян (Тонеян)", "birthdate": "1948-01-30"},
    {"name": "Ишхан", "surname": "Тонеян", "birthdate": "1947-02-20"},

    {"name": "Гарик", "surname": "Тонеян", "birthdate": "1969-11-23"},
    {"name": "Арпине", "surname": "Согоян (Тонеян)", "birthdate": "1974-03-09"},
    {"name": "Мери", "surname": "Тонеян", "birthdate": "1994-09-23"},
    {"name": "Рубен", "surname": "Тонеян", "birthdate": "1997-12-02"},

    {"name": "Мануш", "surname": "Тонеян (Кишмирян)", "birthdate": "1971-10-12"},
    {"name": "Ашот", "surname": "Кишмирян", "birthdate": "1963-04-22"},
    {"name": "Мнацакан", "surname": "Кишмирян", "birthdate": "1992-01-31"},
    {"name": "Ваге", "surname": "Кишмирян", "birthdate": "1993-04-29"},

    {"name": "Лилит", "surname": "Тонеян (Айрапетян)", "birthdate": "1975-09-14"},
    {"name": "Артур", "surname": "Айрапетян", "birthdate": "1967-10-11"},
    {"name": "Гегине", "surname": "Айрапетян", "birthdate": "1995-04-12"},
    {"name": "Тереза", "surname": "Айрапетян", "birthdate": "1996-05-24"},
    {"name": "Геворг", "surname": "Айрапетян", "birthdate": "2000-07-17"},

    {"name": "Асмик", "surname": "Тонеян", "birthdate": "1982-02-06"},
    {"name": "Гарик", "surname": "Кесоян", "birthdate": "1981-10-12"},
    {"name": "Вика", "surname": "Кесоян", "birthdate": "2005-10-12"},
    {"name": "Мари", "surname": "Кесоян", "birthdate": "2008-10-02"},
    {"name": "Давид", "surname": "Кесоян", "birthdate": "2019-02-19"},

    {"name": "Хачик", "surname": "Мхитарян", "birthdate": "1950-07-20"},
    {"name": "Грета", "surname": "Арутюнян", "birthdate": "1950-09-06"},

    {"name": "Ануш", "surname": "Мхитарян (Керобян)", "birthdate": "1974-09-15"},
    {"name": "Левон", "surname": "Керобян", "birthdate": "1971-02-13"},
    {"name": "Айк", "surname": "Керобян", "birthdate": "1998-11-28"},
    {"name": "Спартак", "surname": "Керобян", "birthdate": "2000-12-06"},

    {"name": "Ованес", "surname": "Мхитарян", "birthdate": "1975-11-07"},
    {"name": "Лилит", "surname": "Баграмян", "birthdate": "1979-06-25"},
    {"name": "Гарик", "surname": "Мхитарян", "birthdate": "2004-02-28"},
    {"name": "Алекс", "surname": "Мхитарян", "birthdate": "2015-01-19"},

    {"name": "Давид", "surname": "Мхитарян", "birthdate": "1978-09-17"},
    {"name": "Лусине", "surname": "Дарбинян", "birthdate": "1990-06-12"},
    {"name": "Армен", "surname": "Мхитарян", "birthdate": "2012-04-13"},
    {"name": "Грета", "surname": "Мхитарян", "birthdate": "2014-06-26"},

    {"name": "Арпик", "surname": "Мхитарян (Мгерян)", "birthdate": "1954-12-02"},
    {"name": "Оник", "surname": "Мгерян", "birthdate": "1948-12-27"},

    {"name": "Армен", "surname": "Мгерян", "birthdate": "1977-09-27"},
    {"name": "Нара", "surname": "Абраамян", "birthdate": "1978-06-02"},
    {"name": "Арпи", "surname": "Мгерян", "birthdate": "1997-10-19"},
    {"name": "Арсен", "surname": "Мгерян", "birthdate": "1999-08-29"},

    {"name": "Армине", "surname": "Мгерян (Айвазян)", "birthdate": "1979-01-17"},
    {"name": "Арман", "surname": "Айвазян", "birthdate": "1974-10-23"},
    {"name": "Алла", "surname": "Айвазян", "birthdate": "1999-09-19"},
    {"name": "Элла", "surname": "Айвазян", "birthdate": "2002-09-05"},

    {"name": "Марине", "surname": "Мгерян (Балян)", "birthdate": "1981-06-17"},
    {"name": "Арсен", "surname": "Балян", "birthdate": "1973-01-16"},
    {"name": "Ани", "surname": "Балян", "birthdate": "2009-11-23"},
    {"name": "Арам", "surname": "Балян", "birthdate": "2011-04-27"},

    {"name": "Арамаис", "surname": "Мгерян", "birthdate": "1993-09-09"},
    {"name": "Ерминэ", "surname": "Меликсецян", "birthdate": "1995-01-21"},
    {"name": "Микаел", "surname": "Мгерян", "birthdate": "2021-08-17"},
    {"name": "Оник", "surname": "Мгерян", "birthdate": "2019-10-18"},

    {"name": "Каро", "surname": "Мхитарян", "birthdate": "1956-03-21"},
    {"name": "Лала", "surname": "Арутюнян (Мхитарян)", "birthdate": "1962-09-04"},

    {"name": "Унан", "surname": "Мхитарян", "birthdate": "1984-10-13"},
    {"name": "Лиля", "surname": "Сардарян", "birthdate": "1987-09-05"},
    {"name": "Давид", "surname": "Мхитарян", "birthdate": "2012-11-22"},
    {"name": "Каро", "surname": "Мхитарян", "birthdate": "2024-06-26"},

    {"name": "Гнел", "surname": "Мхитарян", "birthdate": "1986-05-06"},
    {"name": "Карина", "surname": "Швецова", "birthdate": "1986-02-08"},
    {"name": "Диана", "surname": "Мхитарян", "birthdate": "2020-07-31"},
    {"name": "Арман", "surname": "Мхитарян", "birthdate": "2022-06-21"},

    {"name": "Сурен", "surname": "Мхитарян", "birthdate": "1991-06-21"},

    {"name": "Гагик", "surname": "Мхитарян", "birthdate": "1958-10-19"},
    {"name": "Вардитер", "surname": "Саргсян", "birthdate": "1957-12-05"},

    {"name": "Нарине", "surname": "Мхитарян", "birthdate": "1988-07-29"},
    {"name": "Арман", "surname": "Саргсян", "birthdate": "1987-02-27"},
    {"name": "Тигран", "surname": "Саргсян", "birthdate": "2013-06-15"},
    {"name": "Мари", "surname": "Саргсян", "birthdate": "2019-01-09"},

    {"name": "Нарек", "surname": "Мхитарян", "birthdate": "1991-09-05"},
    {"name": "Айарпи", "surname": "Арутюнян", "birthdate": "1994-02-11"},
]

# Список свадеб
wedding = [
    {"groom": "Сурен Мхитарян", "bride": "Феник Манукян", "wedding_date": "1947-01-20"},

    {"groom": "Ишхан Тонеян", "bride": "Лаура Мхитарян", "wedding_date": "1969-02-02"},
    {"groom": "Гарик Тонеян", "bride": "Арпине Согоян", "wedding_date": "1969-10-28"},
    {"groom": "Ашот Кишмирян", "bride": "Мануш Тонеян", "wedding_date": "2015-10-10"},
    {"groom": "Артур Айрапетян", "bride": "Лилит Тонеян", "wedding_date": "1993-12-26"},
    {"groom": "Гарик Кесоян", "bride": "Асмик Тонеян", "wedding_date": "2004-01-22"},

    {"groom": "Хачик Мхитарян", "bride": "Грета Арутюнян", "wedding_date": "1973-10-14"},
    {"groom": "Лева Керобян", "bride": "Ануш Мхитарян", "wedding_date": "1998-10-01"},
    {"groom": "Ованес Мхитарян", "bride": "Лилит Баграмян", "wedding_date": "2003-03-26"},
    {"groom": "Давид Мхитарян", "bride": "Лусине Дарбинян", "wedding_date": "2011-04-08"},

    {"groom": "Оник Мгерян", "bride": "Арпик Мхитарян", "wedding_date": "1976-12-05"},
    {"groom": "Армен Мгерян", "bride": "Нара Абраамян", "wedding_date": "1996-11-02"},
    {"groom": "Арман Айвазян", "bride": "Армине Мгерян", "wedding_date": "1998-09-05"},
    {"groom": "Арсен Балян", "bride": "Марине Мгерян", "wedding_date": "2008-12-05"},
    {"groom": "Арамаис Мгерян", "bride": "Ерминэ Меликсецян", "wedding_date": "2018-09-09"},

    {"groom": "Каро Мхитарян", "bride": "Лала Арутюнян", "wedding_date": "1983-11-23"},
    {"groom": "Унан Мхитарян", "bride": "Лиля Сардарян", "wedding_date": "2011-12-25"},
    {"groom": "Гнел Мхитарян", "bride": "Карина Швецова", "wedding_date": "2018-12-15"},

    {"groom": "Гагик Мхитарян", "bride": "Вардитер Саргсян", "wedding_date": "1987-08-22"},
    {"groom": "Арман Саргсян", "bride": "Нарине Мхитарян", "wedding_date": "2012-03-17"},
    {"groom": "Мхитарян Нарек", "bride": "Айарпи Арутюнян", "wedding_date": "2023-01-19"},
]

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_button = types.KeyboardButton("Ближайшие 🎂")
    start44_button = types.KeyboardButton("В текущем месяце 📅")
    action_button = types.KeyboardButton("Прошедшие 30 дней ⌛")
    action22_button = types.KeyboardButton("Годовщина свадьбы 💍")
    action77_button = types.KeyboardButton("Обратная связь 🔔")
    markup.add(start_button, start44_button, action_button, action22_button, action77_button)
    bot.send_message(message.chat.id, text="Բարև Ձեզ։ 👋, {0.first_name} \nՈղջունում եմ ձեզ այս ալիքում։ Այս ալիքը ստեղծված է Սուրեն Մխիթարյանի և Ֆենիկ Մանուկյանի երեխաների, թոռների ծննդյան օրերը և հարսանեկան տարելիցի օրերը հիշեցնելու համար։ Սկսելու համար խնդրում եմ սեղմեք համապատասխան կոճակին։".format(message.from_user), reply_markup=markup)


#@bot.message_handler(commands=['start'])     # хендлер и функция для обработки команды /start
#def start_message(message):
#    bot.send_message(message.chat.id, "Привет Бро")

@bot.message_handler(content_types=['text'])  # хендлер для обработки нажатий кнопок
def buttons(message):
    if (message.text == "Ближайшие 🎂"):
        bot.send_message(message.chat.id, text="Дни рождения в ближайшие 14 дней:")
        # Дни рождения в ближайшие 14 дней
        print("Дни рождения в ближайшие 14 дней:")
        for person in people:
            birthdate_dt = datetime.strptime(person["birthdate"], "%Y-%m-%d")
            upcoming_birthday = birthdate_dt.replace(year=current_year)    #ОРИГИНАЛ
            #upcoming_birthday = birthdate_dt.replace(year=current_year - (1 if (today.month, today.day) < (birthdate_dt.month, birthdate_dt.day) else 0))

            if today <= upcoming_birthday <= today + timedelta(days=14):    # ОРИГИНАЛ считает правильно, не показывает в текущий день
            #if today - timedelta(days=14)  <= upcoming_birthday <= today :
            #if today - timedelta(days=1) <= upcoming_birthday  <= today + timedelta(days=14):   # считает не правильно, но показывает в текущий день
             #   last_birthday = birthdate_dt.replace( year=current_year - (1 if (today.month, today.day) < (birthdate_dt.month, birthdate_dt.day) else 0))
       #    if today - timedelta(days=30) <= last_birthday <= today:
                age = calculate_age(person["birthdate"])
                k1_bliz14= f"{person['name']} {person['surname']}, {upcoming_birthday.day} {upcoming_birthday.strftime('%B')}, исполнится {age +1} лет"
                print(k1_bliz14)
                bot.send_message(message.chat.id, k1_bliz14)

            if today -timedelta(days=1)<= upcoming_birthday <= today + timedelta(days=0):  # ОРИГИНАЛ считает правильно, не показывает в текущий день
                # if today - timedelta(days=14)  <= upcoming_birthday <= today :
                # if today - timedelta(days=1) <= upcoming_birthday  <= today + timedelta(days=14):   # считает не правильно, но показывает в текущий день
                #   last_birthday = birthdate_dt.replace( year=current_year - (1 if (today.month, today.day) < (birthdate_dt.month, birthdate_dt.day) else 0))
                #    if today - timedelta(days=30) <= last_birthday <= today:
                age = calculate_age(person["birthdate"])
                k1_bliz14 = f"{person['name']} {person['surname']}, {upcoming_birthday.day} {upcoming_birthday.strftime('%B')}, исполнится {age } лет"
                print(k1_bliz14)
                bot.send_message(message.chat.id, k1_bliz14)

    elif (message.text == "В текущем месяце 📅"):
        bot.send_message(message.chat.id, text="Дни рождения в текущем месяце:")

        # Дни рождения в текущем месяце
        print("\nДни рождения в текущем месяце:")
        for person in people:
            birthdate_dt = datetime.strptime(person["birthdate"], "%Y-%m-%d")
            if birthdate_dt.month == current_month:
                age = calculate_age(person["birthdate"])
                k2_tek_mes = (f"{person['name']} {person['surname']}, {birthdate_dt.day} {birthdate_dt.strftime('%B')}")
                print(k2_tek_mes)
                bot.send_message(message.chat.id, k2_tek_mes)

    elif (message.text == "Прошедшие 30 дней ⌛"):
        bot.send_message(message.chat.id, text="Дни рождения в течении последних 30 дней:")
        # Дни рождения в течении 30 дней назад
        print("\nДни рождения в течении последних 30 дней:")
        for person in people:
            birthdate_dt = datetime.strptime(person["birthdate"], "%Y-%m-%d")
            last_birthday = birthdate_dt.replace(year=current_year - (1 if (today.month, today.day) < (birthdate_dt.month, birthdate_dt.day) else 0))
            if today - timedelta(days=30) <= last_birthday <= today:
                age = calculate_age(person["birthdate"])
                k3_prosh30= f"{person['name']} {person['surname']}, {last_birthday.day} {last_birthday.strftime('%B')}, исполнилось {age} лет"
                print(k3_prosh30)
                bot.send_message(message.chat.id, k3_prosh30)

    elif (message.text == "Годовщина свадьбы 💍"):
        bot.send_message(message.chat.id, text="В ближайшее время годовщина свадьбы будет у:")
        # годовщина свадьбы
        print("\nГодовщина свадьбы в ближайшие 30 дней:")
        for couple in wedding:
            wedding_date_dt = datetime.strptime(couple["wedding_date"], "%Y-%m-%d")
            anniversary_date = wedding_date_dt.replace(year=current_year)
           # if today - timedelta(days=2) <= anniversary_date <= today + timedelta(days=30):    #    - timedelta(days=1)
             #   years_married = calculate_age(couple["wedding_date"])  # +1
            if today  <= anniversary_date <= today + timedelta(days=30):  # - timedelta(days=1)
                years_married = calculate_age(couple["wedding_date"]) +1
                k4_brak = f"{couple['groom']} и {couple['bride']}, {anniversary_date.day} {anniversary_date.strftime('%B')}, {years_married} лет в браке 💖"
                print(k4_brak)
                bot.send_message(message.chat.id, k4_brak)

            if today - timedelta(days=2) <= anniversary_date <= today + timedelta(days=1):  # - timedelta(days=1)
                years_married = calculate_age(couple["wedding_date"])
                k4_brak=f"{couple['groom']} и {couple['bride']}, {anniversary_date.day} {anniversary_date.strftime('%B')}, {years_married} лет в браке 💗"
                print(k4_brak)
                bot.send_message(message.chat.id, k4_brak)
                    #f"{couple['groom']} и {couple['bride']}, {anniversary_date.day} {anniversary_date.strftime('%B')}, {years_married} лет в браке")

    elif (message.text == "Обратная связь 🔔"):
        bot.send_message(message.chat.id, text=" Если вы обнаружили неточность в дате рождения, дате бракосочетания или же у вас есть вопросы и предложения по работе Бота, можете написать - @o_qq_oo:")

    else:
        bot.send_message(message.chat.id, text="Я могу отвечать только на нажатие кнопок 😊")

