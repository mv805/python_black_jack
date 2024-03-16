from __future__ import annotations

class StateMachine:
    def __init__(self, initial_state):
        self.state = initial_state

    def change_state(self, new_state) -> None:
        self.state = new_state

    def run(self) -> None:
        while self.state is not None:
            self.change_state(self.state.run())


class State:

    def run(self) -> State | None:
        raise NotImplementedError
