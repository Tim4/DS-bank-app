import app
import numpy as np
import random
from random_word import RandomWords

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
        self.transactions = []

    def open_account(self, account_object):
        assert isinstance(account_object, app.Account), 'Account should be an app.Account'
        assert account_object.number not in self.accounts.keys(), 'Account number {} already taken!'.format(account_object.number)
        self.accounts[account_object.number] = account_object
        account_object.bank_ref = self
        return self.accounts[account_object.number]

    def open_account_manually(self):
        #get input values
        account_number = ''
        print('Work faster!')
        print('Please input a valid number, following accounts are occupied: {}'.format(
            [i for i in self.accounts.keys()]))
        while True:
            account_number = input("Enter account number:")
            if (account_number.isdigit() == True) & (account_number not in str(self.accounts.keys())):
                account_number = int(account_number)
                break
        print('Please enter the customer name')
        name_input = input("Name: ")
        firstname, lastname = ' '.join(name_input.split()[:-1]), name_input.split()[-1]
        print('Please enter the initial balance: ')
        balance_init = float(input())
        self.open_account(app.Account(firstname, lastname, account_number, balance_init))
        return self.accounts[account_number]

    def add_transaction(self, sender, recipient, subject, amount):
        assert sender.number in self.accounts.keys(), 'Sender has no account yet!'
        assert recipient.number in self.accounts.keys(), 'Recipient has no account yet!'
        assert self.accounts[sender.number].balance >= amount, 'Account has not enough funds'
        transaction = app.Transaction(
            sender=sender.number,
            recipient=recipient.number,
            subject=subject,
            amount=amount)
        self.transactions.append(transaction)
        sender.subtract_from_balance(amount)
        recipient.add_to_balance(amount)
        return transaction

    def customer_log(self, customer):
        for i in self.transactions:
            if i.recipient == customer:
                print('Date: {} Sender: {} Subject: {} Amount: +{}'.
                      format(i.time_date, i.sender, i.subject, i.amount))
            elif i.sender == customer:
                print('Date: {} Recipient: {} Subject: {} Amount: -{}'
                      .format(i.time_date, i.recipient, i.subject, i.amount))
        print("Total Balance: " + str(self.accounts[customer].balance))

    def transaction_statistics(self):
        amount_list = ([i.amount for i in self.transactions])
        print('Mean transaction volumne: {}'.format(np.mean(amount_list)))
        print('Min transaction volume: {}'.format(np.min(amount_list)))
        print('Max transaction volume: {}'.format(np.max(amount_list)))
        print('Number of transactions in record: {}'.format(len(self.transactions)))
        for i, q in enumerate(amount_list):
            if q > np.percentile(np.array(amount_list), 95):
                print('Extreme high transaction amount, please crosscheck transaction: {}, Amount: {}'.format(
                    i, amount_list[i]))

    def random_transactions(self):
        r = RandomWords()
        subjects = r.get_random_words()
        for i in range(10):
            sender, recipient = random.sample(self.accounts.keys(), 2)
            subject = subjects[i]
            amount = random.uniform(0.0000001, self.accounts[sender].balance)
            self.add_transaction(sender=self.accounts[sender], recipient=self.accounts[recipient],
                                 subject=subject, amount=amount)
        return self.transactions