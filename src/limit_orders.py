import argparse
from src.client import BinanceBase
from logger import logger

def place_limit(symbol, side, quantity, price, timeInForce='GTC'):
    bot = BinanceBase()
    try:
        order = bot.client.futures_create_order(
            symbol=symbol,
            side=side,
            type='LIMIT',
            timeInForce=timeInForce,
            quantity=quantity,
            price=str(price)
        )
        logger.info(f"Limit order placed: {order}")
        print(order)
        return order
    except Exception as e:
        logger.error(f"Limit order error: {e}")
        print(f"Error placing limit order: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description='Place a limit order on Binance Futures Testnet or Mock')
    parser.add_argument('symbol', type=str, help='Trading pair symbol e.g. BTCUSDT')
    parser.add_argument('side', type=str, choices=['BUY','SELL'], help='BUY or SELL')
    parser.add_argument('quantity', type=float, help='Quantity to trade')
    parser.add_argument('price', type=float, help='Limit price')
    args = parser.parse_args()

    if args.quantity <= 0:
        print("Quantity must be positive.")
        return
    if args.price <= 0:
        print("Price must be positive.")
        return

    place_limit(args.symbol, args.side, args.quantity, args.price)

if __name__ == '__main__':
    main()
