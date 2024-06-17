from stock_broker import StockBroker


class TradingSystem:
    broker: StockBroker = None

    def __init__(self):
        pass

    def select_stock_broker(self, broker: StockBroker):
        self.broker = broker

    def login(self, user_id, password):
        pass

    def buy(self, ticker, quantity, price):
        pass

    def sell(self, ticker, quantity, price):
        pass

    def get_price(self, ticker):
        pass

    def buy_nice_timing(self, ticker, quantity):
        pass

    def sell_nice_timing(self, ticker, quantity):
        pass
