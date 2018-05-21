from boltiot.bolt import Bolt
from unittest import TestCase

client = Bolt('','') # Pass in the API Key and the client ID.

# Testing the digital write function.
class BoltTests(TestCase):

    def test_digitalWrite():
        assert_value = client.digitalWrite('0','HIGH')
        self.assertEqual(assert_value["success"],1)
        self.assertEqual(assert_value["value"],1)

    def test_digitalRead():
        assert_value = client.digitalRead('0')
        self.assertEqual(assert_value["success"],1)
        self.assertEqual(assert_value["value"],1)

    def test_analogRead():
        assert_value = client.analogRead('A0')
        self.assertEqual(assert_value["success"],1)
        self.assertTrue(0 <= int(assert_value["value"]) <= 254)

    def test_analogWrite():
        assert_value = client.analogWrite('A0','100')
        self.assertEqual(assert_value["success"],"1")
        self.assertEqual(assert_value["value"],"1")

    def test_serialBegin():
        assert_value = client.serialBegin('9600')
        self.assertEqual(assert_value["success"],"1")
        self.assertEqual(assert_value["value"],"Success")

    def test_serialWrite():
        assert_value = client.serialWrite('5')
        self.assertEqual(assert_value["success"],"1")
        self.assertEqual(assert_value["value"],"Serial write Successful")

    def test_serialRead():
        assert_value = client.serialRead('10')
        self.assertEqual(assert_value["success"],"1")
        self.assertEqual(assert_value["value"],"inventrom")

    def test_restart():
        assert_value = client.restart()
        self.assertEqual(assert_value["success"],"1")
        self.assertEqual(assert_value["value"],"Restarted")

    def test_isAlive():
        assert_value = client.isAlive()
        self.assertEqual(assert_value["success"],"1")
        self.assertEqual(assert_value["value"],"alive")

    def test_isOnline():
        assert_value = client.isOnline()
        self.assertEqual(assert_value["success"],"1")
        self.assertEqual(assert_value["value"],"online")
        
