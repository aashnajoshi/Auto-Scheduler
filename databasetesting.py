import pyodbc
import pandas as pd
constr=("Driver={SQL Server};"
        "Server=BUDDY;"
    "Database=testdb;"
    "Trusted_connection=yes;")
cnxn=pyodbc.connect(constr)
crsr=cnxn.cursor()
query="select * from login"
# crsr.execute(query)
data=pd.read_sql(query,cnxn)
print(data)
cnxn.commit()