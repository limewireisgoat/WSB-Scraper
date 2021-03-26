import yfinance as yf
import numpy as np
import datetime

def get_change(symbol, startDate):
    delta = datetime.timedelta(days=7)    
    endDate = startDate + delta
    start = str(startDate)[:10]
    end = str(endDate)[:10]
    stock_history = yf.Ticker(symbol).history(start=start, end=end)
    stock_history = stock_history['Close'].to_numpy()
    percent_change = (stock_history[-1] - stock_history[0])/stock_history[0]
    return percent_change * 100
