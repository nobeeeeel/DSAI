# -*- coding: utf-8 -*-
"""stockTraderML.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UW6iDIWZOICyN5HDdc_UMpr5baRsZfvI
"""

#Following are the top 10 NASDAQ stocks which we are using 
#Apple (NASDAQ:AAPL)
#Microsoft (NASDAQ:MSFT)
#Amazon (NASDAQ:AMZN)
#Facebook (NASDAQ:FB)
#Alphabet Class C (NASDAQ:GOOG)
#Alphabet Class A (NASDAQ:GOOGL)
#Tesla (NASDAQ:TSLA)
#NVIDIA (NASDAQ:NVDA)
#PayPal Holdings (NASDAQ:PYPL)
#ASML Holdings (NASDAQ:ASML)

stocksList = ['AAPL', 'MSFT', 'AMZN', 'FB', 'GOOG', 'GOOGL', 'TSLA', 'NVDA', 'PYPL', 'ASML']

import csv

with open(r'input later', 'w') as csvfile:
    # Here, you need to write headers:
    csvfile.write(stocksList)
    for url in urls:
        ISIN = url.split('=')[-1].replace(':', '_')
        ...  # The rest of your code
        df.to_csv(csvfile, index=False, header=False)

import urllib.request
import json

for stock in stocksList:
  url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+stock+"&outputsize=full&apikey=8U32SQR1ECDBFDJ8"  
  request = urllib.request.Request(url)
  request.add_header('api-key', '8U32SQR1ECDBFDJ8')

  response = urllib.request.urlopen(request)
  data = response.read()
  stocksData = json.loads(data.decode('utf-8'))\
  stocksData

"""Indicators We will be using
RSI, MACD, MA

Apple (NASDAQ:AAPL)
Microsoft (NASDAQ:MSFT)
Amazon (NASDAQ:AMZN)
Facebook (NASDAQ:FB)
Alphabet Class C (NASDAQ:GOOG)
Alphabet Class A (NASDAQ:GOOGL)
Tesla (NASDAQ:TSLA)
NVIDIA (NASDAQ:NVDA)
PayPal Holdings (NASDAQ:PYPL)
ASML Holdings (NASDAQ:ASML)
"""

aaplData.keys()

aaplData['Meta Data']

aaplData['Time Series'] = aaplData.pop('Time Series (Daily)')

aaplData['Time Series']

aaplData["Time Series"].keys()
count = 0
for i in aaplData['Time Series'].keys():
  if i == '2010-01-04':
    print(count)
  count += 1



import pandas as pd

aaplDF = pd.DataFrame(aaplData['Time Series']).transpose()

aaplDF

list = []
for i in range(3071,len(aaplDF)):
  list.append(aaplDF.index[i])

for i in list:
  aaplDF = aaplDF.drop(i)

aaplDF