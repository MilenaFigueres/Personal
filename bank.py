class Bank:

    def __init__(self, name, balance):
        self.name = name,
        self.balance = balance,
        self.account = 0,
        min_balance = 500

    def take_out_money(self, money):
        if self.balance - money < self.min_balance:
            return "Mr/Mrs {} don´t have enought money in your account".format(
                self.nombre
            )
        else:
            self.balance -= money
            return "Succesful transaction"

    def deposit_money(self, deposit):
        self.balance += deposit
        return "Your deposit was made correctly"



