import os
import time
from dotenv import load_dotenv

load_dotenv()

USE_MOCK = os.getenv("USE_MOCK", "false").lower() == "true"

if not USE_MOCK:
    try:
        from binance.client import Client
    except Exception:
        Client = None
else:
    Client = None

class MockClient:
    _order_id = int(time.time()) % 1000000

    def __init__(self):
        self._orders = []

        self._balances = [
            {'asset': 'USDT', 'balance': '5000.00000000', 'availableBalance': '5000.00000000'},
            {'asset': 'BTC', 'balance': '0.01000000', 'availableBalance': '0.01000000'}
        ]

    def futures_account_balance(self):

        return self._balances

    def futures_create_order(self, **kwargs):
        MockClient._order_id += 1
        order_type = kwargs.get('type', 'MARKET')
        qty = kwargs.get('quantity')
        price = kwargs.get('price', '0')
        executed_qty = str(qty) if order_type == 'MARKET' else '0'

        order = {
            'orderId': MockClient._order_id,
            'symbol': kwargs.get('symbol'),
            'status': 'FILLED' if order_type == 'MARKET' else 'NEW',
            'side': kwargs.get('side'),
            'type': order_type,
            'origQty': str(qty),
            'executedQty': executed_qty,
            'price': str(price),
            'clientOrderId': f"mock_{MockClient._order_id}",
            'transactTime': int(time.time() * 1000)
        }

        self._orders.append(order)
        return order

class BinanceBase:
    def __init__(self, api_key=None, api_secret=None, base_url=None, testnet=True):
        api_key = api_key or os.getenv("API_KEY")
        api_secret = api_secret or os.getenv("API_SECRET")
        self.base_url = base_url or os.getenv("BASE_URL", "https://testnet.binancefuture.com")

        if USE_MOCK:

            self.client = MockClient()
        else:
            if Client is None:
                raise RuntimeError("python-binance not installed. Run: pip install python-binance")
            self.client = Client(api_key, api_secret, testnet=testnet)
