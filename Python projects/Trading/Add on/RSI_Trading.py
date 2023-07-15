def rsi_trading(trader, symbol, timeframe='1d', limit=100):
    ohlcv = trader.exc.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    
    delta = df['close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    
    if rsi.iloc[-1] < 30:
        print(f'RSI is below 30, opening long position')
        position_size = 0.5
        trader.buy(symbol, position_size)
    elif rsi.iloc[-1] > 70:
        print(f'RSI is above 70, opening short position')
        position_size = 0.5
        trader.sell(symbol, position_size)