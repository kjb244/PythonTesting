import os
import re
from typing import List, Union, Dict, Any

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
        print(
            "Please check your connection details and ensure SQLAlchemy and python-oracledb are installed."
        )
        return None


def get_df(query: str, parm_dict: Union[Dict[str, Any], None] = None):
    params: Dict[str, str] = {}

    if parm_dict:
        cntr: int = 1
        for key, value in parm_dict.items():
            value_is_list: bool = isinstance(value, list)
            if value_is_list:
                query = re.sub(
                    key,
                    ", ".join(
                        [
                            ":in" + str(cntr) + "_" + str(i + 1)
                            for i in range(len(last_names))
                        ]
                    ),
                    query,
                    flags=re.NOFLAG,
                )
                params.update(
                    {
                        "in" + str(cntr) + "_" + str(i + 1): value
                        for i, value in enumerate(last_names)
                    }
                )

            else:
                query = re.sub(key, ":" + key, query, re.NOFLAG)
                params.update({key: value})
            cntr += 1
    df = pd.read_sql(query, con=connection, params=params)
    return df


try:
    query = """
    SELECT *
    from contacts
    where last_name in (in_clause)
    and phone = phone_clause
    """
    # Establish connection
    connection = get_oracle_engine()
    last_names = ["Barnett", "Barry", "Barrera"]

    df = get_df(
        query, parm_dict={"in_clause": last_names, "phone_clause": "+1 616 123 4234"}
    )

    print(df)

except Exception as e:
    print(f"Database error: {e}")
