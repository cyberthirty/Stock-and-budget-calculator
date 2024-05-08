import streamlit as st
import pandas as pd
import yfinance as yf

def load_stock_data(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1mo")
    return hist

def display_stock_data():
    st.subheader('Stock Data')
    ticker = st.text_input('Enter Stock Ticker', 'AAPL').upper()
    if st.button('Display Data'):
        data = load_stock_data(ticker)
        st.write(data)

def budget_calculator():
    st.subheader('Budget Calculator')
    income = st.number_input('Enter your monthly income', min_value=0.0, format='%.2f')
    expenses = st.number_input('Enter your monthly expenses', min_value=0.0, format='%.2f')
    balance = income - expenses
    st.write(f"Monthly Balance: ${balance:.2f}")

st.sidebar.title('Menu')
options = st.sidebar.radio('Select a tool:', ['Stock Data', 'Budget Calculator'])

if options == 'Stock Data':
    display_stock_data()
elif options == 'Budget Calculator':
    budget_calculator()
