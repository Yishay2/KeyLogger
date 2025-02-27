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
