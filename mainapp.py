import yfinance as yf
import pandas as pd
import streamlit as st
import datetime as dt
import cufflinks as cf
import matplotlib.pyplot as plt
import plotly
import plotly.graph_objects as go
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report 
from prophet import Prophet


st.set_page_config(page_title="Stock Price Analysis" , page_icon=":bar_chart:", layout="wide")



st.markdown(
    """
        # Stock Price App\n
        Shown are the stock price data for the query companys!
    """
)
st.write('---')
# sidebar


with st.sidebar:
    st.sidebar.markdown(' # Stock Price Analysis ')
    st.sidebar.title(f"Welcome ")
    start_date = st.sidebar.date_input("start date", dt.date(2021, 1, 1))
    End_date = st.sidebar.date_input("End date",dt.date(2022,1,1)) 
    # Retrieving tickers data
    ticker_list = ('TATASTEEL.NS', 'TCS.NS', 'HDFCLIFE.NS', 'WIPRO.NS', 'EICHERMOT.NS', 'INFY.NS', 'MARUTI.NS', 'TECHM.NS', 'BRITANNIA.NS', 'HCLTECH.NS', 'MM.NS', 'BAJAJ-AUTO.NS', 'SBIN.NS', 'HINDUNILVR.NS', 'DRREDDY.NS', 'ICICIBANK.NS', 'INDUSINDBK.NS', 'JSWSTEEL.NS', 'TATASTEEL.NS', 'NTPC.NS', 'POWERGRID.NS', 'COALINDIA.NS', 'BHARTIARTL.NS', 'SBILIFE.NS',
                'ONGC.NS', 'BAJFINANCE.NS', 'ULTRACEMCO.NS', 'SUNPHARMA.NS', 'ADANIENT.NS', 'LT.NS', 'BAJAJFINSV.NS', 'UPL.NS', 'ADANIPORTS.NS', 'CIPLA.NS', 'HINDALCO.NS', 'BPCL.NS', 'NESTLEIND.NS', 'KOTAKBANK.NS', 'HDFCBANK.NS', 'RELIANCE.NS', 'APOLLOHOSP.NS', 'HDFC.NS', 'DIVISLAB.NS', 'GRASIM.NS', 'TITAN.NS', 'ITC.NS', 'ASIANPAINT.NS', 'HEROMOTOCO.NS')
    # Select ticker symbol
    tickerSymbol = st.sidebar.selectbox(
        'Stock ticker', ticker_list) 
    # Get ticker data
    tickerData = yf.Ticker(tickerSymbol) 
    #pandas profiling 
    navigation = st.radio('Navigation',['Home','Stock Report','Range Of the day','Community']) 
# ---------------------------------------------------------HOME MENU :---------------------------------------------------
if navigation == 'Home' :



    # get the historical prices for this ticke
    tickerDf = tickerData.history(period='1d', start=start_date, end=End_date)
    tickerDf.reset_index(inplace=True)
    #coverting time zone to date :
    tickerDf['Year'] = tickerDf['Date'].apply(lambda x:str(x)[-4:])
    tickerDf['Month'] = tickerDf['Date'].apply(lambda x:str(x)[-6:-4:])
    tickerDf['Day'] = tickerDf['Date'].apply(lambda x:str(x)[-6:])
    tickerDf['date'] = pd.DataFrame(tickerDf['Year'] +'-' +tickerDf['Month'] +'-' + tickerDf['Day'])
   
#     string_summary = tickerData.info['longBusinessSummary']
#     st.info(string_summary)
    # Ticker data
    st.header('**Stock data**')
    st.table(tickerDf)
    # 
    # dividends
    # dividends = tickerDf.Dividends
    dividend,download = st.columns(2)
    with dividend :
      if st.button('BOLLINGER BAND'):
        # Bollinger bands
        st.header('**Bollinger Bands**')
        qf = cf.QuantFig(tickerDf, title='First Quant Figure',
                        legend='top', name='GS')
        qf.add_bollinger_bands()
        fig = qf.iplot(asFigure=True)
        st.plotly_chart(fig)
    with download:
        # download csv
        @st.cache
        def convert_df(df):
            return df.to_csv().encode('utf-8')
        csv = convert_df(tickerDf)
        download = st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='stock.csv',
            mime='text/csv',
        )
    #plot the graph
    def plot_raw_data():
        fig = go.Figure()
        fig.add_trace(go.Scatter( x=tickerDf['Date'], y=tickerDf['Open'], name="stock_open"))
        fig.add_trace(go.Scatter(
            x=tickerDf['Date'], y=tickerDf['Close'], name="stock_close"))
        fig.layout.update(
            title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
        st.plotly_chart(fig , use_container_width=True)
    plot_raw_data()

# -------------------------------------------------------------PROFILING THE STOCK DATA : -------------------------------------------------------------------
if  navigation == 'Stock Report' :
    company_name = tickerData.info['longName']
    st.title(f'{company_name}')
    # Get ticker data
    tickerData = yf.Ticker(tickerSymbol) 
    # get the historical prices for this ticke
    tickerDf = tickerData.history(period='1d', start=start_date, end=End_date)
    tickerDf.reset_index(inplace=True)
    profiling = tickerDf.profile_report()
    st_profile_report(profiling)
#-------------------------------------------------------Range of the day ----------------------------------------------------------------------
if navigation == 'Range Of the day':
    st.write("Coming soon !")
#------------------------------------------------------Community-------------------------------------------------------------------------------
if navigation == 'Community':
    st.write("Coming soon!")
