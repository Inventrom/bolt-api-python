from boltiot.urls import url
from boltiot.requesting import request_from

#Defining a client class
class Bolt():

    def __init__(self, api_key, device_id):
        """
        Creating a class construcor.

        :param str api_key: api key to authenticate user
        :param str device_id: password to

        :returns: None
        :rtype: None
        """
        self.api_key = api_key
        self.device_id = device_id



    def digitalWrite(self, pin, state):
        """
        Write a HIGH or a LOW value to a digital pin.

        :param str pin: pin  numberto write the value
        :param str state: value of pin

        :returns:  request status, value
        :example: {"success": "1", "value": "1"}

        :rtype: JSON
        """
        return request_from(url('digitalWrite'), self.api_key , pin, state, self.device_id)


    def digitalRead(self, pin):
        """
        Reads the value from a specified digital pin.

        :param str: pin: number of the digital pin you want to read

        :returns:  request status, value
        :example: {"success": "1", "value": "1"}

        :rtype: JSON
        """
        return request_from(url('digitalRead'), self.api_key, pin, self.device_id)


    def analogWrite(self, pin, value):
        """
        Writes an analog value to a pin.

        :param str pin: pin  number to write the value
        :param str value: between 0 (always off) and 255 (always on).

        :returns:  request status, command status
        :example: {"success": "1", "value": "1"}

        :rtype: JSON
        """
        return request_from(url('analogWrite'), self.api_key, pin, value , self.device_id)

    def analogRead(self, pin):
        """
        Reads the value from the specified analog pin.

        :param str pin: number of the digital pin you want to read

        :returns:  request status, value(0 to 254)
        :example: {"success": "1", "value": "130"}

        :rtype: JSON
        """
        return request_from(url('analogRead'), self.api_key, pin, self.device_id)


    def serialBegin(self, baud_rate):
        """
        Sets the data rate in bits per second (baud) for serial data transmission.

        :param str baud_rate: speed: in bits per second (baud)

        :returns:  request status, serialBegin Status
        :example: {"success": "1", "value": "Success"}

        :rtype: JSON
        """
        return request_from(url('serialBegin'), self.api_key, baud_rate, self.device_id)


    def serialWrite(self, data):
        """
        Writes the data to the serial port.

        :param str data: in bits per second (baud)

        :returns:  request status, serialWrite Status
        :example: {"success": "1", "value": "Serial write Successful"}

        :rtype: JSON
        """
        return request_from(url('serialWrite'), self.api_key, data, self.device_id)

    def serialRead(self, char_till):
        """
        Reads incoming serial data.

        :param str char_till: read the character upto specific index

        :returns:  request status, value
        :example: {"success": "1", "value": "inventrom"}

        :rtype: JSON
        """
        return request_from(url('serialRead'), self.api_key, char_till, self.device_id)


    def version(self):
        """
        Check the Bolt hardware and firmware version

        :param None

        :returns:  request status, Bolt Hardware Version and Firmware Version
        :example: {"success": "1", "value": "{\"Bolt Hardware Version\":\"2\",
                                            \"Firmware Version\":\"1.0.1\"}"}

        :rtype: JSON
        """
        return request_from(url('version'), self.api_key, self.device_id)


    def restart(self):
        """
        Restart the device

        :param None

        :returns:  request status, command status
        :example: {"success": "1", "value": "Restarted"}

        :rtype: JSON
        """
        return request_from(url('restart'), self.api_key, self.device_id)


    def isAlive(self):
        """
        Check the device status

        :param None

        :returns:  request status, device status: dead,alive
        :example: {"success": "1", "value": "alive"}

        :rtype: JSON
        """
        return request_from(url('isAlive'), self.api_key, self.device_id)

    def isOnline(self):
        """
        The command tells the user about the status of the device,
        if it is Online/Offline along with time when status changed.

        :param None
        :returns : {success: status of the request(1/0),
                    value: device status (online/offline),
                    time: the time when the device was online/offline respectively
                          (format: day yyyy-mm-dd hh:mm:ss TZ)}
        :example: {"success": "1", "value": "online", "time":"Sun 2018-05-06 08:14:43 UTC"}

        :rtype: JSON
        """
        return request_from(url('isOnline'), self.api_key, self.device_id)
