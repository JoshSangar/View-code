import sqlite3
import pandas as pd


conn = sqlite3.connect('STAFF.db')

# Table 
dept_table_name = 'Departments'
dept_attribute_list = ['DEPT_ID', 'DEP_NAME', 'MANAGER_ID', 'LOC_ID']

# Reading the csv file
dept_file_path = '/home/project/Departments.csv'
dept_df = pd.read_csv(dept_file_path, names = dept_attribute_list)
dept_df.to_sql(dept_table_name, conn, if_exists = 'replace', index =False)
print('Table is ready')

data_dict = {'DEPT_ID' : [9],
            'DEP_NAME' : ['Quality Assurance'],
            'MANAGER_ID' : [30010],
            'LOC_ID' : ['L0010']}
data_append = pd.DataFrame(data_dict)
data_append.to_sql(dept_table_name, conn, if_exists = 'append', index =False)
print('Data appended successfully')

# Running a basic queries on the data
dept_query_statement = f"SELECT * FROM {dept_table_name}"
dept_query_output = pd.read_sql(dept_query_statement, conn)
print(dept_query_statement)
print(dept_query_output)

# Viewing only FNAME column of data
dept_query_statement = f"SELECT DEP_NAME FROM {dept_table_name}"
dept_query_output = pd.read_sql(dept_query_statement, conn)
print(dept_query_statement)
print(dept_query_output)

# View the total number of entries in the table
dept_query_statement = f"SELECT COUNT(*) FROM {dept_table_name}"
dept_query_output = pd.read_sql(dept_query_statement, conn)
print(dept_query_statement)
print(dept_query_output)

# close connection
conn.close()