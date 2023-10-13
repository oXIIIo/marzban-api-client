# marzban-api-client
A client library for accessing MarzbanAPI

## Table of Contents

- [Installation](#installation)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

You can install this library using pip:

```bash
pip install marzban-api-client
```

## Getting Started
Before you can start using this library, you need to obtain an access token by logging in.
use the following code to get access token:

```python
from marzban_api_client import Client
from marzban_api_client.api.admin import login_for_access_token
from marzban_api_client.models.body_login_for_access_token import (
    BodyLoginForAccessToken,
)
from marzban_api_client.models.token import Token
from marzban_api_client.types import Response

login_data = BodyLoginForAccessToken(
    username="USERNAME",
    password="PASSWORD",
)

client = Client(base_url="BASE_URL")

with client as client:
    token: Token = login_for_access_token.sync(
        client=client,
        form_data=login_data,
    )
    access_token = token.access_token
    # or if you need more info (e.g. status_code)
    # response: Response[Token] = login_for_access_token.sync_detailed(
    #     client=client,
    #     form_data=login_data,
    # )
```
Replace `BASE_URL`, `USERNAME`, and `PASSWORD` with the actual URL of your Marzban API, your username and your password.
After executing this code, you will have an `access_token` that you can use for authenticated requests.

## Usage
Now that you have obtained an access token, you can use the `AuthenticatedClient` to make authenticated API requests.
Here's an example of how to use it:

```python
from marzban_api_client import AuthenticatedClient
from marzban_api_client.api.user_template import add_user_template
from marzban_api_client.models.user_template_create import UserTemplateCreate
from marzban_api_client.models.user_template_response import UserTemplateResponse

user_template = UserTemplateCreate(
    name="template_1",
    data_limit=320000000000,
    expire_duration=2592000,
    username_prefix="USER_",
)

client = AuthenticatedClient(
    base_url="BASE_URL",
    token="ACCESS_TOKEN",
)

with client as client:
    response: UserTemplateResponse = add_user_template.sync(
        client=client,
        json_body=user_template,
    )

print(response)
```
Replace `BASE_URL` and `ACCESS_TOKEN` with the actual URL of your Marzban API and and access_token.
you can also do the same thing with an async version:

```python
import asyncio

from marzban_api_client import AuthenticatedClient
from marzban_api_client.api.user_template import add_user_template
from marzban_api_client.models.user_template_create import UserTemplateCreate
from marzban_api_client.models.user_template_response import UserTemplateResponse


async def main():
    user_template = UserTemplateCreate(
        name="template_1",
        data_limit=320000000000,
        expire_duration=2592000,
        username_prefix="USER_",
    )

    client = AuthenticatedClient(
        base_url="BASE_URL",
        token="ACCESS_TOKEN",
    )

    async with client as client:
        response: UserTemplateResponse = await add_user_template.asyncio(
            client=client,
            json_body=user_template,
        )

    print(response)


if __name__ == "__main__":
    asyncio.run(main())
```

By default, when you're calling an HTTPS API it will attempt to verify that SSL is working correctly. Using certificate verification is highly recommended most of the time, but sometimes you may need to authenticate to a server (especially an internal server) using a custom certificate bundle.

```python
client = AuthenticatedClient(
    base_url="https://internal_api.example.com", 
    token="SuperSecretToken",
    verify_ssl="/path/to/certificate_bundle.pem",
)
```

You can also disable certificate validation altogether, but beware that **this is a security risk**.

```python
client = AuthenticatedClient(
    base_url="https://internal_api.example.com", 
    token="SuperSecretToken", 
    verify_ssl=False
)
```

Things to know:
1. Every path/method combo becomes a Python module with four functions:
    1. `sync`: Blocking request that returns parsed data (if successful) or `None`
    1. `sync_detailed`: Blocking request that always returns a `Request`, optionally with `parsed` set if the request was successful.
    1. `asyncio`: Like `sync` but async instead of blocking
    1. `asyncio_detailed`: Like `sync_detailed` but async instead of blocking

1. All path/query params, and bodies become method arguments.

## Advanced customizations

There are more settings on the generated `Client` class which let you control more runtime behavior, check out the docstring on that class for more info. You can also customize the underlying `httpx.Client` or `httpx.AsyncClient` (depending on your use-case):

```python
from marzban_api_client import Client

def log_request(request):
    print(f"Request event hook: {request.method} {request.url} - Waiting for response")

def log_response(response):
    request = response.request
    print(f"Response event hook: {request.method} {request.url} - Status {response.status_code}")

client = Client(
    base_url="https://api.example.com",
    httpx_args={"event_hooks": {"request": [log_request], "response": [log_response]}},
)

# Or get the underlying httpx client to modify directly with client.get_httpx_client() or client.get_async_httpx_client()
```

You can even set the httpx client directly, but beware that this will override any existing settings (e.g., base_url):

```python
import httpx
from marzban_api_client import Client

client = Client(
    base_url="https://api.example.com",
)
# Note that base_url needs to be re-set, as would any shared cookies, headers, etc.
client.set_httpx_client(httpx.Client(base_url="https://api.example.com", proxies="http://localhost:8030"))
```

## Examples

You can find more usage examples in the [example](example/) folder. These examples cover various scenarios and use cases to help you get started with this library.

Feel free to explore the examples and adapt them to your own project requirements.

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.
