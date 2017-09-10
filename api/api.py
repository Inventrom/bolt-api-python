import requests
from urls import url

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
        device_status = requests.get(url['digitalWrite'].format(self.api_key , self.pin, self.state, self.device_id))
        return device_status.text

    #Creating a digital read method
    def digitalRead(self, pin):
        self.pin = pin
        device_status = requests.get(url['digitalRead'].format(self.api_key, self.pin, self.device_id))
        return device_status.text

    #Creating an analog write method
    def analogWrite(self, pin, value):
        self.pin = pin
        self.value = value
        device_status = requests.get(url['analogWrite'].format(self.api_key, self.pin, self.value , self.device_id))
        return device_status.text

    #Creating an analog read method
    def analogRead(self, pin):
        self.pin = pin
        self.value = value
        device_status = requests.get(url['analogRead'].format(self.api_key, self.pin, self.device_id))
        return device_status.text

    #UART commands
    def serialBegin(self, baud_rate):
        self.baud_rate = baud_rate
        device_status = requests.get(url['serialBegin'].format(self.api_key, self.baud_rate, self.device_id))
        return device_status.text

    def setialWrite(self, data):
        self.data = data
        device_status = requests.get(url['serialWrite'].format(self.api_key, self.data, self.device_id))
        return device_status.text

    def serialRead(self, char_till):
        self.char_till = char_till
        device_status = requests.get(url['serialRead'].format(self.api_key, self.char_till, self.device_id))
        return device_status.text

    #Version Check
    def version(self):
        device_status = requests.get(url['version'].format(self.api_key, self.device_id))
        return device_status.text

    #Device Restart
    def restart(self):
        device_status = requests.get(url['restart'].format(self.api_key, self.device_id))
        return device_status.text

    #Device Status
    def isAlive(self):
        device_status = requests.get(url['isAlive'].format(self.api_key, self.device_id))
        return device_status.text

#Way it works

#client = Client('768d64d5-05b2-463b-95bc-98eedfc5abe7', 'BOLT3432361')

#result = client.digitalWrite('0','HIGH')

#print(result)
