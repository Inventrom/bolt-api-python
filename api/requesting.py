from urls import url
import requests

#Request data from the url
def request_from(url, *kwargs):
    device_status = requests.get(url.format(*kwargs))
    return device_status.text
