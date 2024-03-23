import os

from game_types import MenuData
from player import Player
from state_machine import State, StateMachine
from black_jack import BlackJackGame, BLACK_JACK_TABLES
from utilities import clear_console, render_menu

class CasinoMainMenu(State):
    """
    Represents the main menu of the casino.

    Attributes:
        __player (Player): The player who is at the main menu.
        __menu (MenuData): The data for the main menu.

    Methods:
        run: Runs the main menu and returns the next state based on the player's choice.
    """

    def __init__(self, player: Player) -> None:
        """
        Initializes a new instance of the CasinoMainMenu class.

        Parameters:
            player (Player): The player who is at the main menu.
        """
        self.__player = player

        self.__menu = MenuData(
            "Welcome to the Casino!", {1: "Play Blackjack", 2: "Quit"}
        )

    def run(self) -> State | None:
        """
        Runs the main menu and returns the next state based on the player's choice.

        Returns:
            State | None: The next state, or None if the player chose to quit.
        """
        clear_console()

        choice = render_menu(self.__menu)

        if self.__menu.options[choice] == "Play Blackjack":
            return BlackJackTableMenu(self.__player)
        elif self.__menu.options[choice] == "Quit":
            return None


class BlackJackTableMenu(State):
    """
    Represents the blackjack table menu of the casino.

    Attributes:
        __player (Player): The player who is at the blackjack table menu.
        __menu_data (MenuData): The data for the blackjack table menu.

    Methods:
        run: Runs the blackjack table menu and returns the next state based on the player's choice.
    """

    def __init__(self, player: Player) -> None:
        """
        Initializes a new instance of the BlackJackTableMenu class.

        Parameters:
            player (Player): The player who is at the blackjack table menu.
        """
        self.__player = player

        self.__menu_data = MenuData(
            "Choose a game table:",
            {
                **{i: str(table) for i, table in BLACK_JACK_TABLES.items()},
                len(BLACK_JACK_TABLES) + 1: "Back",
            },
        )

    def run(self) -> State | None:
        """
        Runs the blackjack table menu and returns the next state based on the player's choice.

        Returns:
            State | None: The next state, or None if the player chose to go back.
        """
        clear_console()

        choice = render_menu(self.__menu_data)

        if choice in BLACK_JACK_TABLES.keys():
            blackjack_game_state = BLACK_JACK_TABLES[choice]
            blackjack_game_state.sit_player_at_table(self.__player)
            BlackJackGame(blackjack_game_state) #starts the game
            return CasinoMainMenu(self.__player)
        elif self.__menu_data.options[choice] == "Back":
            return CasinoMainMenu(self.__player)

def game():
    player = Player(10_000)
    state_machine = StateMachine(CasinoMainMenu(player))
    state_machine.run()    

if __name__ == "__main__":
    game()
    clear_console()
