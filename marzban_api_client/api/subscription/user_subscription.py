from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import Response, Unset


def _get_kwargs(
    token: str,
    *,
    user_agent: Union[Unset, str] = "",
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(user_agent, Unset):
        headers["user-agent"] = user_agent

    return {
        "method": "get",
        "url": "/sub/{token}/".format(
            token=token,
        ),
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(Any, response.json())
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
) -> Response[Union[Any, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    token: str,
    *,
    client: Union[AuthenticatedClient, Client],
    user_agent: Union[Unset, str] = "",
) -> Response[Union[Any, HTTPValidationError]]:
    """User subscription

     Subscription link, V2ray and Clash supported

    Args:
        token (str):
        user_agent (Union[Unset, str]):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        token=token,
        user_agent=user_agent,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    token: str,
    *,
    client: Union[AuthenticatedClient, Client],
    user_agent: Union[Unset, str] = "",
) -> Optional[Union[Any, HTTPValidationError]]:
    """User subscription

     Subscription link, V2ray and Clash supported

    Args:
        token (str):
        user_agent (Union[Unset, str]):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        token=token,
        client=client,
        user_agent=user_agent,
    ).parsed


async def asyncio_detailed(
    token: str,
    *,
    client: Union[AuthenticatedClient, Client],
    user_agent: Union[Unset, str] = "",
) -> Response[Union[Any, HTTPValidationError]]:
    """User subscription

     Subscription link, V2ray and Clash supported

    Args:
        token (str):
        user_agent (Union[Unset, str]):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        token=token,
        user_agent=user_agent,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    token: str,
    *,
    client: Union[AuthenticatedClient, Client],
    user_agent: Union[Unset, str] = "",
) -> Optional[Union[Any, HTTPValidationError]]:
    """User subscription

     Subscription link, V2ray and Clash supported

    Args:
        token (str):
        user_agent (Union[Unset, str]):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            token=token,
            client=client,
            user_agent=user_agent,
        )
    ).parsed
