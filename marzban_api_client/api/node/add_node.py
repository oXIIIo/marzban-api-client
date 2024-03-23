from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.node_create import NodeCreate
from ...models.node_response import NodeResponse
from ...types import Response


def _get_kwargs(
    *,
    body: NodeCreate,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/node",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, NodeResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = NodeResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, HTTPValidationError, NodeResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: NodeCreate,
) -> Response[Union[Any, HTTPValidationError, NodeResponse]]:
    """Add Node

    Args:
        body (NodeCreate):  Example: {'name': 'DE node', 'address': '192.168.1.1', 'port': 62050,
            'api_port': 62051, 'add_as_new_host': True, 'usage_coefficient': 1}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, NodeResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: NodeCreate,
) -> Optional[Union[Any, HTTPValidationError, NodeResponse]]:
    """Add Node

    Args:
        body (NodeCreate):  Example: {'name': 'DE node', 'address': '192.168.1.1', 'port': 62050,
            'api_port': 62051, 'add_as_new_host': True, 'usage_coefficient': 1}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, NodeResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: NodeCreate,
) -> Response[Union[Any, HTTPValidationError, NodeResponse]]:
    """Add Node

    Args:
        body (NodeCreate):  Example: {'name': 'DE node', 'address': '192.168.1.1', 'port': 62050,
            'api_port': 62051, 'add_as_new_host': True, 'usage_coefficient': 1}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, NodeResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: NodeCreate,
) -> Optional[Union[Any, HTTPValidationError, NodeResponse]]:
    """Add Node

    Args:
        body (NodeCreate):  Example: {'name': 'DE node', 'address': '192.168.1.1', 'port': 62050,
            'api_port': 62051, 'add_as_new_host': True, 'usage_coefficient': 1}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, NodeResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
