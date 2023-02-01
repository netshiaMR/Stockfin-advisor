import requests
import pandas as pd
from sklearn.linear_model import LinearRegression

def get_stock_data(symbol, api_key):
    """
    Get stock data from financial API for a given symbol.
    """
    url = f"https://api.iextrading.com/1.0/stock/{symbol}/chart/5y"
    response = requests.get(url, params={"token": api_key})
    return response.json()

def preprocess_data(data):
    """
    Pre-process the stock data.
    """
    df = pd.DataFrame(data)
    df['returns'] = df['close'].pct_change()
    df.dropna(inplace=True)
    return df

def build_model(df):
    """
    Build a linear regression model using returns as the target variable.
    """
    X = df.drop('returns', axis=1)
    y = df['returns']
    model = LinearRegression().fit(X, y)
    return model

def recommend_portfolio(model, risk_tolerance, investment_goal, api_key):
    """
    Recommend a portfolio of stocks based on the user's risk tolerance and investment goal.
    """
    south_african_stocks = ['NPN', 'SHP', 'WHL', 'SOL', 'BGA']
    portfolio = []
    for stock in south_african_stocks:
        data = get_stock_data(stock, api_key)
        df = preprocess_data(data)
        if model.predict(df.iloc[-1].values.reshape(1, -1)) >= risk_tolerance:
            portfolio.append(stock)
    if len(portfolio) == 0:
        return "No stocks found that match your risk tolerance and investment goal."
    else:
        return portfolio

def financial_advisor(risk_tolerance, investment_goal, api_key):
    """
    Main function that implements the financial advisor.
    """
    south_african_stocks = ['NPN', 'SHP', 'WHL', 'SOL', 'BGA']
    stock_data = []
    for stock in south_african_stocks:
        data = get_stock_data(stock, api_key)
        stock_data.extend(data)
    df = preprocess_data(stock_data)
    model = build_model(df)
    portfolio = recommend_portfolio(model, risk_tolerance, investment_goal, api_key)
    return portfolio
