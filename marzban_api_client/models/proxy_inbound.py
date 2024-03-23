from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.proxy_types import ProxyTypes

T = TypeVar("T", bound="ProxyInbound")


@_attrs_define
class ProxyInbound:
    """
    Attributes:
        tag (str):
        protocol (ProxyTypes): An enumeration.
        network (str):
        tls (str):
        port (Union[int, str]):
    """

    tag: str
    protocol: ProxyTypes
    network: str
    tls: str
    port: Union[int, str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tag = self.tag

        protocol = self.protocol.value

        network = self.network

        tls = self.tls

        port: Union[int, str]
        port = self.port

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tag": tag,
                "protocol": protocol,
                "network": network,
                "tls": tls,
                "port": port,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tag = d.pop("tag")

        protocol = ProxyTypes(d.pop("protocol"))

        network = d.pop("network")

        tls = d.pop("tls")

        def _parse_port(data: object) -> Union[int, str]:
            return cast(Union[int, str], data)

        port = _parse_port(d.pop("port"))

        proxy_inbound = cls(
            tag=tag,
            protocol=protocol,
            network=network,
            tls=tls,
            port=port,
        )

        proxy_inbound.additional_properties = d
        return proxy_inbound

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
