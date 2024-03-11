class Card:

    def __unit__(self, number, date, holder):
        self.holder = holder
        self.number = number
        self.validDate = date

    def pay(self, amount):
        print(" с карты ", self.number, "списали ", amount)

