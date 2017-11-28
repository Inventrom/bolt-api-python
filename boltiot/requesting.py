from boltiot.urls import url
import requests

def request_from(url, *kwargs):
    try:
        response = str(requests.get(url.format(*kwargs)).text)
        return response
    except requests.exceptions.ConnectionError as err:
        return {"success":"0", "message":"A Connection error occurred"}
    except requests.exceptions.Timeout as err:
        return {"success":"0", "message":"The request timed out"}
    except requests.exceptions.TooManyRedirects as err :
        return {"success":"0", "message":"Too many redirects"}
    except requests.exceptions.RequestException as err:
        return {"success":"0", "message":"Not able to handle error"}
    except err:
        return {"success":"0", "message":"Something went wrong"}


def request_test(function):
    result = function
    return result
