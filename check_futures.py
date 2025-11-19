import os
from dotenv import load_dotenv

load_dotenv()

from binance.client import Client

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

if not API_KEY or not API_SECRET:
    print("ENV keys missing.")
    raise SystemExit(1)

client = Client(API_KEY, API_SECRET, testnet=True)

client.API_URL = "https://testnet.binancefuture.com"

try:

    info = client.futures_account_balance()
    print("SUCCESS - fetched futures account balance:")
    print(info)
except Exception as e:
    print("ERROR from Binance API:")
    print(e)
