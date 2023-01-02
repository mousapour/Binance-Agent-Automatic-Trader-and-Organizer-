import os
import time
import datetime
import csv
import binance
from binance.client import Client
from binance.websockets import BinanceSocketManager
from binance.exceptions import BinanceAPIException, BinanceOrderException
from twisted.internet import reactor

api_key = 'your-api-key'
api_secret = 'your-api-secret'

class Binance:
    def __init__(self):
        self.api_key = 'your-api-key'
        self.api_secret = 'your-api-secret'
        self.client = Client(api_key, api_secret)
        self.bsm = BinanceSocketManager(client)
        self.conn_key = self.bsm.start_symbol_ticker_socket('BTCUSDT', self.btc_price)
        self.btc_data = {'BTCUSDT': 0, 'error': False}
        self.future_order = 0
        self.spot_order = 0

    def btc_price(self, msg):
        if msg['e'] != 'error':
            self.btc_data['BTCUSDT'] = float(msg['c'])
        else:
            self.btc_data['error']: True

    def future_position(self, size):
        self.future_order = self.client.futures_create_order(symbol='BTCUSDT', side='BUY', type='MARKET', quantity=size)

    def spot_position(self, size):
        self.spot_order = self.client.create_test_order()





def btc_trade_history(msg):
    if msg['e'] != 'error':
        price['BTCUSDT'] = float(msg['c'])
    else:
        price['error']: True


def btc_ask_history(msg):
    if msg['e'] != 'error':
        price['ask'] = float(msg['a'])

        asks.append(price['ask'])
    else:
        price['error']: True


price = {'BTCUSDT': None, 'ask':None, 'error': False}
asks = []

client = Client(api_key, api_secret)
print(client.futures_account_balance())

# bsm = BinanceSocketManager(client)
# conn_key = bsm.start_symbol_ticker_socket('BTCUSDT', btc_trade_history)
# conn_key = bsm.start_symbol_ticker_socket('BTCUSDT', btc_ask_history)
# bsm.start()

print('go!')
# time.sleep(60)
# print(len(asks))

asks = []
start = datetime.datetime.now()
while (datetime.datetime.now()-start).seconds < 60:
    asks.append([datetime.datetime.now(), float(client.get_orderbook_ticker(symbol='BTCUSDT')['askPrice'])])
    time.sleep(0.1)


print(*asks, sep='\n')
print('total number of data: ' + str(len(asks)))

counter = 0
for i in range(1, len(asks)):
    if asks[i][1] != asks[i-1][1]:
        counter += 1

print('total number of changed data: ' + str(counter))

intervals = []
difference = []
variance = 0
for i in range(1, len(asks)):
    intervals.append((asks[i][0] - asks[i-1][0]).microseconds/10**6)
    difference.append(asks[i][1] - asks[i-1][1])
print('mean time difference: ' + str(sum(intervals)/len(intervals)))

m = 0
for i in range(len(difference)):
    m += abs(difference[i])
m /= len(difference)
print('mean price difference: ' + str(m))

m = sum(difference)/len(difference)
for i in range(len(difference)):
    variance = variance + (difference[i] - m)**2
print('variance price difference: ' + str((variance/len(difference))**0.5))








# while not price['BTCUSDT']:
#     time.sleep(0.1)

# print(client.futures_account_trades()[-1])

# order = client.futures_create_order(symbol='BTCUSDT', side='BUY', type='MARKET', quantity=0.001)

# timestamp = client._get_earliest_valid_timestamp('BTCUSDT', '1d')
# timestamp = 1567958400000
# print(datetime.datetime.fromtimestamp(timestamp/1000))
# # print(datetime.datetime.timestamp(datetime.datetime(2021, 4, 5, 23)))
# timestamp = datetime.datetime.timestamp(datetime.datetime(2019, 9, 10, 12, 30, 0))
# bars = client.get_klines(symbol='BTCUSDT', interval='8h', limit=10000000)
# # bars = client.futures_klines('BTCUSDT', '8h', timestamp, limit=1000000000000)
#
# with open('btc_bars.csv', 'w', newline='') as f:
#     wr = csv.writer(f)
#     for line in bars:
#         wr.writerow(line[:6])









# while True:
#     # error check to make sure WebSocket is working
#     if price['error']:
#         # stop and restart socket
#         bsm.stop_socket(conn_key)
#         bsm.start()
#         price['error'] = False
#
#     else:
#
#         if price['BTCUSDT'] > 10000 and datetime.datetime.now() > datetime.datetime(2021, 4, 5, 23):
#             try:
#                 # order = client.order_market_buy(symbol='BTCUSDT', quantity=0.01)
#                 order = client.futures_create_order(symbol='BTCUSDT', side='BUY', type='MARKET', quantity=0.0001)
#                 break
#             except BinanceAPIException as e:
#                 # error handling goes here
#                 print(e)
#             except BinanceOrderException as e:
#                 # error handling goes here
#                 print(e)
#     time.sleep(1)
#     print('hey :)')
#
# buy_order_limit = client.create_test_order(symbol='ETHUSDT', side='BUY', type='LIMIT', timeInForce='GTC', quantity=100, price=2200)
# buy_order = client.create_test_order(symbol='ETHUSDT', side='BUY', type='MARKET', quantity=100)
#
#
# help(BinanceSocketManager)

# bsm.stop_socket(conn_key)
# reactor.stop()



