import requests
import pandas as pd

def get_data(from_symbol, to_symbol, API_KEY):
    r = requests.get('https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=' + from_symbol + '&to_symbol=' + to_symbol + '&apikey=' + API_KEY)

    dataIntraday = r.json()

    return dataIntraday['Time series FX (Daily)']