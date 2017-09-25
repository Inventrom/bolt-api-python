from urls import url
from requesting import request_from
#Defining a client class
class Bolt():
    #Creating a class construcor
    def __init__(self, api_key, device_id):
        self.api_key = api_key
        self.device_id = device_id
    #Creating a digital write method
    def digitalWrite(self, pin, state):
        return request_from(url('digitalWrite'), self.api_key , pin, state, self.device_id)
    #Creating a digital read method
    def digitalRead(self, pin):
        return request_from(url('digitalRead'), self.api_key, pin, self.device_id)
    #Creating an analog write method
    def analogWrite(self, pin, value):
        return request_from(url('analogWrite'), self.api_key, pin, value , self.device_id)
    #Creating an analog read method
    def analogRead(self, pin):
        return request_from(url('analogRead'), self.api_key, pin, self.device_id)
    #UART commands
    def serialBegin(self, baud_rate):
        return request_from(url('serialBegin'), self.api_key, baud_rate, self.device_id)
    def setialWrite(self, data):
        return request_from(url('serialWrite'), self.api_key, data, self.device_id)
    def serialRead(self, char_till):
        return request_from(url('serialRead'), self.api_key, char_till, self.device_id)
    #Version Check
    def version(self):
        return request_from(url('version'), self.api_key, self.device_id)
    #Device Restart
    def restart(self):
        return request_from(url('restart'), self.api_key, self.device_id)
    #Device Status
    def isAlive(self):
        return request_from(url('isAlive'), self.api_key, self.device_id)
#Way it works

#client = Client('768d64d5-05b2-463b-95bc-98eedfc5abe7', 'BOLT3432361')

#result = client.digitalWrite('0','HIGH')

#print(result)
