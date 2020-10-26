


class Player():
    def __init__(self, name, bank_account=1000):
        self.name = name
        self.bank_account = bank_account
    
    def purchase(self, price):
        self.bank_account = self.bank_account - price
    
    def wins(self, winnings):
        self.bank_account = self.bank_account + winnings
    
    def loses(self, winnings):
        self.bank_account = self.bank_account - winnings

    def sell_car(self, price):
        self.bank_account += price
       
            