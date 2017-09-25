from urls import url
import requests

def request_from(url, *kwargs):
    return str(requests.get(url.format(*kwargs)).text)

def request_test(function):
    result = function
    return result
