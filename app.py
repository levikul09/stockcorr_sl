import streamlit as st
from datetime import datetime,timedelta, date
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import yfinance as yf
import seaborn as sns
import pytz

yf.pdr_override()
#tz = pytz.timezone("America/New_York")

end = datetime.now()
start = end - timedelta(days=4000) #We always have more than 10 years of data from today

#end = tz.localize(datetime.now())
#start = tz.localize(end - timedelta(days=3000))

input= st.text_input(label='''List stock tickers. \n 
Seperate them by commas WITHOUT spaces, e.g. MSFT, AAPL, GOOG, META, ADBE, IBM''')
button = st.button("OK")

input=input.split(",")

if button:
    stocks = []
    for i in input:
        stocks.append(i)

    df = pdr.get_data_yahoo(stocks, start, end)
    df

    corr_data = df['Adj Close'].pct_change().corr()


    fig, ax= plt.subplots()

    sns.heatmap(corr_data, vmin=-1, vmax=1, annot=True, cmap=sns.diverging_palette(20,220, as_cmap=True), ax=ax)
    st.pyplot(fig)





