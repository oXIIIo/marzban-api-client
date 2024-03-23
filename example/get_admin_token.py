from marzban_api_client import Client
from marzban_api_client.api.admin import admin_token
from marzban_api_client.models.body_admin_token_api_admin_token_post import (
    BodyAdminTokenApiAdminTokenPost,
)
from marzban_api_client.models.token import Token
from marzban_api_client.types import Response

login_data = BodyAdminTokenApiAdminTokenPost(
    username="USERNAME",
    password="PASSWORD",
)

client = Client(base_url="BASE_URL")

with client as client:
    token: Token = admin_token.sync(
        client=client,
        body=login_data,
    )
    access_token = token.access_token
    print(f"your admin token is: {access_token}")
    # or if you need more info (e.g. status_code)
    response: Response[Token] = admin_token.sync_detailed(
        client=client,
        body=login_data,
    )
    print(response)
