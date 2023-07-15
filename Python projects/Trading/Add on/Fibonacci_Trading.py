def fibonacci_trading(trader, symbol, timeframe='1d', limit=100):
    ohlcv = trader.exc.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    
    high = df['high'].max()
    low = df['low'].min()
    diff = high - low
    levels = [high - diff * factor for factor in [0, 0.236, 0.382, 0.5, 0.618, 0.786, 1]]
    
    current_price = df['close'].iloc[-1]
    if current_price < levels[5]:
        print(f'Price is below the 0.786 Fibonacci level, opening long position')
        position_size = 0.5
        trader.buy(symbol, position_size)
    elif current_price > levels[2]:
        print(f'Price is above the 0.382 Fibonacci level, opening short position')
        position_size = 0.5
        trader.sell(symbol, position_size)