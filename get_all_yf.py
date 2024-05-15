import yfinance as yf
import os
import pandas as pd
import csv
import requests_cache
from requests import Session
from requests_cache import CacheMixin, SQLiteCache
from requests_ratelimiter import LimiterMixin, MemoryQueueBucket
from pyrate_limiter import Duration, RequestRate, Limiter
from pandas_datareader import data as pdr
import sqlite3

yf.pdr_override() # <== that's all it takes :-)

class CachedLimiterSession(CacheMixin, LimiterMixin, Session):
    pass

session = CachedLimiterSession(
    limiter=Limiter(RequestRate(2, Duration.SECOND*5)),  # max 2 requests per 5 seconds
    bucket_class=MemoryQueueBucket,
    backend=SQLiteCache("yfinance.cache"),
)

try:
    symbol_file = 'symbols_only.txt'
    all_history = []

    with open(symbol_file, 'r') as file:
        for line in file:
            symbol = line.strip()

            if not isinstance(symbol, str):
                continue
            history = yf.download(symbol, period="60d", interval="5m")
            # Add the ticker symbol as a column to the history DataFrame
            history['Ticker'] = symbol

            # Append the history DataFrame to the all_history list
            all_history.append(history)

    # Concatenate all the DataFrames in the list into a single DataFrame
    all_history_df = pd.concat(all_history)

    all_history_df.to_csv('all_history.csv')

except Exception as e:
    print(e)