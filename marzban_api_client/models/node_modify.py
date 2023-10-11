from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.node_status import NodeStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="NodeModify")


@_attrs_define
class NodeModify:
    """
    Attributes:
        name (Union[Unset, None, str]):
        address (Union[Unset, None, str]):
        port (Union[Unset, None, int]):
        api_port (Union[Unset, None, int]):
        certificate (Union[Unset, None, str]):
        usage_coefficient (Union[Unset, None, float]):
        status (Union[Unset, None, NodeStatus]): Represents the status of a node. It is an enumeration with the
            following possible values: - `connected`: The node is currently connected. - `connecting`: The node is in the
            process of establishing a connection. - `error`: There is an error with the node. - `disabled`: The node is
            intentionally disabled and not operational.
    """

    name: Union[Unset, None, str] = UNSET
    address: Union[Unset, None, str] = UNSET
    port: Union[Unset, None, int] = UNSET
    api_port: Union[Unset, None, int] = UNSET
    certificate: Union[Unset, None, str] = UNSET
    usage_coefficient: Union[Unset, None, float] = UNSET
    status: Union[Unset, None, NodeStatus] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        address = self.address
        port = self.port
        api_port = self.api_port
        certificate = self.certificate
        usage_coefficient = self.usage_coefficient
        status: Union[Unset, None, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value if self.status else None

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
        if certificate is not UNSET:
            field_dict["certificate"] = certificate
        if usage_coefficient is not UNSET:
            field_dict["usage_coefficient"] = usage_coefficient
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        address = d.pop("address", UNSET)

        port = d.pop("port", UNSET)

        api_port = d.pop("api_port", UNSET)

        certificate = d.pop("certificate", UNSET)

        usage_coefficient = d.pop("usage_coefficient", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, None, NodeStatus]
        if _status is None:
            status = None
        elif isinstance(_status, Unset):
            status = UNSET
        else:
            status = NodeStatus(_status)

        node_modify = cls(
            name=name,
            address=address,
            port=port,
            api_port=api_port,
            certificate=certificate,
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
