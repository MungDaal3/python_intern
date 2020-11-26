"""
app example

"""
import requests
from requests.exceptions import HTTPError


def is_alive_host(hostname: str):
    try:
        response = requests.get("https://"+hostname)
        response.raise_for_status()
    except HTTPError as http_err:
        return http_err
    except Exception:
        return False
    else:
        return True
