from Interfaces import IWriter
import requests

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
