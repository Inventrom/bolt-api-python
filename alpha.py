import requests

#Defining a client class
class Client():

    #Creating a class construcor
    def __init__(self, api_key, device_id):

        self.api_key = api_key
        self.device_id = device_id

    #Creating a digital write method
    def digitalWrite(self, pin, state):

        self.pin = pin
        self.state = state
        device_status = requests.get('http://cloud.boltiot.com/remote//digitalWrite?pin=%s&state=%s&deviceName=%s', self.pin, self.state, self.device_id)
        return device_status.text


#Way it works

#client = Client()

#client.digitalWrite(0,LOW)

