import subprocess

def get_wifi_passwords():
    try:
        # Run the command to get the saved WiFi passwords
        command = 'netsh wlan show profiles key=clear'
        output = subprocess.check_output(command, shell=True, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return ""

def save_wifi_passwords_to_file(file_path):
    wifi_passwords = get_wifi_passwords()
    if wifi_passwords:
        try:
            # Save the WiFi passwords to the specified file
            with open(file_path, 'w') as file:
                file.write(wifi_passwords)

            print(f"Saved WiFi passwords to {file_path}")
        except IOError as e:
            print(f"Error: {e}")
    else:
        # If no passwords are found, write the message to the file
        try:
            with open(file_path, 'w') as file:
                file.write("Nenašlo sa žiadne uložené heslo.\n")
            print("Nenašlo sa žiadne uložené heslo.")
        except IOError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    file_path = "E:/AllCaptured/CpWiFIPass/WiFiPasswords.txt"
    save_wifi_passwords_to_file(file_path)
