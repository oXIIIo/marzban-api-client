from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_template_response_inbounds import UserTemplateResponseInbounds


T = TypeVar("T", bound="UserTemplateResponse")


@_attrs_define
class UserTemplateResponse:
    """
    Attributes:
        id (int):
        name (Union[None, Unset, str]):
        data_limit (Union[Unset, int]): data_limit can be 0 or greater
        expire_duration (Union[Unset, int]): expire_duration can be 0 or greater in seconds
        username_prefix (Union[Unset, str]):
        username_suffix (Union[Unset, str]):
        inbounds (Union[Unset, UserTemplateResponseInbounds]):
    """

    id: int
    name: Union[None, Unset, str] = UNSET
    data_limit: Union[Unset, int] = UNSET
    expire_duration: Union[Unset, int] = UNSET
    username_prefix: Union[Unset, str] = UNSET
    username_suffix: Union[Unset, str] = UNSET
    inbounds: Union[Unset, "UserTemplateResponseInbounds"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
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
        field_dict.update(
            {
                "id": id,
            }
        )
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
        from ..models.user_template_response_inbounds import UserTemplateResponseInbounds

        d = src_dict.copy()
        id = d.pop("id")

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        data_limit = d.pop("data_limit", UNSET)

        expire_duration = d.pop("expire_duration", UNSET)

        username_prefix = d.pop("username_prefix", UNSET)

        username_suffix = d.pop("username_suffix", UNSET)

        _inbounds = d.pop("inbounds", UNSET)
        inbounds: Union[Unset, UserTemplateResponseInbounds]
        if isinstance(_inbounds, Unset):
            inbounds = UNSET
        else:
            inbounds = UserTemplateResponseInbounds.from_dict(_inbounds)

        user_template_response = cls(
            id=id,
            name=name,
            data_limit=data_limit,
            expire_duration=expire_duration,
            username_prefix=username_prefix,
            username_suffix=username_suffix,
            inbounds=inbounds,
        )

        user_template_response.additional_properties = d
        return user_template_response

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
