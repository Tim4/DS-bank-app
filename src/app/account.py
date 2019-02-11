class Account():
    def __init__(self, firstname, lastname, number, balance=0.0):
        assert type(number) == int, 'Number needs to be an integer!'
        assert type(balance) == float, 'Balance needs to be a float!'
        self.firstname = firstname
        self.lastname = lastname
        self.number = number
        self.balance = balance
        self.bank_ref = ''

    def info(self):
        return 'Number {}: {} {} - {} €'.format(
            self.number,
            self.firstname,
            self.lastname,
            self.balance)

    def has_funds_for(self, funds_ask):
        return self.balance > funds_ask

    def add_to_balance(self, add_balance):
        assert add_balance > 0, 'Amount needs to be greater than 0'
        self.balance += add_balance
        return self.balance

    def subtract_from_balance(self, sub_balance):
        assert self.has_funds_for(sub_balance), 'Account has not enough funds'
        self.balance -= sub_balance
        return self.balance

    def account_log(self):
        for i in self.bank_ref.transactions:
            if i.recipient == self.number:
                print('Date: {} Sender: {} Subject: {} Amount: +{}'.
                      format(i.time_date, i.sender, i.subject, i.amount))
            elif i.sender == self.number:
                print('Date: {} Recipient: {} Subject: {} Amount: -{}'
                      .format(i.time_date, i.recipient, i.subject, i.amount))
        print("Total Balance: " + str(self.bank_ref.accounts[self.number].balance))

