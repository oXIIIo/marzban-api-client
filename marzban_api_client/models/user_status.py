from enum import Enum


class UserStatus(str, Enum):
    ACTIVE = "active"
    DISABLED = "disabled"
    EXPIRED = "expired"
    LIMITED = "limited"

    def __str__(self) -> str:
        return str(self.value)
