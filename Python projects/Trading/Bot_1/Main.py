import time
import datetime
import pandas as pd
import ccxt
import matplotlib.pyplot as plt

class BinanceTrader:
    def __init__(self):
        self.apikey_secret()
        self.auto_trading = False
        self.strategies = {}
        
        while True:
            try:
                self.exc = ccxt.binance({
                    'apiKey': self.api_key,
                    'secret': self.secret,
                    'enableRateLimit': True,
                    'options': {
                        'future'
                    }
                })
                self.exc.load_markets()
                break

            except ccxt.AuthenticationError as e:
                print(f'Authentication failed: {e}')
                print('Please try again.')
                self.apikey_secret()

    def apikey_secret(self):
        print('Please enter your binace account data below')
        ak = input('ApiKey: ')
        se = input('Secret: ')
        self.api_key = ak
        self.secret = se

    def dollar_btc(self, c, q):
        return round(q / self.exc.fetch_ticker(c + '/USDT')['last'], 3)

    def buy(self, c, q):
        try:
            balance = self.exc.fetch_balance()
            ticker = self.exc.fetch_ticker(c + '/USDT')
            last_price = ticker['last']
            
            print(f'Current balance: {balance}')
            print(f'Current price of {c}: {last_price}')
            
            self.exc.fapiPrivate_post_order({
                'symbol': c,
                'side': 'buy',
                'type': 'MARKET',
                'quantity': q,
                'workingType': 'CONTRACT_PRICE'
            })

            print(f'Buy order executed for {q} {c}')

        except ccxt.InsufficientFunds as e:
            print(f'Insufficient funds to execute buy order: {e}')

        except Exception as e:
            print(f'Error while executing buy order: {e}')

    def sell(self, c, q):
        try:
            balance = self.exc.fetch_balance()
            ticker = self.exc.fetch_ticker(c + '/USDT')
            last_price = ticker['last']
            
            print(f'Current balance: {balance}')
            print(f'Current price of {c}: {last_price}')
            
            self.exc.fapiPrivate_post_order({
                'symbol': c,
                'side': 'sell',
                'type': 'MARKET',
                'quantity': q,
                'workingType': 'CONTRACT_PRICE'
            })

            print(f'Sell order executed for {q} {c}')

        except ccxt.InsufficientFunds as e:
            print(f'Insufficient funds to execute sell order: {e}')

        except Exception as e:
            print(f'Error while executing sell order: {e}')

    def show_chart(self, symbol, timeframe='1d', limit=100):
        try:
            ohlcv = self.exc.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
            df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])

            df['sma_short'] = df['close'].rolling(window=10).mean()
            df['sma_long'] = df['close'].rolling(window=50).mean()

            plt.plot(df['timestamp'], df['close'], label='Close')
            plt.plot(df['timestamp'], df['sma_short'], label='SMA Short')
            plt.plot(df['timestamp'], df['sma_long'], label='SMA Long')
            plt.legend()
            plt.show()

        except Exception as e:
            print(f'Error while showing chart: {e}')

    def add_strategy(self, name, function):
        strategy_id = str(len(self.strategies) + 1)
        self.strategies[strategy_id] = {
            'name': name,
            'function': function
        }

    def auto_trade(self, symbol, strategy_id, timeframe='1d', limit=100):
        self.auto_trading = True
        while self.auto_trading:
            strategy_function = self.strategies[str(strategy_id)]['function']
            strategy_function(symbol, timeframe, limit)
            time.sleep(60)

    def stop_auto_trade(self):
        self.auto_trading = False

    def show_status(self):
        if self.auto_trading:
            print('The bot is currently auto trading.')
        else:
            print('The bot is currently not auto trading.')

    def menu(self):
        symbol = input('Enter the symbol of the cryptocurrency you want to see the chart of: ')
        self.show_chart(symbol)

        while True:
            print('Choose an action:')
            print('1. Auto trading    3. Stop auto trading')
            print('2. Show status     4. Exit')
            choice = input('Enter the number of your choice: ')

            if choice == '1':
                while True:
                    if not self.strategies:
                        print('No trading strategies available.')
                        break
                    print('Choose a trading strategy:')
                    for strategy_id, strategy in self.strategies.items():
                        print(f'{strategy_id}. {strategy["name"]}')
                    strategy_choice = input('Enter the number of your choice: ')
                    
                    if strategy_choice in self.strategies:
                        symbol = input('Enter the symbol of the cryptocurrency you want to apply the chosen trading strategy to: ')
                        self.auto_trade(symbol, strategy_choice)
                        break
                    else:
                        print('Invalid choice, please try again.')
            elif choice == '2':
                self.show_status()
            elif choice == '3':
                self.stop_auto_trade()
            elif choice == '4':
                break
            else:
                print('Invalid choice, please try again.')

from EMA_Trading import ema_trading

trader = BinanceTrader()
trader.add_strategy('EMA trading', ema_trading)
trader.menu()
