from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.user_usages_response import UserUsagesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    username: str,
    *,
    start: Union[Unset, str] = UNSET,
    end: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["start"] = start

    params["end"] = end

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/user/{username}/usage",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, UserUsagesResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UserUsagesResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, HTTPValidationError, UserUsagesResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    username: str,
    *,
    client: AuthenticatedClient,
    start: Union[Unset, str] = UNSET,
    end: Union[Unset, str] = UNSET,
) -> Response[Union[Any, HTTPValidationError, UserUsagesResponse]]:
    """Get User Usage

     Get users usage

    Args:
        username (str):
        start (Union[Unset, str]):
        end (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, UserUsagesResponse]]
    """

    kwargs = _get_kwargs(
        username=username,
        start=start,
        end=end,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    username: str,
    *,
    client: AuthenticatedClient,
    start: Union[Unset, str] = UNSET,
    end: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, HTTPValidationError, UserUsagesResponse]]:
    """Get User Usage

     Get users usage

    Args:
        username (str):
        start (Union[Unset, str]):
        end (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, UserUsagesResponse]
    """

    return sync_detailed(
        username=username,
        client=client,
        start=start,
        end=end,
    ).parsed


async def asyncio_detailed(
    username: str,
    *,
    client: AuthenticatedClient,
    start: Union[Unset, str] = UNSET,
    end: Union[Unset, str] = UNSET,
) -> Response[Union[Any, HTTPValidationError, UserUsagesResponse]]:
    """Get User Usage

     Get users usage

    Args:
        username (str):
        start (Union[Unset, str]):
        end (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, UserUsagesResponse]]
    """

    kwargs = _get_kwargs(
        username=username,
        start=start,
        end=end,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    username: str,
    *,
    client: AuthenticatedClient,
    start: Union[Unset, str] = UNSET,
    end: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, HTTPValidationError, UserUsagesResponse]]:
    """Get User Usage

     Get users usage

    Args:
        username (str):
        start (Union[Unset, str]):
        end (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, UserUsagesResponse]
    """

    return (
        await asyncio_detailed(
            username=username,
            client=client,
            start=start,
            end=end,
        )
    ).parsed
