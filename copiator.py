import win32gui
import time
import socket

#aici sunt toate numele care sunt ignorate (daca un prograj are in denumirea lui una din denumirile de mai jos este eliminat adica nu se va mai trimite alerta)
IGNORED_TEXTS = ["Code::Blocks", "Command Prompt", "Debug", "Open File", "New From Template", "Save File", "Create new class", "Console application"]

def window_title():
    return win32gui.GetWindowText(win32gui.GetForegroundWindow())

def ignored_window(window_title):
    return any(ignored_text.lower() in window_title.lower() for ignored_text in IGNORED_TEXTS)

def server(window_title):
    host = '-------------'  #inlocuiti adresa IP-ul si portul
    port = ----

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    #numele calculatorului asta trebuie schimbat pe fiecare pc
    client_name = "Nr.1"

    current_time = time.strftime("%H:%M:%S")
    alert_message = f"ALERTĂ: [{current_time}] {client_name} a deschis aplicația: {window_title}!"
    client_socket.send(alert_message.encode('utf-8'))


    client_socket.close()

def main():
    previous_window = window_title()

    while True:
        current_window = window_title()

        if current_window != previous_window and not ignored_window(current_window):
            server(current_window)

        previous_window = current_window

        time.sleep(1)

if __name__ == "__main__":
    main()
