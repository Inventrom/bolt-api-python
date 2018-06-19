"""Test utility functions"""
import unittest
from config import UTILITY_CONFIG, CREDENTIALS
from ..boltiot import Bolt

bolt = Bolt(CREDENTIALS["API_KEY"], CREDENTIALS["DEVICE_ID"])

class TestUtilityFunctions(unittest.TestCase):

    SUCCESS_RESPONSE = UTILITY_CONFIG["SUCCESS_RESPONSE"]
    FAILED_RESPONSE =  UTILITY_CONFIG["FAILED_RESPONSE"]
    RESTART_RESPONSE = UTILITY_CONFIG["RESTART_RESPONSE"]
    RESTART_ALTERNATIVE_RESPONSE = UTILITY_CONFIG["RESTART_ALTERNATIVE_RESPONSE"]
    ONLINE_VALUE = UTILITY_CONFIG["ONLINE_VALUE"]

    def test_is_online_successfull_operation(self):
        resp = json.loads(bolt.isOnline())
        self.assertEqual(resp["success"], self.SUCCESS_RESPONSE)
        self.assertEqual(resp["value"], self.ONLINE_VALUE)

    def test_version_successfull_operation(self):
        resp = json.loads(bolt.version())
        self.assertEqual(resp["success"], self.SUCCESS_RESPONSE)
        self.assertTrue(resp["value"] != None)

    def test_restart_successfull_operation(self):
        resp = json.loads(bolt.restart())
        try:
            self.assertEqual(resp["value"], self.RESTART_RESPONSE)
        except AssertionError:
            self.assertEqual(resp["value"], self.RESTART_ALTERNATIVE_RESPONSE)
