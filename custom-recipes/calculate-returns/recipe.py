# import the classes for accessing DSS objects from the recipe
import dataiku
from dataiku.customrecipe import *
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
from finance.data_management import get_input_data_and_set_date_index
from finance.calculations import calc_returns

input_ds_str = get_input_names_for_role('input_ds')
input_ds = get_input_data_and_set_date_index(input_ds_str[0])

return_type = get_recipe_config()['return_type']


returns = calc_returns(input_ds, return_type=return_type)

# Write recipe outputs


# For outputs, the process is the same:
output_ds_str = get_output_names_for_role('output_ds')
output_ds = dataiku.Dataset(output_ds_str[0])
output_ds.write_with_schema(returns.reset_index())
