import psutil
import os
import socket

MenoZariadenia = socket.gethostname()
DlzkaMena = socket.gethostname()
DlzkaMena = len(DlzkaMena)
file_path = os.path.join("E:/AllCaptured/BatteryCheckPCorNotebook", "CheckIfIsPC.txt")

def is_notebook_with_battery():
    battery_present = psutil.sensors_battery()
    return battery_present is not None

if __name__ == "__main__":
    if is_notebook_with_battery():
        print("Skript sa spustil na NOTEBOOKU s menom : " + MenoZariadenia)
        with open(file_path, "a") as file:
            file.write(" "*38 + "+" + " " + "-"*DlzkaMena + " " + "+\n")
            file.write("Skript sa spustil na notebooku.\n")
            file.write(" "*38 + "+" + " " + "-"*DlzkaMena + " " + "+\n\n")
    else:
        print("Skript sa spustil na počítači.")
        with open(file_path, "a") as file:
            file.write(" "*38 + "+" + " " + "-"*DlzkaMena + " " + "+\n")
            file.write("Skript sa spustil na POCITACI s menom : " + MenoZariadenia + "\n")
            file.write(" "*38 + "+" + " " + "-"*DlzkaMena + " " + "+\n\n")
