import os
import re
from typing import List, Union

import oracledb
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

oracledb.init_oracle_client()


def get_oracle_engine():
    # Database connection parameters

    """
    Creates and returns a SQLAlchemy engine for connecting to Oracle.
    This is the preferred way for pandas.read_sql().
    """
    try:
        # SQLAlchemy connection string format for Oracle with oracledb:
        # 'oracle+oracledb://user:password@host:port/service_name'
        # Note: 'oracledb' is the driver name for the new python-oracledb package
        connection_string = f"oracle+oracledb://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_SID")}"
        engine = create_engine(connection_string)
        # Test the connection

        return engine
    except Exception as e:
        print(f"Error creating SQLAlchemy engine or connecting: {e}")
        print("Please check your connection details and ensure SQLAlchemy and python-oracledb are installed.")
        return None


def get_df(query: str, in_list: Union[List[str], None] = None):
    params = {}
    if in_list and 'in_clause' in query.lower():
        query = re.sub("in_clause", ', '.join([':' + str(i + 1) for i in range(len(last_names))]), query,
                       flags=re.IGNORECASE)

        params = {str(i + 1): value for i, value in enumerate(last_names)}

        # Execute query and load into DataFrame

    df = pd.read_sql(query, con=connection, params=params)
    return df


# SQL query
query = """
SELECT *
from contacts
where last_name in (in_query)
"""

try:
    # Establish connection
    connection = get_oracle_engine()
    last_names = ['Barnett', 'Barry']

    df = get_df("select * from contacts where last_name in (IN_CLAUSE)", last_names)

    print(df)

except Exception as e:
    print(f"Database error: {e}")
