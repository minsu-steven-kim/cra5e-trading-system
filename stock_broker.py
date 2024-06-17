from abc import ABC, abstractmethod


class StockBroker(ABC):
    @abstractmethod
    def login(self, user_id, password):
        pass

    @abstractmethod
    def buy(self, ticker, quantity, price):
        pass

    @abstractmethod
    def sell(self, ticker, quantity, price):
        pass

    @abstractmethod
    def get_current_price(self, ticker):
        pass
