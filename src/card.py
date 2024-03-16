from dataclasses import dataclass

@dataclass(frozen=True)
class Card:
    pass

@dataclass(frozen=True)
class PlayingCard(Card):
    value: str
    suit: str
    
    def __post_init__(self):
        if not (self.value in "JKQA" or 2 <= int(self.value) <= 10):
            raise ValueError("Value must be between 2 and 10 or a face card.")
        elif self.suit not in "♠♣♦♥":
            raise ValueError("Value must be between 2 and 10 or a face card.")

if __name__ == "__main__":
    three_card = PlayingCard("3", "♠")
    
    print(three_card.value, three_card.suit)
