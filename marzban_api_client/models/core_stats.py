from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CoreStats")


@_attrs_define
class CoreStats:
    """
    Attributes:
        version (str):
        started (bool):
        logs_websocket (str):
    """

    version: str
    started: bool
    logs_websocket: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        version = self.version
        started = self.started
        logs_websocket = self.logs_websocket

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version": version,
                "started": started,
                "logs_websocket": logs_websocket,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        version = d.pop("version")

        started = d.pop("started")

        logs_websocket = d.pop("logs_websocket")

        core_stats = cls(
            version=version,
            started=started,
            logs_websocket=logs_websocket,
        )

        core_stats.additional_properties = d
        return core_stats

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
