import os

from player import Player
from state_machine import State, StateMachine
from utilities import clear_console


class PlayerNotSeatedAtTable(Exception):
    """Raised when trying to access player attributes before the player is seated at the table."""

    pass


class BlackJackGameState:

    def __init__(
        self,
        # todo: These rules will come in later
        # can_surrender=False,
        # can_double_down=False,
        # dealer_hits_soft_17=True,
        # can_split=False,
        number_of_decks=10,
        min_bet=5,
        max_bet=100,
    ) -> None:
        self.__player: Player | None = None
        # todo: These rules will come in later
        # self.__can_surrender = (can_surrender,)
        # self.__can_double_down = (can_double_down,)
        # self.__dealer_hits_soft_17 = (dealer_hits_soft_17,)
        # self.__can_split = (can_split,)
        self.__number_of_decks = number_of_decks
        self.__min_bet = min_bet
        self.__max_bet = max_bet

    @property
    def players_cash(self):
        if self.__player is not None:
            return self.__player.cash
        else:
            raise PlayerNotSeatedAtTable("No player is seated at the table.")

    def sit_player_at_table(self, player: Player):
        self.__player = player

    def __str__(self) -> str:
        return f"Table with {self.__number_of_decks} decks, min bet: ${self.__min_bet}, max bet: ${self.__max_bet}"


class BlackJackShuffleState(State):

    def __init__(self, game_state: BlackJackGameState) -> None:
        self.__game_state = game_state

    def run(self):
        clear_console()

        print("The dealer shuffles the deck...")

        choice = input("Choose an option: ")

        return None


BLACK_JACK_TABLES = {
    1: BlackJackGameState(),
    2: BlackJackGameState(number_of_decks=20, min_bet=25, max_bet=1_000),
    3: BlackJackGameState(number_of_decks=20, min_bet=100, max_bet=10_000),
    4: BlackJackGameState(number_of_decks=5, min_bet=1_000, max_bet=100_000),
}

class BlackJackGame:

    def __init__(self, game_state: BlackJackGameState) -> None:
        self.__game_state = game_state
        self.__black_jack_state_machine = StateMachine(
            BlackJackShuffleState(self.__game_state)
        )
        self.__black_jack_state_machine.run()
