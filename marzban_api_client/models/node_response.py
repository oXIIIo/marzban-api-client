from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.node_status import NodeStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="NodeResponse")


@_attrs_define
class NodeResponse:
    """
    Attributes:
        name (str):
        address (str):
        certificate (str):
        id (int):
        status (NodeStatus): Represents the status of a node. It is an enumeration with the following possible values: -
            `connected`: The node is currently connected. - `connecting`: The node is in the process of establishing a
            connection. - `error`: There is an error with the node. - `disabled`: The node is intentionally disabled and not
            operational.
        port (Union[Unset, int]):  Default: 62050.
        api_port (Union[Unset, int]):  Default: 62051.
        usage_coefficient (Union[Unset, float]):  Default: 1.0.
        xray_version (Union[Unset, str]):
        message (Union[Unset, str]):
    """

    name: str
    address: str
    certificate: str
    id: int
    status: NodeStatus
    port: Union[Unset, int] = 62050
    api_port: Union[Unset, int] = 62051
    usage_coefficient: Union[Unset, float] = 1.0
    xray_version: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        address = self.address
        certificate = self.certificate
        id = self.id
        status = self.status.value

        port = self.port
        api_port = self.api_port
        usage_coefficient = self.usage_coefficient
        xray_version = self.xray_version
        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "address": address,
                "certificate": certificate,
                "id": id,
                "status": status,
            }
        )
        if port is not UNSET:
            field_dict["port"] = port
        if api_port is not UNSET:
            field_dict["api_port"] = api_port
        if usage_coefficient is not UNSET:
            field_dict["usage_coefficient"] = usage_coefficient
        if xray_version is not UNSET:
            field_dict["xray_version"] = xray_version
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        address = d.pop("address")

        certificate = d.pop("certificate")

        id = d.pop("id")

        status = NodeStatus(d.pop("status"))

        port = d.pop("port", UNSET)

        api_port = d.pop("api_port", UNSET)

        usage_coefficient = d.pop("usage_coefficient", UNSET)

        xray_version = d.pop("xray_version", UNSET)

        message = d.pop("message", UNSET)

        node_response = cls(
            name=name,
            address=address,
            certificate=certificate,
            id=id,
            status=status,
            port=port,
            api_port=api_port,
            usage_coefficient=usage_coefficient,
            xray_version=xray_version,
            message=message,
        )

        node_response.additional_properties = d
        return node_response

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
