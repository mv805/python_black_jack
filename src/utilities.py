import os
from game_types import MenuData

def clear_console():
    """
    Clears the console.

    This function uses the "cls" command for Windows and the "clear" command for other operating systems.
    """
    os.system("cls" if os.name == "nt" else "clear")


def render_menu(menu_data: MenuData) -> int:
    """
    Renders a menu and gets the user's choice.

    This function prints the title and options of the menu, then prompts the user to choose an option.
    It keeps prompting the user until they enter a valid option.

    Parameters:
        menu_data (MenuData): The data for the menu.

    Returns:
        int: The option chosen by the user.
    """
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
