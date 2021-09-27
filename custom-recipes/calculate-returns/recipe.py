# import the classes for accessing DSS objects from the recipe
import dataiku
from dataiku.customrecipe import *
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
from finance.data_management import get_input_data_and_set_date_index
from finance.calculations import calc_returns
from dataiku.customrecipe import *

recipe_config = get_recipe_config()

input_ds_str = get_input_names_for_role('input_dataset')
input_ds = get_input_data_and_set_date_index(input_ds_str[0])

return_type = get_recipe_config()['return_type']

date_column_name = recipe_config.get("date_col")
price_column_name = recipe_config.get("price_col")

price_ds = input_ds[[date_column_name, price_column_name]]

returns = calc_returns(price_ds, return_type=return_type)


output_df = pd.concat([price_ds, returns], axis=1, join='inner', keys=date_column_name)

# Write recipe outputs


# For outputs, the process is the same:
output_ds_str = get_output_names_for_role('output_dataset')
output_ds = dataiku.Dataset(output_ds_str[0])
output_ds.write_with_schema(output_df.reset_index())
