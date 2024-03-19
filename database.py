import dotenv as dot
import datetime
import pandas as pd

import os
from sqlalchemy import create_engine

dot.load_dotenv()

username = os.getenv("username2")
password = os.getenv("password")
host = os.getenv("host")
dbname = os.getenv("dbname")

conn_str = f"mysql+pymysql://{username}:{password}@{host}/{dbname}"

print(conn_str)

db_engine = create_engine(conn_str)

query = "SELECT * FROM dimcustomer"

df = pd.read_sql(query, db_engine)
db_engine.dispose()

df['BirthDate'] = pd.to_datetime(df['BirthDate'])

filtered_df = df[df['BirthDate'] > '1971-01-01']
# print(filtered_df)

# print(filtered_df.iloc[3])
# print("Femmine", filtered_df.loc[df["Gender"] == "F"])
# print("Femmine", filtered_df.loc[df["Gender"] == "M"])


