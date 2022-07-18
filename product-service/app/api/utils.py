
from typing import Union

def create_action(
    sort_by: str,
    filter_code: Union[str, None]=None,
    filter_name: Union[str, None]=None,
    filter_price: Union[int, None]=None,
    filter_platform: Union[str, None]=None
):
    action = "sort by: " + sort_by + " "
    if filter_code:
        action += "filter_by: " + filter_code + " "
    if filter_name:
        action += "filter_by: " + filter_name + " "
    if filter_price:
        action += "filter_by: " + str(filter_price) + " "
    if filter_platform:
        action += "filter_by: " + filter_platform + " "
    return action.strip()