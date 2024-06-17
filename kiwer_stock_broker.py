from stock_broker import StockBroker
from kiwer_api import KiwerAPI

class KiwerStockBroker(StockBroker):

    def __init__(self):
        self.api = KiwerAPI()

    def login(self, user_id, password):
        self.api.login(user_id, password)

    def buy(self, ticker, quantity, price):
        self.api.buy(ticker, quantity, price)

    def sell(self, ticker, quantity, price):
        self.api.sell(ticker, quantity, price)

    def get_current_price(self, ticker):
        self.api.current_price(ticker)
