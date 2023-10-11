from enum import Enum


class ProxyHostSecurity(str, Enum):
    INBOUND_DEFAULT = "inbound_default"
    NONE = "none"
    TLS = "tls"

    def __str__(self) -> str:
        return str(self.value)
