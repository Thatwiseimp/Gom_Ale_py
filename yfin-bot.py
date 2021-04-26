import yfinance as yf
import plotly.graph_objects as go

url='eichermot.ns'


tickerTag = yf.Ticker(url)
print(tickerTag.recommendations)

old  =  tickerTag.history(start="2021-01-01",  end="2021-03-30")
old = old.reset_index()
for i in ['Open', 'High', 'Close', 'Low']: 
      old[i]  =  old[i].astype('float64')

fig = go.Figure(data=[go.Candlestick(x=old['Date'],open=old['Open'],high=old['High'],low=old['Low'],close=old['Close'])])
fig.show()

# fig = go.Figure(data=go.Ohlc(x=old['Date'],open=old['Open'],high=old['High'],low=old['Low'],close=old['Close']))
# fig.show()