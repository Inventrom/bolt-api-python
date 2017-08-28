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
        device_status = requests.get('http://cloud.boltiot.com/remote/{}/digitalWrite?pin={}&state={}&deviceName={}'.format(self.pin, self.state, self.device_id, self.api_key))
        return device_status.text


#Way it works

#client = Client('768d64d5-05b2-463b-95bc-98eedfc5abe7', 'BOLT3432361')

#result = client.digitalWrite('0','HIGH')

#print(result)
