from asyncio import FastChildWatcher
import os
import requests

def is_user_existed(user_id: int):
    url = os.environ.get('USER_SERVICE_HOST_URL')
    r = requests.get(url + str(user_id))
    return True if r.status_code == 200 else False

def is_user_valid(user_id: int):
    url = os.environ.get('USER_SERVICE_HOST_URL')
    user_role_url = url + "role/"
    user_resp = requests.get(url + str(user_id))
    if user_resp.status_code != 200:
        return False
    user_role_resp = requests.get(user_role_url + str(user_resp.json()["role_id"]))
    user_role = user_role_resp.json()
    return user_role["role_name"] == "Call Center"

def is_product_existed(product_id: int):
    url = os.environ.get('PRODUCT_SERVICE_HOST_URL')
    r = requests.get(url + str(product_id))
    return True if r.status_code == 200 else False