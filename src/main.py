import os
from player import Player
import textwrap


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def render_menu(menu_options):

    print(f"{menu_options["title"]}")
    for option, text in menu_options["options"].items():
        print(f"{option}: {text}")
    
    while True:
        choice = input("Choose an option: ")
        try:
            choice = int(choice)
            if choice not in menu_options["options"].keys():
                print("Invalid choice. Try again.")
            else:
                return choice
        except ValueError:
            print("Invalid input. Please enter a number.")


class StateMachine:
    def __init__(self, initial_state):
        self.state = initial_state

    def change_state(self, new_state):
        self.state = new_state

    def run(self):
        while self.state is not None:
            self.change_state(self.state.run())


class State:
    def run(self):
        raise NotImplementedError


class CasinoMainMenu(State):

    def __init__(self, player) -> None:
        self._player = player

        self._menu_options = {
            "title": "Welcome to the Casino!",
            "options": {1: "Play Blackjack", 2: "Quit"},
        }

    def run(self):
        clear_console()

        choice = render_menu(self._menu_options)

        if self._menu_options["options"][choice] == "Play Blackjack":
            return BlackJackTableMenu(self._player)
        elif self._menu_options["options"][choice] == "Quit":
            return None


class BlackJackGameState:

    def __init__(
        self,
        can_surrender=False,
        can_double_down=False,
        dealer_hits_soft_17=True,
        can_split=False,
        number_of_decks=10,
        min_bet=5,
        max_bet=100,
    ) -> None:
        self._player = None
        self._can_surrender = (can_surrender,)
        self._can_double_down = (can_double_down,)
        self._dealer_hits_soft_17 = (dealer_hits_soft_17,)
        self._can_split = (can_split,)
        self._number_of_decks = number_of_decks
        self._min_bet = min_bet
        self._max_bet = max_bet

    @property
    def players_cash(self):
        return self._player.cash

    def set_player(self, player):
        self._player = player
        
    def __str__(self):
        return f"Table with {self._number_of_decks} decks, min bet: ${self._min_bet}, max bet: ${self._max_bet}"


class BlackJackTableMenu(State):

    black_jack_tables = {
        1: BlackJackGameState(),
        2: BlackJackGameState(number_of_decks=20, min_bet=25, max_bet=1_000),
        3: BlackJackGameState(number_of_decks=20, min_bet=100, max_bet=10_000),
        4: BlackJackGameState(number_of_decks=5, min_bet=1_000, max_bet=100_000),
    }

    def __init__(self, player) -> None:
        self._player = player
        self._menu_options = {
            "title": "Choose a game table:",
            "options": {**BlackJackTableMenu.black_jack_tables, len(BlackJackTableMenu.black_jack_tables) + 1: "Back"},
        }
        
    def run(self):
        clear_console()

        choice = render_menu(self._menu_options)

        if choice in BlackJackTableMenu.black_jack_tables.keys():
            game_state = BlackJackTableMenu.black_jack_tables[choice]
            game_state.set_player(self._player)
            BlackJackGame(game_state)
            return CasinoMainMenu(self._player)
        elif self._menu_options["options"][choice] == "Back":
            return CasinoMainMenu(self._player)


class BlackJackShuffleState(State):

    def __init__(self, game_state: BlackJackGameState) -> None:
        self._game_state = game_state

    def run(self):
        clear_console()

        print(
            textwrap.dedent(
                f"""
        Your current money: ${self._game_state.players_cash}
        Game is playing...
        0. Quit the game
        """
            )
        )

        choice = input("Choose an option: ")

        if choice == "0":
            return None


class BlackJackGame:

    def __init__(self, game_state: BlackJackGameState) -> None:
        self._game_state = game_state
        self._black_jack_state_machine = StateMachine(
            BlackJackShuffleState(self._game_state)
        )
        self._black_jack_state_machine.run()


if __name__ == "__main__":
    player = Player(10_000)
    state_machine = StateMachine(CasinoMainMenu(player))
    state_machine.run()
    clear_console()
