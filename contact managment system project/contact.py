from typing import List, Optional

class Contact:
    def __init__(self, id: int, name: str, numbers_list: List[str], groups: List[str], email: Optional[str] = None):
        self.id = id
        self.name = name
        self.numbers_list = numbers_list
        self.groups = groups
        self.email = email

    def __str__(self):
        return (f"ID: {self.id}, Name: {self.name}, Numbers: {', '.join(self.numbers_list)}, "
                f"Groups: {', '.join(self.groups)}, Email: {self.email if self.email else 'None'}")