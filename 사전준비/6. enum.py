from enum import Enum, auto


class State(Enum):
    NEW = auto()
    FAILED = auto()
    DELETED = auto()

    def __str__(self) -> str:
        return self.name

    @property
    def val(self) -> int:
        return self.value


print(State.NEW, State.NEW.val)
