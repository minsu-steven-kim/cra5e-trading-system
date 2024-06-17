from stock_broker import StockBroker


class TradingSystem:
    broker: StockBroker = None

    def __init__(self):
        pass

    def select_stock_broker(self, broker: StockBroker):
        self.broker = broker

    def login(self, user_id, password):
        self.broker.login(user_id, password)

    def buy(self, ticker, quantity, price):
        self.broker.buy(ticker, quantity, price)

    def sell(self, ticker, quantity, price):
        self.broker.sell(ticker, quantity, price)

    def get_price(self, ticker):
        return self.broker.get_current_price(ticker)

    def buy_nice_timing(self, ticker, user_total_price):
        # TODO: #1
        pass

    def sell_nice_timing(self, ticker, quantity):
        # TODO: #2
        pass
