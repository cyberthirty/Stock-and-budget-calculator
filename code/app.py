import streamlit as st
import pandas as pd
import yfinance as yf

st.set_page_config(page_title="Stock and Budget Calculator", page_icon="📈", layout="wide")

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

def math_calculator():
    st.subheader('Math Calculator')
    num1 = st.number_input('Enter number', key="num1")
    num2 = st.number_input('Enter number', key="num2")
    operation = st.selectbox('Choose operation', ['Add', 'Subtract', 'Multiply', 'Divide'])

    if st.button('Calculate'):
        if operation == 'Add':
            result = num1 + num2
        elif operation == 'Subtract':
            result = num1 - num2
        elif operation == 'Multiply':
            result = num1 * num2
        elif operation == 'Divide':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error! Division by zero."
        st.success(f"Result: {result}")
        
st.sidebar.title('Menu')
options = st.sidebar.radio('Select a tool:', ['Stock Data', 'Budget Calculator', 'Math Calculator'])

if options == 'Stock Data':
    display_stock_data()
    
elif options == 'Budget Calculator':
    budget_calculator()
    
elif options == 'Math Calculator':
    math_calculator()
