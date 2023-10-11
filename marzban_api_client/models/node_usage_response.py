from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NodeUsageResponse")


@_attrs_define
class NodeUsageResponse:
    """
    Attributes:
        node_name (str):
        uplink (int):
        downlink (int):
        node_id (Union[Unset, int]):
    """

    node_name: str
    uplink: int
    downlink: int
    node_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        node_name = self.node_name
        uplink = self.uplink
        downlink = self.downlink
        node_id = self.node_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "node_name": node_name,
                "uplink": uplink,
                "downlink": downlink,
            }
        )
        if node_id is not UNSET:
            field_dict["node_id"] = node_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        node_name = d.pop("node_name")

        uplink = d.pop("uplink")

        downlink = d.pop("downlink")

        node_id = d.pop("node_id", UNSET)

        node_usage_response = cls(
            node_name=node_name,
            uplink=uplink,
            downlink=downlink,
            node_id=node_id,
        )

        node_usage_response.additional_properties = d
        return node_usage_response

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
