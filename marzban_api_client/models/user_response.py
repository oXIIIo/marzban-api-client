import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.user_data_limit_reset_strategy import UserDataLimitResetStrategy
from ..models.user_status import UserStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_response_excluded_inbounds import UserResponseExcludedInbounds
    from ..models.user_response_inbounds import UserResponseInbounds
    from ..models.user_response_proxies import UserResponseProxies


T = TypeVar("T", bound="UserResponse")


@_attrs_define
class UserResponse:
    """
    Attributes:
        proxies (UserResponseProxies):
        username (str):
        status (UserStatus): An enumeration.
        used_traffic (int):
        created_at (datetime.datetime):
        expire (Union[None, Unset, int]):
        data_limit (Union[Unset, int]): data_limit can be 0 or greater
        data_limit_reset_strategy (Union[Unset, UserDataLimitResetStrategy]): An enumeration. Default:
            UserDataLimitResetStrategy.NO_RESET.
        inbounds (Union[Unset, UserResponseInbounds]):
        note (Union[None, Unset, str]):
        sub_updated_at (Union[None, Unset, datetime.datetime]):
        sub_last_user_agent (Union[None, Unset, str]):
        online_at (Union[None, Unset, datetime.datetime]):
        on_hold_expire_duration (Union[None, Unset, int]):
        on_hold_timeout (Union[None, Unset, datetime.datetime]):
        lifetime_used_traffic (Union[Unset, int]):  Default: 0.
        links (Union[Unset, List[str]]):
        subscription_url (Union[Unset, str]):  Default: ''.
        excluded_inbounds (Union[Unset, UserResponseExcludedInbounds]):
    """

    proxies: "UserResponseProxies"
    username: str
    status: UserStatus
    used_traffic: int
    created_at: datetime.datetime
    expire: Union[None, Unset, int] = UNSET
    data_limit: Union[Unset, int] = UNSET
    data_limit_reset_strategy: Union[Unset, UserDataLimitResetStrategy] = UserDataLimitResetStrategy.NO_RESET
    inbounds: Union[Unset, "UserResponseInbounds"] = UNSET
    note: Union[None, Unset, str] = UNSET
    sub_updated_at: Union[None, Unset, datetime.datetime] = UNSET
    sub_last_user_agent: Union[None, Unset, str] = UNSET
    online_at: Union[None, Unset, datetime.datetime] = UNSET
    on_hold_expire_duration: Union[None, Unset, int] = UNSET
    on_hold_timeout: Union[None, Unset, datetime.datetime] = UNSET
    lifetime_used_traffic: Union[Unset, int] = 0
    links: Union[Unset, List[str]] = UNSET
    subscription_url: Union[Unset, str] = ""
    excluded_inbounds: Union[Unset, "UserResponseExcludedInbounds"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        proxies = self.proxies.to_dict()

        username = self.username

        status = self.status.value

        used_traffic = self.used_traffic

        created_at = self.created_at.isoformat()

        expire: Union[None, Unset, int]
        if isinstance(self.expire, Unset):
            expire = UNSET
        else:
            expire = self.expire

        data_limit = self.data_limit

        data_limit_reset_strategy: Union[Unset, str] = UNSET
        if not isinstance(self.data_limit_reset_strategy, Unset):
            data_limit_reset_strategy = self.data_limit_reset_strategy.value

        inbounds: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.inbounds, Unset):
            inbounds = self.inbounds.to_dict()

        note: Union[None, Unset, str]
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        sub_updated_at: Union[None, Unset, str]
        if isinstance(self.sub_updated_at, Unset):
            sub_updated_at = UNSET
        elif isinstance(self.sub_updated_at, datetime.datetime):
            sub_updated_at = self.sub_updated_at.isoformat()
        else:
            sub_updated_at = self.sub_updated_at

        sub_last_user_agent: Union[None, Unset, str]
        if isinstance(self.sub_last_user_agent, Unset):
            sub_last_user_agent = UNSET
        else:
            sub_last_user_agent = self.sub_last_user_agent

        online_at: Union[None, Unset, str]
        if isinstance(self.online_at, Unset):
            online_at = UNSET
        elif isinstance(self.online_at, datetime.datetime):
            online_at = self.online_at.isoformat()
        else:
            online_at = self.online_at

        on_hold_expire_duration: Union[None, Unset, int]
        if isinstance(self.on_hold_expire_duration, Unset):
            on_hold_expire_duration = UNSET
        else:
            on_hold_expire_duration = self.on_hold_expire_duration

        on_hold_timeout: Union[None, Unset, str]
        if isinstance(self.on_hold_timeout, Unset):
            on_hold_timeout = UNSET
        elif isinstance(self.on_hold_timeout, datetime.datetime):
            on_hold_timeout = self.on_hold_timeout.isoformat()
        else:
            on_hold_timeout = self.on_hold_timeout

        lifetime_used_traffic = self.lifetime_used_traffic

        links: Union[Unset, List[str]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links

        subscription_url = self.subscription_url

        excluded_inbounds: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.excluded_inbounds, Unset):
            excluded_inbounds = self.excluded_inbounds.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "proxies": proxies,
                "username": username,
                "status": status,
                "used_traffic": used_traffic,
                "created_at": created_at,
            }
        )
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
        if on_hold_expire_duration is not UNSET:
            field_dict["on_hold_expire_duration"] = on_hold_expire_duration
        if on_hold_timeout is not UNSET:
            field_dict["on_hold_timeout"] = on_hold_timeout
        if lifetime_used_traffic is not UNSET:
            field_dict["lifetime_used_traffic"] = lifetime_used_traffic
        if links is not UNSET:
            field_dict["links"] = links
        if subscription_url is not UNSET:
            field_dict["subscription_url"] = subscription_url
        if excluded_inbounds is not UNSET:
            field_dict["excluded_inbounds"] = excluded_inbounds

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_response_excluded_inbounds import UserResponseExcludedInbounds
        from ..models.user_response_inbounds import UserResponseInbounds
        from ..models.user_response_proxies import UserResponseProxies

        d = src_dict.copy()
        proxies = UserResponseProxies.from_dict(d.pop("proxies"))

        username = d.pop("username")

        status = UserStatus(d.pop("status"))

        used_traffic = d.pop("used_traffic")

        created_at = isoparse(d.pop("created_at"))

        def _parse_expire(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        expire = _parse_expire(d.pop("expire", UNSET))

        data_limit = d.pop("data_limit", UNSET)

        _data_limit_reset_strategy = d.pop("data_limit_reset_strategy", UNSET)
        data_limit_reset_strategy: Union[Unset, UserDataLimitResetStrategy]
        if isinstance(_data_limit_reset_strategy, Unset):
            data_limit_reset_strategy = UNSET
        else:
            data_limit_reset_strategy = UserDataLimitResetStrategy(_data_limit_reset_strategy)

        _inbounds = d.pop("inbounds", UNSET)
        inbounds: Union[Unset, UserResponseInbounds]
        if isinstance(_inbounds, Unset):
            inbounds = UNSET
        else:
            inbounds = UserResponseInbounds.from_dict(_inbounds)

        def _parse_note(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        note = _parse_note(d.pop("note", UNSET))

        def _parse_sub_updated_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sub_updated_at_type_0 = isoparse(data)

                return sub_updated_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        sub_updated_at = _parse_sub_updated_at(d.pop("sub_updated_at", UNSET))

        def _parse_sub_last_user_agent(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sub_last_user_agent = _parse_sub_last_user_agent(d.pop("sub_last_user_agent", UNSET))

        def _parse_online_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                online_at_type_0 = isoparse(data)

                return online_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        online_at = _parse_online_at(d.pop("online_at", UNSET))

        def _parse_on_hold_expire_duration(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        on_hold_expire_duration = _parse_on_hold_expire_duration(d.pop("on_hold_expire_duration", UNSET))

        def _parse_on_hold_timeout(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                on_hold_timeout_type_0 = isoparse(data)

                return on_hold_timeout_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        on_hold_timeout = _parse_on_hold_timeout(d.pop("on_hold_timeout", UNSET))

        lifetime_used_traffic = d.pop("lifetime_used_traffic", UNSET)

        links = cast(List[str], d.pop("links", UNSET))

        subscription_url = d.pop("subscription_url", UNSET)

        _excluded_inbounds = d.pop("excluded_inbounds", UNSET)
        excluded_inbounds: Union[Unset, UserResponseExcludedInbounds]
        if isinstance(_excluded_inbounds, Unset):
            excluded_inbounds = UNSET
        else:
            excluded_inbounds = UserResponseExcludedInbounds.from_dict(_excluded_inbounds)

        user_response = cls(
            proxies=proxies,
            username=username,
            status=status,
            used_traffic=used_traffic,
            created_at=created_at,
            expire=expire,
            data_limit=data_limit,
            data_limit_reset_strategy=data_limit_reset_strategy,
            inbounds=inbounds,
            note=note,
            sub_updated_at=sub_updated_at,
            sub_last_user_agent=sub_last_user_agent,
            online_at=online_at,
            on_hold_expire_duration=on_hold_expire_duration,
            on_hold_timeout=on_hold_timeout,
            lifetime_used_traffic=lifetime_used_traffic,
            links=links,
            subscription_url=subscription_url,
            excluded_inbounds=excluded_inbounds,
        )

        user_response.additional_properties = d
        return user_response

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
