from unittest import TestCase
from unittest.mock import Mock

from kiwer_stock_broker import KiwerStockBroker
from nemo_stock_broker import NemoStockBroker
from stock_broker import StockBroker
from trading_system import TradingSystem

FAKE_USER_ID = 'guest'
FAKE_PASSWORD = 'qwer1234'
FAKE_TICKER = 'GOOG'
FAKE_QUANTITY = 10
FAKE_PRICE = 650


class TestTradingSystem(TestCase):

    def setUp(self):
        self.system = TradingSystem()
        self.mock_broker = Mock(spec=StockBroker)
        self.system.select_stock_broker(self.mock_broker)

    def test_select_stock_broker(self):
        self.assertIs(self.mock_broker, self.system.broker)

    def test_login(self):
        self.system.login(FAKE_USER_ID, FAKE_PASSWORD)
        self.mock_broker.login.assert_called_with(FAKE_USER_ID, FAKE_PASSWORD)

    def test_buy(self):
        self.system.buy(FAKE_TICKER, FAKE_QUANTITY, FAKE_PRICE)
        self.mock_broker.buy.assert_called_with(FAKE_TICKER, FAKE_QUANTITY, FAKE_PRICE)

    def test_sell(self):
        self.system.sell(FAKE_TICKER, FAKE_QUANTITY, FAKE_PRICE)
        self.mock_broker.sell.assert_called_with(FAKE_TICKER, FAKE_QUANTITY, FAKE_PRICE)

    def test_get_price(self):
        self.mock_broker.get_current_price.return_value = FAKE_PRICE
        result = self.system.get_price(FAKE_TICKER)
        self.assertEqual(FAKE_PRICE, result)

    def test_buy_nice_timing_when_always_increasing(self):
        self.mock_broker.get_current_price.side_effect = [10, 20, 30, 40, 50]
        self.system.buy_nice_timing(FAKE_TICKER, FAKE_QUANTITY)
        self.mock_broker.buy.assert_called_with(FAKE_TICKER, FAKE_QUANTITY, 30)

    def test_buy_nice_timing_when_always_decreasing(self):
        self.mock_broker.get_current_price.side_effect = [50, 40, 30, 20, 10]
        self.system.buy_nice_timing(FAKE_TICKER, FAKE_QUANTITY)
        self.mock_broker.buy.assert_not_called()

    def test_buy_nice_timing_when_fluctuating(self):
        self.mock_broker.get_current_price.side_effect = [50, 40, 55, 60, 70, 65, 45]
        self.system.buy_nice_timing(FAKE_TICKER, FAKE_QUANTITY)
        self.mock_broker.buy.assert_called_with(FAKE_TICKER, FAKE_QUANTITY, 60)

    def test_sell_nice_timing_when_always_increasing(self):
        self.mock_broker.get_current_price.side_effect = [10, 20, 30, 40, 50]
        self.system.sell_nice_timing(FAKE_TICKER, FAKE_QUANTITY)
        self.mock_broker.sell.assert_not_called()

    def test_sell_nice_timing_when_always_decreasing(self):
        self.mock_broker.get_current_price.side_effect = [50, 40, 30, 20, 10]
        self.system.sell_nice_timing(FAKE_TICKER, FAKE_QUANTITY)
        self.mock_broker.sell.assert_called_with(FAKE_TICKER, FAKE_QUANTITY, 30)

    def test_sell_nice_timing_when_fluctuating(self):
        self.mock_broker.get_current_price.side_effect = [50, 40, 55, 60, 70, 65, 45]
        self.system.sell_nice_timing(FAKE_TICKER, FAKE_QUANTITY)
        self.mock_broker.sell.assert_called_with(FAKE_TICKER, FAKE_QUANTITY, 45)

    def test_select_kiwer_stock_broker(self):
        self.system.select_stock_broker(KiwerStockBroker())
        self.assertIsInstance(self.system.broker, KiwerStockBroker)

    def test_select_nemo_stock_broker(self):
        self.system.select_stock_broker(NemoStockBroker())
        self.assertIsInstance(self.system.broker, NemoStockBroker)
