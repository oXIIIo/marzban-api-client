from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.nodes_usage_response import NodesUsageResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start: Union[Unset, None, str] = UNSET,
    end: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:

    pass

    params: Dict[str, Any] = {}
    params["start"] = start

    params["end"] = end

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/api/nodes/usage",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, NodesUsageResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = NodesUsageResponse.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, NodesUsageResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start: Union[Unset, None, str] = UNSET,
    end: Union[Unset, None, str] = UNSET,
) -> Response[Union[HTTPValidationError, NodesUsageResponse]]:
    """Get Nodes Usage

     Get nodes usage

    Args:
        start (Union[Unset, None, str]):
        end (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, NodesUsageResponse]]
    """

    kwargs = _get_kwargs(
        start=start,
        end=end,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    start: Union[Unset, None, str] = UNSET,
    end: Union[Unset, None, str] = UNSET,
) -> Optional[Union[HTTPValidationError, NodesUsageResponse]]:
    """Get Nodes Usage

     Get nodes usage

    Args:
        start (Union[Unset, None, str]):
        end (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, NodesUsageResponse]
    """

    return sync_detailed(
        client=client,
        start=start,
        end=end,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start: Union[Unset, None, str] = UNSET,
    end: Union[Unset, None, str] = UNSET,
) -> Response[Union[HTTPValidationError, NodesUsageResponse]]:
    """Get Nodes Usage

     Get nodes usage

    Args:
        start (Union[Unset, None, str]):
        end (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, NodesUsageResponse]]
    """

    kwargs = _get_kwargs(
        start=start,
        end=end,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    start: Union[Unset, None, str] = UNSET,
    end: Union[Unset, None, str] = UNSET,
) -> Optional[Union[HTTPValidationError, NodesUsageResponse]]:
    """Get Nodes Usage

     Get nodes usage

    Args:
        start (Union[Unset, None, str]):
        end (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, NodesUsageResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            start=start,
            end=end,
        )
    ).parsed
