from bot_commands import *
from input_error import input_error


@input_error
def main():
    while True:
        command = input("Enter command: ")
        if command in (".",):
            break
        command = command.lower().split()
        for key in commands:
            if command[0] in key:
                print(commands[key](command[1:]))


if __name__ == "__main__":
    main()