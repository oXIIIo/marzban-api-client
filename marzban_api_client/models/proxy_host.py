from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.proxy_host_alpn import ProxyHostALPN
from ..models.proxy_host_fingerprint import ProxyHostFingerprint
from ..models.proxy_host_security import ProxyHostSecurity
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProxyHost")


@_attrs_define
class ProxyHost:
    """
    Attributes:
        remark (str):
        address (str):
        port (Union[Unset, None, int]):
        sni (Union[Unset, None, str]):
        host (Union[Unset, None, str]):
        security (Union[Unset, ProxyHostSecurity]): An enumeration representing the security configuration for a proxy
            host. It can have one of the following values: - `inbound_default`: Uses the default inbound security settings.
            - `none`: No specific security settings are applied. - `tls`: Employs Transport Layer Security (TLS) for secure
            communication.
             Default: ProxyHostSecurity.INBOUND_DEFAULT.
        alpn (Union[Unset, ProxyHostALPN]): The Application-Layer Protocol Negotiation (ALPN) values supported by a
            proxy host. This is an enumeration with the following possible values: - `''` (empty string): No specific ALPN
            protocol is preferred. - `h2`: Supports HTTP/2. - `http/1.1`: Supports HTTP/1.1. - `h2,http/1.1`: Supports both
            HTTP/2 and HTTP/1.1.
             Default: ProxyHostALPN.VALUE_0.
        fingerprint (Union[Unset, ProxyHostFingerprint]): The fingerprint or identity of a proxy host. This is an
            enumeration with the following possible values: - `''` (empty string): No specific fingerprint is defined. -
            `chrome`: Represents the Chrome browser. - `firefox`: Represents the Firefox browser. - `safari`: Represents the
            Safari browser. - `ios`: Represents the iOS operating system. - `android`: Represents the Android operating
            system. - `edge`: Represents the Microsoft Edge browser. - `360`: Represents the 360 Browser. - `qq`: Represents
            the QQ Browser. - `random`: A randomly selected fingerprint. - `randomized`: A randomized or dynamically
            changing fingerprint.
             Default: ProxyHostFingerprint.VALUE_0.
        allowinsecure (Union[Unset, bool]):
        is_disabled (Union[Unset, bool]):
    """

    remark: str
    address: str
    port: Union[Unset, None, int] = UNSET
    sni: Union[Unset, None, str] = UNSET
    host: Union[Unset, None, str] = UNSET
    security: Union[Unset, ProxyHostSecurity] = ProxyHostSecurity.INBOUND_DEFAULT
    alpn: Union[Unset, ProxyHostALPN] = ProxyHostALPN.VALUE_0
    fingerprint: Union[Unset, ProxyHostFingerprint] = ProxyHostFingerprint.VALUE_0
    allowinsecure: Union[Unset, bool] = UNSET
    is_disabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        remark = self.remark
        address = self.address
        port = self.port
        sni = self.sni
        host = self.host
        security: Union[Unset, str] = UNSET
        if not isinstance(self.security, Unset):
            security = self.security.value

        alpn: Union[Unset, str] = UNSET
        if not isinstance(self.alpn, Unset):
            alpn = self.alpn.value

        fingerprint: Union[Unset, str] = UNSET
        if not isinstance(self.fingerprint, Unset):
            fingerprint = self.fingerprint.value

        allowinsecure = self.allowinsecure
        is_disabled = self.is_disabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "remark": remark,
                "address": address,
            }
        )
        if port is not UNSET:
            field_dict["port"] = port
        if sni is not UNSET:
            field_dict["sni"] = sni
        if host is not UNSET:
            field_dict["host"] = host
        if security is not UNSET:
            field_dict["security"] = security
        if alpn is not UNSET:
            field_dict["alpn"] = alpn
        if fingerprint is not UNSET:
            field_dict["fingerprint"] = fingerprint
        if allowinsecure is not UNSET:
            field_dict["allowinsecure"] = allowinsecure
        if is_disabled is not UNSET:
            field_dict["is_disabled"] = is_disabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        remark = d.pop("remark")

        address = d.pop("address")

        port = d.pop("port", UNSET)

        sni = d.pop("sni", UNSET)

        host = d.pop("host", UNSET)

        _security = d.pop("security", UNSET)
        security: Union[Unset, ProxyHostSecurity]
        if isinstance(_security, Unset):
            security = UNSET
        else:
            security = ProxyHostSecurity(_security)

        _alpn = d.pop("alpn", UNSET)
        alpn: Union[Unset, ProxyHostALPN]
        if isinstance(_alpn, Unset):
            alpn = UNSET
        else:
            alpn = ProxyHostALPN(_alpn)

        _fingerprint = d.pop("fingerprint", UNSET)
        fingerprint: Union[Unset, ProxyHostFingerprint]
        if isinstance(_fingerprint, Unset):
            fingerprint = UNSET
        else:
            fingerprint = ProxyHostFingerprint(_fingerprint)

        allowinsecure = d.pop("allowinsecure", UNSET)

        is_disabled = d.pop("is_disabled", UNSET)

        proxy_host = cls(
            remark=remark,
            address=address,
            port=port,
            sni=sni,
            host=host,
            security=security,
            alpn=alpn,
            fingerprint=fingerprint,
            allowinsecure=allowinsecure,
            is_disabled=is_disabled,
        )

        proxy_host.additional_properties = d
        return proxy_host

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
