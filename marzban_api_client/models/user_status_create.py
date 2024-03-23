from enum import Enum


class UserStatusCreate(str, Enum):
    ACTIVE = "active"
    ON_HOLD = "on_hold"

    def __str__(self) -> str:
        return str(self.value)
