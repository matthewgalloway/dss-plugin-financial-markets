import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu


def calc_volatility(df, rolling_period, observation_days):
    # takes in a dataframe with date index
    # returns volatility as a dataframe with a date index
    log_returns = np.log(df/df.shift(1)) 
    volatlity = df.rolling(window=rolling_period).std()*np.sqrt(observation_days)
    
    return volatlity

def calc_returns(prices, return_type='CumulativeReturns'):
    # put the dataframe in date order    
    prices = prices.sort_index()
    #calculate the returns
    price_shifted = prices.shift(1)
    returns = prices-price_shifted

    if return_type=='PercentageReturns':
        returns = returns/price_shifted
        
    elif return_type=='CumulativeReturns':
        returns = returns/price_shifted
        returns = 1+(returns.cumsum())
        returns = pd.DataFrame(returns)
    
    returns.columns = return_type   
    return returns