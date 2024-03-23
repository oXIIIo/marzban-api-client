from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.user_usage_response import UserUsageResponse


T = TypeVar("T", bound="UserUsagesResponse")


@_attrs_define
class UserUsagesResponse:
    """
    Attributes:
        username (str):
        usages (List['UserUsageResponse']):
    """

    username: str
    usages: List["UserUsageResponse"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        username = self.username

        usages = []
        for usages_item_data in self.usages:
            usages_item = usages_item_data.to_dict()
            usages.append(usages_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
                "usages": usages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_usage_response import UserUsageResponse

        d = src_dict.copy()
        username = d.pop("username")

        usages = []
        _usages = d.pop("usages")
        for usages_item_data in _usages:
            usages_item = UserUsageResponse.from_dict(usages_item_data)

            usages.append(usages_item)

        user_usages_response = cls(
            username=username,
            usages=usages,
        )

        user_usages_response.additional_properties = d
        return user_usages_response

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
