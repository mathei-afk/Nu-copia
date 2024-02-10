import socket
import signal
import sys

def server():
    host = '192.168.0.173'  #inlocuiti IP-ul si portul
    port = 7000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"PORNIT IP= {host} Port= {port}")

    def control_semnal(sig, frame):
        print("Serverul se închide.")
        server_socket.close()
        sys.exit(0)

    signal.signal(signal.SIGINT, control_semnal)

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Conectat la {client_address}")

        alert_message = client_socket.recv(1024).decode('utf-8')
        if not alert_message:
            break
        print(alert_message)

        client_socket.close()

def main():
    server()

if __name__ == "__main__":
    main()

