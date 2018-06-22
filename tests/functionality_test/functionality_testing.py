import json
import time
import unittest

from context import Bolt

client = Bolt("<your-api-key-here>", "<your-bolt-id>") # Pass in the API Key and the client ID.

class BoltTests(unittest.TestCase, unittest.TestLoader):
    """
    This is a test class to test,
    the functionality of the bolt python api library.
    Methods:
    - setUp()
    - tearDown()
    - test_digitalWrite()
    - test_analogWrite()
    - test_digitalRead()
    - test_analogRead()
    - test_serialBegin()
    - test_serialWrite()
    - test_serialRead()
    - test_Restart()
    - test_isOnline()
    - test_isAlive()
    """
    
    def setUp(self):
        """Setup function for all the testcases."""
        self.sortTestMethodsUsing = None

    def tearDown(self):
        """Tear down function for all the testcases"""
        time.sleep(3)

    def test_digitalWrite(self):
        """Testing the digital write function."""
        assert_value = json.loads(client.digitalWrite('4', "HIGH"))
        self.assertEqual(assert_value["success"], '1')
        self.assertEqual(assert_value["value"], '1')
        print("Digital Write Successfull!")

    def test_analogWrite(self):
        """Testing the analog write function"""
        assert_value = json.loads(client.analogWrite('0', "100"))
        self.assertEqual(assert_value["success"], '1')
        self.assertEqual(assert_value["value"], '1')
        print("Analog Write Successfull!")

    def test_digitalRead(self):
        """Testing the digital read function."""
        assert_value = json.loads(client.digitalRead('1'))
        self.assertEqual(assert_value["success"], '1')
        self.assertEqual(int(assert_value["value"]), 1)
        print("Digital Read Successfull!")

    def test_analogRead(self):
        """Testing the analog read function."""
        assert_value = json.loads(client.analogRead("A0"))
        self.assertEqual(assert_value["success"], '1')
        self.assertTrue(0 <= int(assert_value["value"]) <= 1024)
        print("Analog Read Succesfull!")

    def test_serialBegin(self):
        """Testing the serialBegin() function."""
        assert_value = json.loads(client.serialBegin("9600"))
        self.assertEqual(assert_value["success"], '1')
        self.assertEqual(assert_value["value"], "Success")
        print("Serial Begin Successfull!"

    def test_serialWrite(self):
        """Testing the serialWrite() function."""
        assert_value = json.loads(client.serialWrite('inventrom'))
        self.assertEqual(assert_value["success"], '1')
        self.assertEqual(assert_value["value"], "Serial write Successful")
        print("Serial Write Successfull!")

    def test_serialRead(self):
        """Testing the serialRead()"""
        assert_value = json.loads(client.serialRead("10"))
        self.assertEqual(assert_value["success"], '1')
        self.assertEqual(assert_value["value"], "inventrom")
        print("Serial Read Successfull!")

    def test_Restart(self):
        """Testing the restart() function."""
        assert_value = json.loads(client.restart())
        time.sleep(5)
        try:
            self.assertEqual(assert_value["value"], "Restarted")
        except AssertionError:
            self.assertEqual(assert_value["value"], "Command timed out")
        print("Restart Successfull!")

    def test_isAlive(self):
        """Testing the isAlive() function."""
        assert_value = json.loads(client.isAlive())
        self.assertEqual(assert_value["success"], '1')
        self.assertEqual(assert_value["value"], "alive")
        print("isAlive Successfull!")

    def test_isOnline(self):
        """Testing the isOnline()"""
        assert_value = json.loads(client.isOnline())
        self.assertEqual(str(assert_value["success"]), '1')
        self.assertEqual(assert_value["value"], "online")
        print("isOnline Successfull!")

if __name__ == "__main__":
    is_device_online = json.loads(client.isOnline())
    if is_device_online["value"] == "online":
        unittest.main()
    else:
        print("The device is offline test cannot be conducted at the moment. Connect your Bolt to the cloud before testing it.")
