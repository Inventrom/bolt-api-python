"""Tests for UART functions"""
import unittest
import json
from config import UART_CONFIG, CREDENTIALS
from boltiot import Bolt

bolt = Bolt(CREDENTIALS["API_KEY"], CREDENTIALS["DEVICE_ID"])

class TestUARTFunctions(unittest.TestCase):

    VALID_BAUD_RATE = UART_CONFIG["VALID_BAUD_RATE"]
    INVALID_BAUD_RATE = UART_CONFIG["INVALID_BAUD_RATE"]
    VALID_BAUD_RESPONSE = UART_CONFIG["VALID_BAUD_RESPONSE"]
    INVALID_BAUD_RESPONSE = UART_CONFIG["INVALID_BAUD_RESPONSE"]
    VALID_TILL = UART_CONFIG["VALID_TILL"]
    INVALID_TILL = UART_CONFIG["INVALID_TILL"]
    VALID_TILL_VALUE = UART_CONFIG["VALID_TILL_VALUE"]
    INVALID_TILL_VALUE = UART_CONFIG["INVALID_TILL_VALUE"]
    VALID_WRITE_VALUE = UART_CONFIG["VALID_WRITE_VALUE"]
    INVALID_WRITE_VALUE = UART_CONFIG["INVALID_WRITE_VALUE"]
    VALID_DATA_RESPONSE = UART_CONFIG["VALID_DATA_RESPONSE"]
    INVALID_DATA_RESPONSE = UART_CONFIG["INVALID_DATA_RESPONSE"]
    SUCCESS_RESPONSE = UART_CONFIG["SUCCESS_RESPONSE"]
    FAILED_RESPONSE = UART_CONFIG["FAILED_RESPONSE"]

    def test_serial_begin_successfull_operation(self):
        resp = json.loads(bolt.serialBegin(self.VALID_BAUD_RATE))
        self.assertEqual(resp["success"], self.SUCCESS_RESPONSE)
        self.assertEqual(resp["value"], self.VALID_BAUD_RESPONSE)

    def test_serial_begin_failed_with_invalid_baud_rate(self):
        resp = json.loads(bolt.serialBegin(self.INVALID_BAUD_RATE))
        self.assertEqual(resp["success"], self.FAILED_RESPONSE)
        self.assertEqual(resp["value"], self.INVALID_BAUD_RESPONSE)

    def test_serial_read_successfull_operation(self):
        resp = json.loads(bolt.serialRead(self.VALID_TILL))
        self.assertEqual(resp["success"], self.SUCCESS_RESPONSE)
        self.assertEqual(resp["value"], self.VALID_TILL_VALUE)

    def test_serial_read_failed_with_invalid_till(self):
        resp = json.loads(bolt.serialRead(self.INVALID_TILL))
        self.assertEqual(resp["success"], self.FAILED_RESPONSE)
        self.assertEqual(resp["value"], self.INVALID_TILL_VALUE)

    def test_serial_write_successfull_operation(self):
        resp = json.loads(bolt.serialWrite(self.VALID_WRITE_VALUE))
        self.assertEqual(resp["success"], self.SUCCESS_RESPONSE)
        self.assertEqual(resp["value"], self.VALID_DATA_RESPONSE)

    def test_serial_write_failed_with_command_timedout(self):
        resp = json.loads(bolt.serialWrite(self.INVALID_WRITE_VALUE))
        self.assertEqual(resp["success"], self.FAILED_RESPONSE)
        self.assertEqual(resp["value"], self.INVALID_DATA_RESPONSE)

if __name__ == '__main__':
    unittest.main()
