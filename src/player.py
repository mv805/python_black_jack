class InsufficientPlayerFunds(Exception):
    """Raised when the player goes bankrupt."""
    pass


class Player:
    """
    Represents a player in a blackjack game.

    Attributes:
        __money (int): The amount of cash the player has.
        cash (property): A property that gets the amount of money the player has.

    Methods:
        give_money: Adds a specified amount of money to the player's cash.
        take_money: Subtracts a specified amount of money from the player's cash.
    """

    def __init__(self, starting_funds: int) -> None:
        """
        Initializes a new instance of the Player class.

        Parameters:
            starting_funds (int): The starting amount of money for the player.

        Raises:
            ValueError: If starting_funds is None.
        """
        if starting_funds is None:
            raise ValueError("You must provide a starting cash amount for the player.")
        self.__money = starting_funds

    @property
    def cash(self):
        """
        Gets the current amount of money the player has.

        Returns:
            int: The amount of money the player has.
        """
        return self.__money

    def give_money(self, amount: int):
        """
        Adds a specified amount of money to the player's cash.

        Parameters:
            amount (int): The amount of money to add.

        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("The cash amount given cannot be negative.")
        self.__money += amount

    def take_money(self, amount: int):
        """
        Subtracts a specified amount of money from the player's cash.

        Parameters:
            amount (int): The amount of money to subtract.

        Raises:
            ValueError: If the amount is negative.
            InsufficientPlayerFunds: If the player does not have enough cash.
        """
        if amount < 0:
            raise ValueError("The cash amount taken cannot be negative.")
        if self.__money - amount < 0:
            raise InsufficientPlayerFunds("Cannot take this amount. The player does not have enough cash.")

        self.__money -= amount
