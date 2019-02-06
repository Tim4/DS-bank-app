class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []
        self.transactions = []

    def open_account(self, account):
        test = 0
        for i in self.accounts:
            if i["number"] == account["number"]:
                test = 1
                break
        assert test == 0, "Account number {} already taken!".format(account["number"])
        self.accounts.append(account)
        return self.accounts[-1]

    def add_transaction(self, *, sender, recipient, subject, amount):
        assert amount > 0, "Amount has to be greater than 0"
        assert sender in self.accounts, "Sender has no account yet!"
        assert recipient in self.accounts, "Recipient has no account yet!"
        _transaction = {"sender" : sender, "recipient" : recipient, "subject": subject, "amount": amount}
        self.transactions.append([_transaction])
        return [_transaction]





