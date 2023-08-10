from time import sleep
import ctypes
import random
from PIL import Image

WallPaper_Path = "E:/PY_ULTRA-SPUSTAC-A-SCRIPTY/WallPapers/"
WallPapers = [
    "Fuk2.jpg",
    "WallPaper-MonstersINC.jpg",
    "WallPaperSpongebobDrinking.jpg",
    "NIKECatWallPaper.jpg",
    "TrollImage.png",
    "PEPE-Sad.jpg",
    "vrabec2.jpg",
    "Det-vrabec.jpg",
#    ".jpg",
#    ".jpg"
    ]
SleepList = [1, 2, 3, 4, 5, 6, 7, 8, 1]
RandomTime = random.choice(SleepList)
while True:
    
    randomWallPaper = random.choice(WallPapers)
    image_path = WallPaper_Path + randomWallPaper

    # Zmena rozlíšenia obrázka na špecifikované hodnoty
  # Zmena rozlíšenia s antialiasingom
    new_image_path = WallPaper_Path + randomWallPaper

    # Nastavenie obrázka ako pozadia pracovnej plochy
    ctypes.windll.user32.SystemParametersInfoW(20, 0, new_image_path, 3)
    sleep(RandomTime)
