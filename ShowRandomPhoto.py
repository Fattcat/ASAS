import pygame
import random
import time
import keyboard

pygame.init()

ObrazkovyFOlder = "E:/PY_ULTRA-SPUSTAC-A-SCRIPTY/PY-Images/"

# Nastavenie veľkosti obrazovky
sirka = 800
vyska = 800
obrazovka = pygame.display.set_mode((sirka, vyska), pygame.NOFRAME)
pygame.display.set_caption("Zobrazenie obrázkov na náhodnej pozícii")

# Načítanie obrázkov
obrazky = ["TrollImage.png", "Image-Thinkink2.png", "Image-Thinking.png", "Fuk2.jpg"]
obrazky = [pygame.image.load(ObrazkovyFOlder + obrazok) for obrazok in obrazky]

# Hlavná slučka
TimeList = [1, 20, 6, 200, 300, 99]
cas_zobrazenia_max = random.choice(TimeList)
cas_zobrazenia_start = time.time()

bezi = True
while bezi:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bezi = False

    obrazovka.fill((0, 0, 0))

    if time.time() - cas_zobrazenia_start >= cas_zobrazenia_max:
        cas_zobrazenia_start = time.time()
        cas_zobrazenia_max = random.choice(TimeList)
        
        obrazok = random.choice(obrazky)
        x = (sirka - obrazok.get_width()) // 2  # Centrovanie obrázka na osi x
        y = (vyska - obrazok.get_height()) // 2  # Centrovanie obrázka na osi y
        
        obrazovka.blit(obrazok, (x, y))
        pygame.display.flip()
    if keyboard.is_pressed("f7"):
        break
pygame.quit()
