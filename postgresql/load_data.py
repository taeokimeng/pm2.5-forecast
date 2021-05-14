import psycopg2
from config import config
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:learning@localhost:5432/manhole")

conn = None
try:
    # read the connection parameters
    params = config()
    # connect to the PostgreSQL server
    conn = psycopg2.connect(**params)
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()

df = pd.read_sql_query("SELECT * FROM manhole", conn)

print(df.head())
print(df.columns)

# Delete certain columns
df_data = df.drop(columns=['payload', 'raw', 'dec_raw'], axis=1)
print(df_data.head())
print(df_data.columns)

# Save to csv
df_data.to_csv("manhole_from_postgresql.csv", index=False, mode='w')