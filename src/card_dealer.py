import random
from deck import Deck, Card
from abc import ABC, abstractmethod

class CardDealer:
    def __init__(self, deck_type: Deck, decks_in_play=1) -> None:
        self._decks_in_play = decks_in_play
        self._deck_type = deck_type
        self._cards_in_hand = self._fill_hand()

    def shuffle_cards(self):
        random.shuffle()
    
    @classmethod
    def _fill_hand(self) -> list[Card]:
        for deck in range(self._decks_in_play):
            new_deck = self._deck_type()
            for card in new_deck:
                pass
            
    @property
    @abstractmethod
    def cards_in_hand(self)->str:
        pass
    
    

class BlackJackDealer(CardDealer):

    def __init__(self, decks_in_play=6) -> None:
        self._decks_in_play = decks_in_play

    @property
    def cards_in_hand(self) -> str:
        return f"The BlackJack Dealer has {len(self._cards_in_hand)} in their hand at the moment."
    