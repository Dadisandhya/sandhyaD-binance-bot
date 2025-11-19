import time
from client import BinanceBase
from logger import logger

class OCO:
    def __init__(self):
        self.bot = BinanceBase()

    def place_oco(self, symbol, side, quantity, take_profit_price, stop_price, stop_limit_price):

        try:
            tp = self.bot.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='LIMIT',
                timeInForce='GTC',
                quantity=quantity,
                price=str(take_profit_price)
            )
            sl = self.bot.client.futures_create_order(
                symbol=symbol,
                side='SELL' if side=='BUY' else 'BUY',
                type='STOP',
                stopPrice=str(stop_price),
                closePosition=False,
                quantity=quantity
            )
            logger.info(f"OCO orders placed: TP={tp}, SL={sl}")
            return {'take_profit': tp, 'stop': sl}
        except Exception as e:
            logger.error(f"OCO error: {e}")
            raise
