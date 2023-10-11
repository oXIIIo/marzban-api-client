from enum import Enum


class ProxyHostFingerprint(str, Enum):
    ANDROID = "android"
    CHROME = "chrome"
    EDGE = "edge"
    FIREFOX = "firefox"
    IOS = "ios"
    QQ = "qq"
    RANDOM = "random"
    RANDOMIZED = "randomized"
    SAFARI = "safari"
    VALUE_0 = ""
    VALUE_7 = "360"

    def __str__(self) -> str:
        return str(self.value)
