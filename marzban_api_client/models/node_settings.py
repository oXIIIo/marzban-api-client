from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NodeSettings")


@_attrs_define
class NodeSettings:
    """
    Attributes:
        certificate (str):
        min_node_version (Union[Unset, str]):  Default: 'v0.2.0'.
    """

    certificate: str
    min_node_version: Union[Unset, str] = "v0.2.0"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        certificate = self.certificate

        min_node_version = self.min_node_version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "certificate": certificate,
            }
        )
        if min_node_version is not UNSET:
            field_dict["min_node_version"] = min_node_version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        certificate = d.pop("certificate")

        min_node_version = d.pop("min_node_version", UNSET)

        node_settings = cls(
            certificate=certificate,
            min_node_version=min_node_version,
        )

        node_settings.additional_properties = d
        return node_settings

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
