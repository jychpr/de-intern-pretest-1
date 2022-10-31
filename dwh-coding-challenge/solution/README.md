# Solution
## Solution Summary
### Requirements
- pandas

### complete_answer.py Script Output:
1. Three tables. Displaying Accounts table, Cards table, and Savings Account table
2. Joined table from the three tables
3. List of transactions from joined tables. Also, a quick analysis/summary

### About the complete_answer.py solution script:

First, import the requirements or libraries needed and declare the json data path for each folder because tables will be made according to the json data.
Then, create a function to process json data that need 3 input: filepath, dataframe variable, and temporary dataframe variable. Dataframe variable created for each tables that will be made, so it doesn't mix up. Temporary dataframe variable also the same, created for each tables so it will not mix up, but I think it could use one temporary dataframe instead of three.

The next step is to process the json data to create three tables and print those tables.

Task 2, joining three tables. Decided to join table 2 and 3, cards and savings account, in the first step of joining. Table cards as the left part and savings account as the right. Then in the second step, table 1 accounts as the left part and the result of step one as the right part.

For task 2, the join key is the 'ts' or timestamp. The json data itself displaying chronological log of operation. Because it's chronological, then the data also sorted according to the timestamp.

Task 3, the transaction occurred 7 times. There are 3 transaction due to credit used, valued 12000 and 19000 for c1 and valued 37000 for c2. And 4 transaction due to change of balance in savings account, valuing 15000, 40000, 21000, and 33000 for each change/update. Those 7 transaction noticed by 'u' or update operation 'op' from the data chronological log in joined table from task 2.

To display the transaction list, iloc used to display the data index where transaction occured.

## How to run
#### 1. Get the files (choose one)
  - Create a folder on local/host computer then clone (and pull) the repo
  - Download the code straight from browser and unzip the repo folder
#### 2. Open the terminal/command prompt/powershell/etc. and make sure select the directory where Dockerfile and docker-compose.yaml is located
#### 3. Create docker image with this command
```bash
docker-compose build
```
#### 4. Create the container (for the first time) and to (automatically) run the solution script with this command. If wanted to run again, just use this command again. No duplicate container will be made.
```bash
docker-compose up
```
#### 5. (Optional) To remove the container, run this command
```bash
docker-compose down
```
