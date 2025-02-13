import json
from keylogger import Encryptor

path = input("Enter path: ")
secret_key = input("Enter key: ")

def load_path(path: str, key: str) -> None:
    try:
        with open(path, "r") as file:
            try:
                content = json.load(file)
            except json.JSONDecodeError:
                print("It's not valid json file!")
            else:
                enc = Encryptor(key)
                decrypted_data = enc.decrypt_data(content)
                print(decrypted_data)
    except FileNotFoundError:
        print("You insert invalid path!")

load_path(path, secret_key)
