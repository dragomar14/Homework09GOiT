from sanitize_phone_number import sanitize_phone_number
from input_error import input_error

directory = {}


def say_hello(wdh):
    return "How can I help you?"


def say_goodbye(wdh):
    return "Good bye!"


def show_phone(wdh):
    name = " ".join(wdh)
    return directory[name.title()]


def help(wdh):
    rules = """List of commands:
    1) if you want to add new contact, please write command: add {name} {phone number}
    2) if you want to change contact, please write command: change {name} {phone number}
    3) if you want to see the phone of contact, please write command: phone {name}
    4) if you want to see all contacts, please write command: show all
    5) if you want to say goodbye, please write one of these commands: good bye / close / exit
    6) if you want to say hello, please write command: hello
    """
    return rules


@input_error
def set_number(wdh):
    phone = str(wdh[-1])
    name = " ".join(wdh[:-1])
    phone = sanitize_phone_number(phone)
    if phone:
        directory[name.title()] = phone
        return f"Contact {name.title()} was created/updated"
    else:
        return ""


@input_error
def show_all(wdh):
    if len(directory) == 0:
        return "Directory is empty"
    text = ""
    for name, phone in directory.items():
        text += f"{name} {phone}\n"
    return text.strip()


commands ={
    ("add", "change"): set_number,
    "phone": show_phone,
    "show all": show_all,
    "hello": say_hello,
    ("good bye", "close", "exit"): say_goodbye,
    "help": help}