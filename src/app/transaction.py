import time
import datetime


class Transaction():
    def __init__(self, sender, recipient, subject, amount):
        assert type(sender) == int, 'Sender needs to be an integer'
        assert type(recipient) == int, 'Recipient needs to be an integer'
        assert type(amount) == float, 'Amount needs to be a float'
        assert amount > 0, 'Amount needs to be greater than 0'
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.amount = amount
        self.time_date = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

    def info(self):
        return 'From {} to {}: {} - {} €'.format(
            self.sender,
            self.recipient,
            self.subject,
            self.amount
        )
