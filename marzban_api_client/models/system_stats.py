from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SystemStats")


@_attrs_define
class SystemStats:
    """
    Attributes:
        version (str):
        mem_total (int):
        mem_used (int):
        cpu_cores (int):
        cpu_usage (float):
        total_user (int):
        users_active (int):
        incoming_bandwidth (int):
        outgoing_bandwidth (int):
        incoming_bandwidth_speed (int):
        outgoing_bandwidth_speed (int):
    """

    version: str
    mem_total: int
    mem_used: int
    cpu_cores: int
    cpu_usage: float
    total_user: int
    users_active: int
    incoming_bandwidth: int
    outgoing_bandwidth: int
    incoming_bandwidth_speed: int
    outgoing_bandwidth_speed: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        version = self.version

        mem_total = self.mem_total

        mem_used = self.mem_used

        cpu_cores = self.cpu_cores

        cpu_usage = self.cpu_usage

        total_user = self.total_user

        users_active = self.users_active

        incoming_bandwidth = self.incoming_bandwidth

        outgoing_bandwidth = self.outgoing_bandwidth

        incoming_bandwidth_speed = self.incoming_bandwidth_speed

        outgoing_bandwidth_speed = self.outgoing_bandwidth_speed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version": version,
                "mem_total": mem_total,
                "mem_used": mem_used,
                "cpu_cores": cpu_cores,
                "cpu_usage": cpu_usage,
                "total_user": total_user,
                "users_active": users_active,
                "incoming_bandwidth": incoming_bandwidth,
                "outgoing_bandwidth": outgoing_bandwidth,
                "incoming_bandwidth_speed": incoming_bandwidth_speed,
                "outgoing_bandwidth_speed": outgoing_bandwidth_speed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        version = d.pop("version")

        mem_total = d.pop("mem_total")

        mem_used = d.pop("mem_used")

        cpu_cores = d.pop("cpu_cores")

        cpu_usage = d.pop("cpu_usage")

        total_user = d.pop("total_user")

        users_active = d.pop("users_active")

        incoming_bandwidth = d.pop("incoming_bandwidth")

        outgoing_bandwidth = d.pop("outgoing_bandwidth")

        incoming_bandwidth_speed = d.pop("incoming_bandwidth_speed")

        outgoing_bandwidth_speed = d.pop("outgoing_bandwidth_speed")

        system_stats = cls(
            version=version,
            mem_total=mem_total,
            mem_used=mem_used,
            cpu_cores=cpu_cores,
            cpu_usage=cpu_usage,
            total_user=total_user,
            users_active=users_active,
            incoming_bandwidth=incoming_bandwidth,
            outgoing_bandwidth=outgoing_bandwidth,
            incoming_bandwidth_speed=incoming_bandwidth_speed,
            outgoing_bandwidth_speed=outgoing_bandwidth_speed,
        )

        system_stats.additional_properties = d
        return system_stats

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
