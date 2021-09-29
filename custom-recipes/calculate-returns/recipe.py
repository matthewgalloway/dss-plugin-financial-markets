# import the classes for accessing DSS objects from the recipe
import dataiku
from dataiku.customrecipe import *
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
from finance.data_management import get_input_data_and_set_date_index
from finance.calculations import calc_returns
from dataiku.customrecipe import *

# gets config variables
recipe_config = get_recipe_config()
input_ds_str = get_input_names_for_role('input_dataset')
input_ds = get_input_data_and_set_date_index(input_ds_str[0])
return_type = get_recipe_config()['return_type']
date_column_name = recipe_config.get("date_col")
price_column_name = recipe_config.get("price_col")
all_columns = get_recipe_config()['all_columns']
print(f'All columns var is {all_columns}')
if all_columns:
     output_df = calc_returns(input_ds[price_column_name], return_type=return_type)
else:
    # calculates returns
    returns = calc_returns(input_ds[price_column_name], return_type=return_type)

    # concats with orginal df
    output_df = pd.concat([input_ds, returns], axis=1, join='inner')




# Write recipe outputs
output_ds_str = get_output_names_for_role('output_dataset')
output_ds = dataiku.Dataset(output_ds_str[0])
output_ds.write_with_schema(output_df.reset_index())
