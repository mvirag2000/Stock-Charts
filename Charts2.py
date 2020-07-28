import pandas as pd
from pandas_datareader import data
from bokeh.plotting import figure
from bokeh.io import show, output_file  
from bokeh.layouts import column 
import datetime
import stoli as st
import util as u 
      
stock = 'MSFT'
start = datetime.datetime(2020,1,28)
end = datetime.datetime(2020,7,28)
g = data.DataReader([stock], 'yahoo', start, end)

stocks = g['Close']
stocks['Date'] = pd.to_datetime(stocks.index)
stocks.insert(0, 'ID', range(0, stocks.shape[0]))
stocks['Open'] = g['Open']
stocks['High'] = g['High']
stocks['Low'] = g['Low'] 
stocks['Close'] = stocks[stock]
stocks['Up'] = stocks['ID'][stocks['Close'] > stocks['Open']]
stocks['Down'] = stocks['ID'][stocks['Open'] > stocks['Close']] 
st.Bollinger(stocks, stock)
st.MACD(stocks, stock)

u.frame_stats(stocks)

output_file('chart.htm')
s1 = figure(plot_width=940, plot_height=420, title=stock)
s1.xaxis.major_label_overrides = {
    i: date.strftime('%b %d') for i, date in enumerate(pd.to_datetime(stocks['Date']))
}
s1.line(stocks['ID'], stocks[stock + '_LO'], line_color='gray')
s1.line(stocks['ID'], stocks[stock + '_HI'], line_color='gray')
s1.line(stocks['ID'], stocks[stock + '_MID'], line_color='gray', line_dash='dashed')

s1.segment(stocks['ID'], stocks['High'], stocks['ID'], stocks['Low'], color="black")
s1.vbar(stocks['Up'], 0.5, stocks['Open'], stocks['Close'], fill_color="#D5E1DD", line_color="black")
s1.vbar(stocks['Down'], 0.5, stocks['Open'], stocks['Close'], fill_color="#F2583E", line_color="black")

s2 = figure(plot_width=940, plot_height=150, title='MACD') 
s2.xaxis.major_label_overrides = {
    i: date.strftime('%b %d') for i, date in enumerate(pd.to_datetime(stocks['Date']))
}
s2.line(stocks['ID'], stocks[stock + '_MACD'], line_color='black')
s2.line(stocks['ID'], stocks[stock + '_Signal'], line_color='red')
s2.vbar(stocks['ID'], 0.5, stocks[stock + '_Histo'], line_color='blue')
#s2.line(stocks['ID'], 20, line_color='grey')
#s2.line(stocks['ID'], 80, line_color='grey')
show(column(s1, s2),browser=None) 
