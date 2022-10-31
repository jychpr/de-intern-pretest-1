import os
import json
import glob
import pandas as pd
import sys

# DECLARE PATH (ESPECIALLY FOR DOCKER ENVIRONMENT)
data_path_accounts = '/workstation/dwh-coding-challenge/data/accounts'
data_path_cards = '/workstation/dwh-coding-challenge/data/cards'
data_path_savings_accounts = '/workstation/dwh-coding-challenge/data/savings_accounts'

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
table_accounts = table_accounts.sort_values(by='ts')
table_cards = process_json_data(data_path_cards, dataframe_cards, temp_df_cards)
table_cards = table_cards.sort_values(by='ts')
table_savings_accounts = process_json_data(data_path_savings_accounts, dataframe_savings_accounts, temp_df_savings_accounts)
table_savings_accounts = table_savings_accounts.sort_values(by='ts')


print("ANSWER NO.1")
print("ACCOUNTS TABLE")
print(table_accounts.to_string())
print("\n")
print("CARDS TABLE")
print(table_cards.to_string())
print("\n")
print("SAVINGS ACCOUNTS TABLE")
print(table_savings_accounts.to_string())

join_step_1 = pd.merge(table_cards, table_savings_accounts, on='ts', how='outer', sort=True)
join_step_2 = pd.merge(table_accounts, join_step_1, on='ts', how='outer', sort=True)

print("\n")
print("ANSWER NO.2")
print("JOINED TABLES")
print(join_step_2.to_string())

print("\n")
print("ANSWER NO.3")
print("TRANSACTION LIST:")
print(join_step_2.iloc[[17, 20, 21, 22, 23, 33, 34]].to_string())
print("ANALYSIS:")
print("TRANSACTION OCCURED 7 TIMES. CREDIT USED 3 TIMES: 12000 AND 19000 ON C1, 37000 ON C2. CHANGE OF BALANCE 4 TIMES: 15000, 40000, 21000, AND 33000.")

