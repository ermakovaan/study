import pandas as pd
import sqlite3


database_name = input()
csv_file = input()
table_name = input()


df = pd.read_csv(csv_file)
con = sqlite3.connect(database_name)
cur = con.cursor()
df.to_sql(name=table_name, con=con, if_exists='fail', index=False)
con.commit()
print(table_name)

#Курсы валют в БД