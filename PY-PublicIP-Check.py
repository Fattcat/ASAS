import requests as req
import os
import datetime
import socket

NazovPC = socket.gethostname()
AktualnyDatum = datetime.datetime.now().strftime("%Y.%d.%m %H:%M:%S")
Directory = "E:/AllCaptured/"

if not os.path.exists("IP-Adress.txt"):
    os.makedirs("IP-Adress.txt")

url = "https://checkip.amazonaws.com"
response = req.get(url)
ip = response.text.strip()  # Odstránenie medzier a znakov nového riadku z IP adresy
#print("IP:", ip)
with open(os.path.join(Directory + "IP-Adress.txt"), "a") as file: # Použitie "w" namiesto "a" pre vytvorenie/zápis do súboru
    file.write("+" + "-"*30 + "+" + "\n")
    file.write("  Dátum : " + AktualnyDatum + "\n  IP-Adresa : " + ip + "\n" + "  Názov PC : " + NazovPC + "\n")  # Spojenie reťazcov namiesto viacerých argumentov
    file.write("+" + "-"*30 + "+" + "\n"*2)
