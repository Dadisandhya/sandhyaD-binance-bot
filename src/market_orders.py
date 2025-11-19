import argparse
from src.client import BinanceBase
from logger import logger

def place_market(symbol, side, quantity):
    bot = BinanceBase()
    try:
        order = bot.client.futures_create_order(
            symbol=symbol,
            side=side,
            type='MARKET',
            quantity=quantity
        )
        logger.info(f"Market order placed: {order}")
        print(order)
        return order
    except Exception as e:
        logger.error(f"Market order error: {e}")
        print(f"Error placing market order: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description='Place a market order on Binance Futures Testnet or Mock')
    parser.add_argument('symbol', type=str, help='Trading pair symbol e.g. BTCUSDT')
    parser.add_argument('side', type=str, choices=['BUY','SELL'], help='BUY or SELL')
    parser.add_argument('quantity', type=float, help='Quantity to trade')
    args = parser.parse_args()

    if args.quantity <= 0:
        print("Quantity must be positive.")
        return

    place_market(args.symbol, args.side, args.quantity)

if __name__ == '__main__':
    main()
