from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.proxy_inbound import ProxyInbound


T = TypeVar("T", bound="GetInboundsResponseGetInboundsApiInboundsGet")


@_attrs_define
class GetInboundsResponseGetInboundsApiInboundsGet:
    """ """

    additional_properties: Dict[str, List["ProxyInbound"]] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = []
            for additional_property_item_data in prop:
                additional_property_item = additional_property_item_data.to_dict()
                field_dict[prop_name].append(additional_property_item)

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.proxy_inbound import ProxyInbound

        d = src_dict.copy()
        get_inbounds_response_get_inbounds_api_inbounds_get = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = []
            _additional_property = prop_dict
            for additional_property_item_data in _additional_property:
                additional_property_item = ProxyInbound.from_dict(additional_property_item_data)

                additional_property.append(additional_property_item)

            additional_properties[prop_name] = additional_property

        get_inbounds_response_get_inbounds_api_inbounds_get.additional_properties = additional_properties
        return get_inbounds_response_get_inbounds_api_inbounds_get

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> List["ProxyInbound"]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: List["ProxyInbound"]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
