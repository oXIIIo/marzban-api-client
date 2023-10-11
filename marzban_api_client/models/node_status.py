from enum import Enum


class NodeStatus(str, Enum):
    CONNECTED = "connected"
    CONNECTING = "connecting"
    DISABLED = "disabled"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)
