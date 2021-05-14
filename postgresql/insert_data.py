import psycopg2
from config import config
import sqlalchemy
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("postgresql://postgres:learning@localhost:5432/manhole")

def get_table_columns(table_name):
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        sql = f'SELECT * FROM {table_name} WHERE 1=0'
        cur.execute(sql)

        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return [d[0] for d in cur.description]

# Get columns' name from the table
col_name = get_table_columns('manhole')
print(col_name)

# Read CSV
df = pd.read_csv('../manhole_log.csv', parse_dates=['reg_date'])
# df = pd.read_csv('manhole_log.csv', names=col_name)

# Change columns name
df.columns = col_name
print(df.columns)

print(df.info())

# Append to the database
df.to_sql(name="manhole_temp", con=engine, schema='public', if_exists='append', index=False)

engine.execute("INSERT INTO manhole SELECT * FROM manhole_temp ON CONFLICT DO NOTHING")