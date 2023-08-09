import requests as req
import os

Directory = "E:/AllCaptured/Ip-Adress/"
if not os.path.exists(Directory + "IP-Address.txt"):
    os.makedirs("IP-Address.txt")

url = "https://checkip.amazonaws.com"
response = req.get(url)
ip = response.text.strip()  # Odstránenie medzier a znakov nového riadku z IP adresy

print("IP:", ip)

with open(Directory + "IP-Address.txt", "w") as file:  # Použitie "w" namiesto "a" pre vytvorenie/zápis do súboru
    file.write("IP-Address: " + ip)  # Spojenie reťazcov namiesto viacerých argumentov
