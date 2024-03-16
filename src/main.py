import os

from game_types import *
from player import Player
from state_machine import State, StateMachine
from black_jack import BlackJackGame, BlackJackGameState, BLACK_JACK_TABLES
from utilities import clear_console, render_menu

class CasinoMainMenu(State):

    def __init__(self, player: Player) -> None:
        self.__player = player

        self.__menu = MenuData(
            "Welcome to the Casino!", {1: "Play Blackjack", 2: "Quit"}
        )

    def run(self) -> State | None:
        clear_console()

        choice = render_menu(self.__menu)

        if self.__menu.options[choice] == "Play Blackjack":
            return BlackJackTableMenu(self.__player)
        elif self.__menu.options[choice] == "Quit":
            return None


class BlackJackTableMenu(State):

    def __init__(self, player: Player) -> None:
        self.__player = player

        self.__menu_data = MenuData(
            "Choose a game table:",
            {
                **{i: str(table) for i, table in BLACK_JACK_TABLES.items()},
                len(BLACK_JACK_TABLES) + 1: "Back",
            },
        )

    def run(self) -> State | None:
        clear_console()

        choice = render_menu(self.__menu_data)

        if choice in BLACK_JACK_TABLES.keys():
            game_state = BLACK_JACK_TABLES[choice]
            game_state.sit_player_at_table(self.__player)
            BlackJackGame(game_state)
            return CasinoMainMenu(self.__player)
        elif self.__menu_data.options[choice] == "Back":
            return CasinoMainMenu(self.__player)


if __name__ == "__main__":
    player = Player(10_000)
    state_machine = StateMachine(CasinoMainMenu(player))
    state_machine.run()
    clear_console()
