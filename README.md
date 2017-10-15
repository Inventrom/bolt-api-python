# bolt-api-python

## Goal
The goal of this library is to provide an easy to use interface of Bolt Cloud API's. The functions will be quite similar to the Raspberry Pi and Arduino functions.

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

    `pip install boltiot`
    

2. The user will set the client once and he can use the same client for every operation.
    For example.
    
    ```python
    from boltiot import Bolt
    api_key = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    device_id  = “BOLT1234"
    mybolt = Bolt(api_key, device_id)
    response = client.digitalWrite('0', 'HIGH')
    ```
##  GPIO Functions

1. digitalWrite Command
    
    ```python
    from boltiot import Bolt
    api_key = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    device_id  = “BOLT1234"
    mybolt = Bolt(api_key, device_id)
    response = mybolt.digitalWrite('0', 'HIGH')
    ```
 2. digitalRead Command
    
    ```python
    from boltiot import Bolt
    api_key = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    device_id  = “BOLT1234"
    mybolt = Bolt(api_key, device_id)
    response = mybolt.digitalRead('A0')
    ```
 3. analogRead Command
    
    ```python
    from boltiot import Bolt
    api_key = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    device_id  = “BOLT1234"
    mybolt = Bolt(api_key, device_id)
    response = mybolt.analogRead('A0')
    ```
 4. analogWrite Command
    
    ```python
    from boltiot import Bolt
    api_key = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    device_id  = “BOLT1234"
    mybolt = Bolt(api_key, device_id)
    response = mybolt.analogWrite('0', '100')
    ```

##  UART Functions

1. serialBegin Command
    
    ```python
    from boltiot import Bolt
    api_key = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    device_id  = “BOLT1234"
    mybolt = Bolt(api_key, device_id)
    response = mybolt.serialBegin('9600')
    ```
 2. serialWrite Command
    
    ```python
    from boltiot import Bolt
    api_key = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    device_id  = “BOLT1234"
    mybolt = Bolt(api_key, device_id)
    response = mybolt.serialWrite('Hello')
    ```
3. serialRead Command
       
    ```python
    from boltiot import Bolt
    api_key = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    device_id  = “BOLT1234"
    mybolt = Bolt(api_key, device_id)
    response = mybolt.serialRead('10')
    ```
 ##  Utility Functions
1. isAlive Command (to check the status of device)
    
    ```python
    from boltiot import Bolt
    api_key = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    device_id  = “BOLT1234"
    mybolt = Bolt(api_key, device_id)
    response = mybolt.isAlive()
    ```
    
2. restart Command (to restart the Bolt)
    
    ```python
    from boltiot import Bolt
    api_key = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    device_id  = “BOLT1234"
    mybolt = Bolt(api_key, device_id)
    response = mybolt.restart()
    ```
 3. version Command (to check device version)
    
    ```python
    from boltiot import Bolt
    api_key = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    device_id  = “BOLT1234"
    mybolt = Bolt(api_key, device_id)
    response = mybolt.version()
    ```
## Bolt API documenation

You can find the Bolt API documentation here http://cloud.boltiot.com/api_credentials.

## Contributing

Your contributions are always welcome! Please refer to the contribution guidelines. 

### Guidelines
* Fork the repository on GitHub.
* First checkout to dev branch.
* Create a feature branch only when you are working on a new feature. 
* Write a test which shows that the bug was fixed or that the feature works as expected.
* Never work on master branch
* Send a pull request and wait until it gets merged and published. :)
* Check your spelling and grammar.
* Remove any trailing whitespaces.


