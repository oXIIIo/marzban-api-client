from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.user_status import UserStatus
from ...models.users_response import UsersResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    offset: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    username: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, UserStatus] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:

    pass

    params: Dict[str, Any] = {}
    params["offset"] = offset

    params["limit"] = limit

    params["username"] = username

    json_status: Union[Unset, None, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value if status else None

    params["status"] = json_status

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/api/users",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, UsersResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UsersResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HTTPValidationError, UsersResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    username: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, UserStatus] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Response[Union[HTTPValidationError, UsersResponse]]:
    """Get Users

     Get all users

    Args:
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        username (Union[Unset, None, str]):
        status (Union[Unset, None, UserStatus]): An enumeration representing different user
            statuses. It can have one of the following values: - `active`: The user is currently
            active. - `disabled`: The user's account is disabled. - `limited`: The user has limited
            access or privileges. - `expired`: The user's account has expired.
        sort (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, UsersResponse]]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        username=username,
        status=status,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    username: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, UserStatus] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Optional[Union[HTTPValidationError, UsersResponse]]:
    """Get Users

     Get all users

    Args:
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        username (Union[Unset, None, str]):
        status (Union[Unset, None, UserStatus]): An enumeration representing different user
            statuses. It can have one of the following values: - `active`: The user is currently
            active. - `disabled`: The user's account is disabled. - `limited`: The user has limited
            access or privileges. - `expired`: The user's account has expired.
        sort (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, UsersResponse]
    """

    return sync_detailed(
        client=client,
        offset=offset,
        limit=limit,
        username=username,
        status=status,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    username: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, UserStatus] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Response[Union[HTTPValidationError, UsersResponse]]:
    """Get Users

     Get all users

    Args:
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        username (Union[Unset, None, str]):
        status (Union[Unset, None, UserStatus]): An enumeration representing different user
            statuses. It can have one of the following values: - `active`: The user is currently
            active. - `disabled`: The user's account is disabled. - `limited`: The user has limited
            access or privileges. - `expired`: The user's account has expired.
        sort (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, UsersResponse]]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        username=username,
        status=status,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    username: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, UserStatus] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Optional[Union[HTTPValidationError, UsersResponse]]:
    """Get Users

     Get all users

    Args:
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        username (Union[Unset, None, str]):
        status (Union[Unset, None, UserStatus]): An enumeration representing different user
            statuses. It can have one of the following values: - `active`: The user is currently
            active. - `disabled`: The user's account is disabled. - `limited`: The user has limited
            access or privileges. - `expired`: The user's account has expired.
        sort (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, UsersResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            offset=offset,
            limit=limit,
            username=username,
            status=status,
            sort=sort,
        )
    ).parsed
