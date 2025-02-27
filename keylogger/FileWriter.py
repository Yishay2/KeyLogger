from Interfaces import IWriter
import json

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

