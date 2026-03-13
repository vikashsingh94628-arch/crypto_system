import requests
import time

def get_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    response = requests.get(url)
    return float(response.json()['price'])

while True:
    eth_price = get_price("ETHUSDT")
    btc_price = get_price("BTCUSDT")
    print(f"ETH: ${eth_price} | BTC: ${btc_price}")
    time.sleep(5)
