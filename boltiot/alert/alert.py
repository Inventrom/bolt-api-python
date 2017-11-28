# from sms_sender import sms
# from email_sender import email
# import conf

from twilio.rest import Client

class Sms():
    def __init__(self, account_sid, auth_token, to_number, from_number):
        self.account_sid, self.auth_token = account_sid, auth_token
        self.to_number, self.from_number = to_number, from_number
        self.client = Client(self.account_sid, self.auth_token)

    def send(self):
        message = self.client.messages.create(
            to=self.to_number,
            from_=self.from_number,
            body="Hello from Python!")
        return message
