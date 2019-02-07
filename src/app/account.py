class Account():
    def __init__(self, firstname, lastname, number, balance=0.0):
        assert type(number) == int, 'Number needs to be an integer!'
        assert type(balance) == float, 'Balance needs to be a float!'
        self.firstname = firstname
        self.lastname = lastname
        self.number = number
        self.balance = balance

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
