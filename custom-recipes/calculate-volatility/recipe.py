# import the classes for accessing DSS objects from the recipe
import dataiku
from dataiku.customrecipe import *
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
from finance.data_management import get_input_data_and_set_date_index
from finance.calculations import calc_volatility
# get variables 
input_dataset = get_input_names_for_role('input')
observation_days = int(get_recipe_config()['ObservationDays'])
rolling_period = int(get_recipe_config()['RollingPeriod'])
output_dataset_str = get_output_names_for_role('output')

# get dataset
prices_df = get_input_data_and_set_date_index(input_dataset[0])

# calculate volatility
volatlity = calc_volatility(prices_df, rolling_period, observation_days)


# save dataframe to dk object
ouput_dataset = dataiku.Dataset(output_dataset_str[0])
ouput_dataset.write_with_schema(volatlity.reset_index())
