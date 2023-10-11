from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.user_modify import UserModify
from ...models.user_response import UserResponse
from ...types import Response


def _get_kwargs(
    username: str,
    *,
    json_body: UserModify,
) -> Dict[str, Any]:

    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": "/api/user/{username}".format(
            username=username,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, UserResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UserResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, HTTPValidationError, UserResponse]]:
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
    json_body: UserModify,
) -> Response[Union[Any, HTTPValidationError, UserResponse]]:
    """Modify User

     Modify a user

    - set **expire** to 0 to make the user unlimited in time, null to no change
    - set **data_limit** to 0 to make the user unlimited in data, null to no change
    - **proxies** dictionary of protocol:settings, empty means no change
    - **inbounds** dictionary of protocol:inbound_tags, empty means no change

    Args:
        username (str):
        json_body (UserModify):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, UserResponse]]
    """

    kwargs = _get_kwargs(
        username=username,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    username: str,
    *,
    client: AuthenticatedClient,
    json_body: UserModify,
) -> Optional[Union[Any, HTTPValidationError, UserResponse]]:
    """Modify User

     Modify a user

    - set **expire** to 0 to make the user unlimited in time, null to no change
    - set **data_limit** to 0 to make the user unlimited in data, null to no change
    - **proxies** dictionary of protocol:settings, empty means no change
    - **inbounds** dictionary of protocol:inbound_tags, empty means no change

    Args:
        username (str):
        json_body (UserModify):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, UserResponse]
    """

    return sync_detailed(
        username=username,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    username: str,
    *,
    client: AuthenticatedClient,
    json_body: UserModify,
) -> Response[Union[Any, HTTPValidationError, UserResponse]]:
    """Modify User

     Modify a user

    - set **expire** to 0 to make the user unlimited in time, null to no change
    - set **data_limit** to 0 to make the user unlimited in data, null to no change
    - **proxies** dictionary of protocol:settings, empty means no change
    - **inbounds** dictionary of protocol:inbound_tags, empty means no change

    Args:
        username (str):
        json_body (UserModify):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, UserResponse]]
    """

    kwargs = _get_kwargs(
        username=username,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    username: str,
    *,
    client: AuthenticatedClient,
    json_body: UserModify,
) -> Optional[Union[Any, HTTPValidationError, UserResponse]]:
    """Modify User

     Modify a user

    - set **expire** to 0 to make the user unlimited in time, null to no change
    - set **data_limit** to 0 to make the user unlimited in data, null to no change
    - **proxies** dictionary of protocol:settings, empty means no change
    - **inbounds** dictionary of protocol:inbound_tags, empty means no change

    Args:
        username (str):
        json_body (UserModify):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, UserResponse]
    """

    return (
        await asyncio_detailed(
            username=username,
            client=client,
            json_body=json_body,
        )
    ).parsed
