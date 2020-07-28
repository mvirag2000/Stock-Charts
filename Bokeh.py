import pandas as pd
from pandas_datareader import data
from bokeh.io import show 
from bokeh.plotting import figure
import datetime
import util as u 

stock = 'AAPL'
start = datetime.datetime(2017,6,1)
end = datetime.datetime(2018,1,14)
g = data.DataReader([stock], 'google', start, end)
stocks = g['Close']
stocks['Date'] = pd.to_datetime(stocks.index)
stocks.insert(0, 'ID', range(0, stocks.shape[0]))
stocks['Open'] = g['Open']
stocks['High'] = g['High']
stocks['Low'] = g['Low'] 
stocks['Close'] = stocks[stock]

u.frame_stats(stocks)

stocks['Up'] = stocks['ID'][stocks['Close'] > stocks['Open']]
stocks['Down'] = stocks['ID'][stocks['Open'] > stocks['Close']] 

p = figure(plot_width=1000, title="Candlestick with Custom X-Axis")
p.xaxis.major_label_overrides = {
    i: date.strftime('%b %d') for i, date in enumerate(pd.to_datetime(stocks['Date']))
}

p.x_range.range_padding = 0.05

p.segment(stocks['ID'], stocks['High'], stocks['ID'], stocks['Low'], color="black")
p.vbar(stocks['Up'], 0.5, stocks['Open'], stocks['Close'], fill_color="#D5E1DD", line_color="black")
p.vbar(stocks['Down'], 0.5, stocks['Open'], stocks['Close'], fill_color="#F2583E", line_color="black")

show(p)