class Player:
    
    def __init__(self, starting_funds: int) -> None:
        self._money = starting_funds
        
    @property
    def cash(self):
        return self._money