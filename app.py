"""
app example

"""
import requests

def is_alive_host(hostname):
    response = requests.get("https://www."+hostname)
    return response.status_code == requests.codes.ok

