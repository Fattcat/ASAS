import os
import datetime
import time
from PIL import ImageGrab

if not os.path.exists("E:/AllCaptured/CpScreenShotter"):
    os.makedirs("E:/AllCaptured/CpScreenShotter")
    
counter = 1

while True:
    im = ImageGrab.grab()
    FileName = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S.png")
    im.save(f"E:/AllCaptured/CpScreenShotter/{FileName}")
    counter += 1
    time.sleep(1)