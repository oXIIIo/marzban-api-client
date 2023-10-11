from enum import Enum


class ProxyTypes(str, Enum):
    SHADOWSOCKS = "shadowsocks"
    TROJAN = "trojan"
    VLESS = "vless"
    VMESS = "vmess"

    def __str__(self) -> str:
        return str(self.value)
