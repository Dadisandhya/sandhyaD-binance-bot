Binance Futures Order Bot

Candidate: Sandhya D
Project: CLI-Based Trading Bot (Market + Limit Orders)

Overview

This project implements a Command-Line Interface (CLI) trading bot for Binance USDT-M Futures.
It supports:

Market Orders

Limit Orders

(Bonus) OCO & TWAP structure

The bot includes full logging, modular structure, and a mock mode to simulate orders when Testnet is blocked in certain regions.

Project Structure
sandhyaD_binance_bot/
│
├── src/
│   ├── client.py
│   ├── market_orders.py
│   ├── limit_orders.py
│   ├── __init__.py
│   └── advanced/
│       ├── oco.py
│       ├── twap.py
│       └── __init__.py
│
├── logger.py
├── bot.log
├── README.md
└── .env.example

Environment Setup
1. Install required packages:
pip install python-binance python-dotenv

2. Create a .env file (do NOT upload):
API_KEY=your_testnet_api_key
API_SECRET=your_testnet_api_secret
BASE_URL=https://testnet.binancefuture.com

# Mock mode enabled (recommended in restricted regions)
USE_MOCK=true

-> About USE_MOCK=true

If Testnet is blocked in your region, mock mode:

Simulates trading

Produces Binance-style JSON responses

Requires no real keys

Ensures project works anywhere

No real trades or money involved.

How to Run the Bot
Market Order
python -m src.market_orders BTCUSDT BUY 0.01

Limit Order
python -m src.limit_orders BTCUSDT SELL 0.01 60000

Check order logs in:

bot.log

Mock Mode (Recommended for Testing)

Mock mode allows:

Offline execution

No API key requirement

Safe simulated orders

Identical structure to Binance API

To enable mock mode:

USE_MOCK=true

Switching to Real Testnet (Optional)

If your region supports Binance Futures Testnet:

Set:

USE_MOCK=false


Get API keys from Futures Testnet

Install python-binance

Use the same commands to place orders

Bonus Features (Advanced Orders)

Located in src/advanced/:

OCO order structure (oco.py)

TWAP strategy structure (twap.py)

These modules show how advanced strategies can be built into the bot.

Note:

This project was executed using dummy data and USE_MOCK mode due to Binance Testnet regional restrictions.
All order outputs are simulated for demonstration and evaluation purposes.

Commands Reference
Market Buy BTC:
python -m src.market_orders BTCUSDT BUY 0.01

Limit Sell BTC:
python -m src.limit_orders BTCUSDT SELL 0.01 60000

Contact

Submitted by: Sandhya D
