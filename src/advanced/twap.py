import time
from client import BinanceBase
from logger import logger

class TWAP:
    def __init__(self):
        self.bot = BinanceBase()

    def execute_twap(self, symbol, side, total_qty, slices, interval_seconds):
        slice_qty = total_qty / slices
        results = []
        for i in range(slices):
            try:
                res = self.bot.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type='MARKET',
                    quantity=round(slice_qty, 8)
                )
                logger.info(f"TWAP slice {i+1}/{slices} executed: {res}")
                results.append(res)
            except Exception as e:
                logger.error(f"TWAP slice error: {e}")
            time.sleep(interval_seconds)
        return results
