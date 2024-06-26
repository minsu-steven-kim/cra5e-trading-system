from stock_broker import StockBroker

MOVING_AVG_WINDOW = 2

class TradingSystem:
    broker: StockBroker = None

    def __init__(self):
        self.prices = []
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
                increase_count = self.update_increase_count(current_price, increase_count, next_price)

                if self.check_increase_trend(increase_count):
                    self.buy(ticker, user_total_price//current_price, current_price)
                    break

                current_price = next_price
            except:
                break

    def update_increase_count(self, current_price, increase_count, next_price):
        if current_price <= next_price:
            increase_count += 1
        else:
            increase_count = 0
        return increase_count

    def check_increase_trend(self, increase_count):
        return increase_count == 3

    def sell_nice_timing(self, ticker, quantity):
        if len(self.prices) < MOVING_AVG_WINDOW:
            self.prices.append(self.get_price(ticker))
            if len(self.prices) == MOVING_AVG_WINDOW:
                self.prvPriceAvg = self.avg_of_price()
            return

        self.prices = [self.prices[1], self.get_price(ticker)]
        if (self.avg_of_price()) < self.prvPriceAvg:
            self.sell(ticker, quantity, self.prices[-1])
        self.prvPriceAvg = self.avg_of_price()

    def avg_of_price(self):
        return self.sum_of_prices() / MOVING_AVG_WINDOW

    def sum_of_prices(self):
        priceSum = 0
        for price in self.prices:
            priceSum += price
        return priceSum

