import requests

response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=강서구&appid=3dc06380d440e4afeac98d7f604cbeb4")
print(response.text)