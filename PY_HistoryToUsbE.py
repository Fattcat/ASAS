import os
import sqlite3
from datetime import datetime

def get_chrome_history(output_folder):
    try:
        chrome_history_file = os.path.expanduser("~") + r"\AppData\Local\Google\Chrome\User Data\Default\History"
        connection = sqlite3.connect(chrome_history_file)
        cursor = connection.cursor()
        cursor.execute("SELECT title, url, last_visit_time FROM urls")
        rows = cursor.fetchall()

        with open(os.path.join(output_folder, "Chrome_History.txt"), "w", encoding="utf-8") as file:
            for row in rows:
                title, url, last_visit_time = row
                file.write(f"{title}\t{url}\t{last_visit_time}\n")

        connection.close()
        print("Chrome history saved.")
    except Exception as e:
        print(f"Error while getting Chrome history: {e}")

def get_firefox_history(output_folder):
    try:
        firefox_history_file = os.path.expanduser("~") + r"\AppData\Roaming\Mozilla\Firefox\Profiles\places.sqlite"
        connection = sqlite3.connect(firefox_history_file)
        cursor = connection.cursor()
        cursor.execute("SELECT title, url, last_visit_date FROM moz_places")
        rows = cursor.fetchall()

        with open(os.path.join(output_folder, "Firefox_History.txt"), "w", encoding="utf-8") as file:
            for row in rows:
                title, url, last_visit_date = row
                file.write(f"{title}\t{url}\t{last_visit_date}\n")

        connection.close()
        print("Firefox history saved.")
    except Exception as e:
        print(f"Error while getting Firefox history: {e}")

def get_edge_history(output_folder):
    try:
        edge_history_file = os.path.expanduser("~") + r"\AppData\Local\Microsoft\Edge\User Data\Default\History"
        connection = sqlite3.connect(edge_history_file)
        cursor = connection.cursor()
        cursor.execute("SELECT title, url, last_visit_time FROM urls")
        rows = cursor.fetchall()

        with open(os.path.join(output_folder, "Edge_History.txt"), "w", encoding="utf-8") as file:
            for row in rows:
                title, url, last_visit_time = row
                file.write(f"{title}\t{url}\t{last_visit_time}\n")

        connection.close()
        print("Edge history saved.")
    except Exception as e:
        print(f"Error while getting Edge history: {e}")

def get_opera_history(output_folder):
    try:
        opera_history_file = os.path.expanduser("~") + r"\AppData\Roaming\Opera Software\Opera Stable\History"
        connection = sqlite3.connect(opera_history_file)
        cursor = connection.cursor()
        cursor.execute("SELECT title, url, last_visit_time FROM urls")
        rows = cursor.fetchall()

        with open(os.path.join(output_folder, "Opera_History.txt"), "w", encoding="utf-8") as file:
            for row in rows:
                title, url, last_visit_time = row
                file.write(f"{title}\t{url}\t{last_visit_time}\n")

        connection.close()
        print("Opera history saved.")
    except Exception as e:
        print(f"Error while getting Opera history: {e}")

def main():
    current_datetime = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    output_folder = f"E:/AllCaptured/CpHistory/{current_datetime}"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    get_chrome_history(output_folder)
    get_firefox_history(output_folder)
    get_edge_history(output_folder)
    get_opera_history(output_folder)

if __name__ == "__main__":
    main()
