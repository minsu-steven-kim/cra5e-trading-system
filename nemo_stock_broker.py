from nemo_api import NemoAPI
from stock_broker import StockBroker


class NemoStockBroker(StockBroker):
    def __init__(self):
        self.nemoStock = NemoAPI()

    def login(self, user_id, password):
        self.nemoStock.cerification(user_id, password)

    def buy(self, ticker, quantity, price):
        self.nemoStock.purchasing_stock(ticker, price, quantity)

    def sell(self, ticker, quantity, price):
        self.nemoStock.selling_stock(ticker, price, quantity)

    def get_current_price(self, ticker):
        print(f"[NEMO]{ticker} current price : {self.nemoStock.get_market_price(ticker, 1000)}")
