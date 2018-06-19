"""Testing file for GPIO functions"""
import unittest
import json
from config import GPIO_CONFIG, CREDENTIALS
from boltiot import Bolt

bolt = Bolt(CREDENTIALS["API_KEY"],CREDENTIALS["DEVICE_ID"])

class TestGPIOFunctions(unittest.TestCase):

    VALID_PIN = GPIO_CONFIG["VALID_PIN"]
    INVALID_PIN = GPIO_CONFIG["INVALID_PIN"]
    VALID_DIGITAL_WRITE_VALUE = GPIO_CONFIG["VALID_DIGITAL_WRITE_VALUE"]
    INVALID_DIGITAL_WRITE_VALUE = GPIO_CONFIG["INVALID_PIN"]
    INVALID_PIN_RESPONSE = GPIO_CONFIG["INVALID_PIN_RESPONSE"]
    INVALID_STATE_RESPONSE = GPIO_CONFIG["INVALID_STATE_RESPONSE"]
    SUCCESS_RESPONSE = GPIO_CONFIG["SUCCESS_RESPONSE"]
    FAILED_RESPONSE = GPIO_CONFIG["FAILED_RESPONSE"]
    READ_VALUE = GPIO_CONFIG["READ_VALUE"]
    ANALOG_WRITE_PIN = GPIO_CONFIG["ANALOG_WRITE_PIN"]
    ANALOG_READ_PIN = GPIO_CONFIG["ANALOG_READ_PIN"]
    ANALOG_WRITE_VALUE = GPIO_CONFIG["ANALOG_WRITE_VALUE"]

    def test_digital_write_successfull_write_operation(self):
        resp = json.loads(bolt.digitalWrite(self.VALID_PIN,
                                            self.VALID_DIGITAL_WRITE_VALUE))
        self.assertEqual(resp["success"], self.SUCCESS_RESPONSE)
        self.assertEqual(resp["value"], self.SUCCESS_RESPONSE)

    def test_digital_write_failed_write_with_invalid_pin_value(self):
        resp = json.loads(bolt.digitalWrite(self.INVALID_PIN,
                                            self.VALID_DIGITAL_WRITE_VALUE))
        self.assertEqual(resp["success"], self.FAILED_RESPONSE)
        self.assertEqual(resp["value"], self.INVALID_PIN_RESPONSE)

    def test_digital_write_failed_write_with_invalid_write_value(self):
        resp = json.loads(bolt.digitalWrite(self.VALID_PIN,
                                            self.INVALID_DIGITAL_WRITE_VALUE))
        self.assertEqual(resp["success"], self.FAILED_RESPONSE)
        self.assertEqual(resp["value"], self.INVALID_STATE_RESPONSE)

    def test_analog_write_successfull_write_operation(self):
        resp = json.loads(bolt.analogWrite(self.ANALOG_WRITE_PIN,
                                           self.ANALOG_WRITE_VALUE))
        self.assertEqual(resp["success"], self.SUCCESS_RESPONSE)
        self.assertEqual(resp["value"], self.SUCCESS_RESPONSE)

    def test_analog_write_failed_write_with_invalid_pin_value(self):
        resp = json.loads(bolt.analogWrite(self.INVALID_PIN,
                                           self.ANALOG_WRITE_VALUE))
        self.assertEqual(resp["success"], self.FAILED_RESPONSE)
        self.assertEqual(resp["value"], self.INVALID_PIN_RESPONSE)

    def test_digital_read_successfull_read_operation(self):
        resp = json.loads(bolt.digitalRead(self.VALID_PIN))
        self.assertEqual(resp["success"], self.SUCCESS_RESPONSE)
        self.assertEqual(resp["value"], self.READ_VALUE)

    def test_digital_read_failed_read_with_invalid_pin_value(self):
        resp = json.loads(bolt.digitalRead(self.INVALID_PIN))
        self.assertEqual(resp["success"], self.FAILED_RESPONSE)
        self.assertEqual(resp["value"], self.INVALID_PIN_RESPONSE)

    def test_analog_read_successfull_read_operation(self):
        resp = json.loads(bolt.analogRead(self.ANALOG_READ_PIN))
        self.assertEqual(resp["success"], self.SUCCESS_RESPONSE)
        self.assertTrue(0 <= int(resp["value"]) <= 1024)

    def test_analog_read_failed_with_invalid_pin(self):
        resp = json.loads(bolt.analogRead(self.INVALID_PIN))
        self.assertEqual(resp["success"], self.FAILED_RESPONSE)
        self.assertEqual(resp["value"], self.INVALID_PIN_RESPONSE)

if __name__ == '__main__':
    unittest.main()
