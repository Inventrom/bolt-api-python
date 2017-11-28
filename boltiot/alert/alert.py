from twilio.rest import Client

class Sms():
    def __init__(self, account_sid, auth_token, to_number, from_number):
        self.account_sid, self.auth_token = account_sid, auth_token
        self.to_number, self.from_number = to_number, from_number
        self.client = Client(self.account_sid, self.auth_token)

    def send(self, message = None):
        response = self.client.messages.create(
            to = self.to_number,
            from_ = self.from_number,
            body = message)
        return response
