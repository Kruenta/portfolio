import requests
import json

key = "042eae53-2190-4a14-ad70-9234c77ef5b5"
payload = {
    "lat": 55,
    "lon": 83,
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
print(data["fact"]["temp"], data["fact"]["feels_like"])

