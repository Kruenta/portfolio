import requests

key = "7e4f08d875213327b6894d5692820ae8"
payload = {
    "lat": 55,
    "lon": 83,
    "appid": '7e4f08d875213327b6894d5692820ae8'
}
k = requests.get(
    'https://api.openweathermap.org/data/2.5/weather',
    params=payload
)
print(k.content)