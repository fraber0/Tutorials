def ema_trading(trader, symbol, timeframe='1d', limit=100):
    try:
        ohlcv = trader.exc.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
        df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])

        df['ema_short'] = df['close'].ewm(span=10).mean()
        df['ema_long'] = df['close'].ewm(span=50).mean()

        if df['ema_short'].iloc[-1] < df['ema_long'].iloc[-1]:
            print(f'Short EMA is below long EMA, opening long position')
            position_size = 0.5
            trader.buy(symbol, position_size)

        elif df['ema_short'].iloc[-1] > df['ema_long'].iloc[-1]:
            print(f'Short EMA is above long EMA, opening short position')
            position_size = 0.5
            trader.sell(symbol, position_size)

    except Exception as e:
        print(f'Error while executing EMA trading strategy: {e}')
