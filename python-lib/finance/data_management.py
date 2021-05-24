import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

def get_input_data_and_set_date_index(var, set_date=True):
    # converts a dataiku dataset object to dataframe 
    # and sets the date as the index
    
    dk_obj = dataiku.Dataset(var)
    df = dk_obj.get_dataframe()
    if set_date:
        df.set_index('date',inplace=True)
    return df