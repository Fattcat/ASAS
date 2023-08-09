import pygame
import random
from time import sleep
import keyboard

song_list = ["Minecraft-Hurt.mp3", "Villager-Hmm.mp3", "Villager-Huh.mp3", "RickRoll.mp3", "spongebob-disappointed.mp3", "Cikoki.wav", "EmotionalDamage.wav", "Papuca.wav"]
cas = [499, 200, 300, 10, 80, 20, 8, 99, 130, 50]
pygame.mixer.init()

for x in range(99):
#while True:
    nahodna_songa = random.choice(song_list)
    piesen_cesta = "E:/PY_ULTRA-SPUSTAC-A-SCRIPTY/MinecraftMEMEhlasky/" + nahodna_songa # Úplná cesta k piesni na USB disku E:
    pygame.mixer.music.load(piesen_cesta)
    
    nahodny_cas = random.choice(cas) #/ 1000.0  # Prevod na sekundy
    pygame.mixer.music.play()
    sleep(nahodny_cas)
    if keyboard.is_pressed("CTRL") and keyboard.is_pressed("l"):
        pygame.mixer.quit()
        break
pygame.mixer.quit()