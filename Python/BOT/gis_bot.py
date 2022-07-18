import json
import requests
import telebot

bot = telebot.TeleBot('1455423122:AAEhYVpJhIYbVjZa1nrq_NEzo7Fn2N0eW-Q')


def get_weather(lat, lon):
    key = "042eae53-2190-4a14-ad70-9234c77ef5b5"
    payload = {
        "lat": lat,
        "lon": lon,
        "lang": "ru_RU",
        "hours": False,
    }
    gis = {
        "X-Yandex-API-Key": key
    }
    k = requests.get(
        'https://api.weather.yandex.ru/v2/forecast',
        params=payload,
        headers=gis
    ).content
    data = json.loads(k)
    out = {
        "country": data["geo_object"]["country"]['name'],
        "city": data["geo_object"]["locality"]["name"],
        "temp": data["fact"]["temp"],
        "feels_like": data["fact"]["feels_like"],
    }
    return out


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, u'\U0001F6A9' + " Отправь мне свою геопозицию, я скажу на сколько холодно")


@bot.message_handler(content_types=["location"])
def location(message):
    if message.location is not None:
        data = get_weather(message.location.latitude, message.location.longitude)
        text = u'\U0001F6A9' + "Ваше местоположение: " + data["country"] + ", " + data["city"] + "\n" + \
                  "Температура за окном: " + str(data["temp"]) + "\n" + \
                  "Ощущается как: " + str(data["feels_like"])
        bot.send_message(message.chat.id, text)


bot.polling()
