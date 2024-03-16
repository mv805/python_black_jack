import os
from game_types import MenuData

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def render_menu(menu_data: MenuData) -> int:

    print(f"{menu_data.title}")
    for option, text in menu_data.options.items():
        print(f"{option}: {text}")

    while True:
        choice = input("Choose an option: ")
        try:
            choice = int(choice)
            if choice not in menu_data.options.keys():
                print("Invalid choice. Try again.")
            else:
                return choice
        except ValueError:
            print("Invalid input. Please enter a number.")
