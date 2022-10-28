import os
import json
import glob
import pandas as pd
from functools import reduce

# DECLARE PATH
data_path_accounts = '../data/accounts/'
data_path_cards = '../data/cards/'
data_path_savings_accounts = '../data/savings_accounts/'

# DECLARE VARIABLES
dataframe_accounts = []
dataframe_cards = []
dataframe_savings_accounts = []
temp_df_accounts = []
temp_df_cards = []
temp_df_savings_accounts = []

def process_json_data(filepath, dataframe, temp_df):
    json_data = os.path.join(filepath, '*.json')
    file_list = glob.glob(json_data)

    # CREATE TABLE ACCOUNTS
    for file in file_list:
        data = pd.read_json(file)
        temp_df.append(data)
    dataframe = pd.concat(temp_df, ignore_index=False)

    return dataframe

table_accounts = process_json_data(data_path_accounts, dataframe_accounts, temp_df_accounts)
table_cards = process_json_data(data_path_cards, dataframe_cards, temp_df_cards)
table_savings_accounts = process_json_data(data_path_savings_accounts, dataframe_savings_accounts, temp_df_savings_accounts)

join_step_1 = pd.merge(table_cards, table_savings_accounts, on='ts', how='outer')
join_step_2 = pd.merge(table_accounts, join_step_1, on='ts', how='outer')


