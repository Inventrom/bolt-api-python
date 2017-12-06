from twilio.rest import Client
import requests


BASE_URL = 'https://api.mailgun.net/v3/{}/messages'

class Sms():
    '''will handle the sending sms'''

    def __init__(self, account_sid, auth_token, to_number, from_number):
        """
        Creating a class construcor.

        :param str account_sid: account_sid key to authenticate user
        :param str auth_token: auth_token key to authenticate user
        :param str to_number: number where you want to send sms
        :param str from_number:number from where user will receive the sms

        :returns: None
        :rtype: None
        """
        self.account_sid, self.auth_token = account_sid, auth_token
        self.to_number, self.from_number = to_number, from_number
        self.client = Client(self.account_sid, self.auth_token)

    def send_sms(self, message=None):
        """
        send the sms using twilio client

        :param str pin: pin  numberto write the value
        :param str state: value of pin

        :returns:  class type
        :example: <Twilio.Api.V2010.MessageInstance
        sid=SM2452658d2c9c485584ffa399b22880b2
        account_sid=AC8069c9ad11bf7e5b878bce3266c4ec1e>

        :rtype: Instance
        """
        response = self.client.messages.create(
            to=self.to_number,
            from_=self.from_number,
            body=message)
        return response


class Email():
    '''will handle the seding email'''

    def __init__(self, api_key, mailgun_domain_name, from_email, to_email):
        """
        Creating a class construcor.

        :param str api_key : api_key key to authenticate user
        :param str mailgun_domain_name : verified domain on mailgun
        :param str from_email : email from where user will receive the sms
        :param str to_email : email where you want to send email

        :returns: None
        :rtype: None
        """
        self.auth = api_key
        self.url = BASE_URL.format(mailgun_domain_name)
        self.mailgun_domain_name = mailgun_domain_name
        self.from_email = from_email
        self.to_email = to_email

    def send_email(self, subject, body):
        """
        send the sms using mailgun

        :param str subject: subject line of email
        :param str body: cotent of email

        :returns: class
        :rtype: Instance
        """
        return requests.post(
            self.url,
            auth=("api", self.auth),
            data={"from": self.from_email,
                  "to": self.to_email,
                  "subject": subject,
                  "text": body})
