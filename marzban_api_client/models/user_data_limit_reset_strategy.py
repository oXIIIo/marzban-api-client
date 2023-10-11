from enum import Enum


class UserDataLimitResetStrategy(str, Enum):
    DAY = "day"
    MONTH = "month"
    NO_RESET = "no_reset"
    WEEK = "week"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
