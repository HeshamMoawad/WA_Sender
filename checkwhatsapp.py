import pandas
from time import sleep
import sqlite3 as sq
from DB_online import Dataframe
import datetime
from mainclass import Whatsapp
con = sq.connect("Numbers.db")

# con.cursor().execute("""
# create table number (
#     number text,
#     whatsapp boolean
# );
#  """)
# print("making Succesfully")
t1 = datetime.datetime.now()
df = Dataframe(pandas.read_sql_query("select * from number",con))
#new_df = Dataframe(pandas.read_sql_query("select * from test",con))
t2= datetime.datetime.now()


whats = Whatsapp()
whats.start_browser(["","",2])

data = whats.have_whatsapp(df.df["number"].to_list()[1:2])
print(data)

t3= datetime.datetime.now()

# for lista in data :
#     print(lista)
#     new_df.insert_row_from_end(data)
# con.cursor().execute("""
# drop table number;
# """)
# new_df.df.to_sql("number",con,index=False)
print(f"----{t2-t1}--{t3-t1}-")
sleep(100)

#df.df.drop_duplicates(inplace=True)

#print(df.df)

# sleep(10)

# print(t2-t1)


# i = 0
# t1 = datetime.datetime.now()
# while i < 100000:
#     phone = f"+966{random.randrange(500000000,599999999)}"
#     if df.is_double(phone):
#         df.insert_row_from_end([phone,True])
#         print(phone)
#         i += 1
# t2 = datetime.datetime.now()
# df.df.to_excel("hhhh.xlsx" , index=False)
# t3 = datetime.datetime.now()
# con.cursor().execute("""
# drop table number;
# """)
# df.df.to_sql("number",con,index=False)
# t4 = datetime.datetime.now()


# print(f"time of making {t2-t1} and time of saving {t4-t3} total tome is {t4-t1}")