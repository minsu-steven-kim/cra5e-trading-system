import random


class KiwerAPI:
    def login(self, id, password):
        print(id + ' login success')

    def buy(self, stock_code, count, price):
        print(stock_code + ' : Buy stock ( ' + str(price) + ' * ' + str(count))

    def sell(self, stock_code, count, price):
        print(stock_code + ' : Sell stock ( ' + str(price) + ' * ' + str(count))

    def current_price(self, stock_code) -> int:
        return random.randrange(0, 900) + 5000
