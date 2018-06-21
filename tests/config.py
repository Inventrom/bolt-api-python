"""This file contains all the configurations for unit testing."""

# Configurations for testing GPIO related functions.
GPIO_CONFIG = {
    "VALID_PIN": '0',
    "VALID_DIGITAL_WRITE_VALUE": "HIGH",
    "INVALID_PIN": "16",
    "INVALID_DIGITAL_WRITE_VALUE": "MEDIUM",
    "SUCCESS_RESPONSE": '1',
    "FAILED_RESPONSE": '0',
    "INVALID_PIN_RESPONSE": "Invalid pin value",
    "INVALID_STATE_RESPONSE": "Invalid state",
    "ANALOG_WRITE_VALUE": "100",
    "ANALOG_READ_PIN": "A0",
    "ANALOG_WRITE_PIN": '0',
    "READ_VALUE": "0"
}

# Configurations for testing UART realted functions.
UART_CONFIG = {
    "SUCCESS_RESPONSE": '1',
    "FAILED_RESPONSE": '0',
    "VALID_BAUD_RATE": "9600",
    "INVALID_BAUD_RATE": "10",
    "VALID_BAUD_RESPONSE": "Success",
    "INVALID_BAUD_RESPONSE": "Invalid baud value",
    "VALID_TILL": "10",
    "INVALID_TILL": "1000",
    "VALID_TILL_VALUE": "",
    "INVALID_TILL_VALUE": "Invalid till value",
    "VALID_WRITE_VALUE": "hello",
    "INVALID_WRITE_VALUE": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    "VALID_DATA_RESPONSE": "Serial write Successful",
    "INVALID_DATA_RESPONSE": "Command timed out"
}

# Configurations for testing Utilities realted functions.
UTILITY_CONFIG = {
    "SUCCESS_RESPONSE": '1',
    "FAILED_RESPONSE": '0',
    "RESTART_RESPONSE": "Restarted",
    "RESTART_ALTERNATIVE_RESPONSE": "Command timed out",
    "ONLINE_VALUE": "online"
}

# User configurations.
'''
CREDENTIALS = {
    "API_KEY": "xxxx",
    "DEVICE_ID": "xxxx"
}
'''

CREDENTIALS = {
  "API_KEY": "a0aad35f-9050-4557-870d-7c349356713e",
   "DEVICE_ID": "BOLT3463241"
}
