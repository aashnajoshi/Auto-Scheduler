import pyodbc
import pandas as pd
def connect():
    constr=("Driver={SQL Server};"
            "Server=BUDDY;"
        "Database=testdb;"
        "Trusted_connection=yes;")
    cnxn=pyodbc.connect(constr)
    return cnxn
# crsr=cnxn.cursor()
# query="select * from login"
# # crsr.execute(query)
# data=pd.read_sql(query,cnxn)
# print(data)
# cnxn.commit()