def pivot_point(trader, symbol, timeframe='1d', limit=100):
    ohlcv = trader.exc.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    
    pivot = (df['high'] + df['low'] + df['close']) / 3
    r1 = 2 * pivot - df['low']
    s1 = 2 * pivot - df['high']
    r2 = pivot + (df['high'] - df['low'])
    s2 = pivot - (df['high'] - df['low'])
    
    current_price = df['close'].iloc[-1]
    if current_price < s1.iloc[-1]:
        print(f'Price is below the first support level, opening long position')
        position_size = 0.5
        trader.buy(symbol, position_size)
    elif current_price > r1.iloc[-1]:
        print(f'Price is above the first resistance level, opening short position')
        position_size = 0.5
        trader.sell(symbol, position_size)