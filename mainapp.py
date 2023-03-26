
import os
import yfinance as yf
import pandas as pd
import streamlit as st
from datetime import datetime , date,timedelta
import cufflinks as cf
import matplotlib.pyplot as plt
import plotly
import plotly.graph_objects as go
# from deta import Deta
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report 
# from dotenv import load_dotenv
# import streamlit_authenticator as sa
# from pathlib import Path
from prophet import Prophet
# import streamlit as st
# from deta import Deta
# import database as db
# import yaml 
# from yaml.loader import SafeLoader
# import streamlit.components.v1 as components



# import yfinance as yf
# stock_info = yf.Ticker('TSLA').info
# # stock_info.keys() for other properties you can explore
# market_price = stock_info['regularMarketPrice']
# previous_close_price = stock_info['regularMarketPreviousClose']
# print('market price ', market_price)
# print('previous close price ', previous_close_price)












st.set_page_config(page_title="Stock Price Analysis" , page_icon=":bar_chart:", layout="wide")
# 
# 
# streamlit_app.py
# user authentication 


# # Creating an update user details widget
# if st.sidebar.button ('Sign Up'):
#     if authentication_status:
#         try:
#             if authenticator.update_user_details(username, 'Update user details'):
#                 st.success('Entries updated successfully')
#         except Exception as e:
#             st.error(e)





def data(symbol,period,timeframe,st_date, ed_date):
    tickerData = yf.Ticker(symbol)
    tickerDf= tickerData.history(period=period,interval=timeframe,start=st_date,end=ed_date)
    return tickerDf







# if authenticator == False:
#    st.error("Username/password is incorrect")
# 
# if authenticator == None:
#    st.warning("Please enter your username and password ")
# 
# if authenticator == True  :
# 

# if authentication_status == None :
    

#     st.warning('Please enter your username and password')

# elif authentication_status == False:
#     st.error('Username/password is incorrect')

# if authentication_status == None or authentication_status==False :
#     front = 'Log In'

# else :
#     front = 'Log out'

#     if st.sidebar.button(front):
#         authenticator.logout('Logout', 'main')



st.markdown(
    """
        # Stock Price App\n
        Shown are the stock price data for the query companys!
    """
)
st.write('---')
# sidebar
#authenticator.logout("Logout","sidebar")
# from datetime import date
# today = date.today().strftime("%Y")
# today1 = date.today().strftime("%m")
# today2 = date.today().strftime("%d")
# main_today = int(today+today1+today2)
# st.write(today)
with st.sidebar:
    st.sidebar.markdown(' # Stock Price Analysis ')
    st.sidebar.title(f"Welcome ")
    # get current datetime
    dt = datetime.now()
        
    DAY = dt.strftime('%A')
   
    if DAY == 'Saturday' or DAY == 'Sunday':
        Start_date =  date.today() - timedelta(days=3)
        end_date = date.today() - timedelta(days=2)
    else:
        Start_date = date.today()
        end_date = date.today() + timedelta(days=1)

    start_date = st.sidebar.date_input("start date", Start_date)
    End_date = st.sidebar.date_input("End date",end_date) 
    # Retrieving tickers data
    ticker_list = ('TATASTEEL.NS', 'TCS.NS', 'HDFCLIFE.NS', 'WIPRO.NS', 'EICHERMOT.NS', 'INFY.NS', 'MARUTI.NS', 'TECHM.NS', 'BRITANNIA.NS', 'HCLTECH.NS', 'MM.NS', 'BAJAJ-AUTO.NS', 'SBIN.NS', 'HINDUNILVR.NS', 'DRREDDY.NS', 'ICICIBANK.NS', 'INDUSINDBK.NS', 'JSWSTEEL.NS', 'TATASTEEL.NS', 'NTPC.NS', 'POWERGRID.NS', 'COALINDIA.NS', 'BHARTIARTL.NS', 'SBILIFE.NS',
                'ONGC.NS', 'BAJFINANCE.NS', 'ULTRACEMCO.NS', 'SUNPHARMA.NS', 'ADANIENT.NS', 'LT.NS', 'BAJAJFINSV.NS', 'UPL.NS', 'ADANIPORTS.NS', 'CIPLA.NS', 'HINDALCO.NS', 'BPCL.NS', 'NESTLEIND.NS', 'KOTAKBANK.NS', 'HDFCBANK.NS', 'RELIANCE.NS', 'APOLLOHOSP.NS', 'HDFC.NS', 'DIVISLAB.NS', 'GRASIM.NS', 'TITAN.NS', 'ITC.NS', 'ASIANPAINT.NS', 'HEROMOTOCO.NS')
    # Select ticker symbol
    tickerSymbol = st.sidebar.selectbox('Stock ticker', ticker_list) 
    # Get ticker data
#     tickerData = yf.Ticker(tickerSymbol) 
    #pandas profiling 
    navigation = st.radio('Navigation',['Home','Stock Report','Range Of the day','Community']) 
# ---------------------------------------------------------HOME MENU :---------------------------------------------------
if navigation == 'Home' :



    # get the historical prices for this ticke
#     st.write(tickerData)
#     tickerDf = tickerData.history(period='1d', start=start_date, end=End_date)
    tickerDf = data(tickerSymbol,'1d','5m',start_date,End_date)
    st.write(tickerDf)
#     tickerDf.reset_index(inplace=True)
#     #coverting time zone to date :
#     tickerDf['Year'] = tickerDf['Date'].apply(lambda x:str(x)[-4:])
#     tickerDf['Month'] = tickerDf['Date'].apply(lambda x:str(x)[-6:-4:])
#     tickerDf['Day'] = tickerDf['Date'].apply(lambda x:str(x)[-6:])
#     tickerDf['date'] = pd.DataFrame(tickerDf['Year'] +'-' +tickerDf['Month'] +'-' + tickerDf['Day'])
#     # Ticker information
    # string_logo = components.html("""'<img src=%s>' % tickerData.info['logo_url']""")
    # st.markdown(string_logo, unsafe_allow_html=True)
    # # for getting companys full name
    # string_name = tickerData.info['longName']
    # st.header('**%s**' % string_name)
    # for getting information of company
    # string_summary = tickerData.info['longBusinessSummary']
    # st.info(string_summary)
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
    # Predict forecast with Prophet.
# 
    # df_train = tickerDf[['date','Close']]
    # df_train = df_train.rename(columns={"date": "ds", "Close": "y"})
# 
    # m = Prophet()
    # m.fit(df_train)
    # future = m.make_future_dataframe(periods=(start_date - End_date))
    # forecast = m.predict(future)
# 
    # Show and plot forecast
    # st.subheader('Forecast data')
    # st.write(forecast.tail())
    # n_years = st.slider('Years of prediction:', 1, 4)
# period = n_years * 365
# st.write(f'Forecast plot for {n_years} years')
# fig1  = m.plot(forecast)
# st.plotly_chart(fig1)
#
# st.write("Forecast components")
# fig2 = m.plot_components(forecast)
# st.write(fig2)
#describe the bollinger band on the graph
  
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
