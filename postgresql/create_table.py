import psycopg2
from config import config


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE IF NOT EXISTS manhole (
            payload VARCHAR(4000) NOT NULL,
            raw VARCHAR(500) NOT NULL,
            dec_raw VARCHAR(1000) NOT NULL,
            battery_voltage VARCHAR(20) DEFAULT NULL,
            status VARCHAR(20) DEFAULT NULL,
            manhole_cap_status VARCHAR(20) DEFAULT NULL,
            temperature VARCHAR(20) DEFAULT NULL,
            humidity VARCHAR(20) DEFAULT NULL,
            water_level VARCHAR(20) DEFAULT NULL,
            CO VARCHAR(20) DEFAULT NULL,
            CO2 VARCHAR(20) DEFAULT NULL,
            CH4 VARCHAR(20) DEFAULT NULL,
            O2 VARCHAR(20) DEFAULT NULL,
            H2S VARCHAR(20) DEFAULT NULL,
            sensor_time VARCHAR(25) NOT NULL,
            convert_time timestamp,
            PRIMARY KEY (sensor_time)
        )
        """,
    )
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

        # create table one by one
        for command in commands:
            print(command)
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()

# """
#         CREATE TABLE IF NOT EXISTS manhole (
#             payload VARCHAR(4000) NOT NULL,
#             raw VARCHAR(500) NOT NULL,
#             dec_raw VARCHAR(1000) NOT NULL,
#             battery_voltage VARCHAR(20) DEFAULT NULL,
#             status VARCHAR(20) DEFAULT NULL,
#             manhole_cap_status VARCHAR(20) DEFAULT NULL,
#             temperature VARCHAR(20) DEFAULT NULL,
#             humidity VARCHAR(20) DEFAULT NULL,
#             water_level VARCHAR(20) DEFAULT NULL,
#             CO VARCHAR(20) DEFAULT NULL,
#             CO2 VARCHAR(20) DEFAULT NULL,
#             CH4 VARCHAR(20) DEFAULT NULL,
#             O2 VARCHAR(20) DEFAULT NULL,
#             H2S VARCHAR(20) DEFAULT NULL,
#             sensor_time VARCHAR(25) NOT NULL,
#             convert_time timestamp,
#             PRIMARY KEY (sensor_time)
#         )
# """