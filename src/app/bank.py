from .account import Account
from .transaction import Transaction


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
        self.transactions = []

    def open_account(self, account_object):
        assert isinstance(account_object, Account), 'Account should be an app.Account'
        assert account_object.number not in self.accounts.keys(), 'Account number {} already taken!'.format(account_object.number)
        self.accounts[account_object.number] = account_object
        return self.accounts[account_object.number]

    def add_transaction(self, sender, recipient, subject, amount):
        assert sender.number in self.accounts.keys(), 'Sender has no account yet!'
        assert recipient.number in self.accounts.keys(), 'Recipient has no account yet!'
        assert self.accounts[sender.number].balance >= amount, 'Account has not enough funds'
        transaction = Transaction(
            sender=sender.number,
            recipient=recipient.number,
            subject=subject,
            amount=amount)
        self.transactions.append(transaction)
        self.accounts[sender.number].balance -= amount
        self.accounts[recipient.number].balance += amount
        return transaction
