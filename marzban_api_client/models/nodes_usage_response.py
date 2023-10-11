from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.node_usage_response import NodeUsageResponse


T = TypeVar("T", bound="NodesUsageResponse")


@_attrs_define
class NodesUsageResponse:
    """
    Attributes:
        usages (List['NodeUsageResponse']):
    """

    usages: List["NodeUsageResponse"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        usages = []
        for usages_item_data in self.usages:
            usages_item = usages_item_data.to_dict()

            usages.append(usages_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "usages": usages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.node_usage_response import NodeUsageResponse

        d = src_dict.copy()
        usages = []
        _usages = d.pop("usages")
        for usages_item_data in _usages:
            usages_item = NodeUsageResponse.from_dict(usages_item_data)

            usages.append(usages_item)

        nodes_usage_response = cls(
            usages=usages,
        )

        nodes_usage_response.additional_properties = d
        return nodes_usage_response

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
