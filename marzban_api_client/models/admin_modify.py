from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminModify")


@_attrs_define
class AdminModify:
    """
    Attributes:
        is_sudo (bool):
        password (Union[Unset, str]):
        telegram_id (Union[Unset, int]):
        discord_webhook (Union[Unset, str]):
    """

    is_sudo: bool
    password: Union[Unset, str] = UNSET
    telegram_id: Union[Unset, int] = UNSET
    discord_webhook: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_sudo = self.is_sudo

        password = self.password

        telegram_id = self.telegram_id

        discord_webhook = self.discord_webhook

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "is_sudo": is_sudo,
            }
        )
        if password is not UNSET:
            field_dict["password"] = password
        if telegram_id is not UNSET:
            field_dict["telegram_id"] = telegram_id
        if discord_webhook is not UNSET:
            field_dict["discord_webhook"] = discord_webhook

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_sudo = d.pop("is_sudo")

        password = d.pop("password", UNSET)

        telegram_id = d.pop("telegram_id", UNSET)

        discord_webhook = d.pop("discord_webhook", UNSET)

        admin_modify = cls(
            is_sudo=is_sudo,
            password=password,
            telegram_id=telegram_id,
            discord_webhook=discord_webhook,
        )

        admin_modify.additional_properties = d
        return admin_modify

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
