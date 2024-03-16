from card import PlayingCard, Card
from abc import abstractmethod, ABC


class Deck(ABC):

    def __init__(self, card_type: Card) -> None:
        self._card_type = card_type
        self._deck = self._build_deck(self._card_type)

    @abstractmethod
    def _build_deck(self) -> list[Card]:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @property
    def card_type(self) -> Card:
        return self._card_type


class PlayingCardDeck(Deck):

    _arrangement = {
        "suits": "♠♣♦♥",
        "numbers": [2, 3, 4, 5, 6, 7, 8, 9, 10],
        "faces": "JQKA",
    }

    def __init__(self) -> None:
        super().__init__(PlayingCard)

    @classmethod
    def _build_deck(cls, playing_card: PlayingCard) -> list[PlayingCard]:
        deck = []
        for suit in cls._arrangement["suits"]:
            for number in cls._arrangement["numbers"]:
                deck.append(playing_card(str(number), suit))
            for face in cls._arrangement["faces"]:
                deck.append(playing_card(face, suit))
        return deck

    def __str__(self) -> str:
        deck_readout = ""

        for card in self._deck:
            deck_readout += f"{card.value} of {card.suit}\n"

        deck_readout += f"{len(self._deck)} cards in this deck.\n"

        for suit in self._arrangement["suits"]:
            deck_readout += f"{len([card for card in self._deck if card.suit == suit])} ranks of {suit}.\n"
        return deck_readout


if __name__ == "__main__":

    test_deck = PlayingCardDeck()
    print(test_deck.card_type)
