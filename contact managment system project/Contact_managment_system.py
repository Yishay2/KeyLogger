import json
from typing import Optional
from contact import Contact
from validation import Validation

class ContactSystemManagement:

    def __init__(self):
        self.contacts = {}
        self.id = 0

    def add_contact(self, name: str, numbers_list: list[str], groups: list[str], email: Optional[str] = None) -> int:
        self.id += 1
        self.contacts[self.id] = Contact(self.id, name, numbers_list, groups, email)
        return self.id

    def get_contact(self, id: int) -> Optional[Contact]:
        if id in self.contacts:
            return self.contacts[id]
        print("The contact wasn't found!")

    def display_contacts(self) -> list[Contact]:
        return print_list([self.contacts.values()], "contacts")

    def remove_contact(self, id: int) -> bool:
        if id in self.contacts:
            del self.contacts[id]
            return True
        return False

    def search_person_by_name(self, name: str) -> list[Optional[Contact | None]]:
        return [self.contacts[key] for key in self.contacts if name.lower() in self.contacts[key].name.lower()]

    def search_person_by_phone(self, phone: str) -> list[Optional[Contact | None]]:
        return [self.contacts[key] for key in self.contacts if any(number for number in self.contacts[key].numbers_list if phone in number)]

    def filter_by_groups(self, g: str) -> list[Optional[Contact | None]]:
        return [self.contacts[key] for key in self.contacts if any(group for group in self.contacts[key].groups if g.lower() in group.lower())]

    def filter_by_email(self, email: str) -> list[Optional[Contact | None]]:
        return [self.contacts[key] for key in self.contacts if email in self.contacts[key].email]

    def filter_by_existing_email(self, has_email: bool) -> list[Optional[Contact | None]]:
        return [self.contacts[key] for key in self.contacts if has_email and self.contacts[key].email or not has_email and not self.contacts[key].email]

    def filter_by_conditions(self, name: Optional[str] = None, phone: Optional[str] = None, email: Optional[str] = None, group: Optional[str] = None):
        filtered_contacts = [contact for contact in self.contacts.values()]
        if name:
            filtered_by_name = self.search_person_by_name(name)
            filtered_contacts = [contact for contact in filtered_contacts if contact in filtered_by_name]
        if phone:
            filtered_by_phone = self.search_person_by_phone(phone)
            filtered_contacts = [contact for contact in filtered_contacts if contact in filtered_by_phone]
        if email:
            filtered_by_email = self.filter_by_email(email)
            filtered_contacts = [contact for contact in self.contacts if contact in filtered_by_email]
        if group:
            filtered_by_group = self.filter_by_groups(group)
            filtered_contacts = [contact for contact in filtered_contacts if contact in filtered_by_group]
        return filtered_contacts

    def gathering_by_domain(self):
        domains = {}
        has_email = self.filter_by_existing_email(True)
        for contact in has_email:
            domain = contact.email.split("@")[1]
            if domain in domains:
                domains[domain].append(contact)
            else:
                domains[domain] = [contact]

        return domains

    def save_contacts_to_file(self, file_name):

        try:
            with open(file_name, "w") as f:
                f.write(json.dumps(self.contacts, indent=4))
                print("successfully done!")
                return True
        except Exception as e:
            print("Error: ", repr(e))
            return False

    def read_contacts_from_file(self, file_name):
        try:
            with open(file_name, "r") as f:
                f.read(json.load(file_name))
                print("Successfully read!")
                return True
        except Exception as e:
            print("Error: " + repr(e))
            return False

    def get_num_of_contacts(self):
        return len(self.contacts)

    def get_num_of_each_group(self):
        groups = {}
        for contact in self.contacts:
            if contact.groups:
                for group in contact.groups:
                    if group in groups:
                        groups[group] += 1
                    else:
                        groups[group] = 1
        return groups

    def get_percents_of_people_with_email(self):
        has_email = self.filter_by_existing_email(True)
        return self.get_num_of_contacts() / len(has_email)

    def get_percent_of_each_email(self):
        all_amount_domains = self.gathering_by_domain()
        num_of_people_with_email = len(self.filter_by_existing_email(True))
        return {domain: len(all_amount_domains[domain]) / num_of_people_with_email for domain in all_amount_domains}

    def gathering_contacts_by_theirs_groups(self):
        groups = dict()
        for contact in self.contacts:
            if contact.groups:
                for group in contact.groups:
                    if group not in groups:
                        groups[group] = [contact]
                    else:
                        groups[group].append(contact)

        return groups


def get_an_email_from_user():
    has_email = get_y_or_n_from_user("Do u have an email? ")

    if has_email:
        email = input("Enter your email: ")
        while not Validation.check_email(email):
            print("You have to insert a valid email!")
            email = input("Enter your email: ")
    else:
        email = None

    return email

def get_numbers_from_user() -> list[str]:
    numbers_list = []
    flag = True
    while len(numbers_list) < 0 or flag:
        number = input("Enter your phone number: ")
        while not Validation.check_phone(number):
            print("You must insert a valid phone number!")
            number = input("Enter your phone number: ")

        numbers_list.append(number)
        cont = get_y_or_n_from_user("Do u have more numbers")
        if not cont:
            print("OK!")
            flag = False
    return numbers_list

def get_groups_from_user() -> list[str]:

    flag = True
    groups = []
    while len(groups) == 0 or flag:
        cont = get_y_or_n_from_user("Do u want to join to a group: ")
        if cont:
            group = input("Enter your group name: ")
            while not Validation.check_name(group):
                print("You have to insert a valid group!")
                group = input("Enter your group name: ")

            groups.append(group)
            cont = get_y_or_n_from_user("Do u have more groups: ")
            if not cont:
                print("OK!")
                flag = False
        else:
            break
    return groups

def get_name_from_user() -> str:
    name = input("Enter your name: ")
    while not Validation.check_name(name):
        print("You must insert invalid name!")
        name = input("Enter your name: ")
    return name

def add_new_contact() -> tuple[str, list[str], list[str], str]:
    name = get_name_from_user()
    numbers_list = get_numbers_from_user()
    email = get_an_email_from_user()
    groups = get_groups_from_user()
    return name, numbers_list, groups, email

def get_id_from_user() -> int:
    id = input("Enter id: ")
    while not id.isdigit():
        print("You have to insert a number! ")
        id = input("Enter id: ")

    return int(id)

def get_y_or_n_from_user(message: str) -> bool:
    inp = input(f"{message}, Enter y for yes or n for no: ").lower()
    while inp not in ["y", "n"]:
        print("You have to insert only n for no or y for yes!")
        inp = input("Enter y or n: ").lower()
    return inp == "y"

def print_list(arr, items) -> list:
    if not arr:
        print(f"You don't have any {items} yet")
    else:
        for i, item in enumerate(list(arr)):
            print(f"{i + 1}: {item}")
    return arr

def get_phone_from_user():
    phone = input("Enter your phone: ")
    while not Validation.check_phone(phone):
        print("You entered a wrong number, please try again...!")
        phone = input("Enter your phone: ")
    return phone

s = ContactSystemManagement()
def main():
    while True:
        print("1: add contact: ")
        print("2: get contact: ")
        print("3: display contact: ")
        print("4: remove contact: ")
        print("5: search person by name: ")
        print("6: search person by phone: ")
        print("7: filter by groups: ")
        print("8: filter by email: ")
        print("9: filter by people with email or not: ")
        print("10: filter by some conditions: ")
        print("11: gathering by domain: ")
        print("12: save to file: ")
        print("13: load from file: ")
        print("14: get number of contacts: ")
        print("15: get length of each group: ")
        print("16: get percents of people with email: ")
        print("17: get percents of people each email: ")
        print("18: gathering contacts by their groups: ")
        user_choice = input("Enter your choice: ")
        while not user_choice.isdigit() or not 1 <= int(user_choice) <= 18:
            print("You have to insert a number between 1 to 18! ")
            user_choice = input("Enter your choice: ")
        user_choice = int(user_choice)
        if user_choice == 1:
            name, numbers, groups, email = add_new_contact()
            id = s.add_contact(name, numbers, groups, email)
            print(f"User was added successfully! Your id is {id}")
        if user_choice == 2:
            id = get_id_from_user()
            contact = s.get_contact(id)
            if contact:
                print(contact)
        if user_choice == 3:
            s.display_contacts()
        if user_choice == 4:
            contacts = s.display_contacts()
            id_person = input(f"Enter number between 1 - {len(contacts)}")
            while not 1 <= int(id_person) <= len(contacts):
                print("You insert wrong number!")
                id_person = input(f"Enter number between 1 - {len(contacts)}")
            result = s.remove_contact(int(id_person))
            print("The user was removed successfully!" if result else "There was an error during the process!")
        if user_choice == 5:
            name = get_name_from_user()
            result = s.search_person_by_name(name)
            print_list(result, "contact with that name")
        if user_choice == 6:
            phone = get_phone_from_user()
            phone_result = s.search_person_by_phone(phone)
            print_list(phone_result, "contact with that phone")
        if user_choice == 7:
            group = get_name_from_user()
            groups = s.filter_by_groups(group)
            print_list(groups, "groups")
        if user_choice == 8:
            email = get_an_email_from_user()
            print_list(s.filter_by_email(email), "contact with that email")
        if user_choice == 9:
            with_email = get_y_or_n_from_user("Do you want users with email?")
            print_list(s.filter_by_existing_email(with_email), "contacts")
        if user_choice == 10:
            with_name = get_y_or_n_from_user("Do you want to filter by name: ")
            with_phone = get_y_or_n_from_user("Do you want to filter by phone: ")
            with_numbers = get_y_or_n_from_user("Do you want to filter by email: ")
            with_group = get_y_or_n_from_user("Do  you want to filter by group: ")
            name = phone = numbers = group = None
            if with_name:
                name = get_name_from_user()
            if with_phone:
                phone = get_phone_from_user()
            if with_numbers:
                numbers = get_numbers_from_user()
            if with_group:
                group = get_groups_from_user()
            all_filtered_contacts = s.filter_by_conditions(name, phone, numbers, group)
            print_list(all_filtered_contacts, "contacts")
        if user_choice == 11:
            gathered = s.gathering_by_domain()
            for i, domain in enumerate(gathered):
                print(f"{i + 1}: {domain}")
                for j, contact in enumerate(gathered[domain]):
                    print(f"\t{j + 1}: {contact}")
        if user_choice == 12:
            name_of_file = get_name_from_user()
            s.save_contacts_to_file(name_of_file)
        if user_choice == 13:
            name_of_file = get_name_from_user()
            s.read_contacts_from_file(name_of_file)
        if user_choice == 14:
            print(f"Now you have {s.get_num_of_contacts()} contacts in the system!")
        if user_choice == 15:
            s.get_num_of_each_group()
        if user_choice == 16:
            all_contacts = s.get_num_of_contacts()
            print(f"You have {s.get_percents_of_people_with_email()}% with email in the system!")
        if user_choice == 17:
            my_dict = s.get_percent_of_each_email()
            for i, item in enumerate(my_dict):
                print(f"{i + 1}: domain: /t {item} {my_dict[item]}")
        if user_choice == 18:
            my_dict = s.gathering_contacts_by_theirs_groups()
            for i, item in enumerate(my_dict):
                print(f"{i + 1}: group: {item}")
                if my_dict[item]:
                    for i, item1 in enumerate(my_dict[item]):
                        print(f"/t {item1}")

if __name__ == "__main__":
    main()