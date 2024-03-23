import asyncio

from marzban_api_client import AuthenticatedClient
from marzban_api_client.api.user_template import add_user_template
from marzban_api_client.models.user_template_create import UserTemplateCreate
from marzban_api_client.models.user_template_response import UserTemplateResponse


async def main():
    user_template = UserTemplateCreate(
        name="template_2",
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
            body=user_template,
        )

    print(response)


if __name__ == "__main__":
    asyncio.run(main())
