
class Player():
    def __init__(self, name, bank_account=1000):
        self.name = name
        self.bank_account = bank_account
    
    def purchase(self, price):
        self.bank_account = self.bank_account - price
    
    def wins(self, winnings):
        self.bank_account = self.bank_account + winnings

    def __str__(self):
        inv = ""
        for ivt in self.bank_account:
            inv += " "+ ivt.name
        return """
            Bank Account Balance: %s
        """ % (self.bank_account)