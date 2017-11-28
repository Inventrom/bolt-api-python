from twilio.rest import Client
import requests


BASE_URL = 'https://api.mailgun.net/v3/{}/messages'

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


class Email():
    def __init__(self, api_key, mailgun_domain_name, from_email, to_email):
        self.auth =  api_key
        self.url = BASE_URL.format(mailgun_domain_name)
        self.mailgun_domain_name = mailgun_domain_name
        self.from_email = from_email
        self.to_email = to_email

    def send_email(self, subject, body):
        return requests.post(
            self.url,
            auth=("api", self.auth),
            data={"from": self.from_email,
              "to": self.to_email,
              "subject": subject,
              "text": body})
