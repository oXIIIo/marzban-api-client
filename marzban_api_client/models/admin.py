from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Admin")


@_attrs_define
class Admin:
    """
    Attributes:
        username (str):
        is_sudo (bool):
        telegram_id (Union[Unset, int]):
        discord_webhook (Union[Unset, str]):
    """

    username: str
    is_sudo: bool
    telegram_id: Union[Unset, int] = UNSET
    discord_webhook: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        username = self.username

        is_sudo = self.is_sudo

        telegram_id = self.telegram_id

        discord_webhook = self.discord_webhook

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
                "is_sudo": is_sudo,
            }
        )
        if telegram_id is not UNSET:
            field_dict["telegram_id"] = telegram_id
        if discord_webhook is not UNSET:
            field_dict["discord_webhook"] = discord_webhook

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        username = d.pop("username")

        is_sudo = d.pop("is_sudo")

        telegram_id = d.pop("telegram_id", UNSET)

        discord_webhook = d.pop("discord_webhook", UNSET)

        admin = cls(
            username=username,
            is_sudo=is_sudo,
            telegram_id=telegram_id,
            discord_webhook=discord_webhook,
        )

        admin.additional_properties = d
        return admin

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
