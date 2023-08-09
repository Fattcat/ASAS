import cv2
import os
import time
from datetime import datetime

# Cesta k adresáru, kde sa majú uložiť fotografie
save_directory = "E:/AllCaptured/CpCamera"

if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# Inicializácia kamery
camera = cv2.VideoCapture(0)

while True:
    # Načítanie snímky z kamery
    ret, frame = camera.read()

    if ret:
        # Získanie aktuálneho dátumu a času
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

        # Vytvorenie názvu súboru s cestou k uloženiu
        filename = os.path.join(save_directory, f"{timestamp}.jpg")

        # Uloženie snímky
        cv2.imwrite(filename, frame)
        print(f"Snímka uložená: {filename}")
    # Čakanie 3 sekundy
    #cv2.waitKey(5)
    time.sleep(5)
    # Zastavenie programu stlačením klávesy 'q'
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break
# Uvoľnenie kamery
camera.release()
# Zatvorenie všetkých otvorených okien OpenCV
cv2.destroyAllWindows()
