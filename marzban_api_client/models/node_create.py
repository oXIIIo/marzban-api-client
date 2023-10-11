from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NodeCreate")


@_attrs_define
class NodeCreate:
    """
    Attributes:
        name (str):
        address (str):
        certificate (str):
        port (Union[Unset, int]):  Default: 62050.
        api_port (Union[Unset, int]):  Default: 62051.
        usage_coefficient (Union[Unset, float]):  Default: 1.0.
        add_as_new_host (Union[Unset, bool]):  Default: True.
    """

    name: str
    address: str
    certificate: str
    port: Union[Unset, int] = 62050
    api_port: Union[Unset, int] = 62051
    usage_coefficient: Union[Unset, float] = 1.0
    add_as_new_host: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        address = self.address
        certificate = self.certificate
        port = self.port
        api_port = self.api_port
        usage_coefficient = self.usage_coefficient
        add_as_new_host = self.add_as_new_host

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "address": address,
                "certificate": certificate,
            }
        )
        if port is not UNSET:
            field_dict["port"] = port
        if api_port is not UNSET:
            field_dict["api_port"] = api_port
        if usage_coefficient is not UNSET:
            field_dict["usage_coefficient"] = usage_coefficient
        if add_as_new_host is not UNSET:
            field_dict["add_as_new_host"] = add_as_new_host

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        address = d.pop("address")

        certificate = d.pop("certificate")

        port = d.pop("port", UNSET)

        api_port = d.pop("api_port", UNSET)

        usage_coefficient = d.pop("usage_coefficient", UNSET)

        add_as_new_host = d.pop("add_as_new_host", UNSET)

        node_create = cls(
            name=name,
            address=address,
            certificate=certificate,
            port=port,
            api_port=api_port,
            usage_coefficient=usage_coefficient,
            add_as_new_host=add_as_new_host,
        )

        node_create.additional_properties = d
        return node_create

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
