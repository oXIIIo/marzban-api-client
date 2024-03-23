from enum import Enum


class UserStatus(str, Enum):
    ACTIVE = "active"
    DISABLED = "disabled"
    EXPIRED = "expired"
    LIMITED = "limited"
    ON_HOLD = "on_hold"

    def __str__(self) -> str:
        return str(self.value)
