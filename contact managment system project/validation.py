import re
class Validation:

    @staticmethod
    def check_name(name: str):
        return 2 <= len(name) <= 50

    @staticmethod
    def check_phone(phone: str):
        return phone.isdigit() and len(phone) >= 9

    @staticmethod
    def check_email(email: str):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None
