import requests

respons = requests.get("https://www.ceneo.pl/78739350#tab=reviews")
print(respons.text)