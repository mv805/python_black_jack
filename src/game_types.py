from typing import Dict


class MenuData:
    """
    Represents a menu with a title and a set of options.

    Attributes:
        title (str): The title of the menu.
        menu_options (Dict[int, str]): A dictionary of menu options, where the key is the option number and the value is the option text.
    """

    def __init__(self, title: str, menu_options: Dict[int, str]) -> None:
        self.__title = title
        self.__options = menu_options

    @property
    def options(self):
        """
        Get the menu options.

        Returns:
            Dict[int, str]: A dictionary of menu options, where the key is the option number and the value is the option text.
        """
        return self.__options

    @property
    def title(self):
        """
        Get the title of the menu.

        Returns:
            str: The title of the menu.
        """
        return self.__title
