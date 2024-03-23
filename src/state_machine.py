from __future__ import annotations

class StateMachine:
    """
    A class representing a state machine.

    Attributes:
        state: The current state of the state machine.

    Methods:
        __init__(self, initial_state): Initializes the state machine with an initial state.
        change_state(self, new_state): Changes the state of the state machine to a new state.
        run(self): Runs the state machine until the state is None.
    """

    def __init__(self, initial_state):
        """
        Initializes the state machine with an initial state.

        Args:
            initial_state: The initial state of the state machine.
        """
        self.state = initial_state

    def change_state(self, new_state) -> None:
        """
        Changes the state of the state machine to a new state.

        Args:
            new_state: The new state to change to.
        """
        self.state = new_state

    def run(self) -> None:
        """
        Runs the state machine until the state is None.
        """
        while self.state is not None:
            self.change_state(self.state.run())


class State:
    """
    Represents a state in the state machine.

    Each state should inherit from this base class and implement the `run` method.

    Attributes:
        None

    Methods:
        run: Executes the logic of the state.

    Returns:
        State or None: The next state to transition to, or None if there is no transition.
    """

    def run(self) -> State | None:
        raise NotImplementedError
