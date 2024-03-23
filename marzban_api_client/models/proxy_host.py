from typing import Any, Dict, List, Type, TypeVar, Union, cast

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
        port (Union[None, Unset, int]):
        sni (Union[None, Unset, str]):
        host (Union[None, Unset, str]):
        path (Union[None, Unset, str]):
        security (Union[Unset, ProxyHostSecurity]): An enumeration. Default: ProxyHostSecurity.INBOUND_DEFAULT.
        alpn (Union[Unset, ProxyHostALPN]): An enumeration. Default: ProxyHostALPN.VALUE_0.
        fingerprint (Union[Unset, ProxyHostFingerprint]): An enumeration. Default: ProxyHostFingerprint.VALUE_0.
        allowinsecure (Union[Unset, bool]):
        is_disabled (Union[Unset, bool]):
        mux_enable (Union[Unset, bool]):
        fragment_setting (Union[None, Unset, str]):
    """

    remark: str
    address: str
    port: Union[None, Unset, int] = UNSET
    sni: Union[None, Unset, str] = UNSET
    host: Union[None, Unset, str] = UNSET
    path: Union[None, Unset, str] = UNSET
    security: Union[Unset, ProxyHostSecurity] = ProxyHostSecurity.INBOUND_DEFAULT
    alpn: Union[Unset, ProxyHostALPN] = ProxyHostALPN.VALUE_0
    fingerprint: Union[Unset, ProxyHostFingerprint] = ProxyHostFingerprint.VALUE_0
    allowinsecure: Union[Unset, bool] = UNSET
    is_disabled: Union[Unset, bool] = UNSET
    mux_enable: Union[Unset, bool] = UNSET
    fragment_setting: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        remark = self.remark

        address = self.address

        port: Union[None, Unset, int]
        if isinstance(self.port, Unset):
            port = UNSET
        else:
            port = self.port

        sni: Union[None, Unset, str]
        if isinstance(self.sni, Unset):
            sni = UNSET
        else:
            sni = self.sni

        host: Union[None, Unset, str]
        if isinstance(self.host, Unset):
            host = UNSET
        else:
            host = self.host

        path: Union[None, Unset, str]
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

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

        mux_enable = self.mux_enable

        fragment_setting: Union[None, Unset, str]
        if isinstance(self.fragment_setting, Unset):
            fragment_setting = UNSET
        else:
            fragment_setting = self.fragment_setting

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
        if path is not UNSET:
            field_dict["path"] = path
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
        if mux_enable is not UNSET:
            field_dict["mux_enable"] = mux_enable
        if fragment_setting is not UNSET:
            field_dict["fragment_setting"] = fragment_setting

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        remark = d.pop("remark")

        address = d.pop("address")

        def _parse_port(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        port = _parse_port(d.pop("port", UNSET))

        def _parse_sni(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sni = _parse_sni(d.pop("sni", UNSET))

        def _parse_host(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        host = _parse_host(d.pop("host", UNSET))

        def _parse_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        path = _parse_path(d.pop("path", UNSET))

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

        mux_enable = d.pop("mux_enable", UNSET)

        def _parse_fragment_setting(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        fragment_setting = _parse_fragment_setting(d.pop("fragment_setting", UNSET))

        proxy_host = cls(
            remark=remark,
            address=address,
            port=port,
            sni=sni,
            host=host,
            path=path,
            security=security,
            alpn=alpn,
            fingerprint=fingerprint,
            allowinsecure=allowinsecure,
            is_disabled=is_disabled,
            mux_enable=mux_enable,
            fragment_setting=fragment_setting,
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
