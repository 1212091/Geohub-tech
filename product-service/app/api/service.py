"""Service class to handle communicate with other service"""
import json
import os
from typing import Union

import httpx
from app.api.utils import create_action

#pylint: disable=too-many-arguments


async def save_user_activity(
    user_id: int,
    sort_by: str,
    sort_asc: bool,
    filter_code: Union[str, None] = None,
    filter_name: Union[str, None] = None,
    filter_price: Union[int, None] = None,
    filter_platform: Union[str, None] = None
):
    """Save user activity"""
    action = create_action(sort_by, sort_asc, filter_code,
                           filter_name, filter_price, filter_platform)
    user_activity_url = os.environ.get('USER_SERVICE_HOST_URL') + "activity"

    # We send user activity asynchronously to user service
    async with httpx.AsyncClient() as client:
        await client.post(
            user_activity_url,
            data=json.dumps({
                "user_id": user_id,
                "action": action
            })
        )
