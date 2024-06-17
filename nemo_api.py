import random
from time import sleep


class NemoAPI:
    def cerification(self, id, password):
        print('[NEMO]' + id + ' login GOOD')

    def purchasing_stock(self, stock_code, price, count):
        print('[NEMO]' + stock_code + ' buy stock ( price : ' + str(price) + ' ) * ( count : ' + str(count) + ')')

    def selling_stock(self, stock_code, price, count):
        print('[NEMO]' + stock_code + ' sell stock ( price : ' + str(price) + ' ) * ( count : ' + str(count) + ')')

    def get_market_price(self, stock_code, minute) -> int:
        if minute <= 0: minute = 1
        sleep(minute / 1000)
        return random.randrange(0, 900) + 5000
