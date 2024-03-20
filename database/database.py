import dotenv as dot
import numpy as np
import datetime
import pandas as pd

import os
from sqlalchemy import create_engine

dot.load_dotenv("../.env")

username = os.getenv("username2")
password = os.getenv("password")
host = os.getenv("host")
dbname = os.getenv("dbname")

conn_str = f"mysql+pymysql://{username}:{password}@{host}/{dbname}"

print(conn_str)

db_engine = create_engine(conn_str)

query = "SELECT * FROM dimemployee"

dimemployee = pd.read_sql(query, db_engine)

query = "SELECT * FROM dimemployeesalesterritory"
dimemployeesalesterritory = pd.read_sql(query, db_engine)

query = "SELECT * FROM dimsalesterritory"
dimsalesterritory = pd.read_sql(query, db_engine)

db_engine.dispose()

print(dimemployee.shape)
print(dimemployee["EmployeeKey"].nunique())
print(dimemployeesalesterritory.shape)
print(dimemployeesalesterritory["EmployeeKey"].nunique())

dimemployee.set_index("EmployeeKey", inplace=True, drop=False)
dimemployeesalesterritory.set_index("EmployeeKey", inplace=True)

dimemployee_join_dimemployeesalesterritory = dimemployeesalesterritory.join(dimemployee)
print(dimemployee_join_dimemployeesalesterritory.shape)

# print(dimemployee_join_dimemployeesalesterritory["SalesTerritoryKey"].count())
# print(dimemployee_join_dimemployeesalesterritory["SalesTerritoryKey"].isnull().count())

print(dimemployee_join_dimemployeesalesterritory.columns)
#dimemployee_join_dimemployeesalesterritory.reset_index("EmployeeKey", inplace=True)
dimemployee_join_dimemployeesalesterritory.set_index("SalesTerritoryKey", inplace=True)
print(dimemployee_join_dimemployeesalesterritory.columns)
dimsalesterritory.set_index("SalesTerritoryKey", inplace=True)

dimemployee_join_dimemployeesalesterritory_join_dimsalesterritory = dimemployee_join_dimemployeesalesterritory.join(
    dimsalesterritory)

# print(dimemployee_join_dimemployeesalesterritory_join_dimsalesterritory.shape)
# print(dimemployee_join_dimemployeesalesterritory_join_dimsalesterritory)

dimemployee_join_dimemployeesalesterritory_join_dimsalesterritory = dimsalesterritory.join(
    dimemployee_join_dimemployeesalesterritory)
# print(dimemployee_join_dimemployeesalesterritory_join_dimsalesterritory.shape)
# print(dimemployee_join_dimemployeesalesterritory_join_dimsalesterritory)

# print(dimemployee_join_dimemployeesalesterritory["EmployeeKey"].nunique())
# print(filtered_df.iloc[3])
# print("Femmine", filtered_df.loc[df["Gender"] == "F"])
# print("Femmine", filtered_df.loc[df["Gender"] == "M"])
