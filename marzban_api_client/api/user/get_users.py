from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.user_status import UserStatus
from ...models.users_response import UsersResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    username: Union[Unset, List[str]] = UNSET,
    status: Union[Unset, UserStatus] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    json_username: Union[Unset, List[str]] = UNSET
    if not isinstance(username, Unset):
        json_username = username

    params["username"] = json_username

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/users",
        "params": params,
    }

    return _kwargs


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
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    username: Union[Unset, List[str]] = UNSET,
    status: Union[Unset, UserStatus] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, UsersResponse]]:
    """Get Users

     Get all users

    Args:
        offset (Union[Unset, int]):
        limit (Union[Unset, int]):
        username (Union[Unset, List[str]]):
        status (Union[Unset, UserStatus]): An enumeration.
        sort (Union[Unset, str]):

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
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    username: Union[Unset, List[str]] = UNSET,
    status: Union[Unset, UserStatus] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, UsersResponse]]:
    """Get Users

     Get all users

    Args:
        offset (Union[Unset, int]):
        limit (Union[Unset, int]):
        username (Union[Unset, List[str]]):
        status (Union[Unset, UserStatus]): An enumeration.
        sort (Union[Unset, str]):

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
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    username: Union[Unset, List[str]] = UNSET,
    status: Union[Unset, UserStatus] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, UsersResponse]]:
    """Get Users

     Get all users

    Args:
        offset (Union[Unset, int]):
        limit (Union[Unset, int]):
        username (Union[Unset, List[str]]):
        status (Union[Unset, UserStatus]): An enumeration.
        sort (Union[Unset, str]):

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
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    username: Union[Unset, List[str]] = UNSET,
    status: Union[Unset, UserStatus] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, UsersResponse]]:
    """Get Users

     Get all users

    Args:
        offset (Union[Unset, int]):
        limit (Union[Unset, int]):
        username (Union[Unset, List[str]]):
        status (Union[Unset, UserStatus]): An enumeration.
        sort (Union[Unset, str]):

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
