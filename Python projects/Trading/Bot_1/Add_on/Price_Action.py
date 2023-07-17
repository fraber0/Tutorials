def price_action(trader, symbol, timeframe='1d', limit=100):
    ohlcv = trader.exc.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    
    max_idx = argrelextrema(df['high'].values, np.greater, order=5)
    min_idx = argrelextrema(df['low'].values, np.less, order=5)
    
    support_levels = df['low'].iloc[min_idx]
    resistance_levels = df['high'].iloc[max_idx]
    
    current_price = df['close'].iloc[-1]
    if current_price < support_levels.iloc[-1]:
        print(f'Price is below the most recent support level, opening long position')
        position_size = 0.5
        trader.buy(symbol, position_size)
    elif current_price > resistance_levels.iloc[-1]:
        print(f'Price is above the most recent resistance level, opening short position')
        position_size = 0.5
        trader.sell(symbol, position_size)

    except Exception as e:
        print(f'Error while executing price action trading strategy: {e}')