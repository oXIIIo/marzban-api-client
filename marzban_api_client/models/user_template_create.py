from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_template_create_inbounds import UserTemplateCreateInbounds


T = TypeVar("T", bound="UserTemplateCreate")


@_attrs_define
class UserTemplateCreate:
    """
    Attributes:
        name (Union[Unset, None, str]):
        data_limit (Union[Unset, int]): data_limit can be 0 or greater
        expire_duration (Union[Unset, int]): expire_duration can be 0 or greater in seconds
        username_prefix (Union[Unset, str]):
        username_suffix (Union[Unset, str]):
        inbounds (Union[Unset, UserTemplateCreateInbounds]):
    """

    name: Union[Unset, None, str] = UNSET
    data_limit: Union[Unset, int] = UNSET
    expire_duration: Union[Unset, int] = UNSET
    username_prefix: Union[Unset, str] = UNSET
    username_suffix: Union[Unset, str] = UNSET
    inbounds: Union[Unset, "UserTemplateCreateInbounds"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        data_limit = self.data_limit
        expire_duration = self.expire_duration
        username_prefix = self.username_prefix
        username_suffix = self.username_suffix
        inbounds: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.inbounds, Unset):
            inbounds = self.inbounds.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if data_limit is not UNSET:
            field_dict["data_limit"] = data_limit
        if expire_duration is not UNSET:
            field_dict["expire_duration"] = expire_duration
        if username_prefix is not UNSET:
            field_dict["username_prefix"] = username_prefix
        if username_suffix is not UNSET:
            field_dict["username_suffix"] = username_suffix
        if inbounds is not UNSET:
            field_dict["inbounds"] = inbounds

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_template_create_inbounds import UserTemplateCreateInbounds

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        data_limit = d.pop("data_limit", UNSET)

        expire_duration = d.pop("expire_duration", UNSET)

        username_prefix = d.pop("username_prefix", UNSET)

        username_suffix = d.pop("username_suffix", UNSET)

        _inbounds = d.pop("inbounds", UNSET)
        inbounds: Union[Unset, UserTemplateCreateInbounds]
        if isinstance(_inbounds, Unset):
            inbounds = UNSET
        else:
            inbounds = UserTemplateCreateInbounds.from_dict(_inbounds)

        user_template_create = cls(
            name=name,
            data_limit=data_limit,
            expire_duration=expire_duration,
            username_prefix=username_prefix,
            username_suffix=username_suffix,
            inbounds=inbounds,
        )

        user_template_create.additional_properties = d
        return user_template_create

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
