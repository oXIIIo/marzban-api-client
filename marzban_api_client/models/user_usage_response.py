from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserUsageResponse")


@_attrs_define
class UserUsageResponse:
    """
    Attributes:
        node_name (str):
        used_traffic (int):
        node_id (Union[Unset, int]):
    """

    node_name: str
    used_traffic: int
    node_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        node_name = self.node_name
        used_traffic = self.used_traffic
        node_id = self.node_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "node_name": node_name,
                "used_traffic": used_traffic,
            }
        )
        if node_id is not UNSET:
            field_dict["node_id"] = node_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        node_name = d.pop("node_name")

        used_traffic = d.pop("used_traffic")

        node_id = d.pop("node_id", UNSET)

        user_usage_response = cls(
            node_name=node_name,
            used_traffic=used_traffic,
            node_id=node_id,
        )

        user_usage_response.additional_properties = d
        return user_usage_response

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
