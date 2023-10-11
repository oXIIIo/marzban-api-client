from enum import Enum


class ProxyHostALPN(str, Enum):
    H2 = "h2"
    H2HTTP1_1 = "h2,http/1.1"
    HTTP1_1 = "http/1.1"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
