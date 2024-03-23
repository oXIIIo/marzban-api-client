from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.node_status import NodeStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="NodeModify")


@_attrs_define
class NodeModify:
    """
    Example:
        {'name': 'DE node', 'address': '192.168.1.1', 'port': 62050, 'api_port': 62051, 'status': 'disabled',
            'usage_coefficient': 1.0}

    Attributes:
        name (Union[None, Unset, str]):
        address (Union[None, Unset, str]):
        port (Union[None, Unset, int]):
        api_port (Union[None, Unset, int]):
        usage_coefficient (Union[None, Unset, float]):
        status (Union[NodeStatus, None, Unset]):
    """

    name: Union[None, Unset, str] = UNSET
    address: Union[None, Unset, str] = UNSET
    port: Union[None, Unset, int] = UNSET
    api_port: Union[None, Unset, int] = UNSET
    usage_coefficient: Union[None, Unset, float] = UNSET
    status: Union[NodeStatus, None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        address: Union[None, Unset, str]
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        port: Union[None, Unset, int]
        if isinstance(self.port, Unset):
            port = UNSET
        else:
            port = self.port

        api_port: Union[None, Unset, int]
        if isinstance(self.api_port, Unset):
            api_port = UNSET
        else:
            api_port = self.api_port

        usage_coefficient: Union[None, Unset, float]
        if isinstance(self.usage_coefficient, Unset):
            usage_coefficient = UNSET
        else:
            usage_coefficient = self.usage_coefficient

        status: Union[None, Unset, str]
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, NodeStatus):
            status = self.status.value
        else:
            status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if address is not UNSET:
            field_dict["address"] = address
        if port is not UNSET:
            field_dict["port"] = port
        if api_port is not UNSET:
            field_dict["api_port"] = api_port
        if usage_coefficient is not UNSET:
            field_dict["usage_coefficient"] = usage_coefficient
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        address = _parse_address(d.pop("address", UNSET))

        def _parse_port(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        port = _parse_port(d.pop("port", UNSET))

        def _parse_api_port(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        api_port = _parse_api_port(d.pop("api_port", UNSET))

        def _parse_usage_coefficient(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        usage_coefficient = _parse_usage_coefficient(d.pop("usage_coefficient", UNSET))

        def _parse_status(data: object) -> Union[NodeStatus, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_1 = NodeStatus(data)

                return status_type_1
            except:  # noqa: E722
                pass
            return cast(Union[NodeStatus, None, Unset], data)

        status = _parse_status(d.pop("status", UNSET))

        node_modify = cls(
            name=name,
            address=address,
            port=port,
            api_port=api_port,
            usage_coefficient=usage_coefficient,
            status=status,
        )

        node_modify.additional_properties = d
        return node_modify

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
