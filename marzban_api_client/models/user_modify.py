import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.user_data_limit_reset_strategy import UserDataLimitResetStrategy
from ..models.user_status_modify import UserStatusModify
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_modify_inbounds import UserModifyInbounds
    from ..models.user_modify_proxies import UserModifyProxies


T = TypeVar("T", bound="UserModify")


@_attrs_define
class UserModify:
    """
    Attributes:
        proxies (Union[Unset, UserModifyProxies]):
        expire (Union[Unset, None, int]):
        data_limit (Union[Unset, int]): data_limit can be 0 or greater
        data_limit_reset_strategy (Union[Unset, UserDataLimitResetStrategy]): An enumeration representing different user
            data limit reset strategies. It can have one of the following values: - `no_reset`: No automatic reset of user
            data limits. - `day`: Reset on a daily basis. - `week`: Reset on a weekly basis. - `month`: Reset on a monthly
            basis. - `year`: Reset on a yearly basis.
        inbounds (Union[Unset, UserModifyInbounds]):
        note (Union[Unset, None, str]):
        sub_updated_at (Union[Unset, None, datetime.datetime]):
        sub_last_user_agent (Union[Unset, None, str]):
        online_at (Union[Unset, None, datetime.datetime]):
        status (Union[Unset, UserStatusModify]): An enumeration representing different user status modification options.
            It can have one of the following values: - `active`: Activate the user's account. - `disabled`: Disable the
            user's account.
    """

    proxies: Union[Unset, "UserModifyProxies"] = UNSET
    expire: Union[Unset, None, int] = UNSET
    data_limit: Union[Unset, int] = UNSET
    data_limit_reset_strategy: Union[Unset, UserDataLimitResetStrategy] = UNSET
    inbounds: Union[Unset, "UserModifyInbounds"] = UNSET
    note: Union[Unset, None, str] = UNSET
    sub_updated_at: Union[Unset, None, datetime.datetime] = UNSET
    sub_last_user_agent: Union[Unset, None, str] = UNSET
    online_at: Union[Unset, None, datetime.datetime] = UNSET
    status: Union[Unset, UserStatusModify] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        proxies: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.proxies, Unset):
            proxies = self.proxies.to_dict()

        expire = self.expire
        data_limit = self.data_limit
        data_limit_reset_strategy: Union[Unset, str] = UNSET
        if not isinstance(self.data_limit_reset_strategy, Unset):
            data_limit_reset_strategy = self.data_limit_reset_strategy.value

        inbounds: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.inbounds, Unset):
            inbounds = self.inbounds.to_dict()

        note = self.note
        sub_updated_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.sub_updated_at, Unset):
            sub_updated_at = self.sub_updated_at.isoformat() if self.sub_updated_at else None

        sub_last_user_agent = self.sub_last_user_agent
        online_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.online_at, Unset):
            online_at = self.online_at.isoformat() if self.online_at else None

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if proxies is not UNSET:
            field_dict["proxies"] = proxies
        if expire is not UNSET:
            field_dict["expire"] = expire
        if data_limit is not UNSET:
            field_dict["data_limit"] = data_limit
        if data_limit_reset_strategy is not UNSET:
            field_dict["data_limit_reset_strategy"] = data_limit_reset_strategy
        if inbounds is not UNSET:
            field_dict["inbounds"] = inbounds
        if note is not UNSET:
            field_dict["note"] = note
        if sub_updated_at is not UNSET:
            field_dict["sub_updated_at"] = sub_updated_at
        if sub_last_user_agent is not UNSET:
            field_dict["sub_last_user_agent"] = sub_last_user_agent
        if online_at is not UNSET:
            field_dict["online_at"] = online_at
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_modify_inbounds import UserModifyInbounds
        from ..models.user_modify_proxies import UserModifyProxies

        d = src_dict.copy()
        _proxies = d.pop("proxies", UNSET)
        proxies: Union[Unset, UserModifyProxies]
        if isinstance(_proxies, Unset):
            proxies = UNSET
        else:
            proxies = UserModifyProxies.from_dict(_proxies)

        expire = d.pop("expire", UNSET)

        data_limit = d.pop("data_limit", UNSET)

        _data_limit_reset_strategy = d.pop("data_limit_reset_strategy", UNSET)
        data_limit_reset_strategy: Union[Unset, UserDataLimitResetStrategy]
        if isinstance(_data_limit_reset_strategy, Unset):
            data_limit_reset_strategy = UNSET
        else:
            data_limit_reset_strategy = UserDataLimitResetStrategy(_data_limit_reset_strategy)

        _inbounds = d.pop("inbounds", UNSET)
        inbounds: Union[Unset, UserModifyInbounds]
        if isinstance(_inbounds, Unset):
            inbounds = UNSET
        else:
            inbounds = UserModifyInbounds.from_dict(_inbounds)

        note = d.pop("note", UNSET)

        _sub_updated_at = d.pop("sub_updated_at", UNSET)
        sub_updated_at: Union[Unset, None, datetime.datetime]
        if _sub_updated_at is None:
            sub_updated_at = None
        elif isinstance(_sub_updated_at, Unset):
            sub_updated_at = UNSET
        else:
            sub_updated_at = isoparse(_sub_updated_at)

        sub_last_user_agent = d.pop("sub_last_user_agent", UNSET)

        _online_at = d.pop("online_at", UNSET)
        online_at: Union[Unset, None, datetime.datetime]
        if _online_at is None:
            online_at = None
        elif isinstance(_online_at, Unset):
            online_at = UNSET
        else:
            online_at = isoparse(_online_at)

        _status = d.pop("status", UNSET)
        status: Union[Unset, UserStatusModify]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = UserStatusModify(_status)

        user_modify = cls(
            proxies=proxies,
            expire=expire,
            data_limit=data_limit,
            data_limit_reset_strategy=data_limit_reset_strategy,
            inbounds=inbounds,
            note=note,
            sub_updated_at=sub_updated_at,
            sub_last_user_agent=sub_last_user_agent,
            online_at=online_at,
            status=status,
        )

        user_modify.additional_properties = d
        return user_modify

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
