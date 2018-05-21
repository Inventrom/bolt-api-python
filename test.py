from boltiot.bolt import Bolt
from unittest import TestCase
import json

client = Bolt('123','123') # Pass in the API Key and the client ID.

class BoltTests(TestCase):
    
# Testing the digital write function.
    
    def test_digitalWrite():
        assert_value = json.loads(client.digitalWrite('0','HIGH'))
        self.assertEqual(assert_value["success"],1)
        self.assertEqual(assert_value["value"],1)

# Testing the digital read function.
        
    def test_digitalRead():
        assert_value = json.loads(client.digitalRead('0'))
        self.assertEqual(assert_value["success"],1)
        self.assertEqual(assert_value["value"],1)

# Testing the analog read function.
        
    def test_analogRead():
        assert_value = json.loads(client.analogRead('A0'))
        self.assertEqual(assert_value["success"],1)
        self.assertTrue(0 <= int(assert_value["value"]) <= 254)

# Testing the analog write function
        
    def test_analogWrite():
        assert_value = json.loads(client.analogWrite('A0','100'))
        self.assertEqual(assert_value["success"],"1")
        self.assertEqual(assert_value["value"],"1")

# Testing the serialBegin() function.
        
    def test_serialBegin():
        assert_value = json.loads(client.serialBegin('9600'))
        self.assertEqual(assert_value["success"],"1")
        self.assertEqual(assert_value["value"],"Success")

# Testing the serialWrite() function.
        
    def test_serialWrite():
        assert_value = json.loads(client.serialWrite('5'))
        self.assertEqual(assert_value["success"],"1")
        self.assertEqual(assert_value["value"],"Serial write Successful")

# Testing the serialRead() function.
        
    def test_serialRead():
        assert_value = json.loads(client.serialRead('10'))
        self.assertEqual(assert_value["success"],"1")
        self.assertEqual(assert_value["value"],"inventrom")

# Testing the restart() function.
        
    def test_restart():
        assert_value = json.loads(client.restart())
        self.assertEqual(assert_value["success"],"1")
        self.assertEqual(assert_value["value"],"Restarted")

# Testing the isAlive() function.
        
    def test_isAlive():
        assert_value = json.loads(client.isAlive())
        self.assertEqual(assert_value["success"],"1")
        self.assertEqual(assert_value["value"],"alive")

# Testing the isOnline() function
        
    def test_isOnline():
        assert_value = json.loads(client.isOnline())
        self.assertEqual(assert_value["success"],"1")
        self.assertEqual(assert_value["value"],"online")
        

if __name__ == "__main__":
    device_status = json.loads(client.isOnline())
    if(device_status["value"] == "online"):
        unittest.main()
    else:
        print("The device is offline test cannot be conducted at the moment. Connect your Bolt to the cloud before testing it.")


