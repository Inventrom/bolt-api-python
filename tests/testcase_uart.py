"""Tests for UART functions"""
import unittest
import json
import time
from context import Bolt
from config import UART_CONFIG, CREDENTIALS

bolt = Bolt(CREDENTIALS["API_KEY"], CREDENTIALS["DEVICE_ID"])

class TestUARTFunctions(unittest.TestCase):
    """
    A simple class to test all the functions realted to UART.
    Methods:
    -test_serial_begin_successfull_operation()
    -test_serial_begin_failed_with_invalid_baud_rate()
    -test_serial_read_successfull_operation()
    -test_serial_read_failed_with_invalid_till()
    -test_serial_write_successfull_operation()
    -test_serial_write_failed_with_command_timedout()
    """

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

    def tearDown(self):
        time.sleep(3)

    def test_serial_begin_successfull_operation(self):
        """
        The function tests for a successfull serial begin operation.
        """
        resp = json.loads(bolt.serialBegin(self.VALID_BAUD_RATE))
        self.assertEqual(resp["success"], self.SUCCESS_RESPONSE)
        self.assertEqual(resp["value"], self.VALID_BAUD_RESPONSE)

    def test_serial_begin_failed_with_invalid_baud_rate(self):
        """
        The function tests for a failed serial begin operation,
        if an incorrect baud rate is passed.
        """
        resp = json.loads(bolt.serialBegin(self.INVALID_BAUD_RATE))
        self.assertEqual(resp["success"], self.FAILED_RESPONSE)
        self.assertEqual(resp["value"], self.INVALID_BAUD_RESPONSE)

    def test_serial_read_successfull_operation(self):
        """
        The function tests for a successfull serial read operation.
        """
        resp = json.loads(bolt.serialRead(self.VALID_TILL))
        self.assertEqual(resp["success"], self.SUCCESS_RESPONSE)
        self.assertEqual(resp["value"], self.VALID_TILL_VALUE)

    @unittest.skip("Will be implemented after API fix.")
    def test_serial_read_failed_with_invalid_till(self):
        """
        The function tests for a failed serial read operation,
        if an incorrect read till value is passed.
        """
        resp = json.loads(bolt.serialRead(self.INVALID_TILL))
        self.assertEqual(resp["success"], self.FAILED_RESPONSE)
        self.assertEqual(resp["value"], self.INVALID_TILL_VALUE)

    def test_serial_write_successfull_operation(self):
        """
        The function tests for a successfull serial write operation.
        """
        resp = json.loads(bolt.serialWrite(self.VALID_WRITE_VALUE))
        self.assertEqual(resp["success"], self.SUCCESS_RESPONSE)
        self.assertEqual(resp["value"], self.VALID_DATA_RESPONSE)

    def test_serial_write_failed_with_command_timedout(self):
        """
        The function tests for a failed serial write operation,
        if a large amount of data is passed on serial
        """
        resp = json.loads(bolt.serialWrite(self.INVALID_WRITE_VALUE))
        self.assertEqual(resp["success"], self.FAILED_RESPONSE)
        self.assertEqual(resp["value"], self.INVALID_DATA_RESPONSE)

if __name__ == '__main__':
    unittest.main()
