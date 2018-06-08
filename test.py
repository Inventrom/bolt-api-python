import time
import json
import unittest
from boltiot.bolt import Bolt

client = Bolt('<your-api-key-here>', '<your-bolt-id>') # Pass in the API Key and the client ID.

class BoltTests(unittest.TestCase, unittest.TestLoader):

    def setUp(self):
        self.sortTestMethodsUsing = None

# Testing the digital write function.

    def test_digitalWrite(self):
        assert_value = json.loads(client.digitalWrite('4', 'HIGH'))
        self.assertEqual(assert_value["success"], "1")
        self.assertEqual(assert_value["value"], "1")
        print("Digital Write Successfull!")

# Testing the analog write function

    def test_analogWrite(self):
        assert_value = json.loads(client.analogWrite('0', '100'))
        self.assertEqual(assert_value["success"], "1")
        self.assertEqual(assert_value["value"], "1")
        print("Analog Write Successfull!")

# Testing the digital read function.

    def test_digitalRead(self):
        assert_value = json.loads(client.digitalRead('1'))
        self.assertEqual(assert_value["success"], "1")
        self.assertEqual(int(assert_value["value"]), 1)
        print("Digital Read Successfull!")

# Testing the analog read function.
        
    def test_analogRead(self):
        assert_value = json.loads(client.analogRead('A0'))
        self.assertEqual(assert_value["success"], "1")
        self.assertTrue(0 <= int(assert_value["value"]) <= 1024)
        print("Analog Read Succesfull!")

# Testing the serialBegin() function.

    def test_serialBegin(self):
        assert_value = json.loads(client.serialBegin("9600"))
        self.assertEqual(assert_value["success"], "1")
        self.assertEqual(assert_value["value"], "Success")
        print("Serial Begin Successfull!")

# Testing the serialWrite() function.

    def test_serialWrite(self):
        assert_value = json.loads(client.serialWrite('inventrom'))
        self.assertEqual(assert_value["success"], "1")
        self.assertEqual(assert_value["value"], "Serial write Successful")
        print("Serial Write Successfull!")

# Testing the serialRead()

    def test_serialRead(self):
        assert_value = json.loads(client.serialRead('10'))
        self.assertEqual(assert_value["success"], "1")
        self.assertEqual(assert_value["value"], "inventrom")
        print("Serial Read Successfull!")

# Testing the restart() function.

    def test_Restart(self):
        assert_value = json.loads(client.restart())
        time.sleep(5)
        try:
            self.assertEqual(assert_value["value"], "Restarted")
        except AssertionError:
            self.assertEqual(assert_value["value"], "Command timed out")
        print("Restart Successfull!")

# Testing the isAlive() function.

    def test_isAlive(self):
        assert_value = json.loads(client.isAlive())
        self.assertEqual(assert_value["success"], "1")
        self.assertEqual(assert_value["value"], "alive")
        print("isAlive Successfull!") 

# Testing the isOnline()

    def test_isOnline(self):
        assert_value = json.loads(client.isOnline())
        self.assertEqual(str(assert_value["success"]), "1")
        self.assertEqual(assert_value["value"], "online")
        print("isOnline Successfull!")

if __name__ == "__main__":
    is_device_online = json.loads(client.isOnline())
    if is_device_online["value"] == "online":
        unittest.main()
    else:
        print("The device is offline test cannot be conducted at the moment. Connect your Bolt to the cloud before testing it.")
