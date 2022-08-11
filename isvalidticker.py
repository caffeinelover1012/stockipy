import yfinance as yf

def isvalid(t):
    ticker = yf.Ticker(t)
    info = ticker.info
    if not info or not info.get('longBusinessSummary'):
        return False
    else:
        return info.get('shortName')