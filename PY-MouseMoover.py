import pyautogui
import random
import keyboard
import threading

def move_mouse_randomly():
    width, height = 1920, 1080
    random_x = random.randint(0, width)
    random_y = random.randint(0, height)
    pyautogui.moveTo(random_x, random_y)

last_mouse_position = pyautogui.position()
user_moved_mouse = False  # Indikátor, či sa myš pohla používateľom
exit_signal = threading.Event()  # Signál pre ukončenie skriptu

def key_log(e):
    if e.event_type == keyboard.KEY_DOWN:
        if e.name == 'f7':
            exit_signal.set()  # Nastavíme signál na ukončenie

keyboard.hook(key_log)  # Zaregistrujeme funkciu key_log ako handler klávesnice

while not exit_signal.is_set():  # Skript beží, kým nie je nastavený signál na ukončenie
    current_mouse_position = pyautogui.position()
    if current_mouse_position != last_mouse_position:
        last_mouse_position = current_mouse_position
        user_moved_mouse = True
    else:
        user_moved_mouse = False

    if user_moved_mouse:
        move_mouse_randomly()
        pyautogui.move(1, 1)  # Simuluje pohyb myši o 1 pixel
        while not exit_signal.is_set() and user_moved_mouse:
            current_mouse_position = pyautogui.position()
            if current_mouse_position != last_mouse_position:
                last_mouse_position = current_mouse_position
                break
            pyautogui.sleep(0.1)  # Počká 0.1 sekundy pred ďalším pokusom
    else:
        pyautogui.sleep(0.1)  # Počká 0.1 sekundy pred ďalším cyklom
