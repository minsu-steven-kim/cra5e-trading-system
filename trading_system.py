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
        increase_count = 0
        current_price = self.get_price(ticker)
        while True:
            try:
                next_price = self.get_price(ticker)
                if current_price <= next_price:
                    increase_count += 1
                else:
                    increase_count = 0

                if increase_count == 3:
                    self.buy(ticker, user_total_price//current_price, current_price)
                    break
                else:
                    current_price = next_price
            except:
                break
    def sell_nice_timing(self, ticker, quantity):
        # TODO: #2
        pass
