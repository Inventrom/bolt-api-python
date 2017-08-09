# bolt-api-python

## Problem Statment

1. Currently, the user has to set the API key and  device id every time with cloud URL.

    For example.
    
    `http://cloud.boltiot.com/remote/abc061df-bef5-4881-b54e-a73099e3f66b/digitalWrite?pin=0&state=LOW&deviceName=BOLTxXXXXX`

2. The user has to install the request library by himself and there is a learning curve of request library of itself.
    For example.
    
    `pip install requests`
    ```python
    import requests 
    urlON="http://cloud.boltiot.com/remote/YourDeviceAPI/ONCommand&deviceName=BOLTxxxxxxx"
    urlOFF="http://cloud.boltiot.com/remote/YourDeviceAPI/OFFCommand&deviceName=BOLTxxxxxxx" 
    r=requests.get(urlON) 
    r=requests.get(urlOFF)
    ```
## Expected Solution

1. User need to type just one command

    `pip install bolt`
    

2. The user will set the client once and he can use the same client for every operation.
    For example.
    
    `pip install requests`
    ```python
    from bolt import Client
    api_key = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    device_id  = “BOLT1234"
    client = Client(api_key, device_id)
    response = client.digitalWrite('0', 'HIGH')
    ```

## Bolt API documenation

You can find the Bolt API documentation here http://cloud.boltiot.com/api_credentials.

## Contributing

Your contributions are always welcome! Please refer ths contribution guidelines. 

### Guidelines
* Fork the repository on GitHub.
* First checkout to dev branch.
* Create a feature branch only when you are working on a new feature. 
* Write a test which shows that the bug was fixed or that the feature works as expected.
* Never work on master branch
* Send a pull request and until it gets merged and published. :)
* Check your spelling and grammar.
* Remove any trailing whitespace.


