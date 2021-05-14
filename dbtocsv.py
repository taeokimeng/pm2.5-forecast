import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('manhole.db')
# Allow us to execute SQL queries
# cur = conn.cursor()
#
# cur.execute("SELECT * FROM manhole")

df = pd.read_sql_query("SELECT * FROM manhole", conn)

print(df.head())
print(df.columns)

# Delete certain columns
df_data = df.drop(columns=['payload', 'raw', 'dec_raw'], axis=1)
print(df_data.head())
print(df_data.columns)

# Save to csv
df_data.to_csv("manhole.csv", index=False, mode='w')

# Read CSV
df_read = pd.read_csv('manhole.csv')

print("READ ...")
print(df_read.head())
print(df_read.columns)
