import dotenv as dot
import numpy as np
import pandas as pd
import os
from sqlalchemy import create_engine

dot.load_dotenv("../.env")
username = os.getenv("username2")
password = os.getenv("password")
host = os.getenv("host")
dbname = os.getenv("dbname")

conn_str = f"mysql+pymysql://{username}:{password}@{host}/{dbname}"

db_engine = create_engine(conn_str)

dimproduct = pd.read_sql("SELECT * FROM dimproduct",db_engine)

