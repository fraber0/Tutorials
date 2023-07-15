def bollinger_bands(trader, symbol, timeframe='1d', limit=100):
    ohlcv = trader.exc.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    
    sma = df['close'].rolling(window=20).mean()
    std = df['close'].rolling(window=20).std()
    upper_band = sma + 2 * std
    lower_band = sma - 2 * std
    
    if df['close'].iloc[-1] > upper_band.iloc[-1]:
        print(f'Price is above the upper Bollinger Band, opening short position')
        position_size = 0.5
        trader.sell(symbol, position_size)
    elif df['close'].iloc[-1] < lower_band.iloc[-1]:
        print(f'Price is below the lower Bollinger Band, opening long position')
        position_size = 0.5
        trader.buy(symbol, position_size)