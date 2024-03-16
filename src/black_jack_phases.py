from

class BlackJackShuffleState(State):

    def __init__(self, game_state: BlackJackGameState) -> None:
        self.__game_state = game_state

    def run(self):
        clear_console()

        print("The dealer shuffles the deck...")

        choice = input("Choose an option: ")

        return None
