import sqlite3
import pandas as pd

conn = sqlite3.connect('manhole.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS manhole(payload TEXT, raw TEXT, dec_raw TEXT, "
              "battery_voltage INTEGER, status INTEGER, manhole_cap_status INTEGER, "
              "temperature INTEGER, humidity INTEGER, water_level INTEGER, CO INTEGER, "
              "CO2 INTEGER, CH4 INTEGER, O2 INTEGER, H2S INTEGER, "
              "sensor_time TEXT PRIMARY KEY ON CONFLICT IGNORE, convert_time TEXT)") # PRIMARY KEY (sensor_time)

create_table()

def get_table_columns(table_name):
    sql = f'SELECT * FROM {table_name} WHERE 1=0'
    c.execute(sql)
    return [d[0] for d in c.description]

# Get columns' name from the table
col_name = get_table_columns('manhole')
print(col_name)

# Read CSV
df = pd.read_csv('manhole_log.csv')
# df = pd.read_csv('manhole_log.csv', names=col_name)

# Change columns name
df.columns = col_name
print(df.columns)

# Append to the database
df.to_sql("manhole", conn, if_exists='append', index=False)

# def append_db(data):
#     try:
#         data.to_sql('manhole', con=conn, index=True, index_label='sensor_time', if_exists='append')
#         return 'Success'
#     except Exception as e:
#         print("Initial failure to append: {}\n".format(e))
#         print("Attempting to rectify...")
#         existing = pd.read_sql('manhole', con=conn)
#         to_insert = data.reset_index().rename(columns={'index':'sensor_time'})
#         mask = ~to_insert.id.isin(existing.id)
#         try:
#             to_insert.loc[mask].to_sql('manhole', con=conn, index=False, if_exists='append')
#             print("Successful deduplication.")
#         except Exception as e2:
#             "Could not rectify duplicate entries. \n{}".format(e2)
#         return 'Success after dedupe'

# print(append_db(df))

# df.columns = df.columns.str.strip()

# def add_data(data):
#     c.executemany("INSERT INTO manhole VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", data)
#     conn.commit()
#
# add_data(df)

# read = pd.read_sql("pragma table_info(mandhole)", con=conn)
# print(read)

