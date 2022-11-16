import pymysql.cursors
import pandas
from pandas.core.frame import DataFrame
#from Start import Myhash

# Connect to the database
#connection = pymysql.connect(host='localhost',user="root",port=3306,database="test2")#,password="mysql"


    #with connection.cursor() as cursor:
        # Create a new record
        #sql = f"INSERT INTO `test_taple` (`numbers`, `contry_code`) VALUES ('hhhhhhhhhhhh', 'hhhhhhhhhhhh')"
        #cursor.execute(sql)

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    #connection.commit()


# class Database_connection():#pymysql.cursors

#     SQL_SELECT_ALL = "SELECT * FROM "
#     hash =  Myhash()
#     k7 = hash.delayers("YeA_UB=I[}OudYgSG<5@5{ycYeA_UB=I:WyaUW8-n*A>Ym5@",3)
#     m9n = hash.delayers("qqNDN^98qE+|ppSLkIq~[}OuG<5@5{ycA>GTqEJ&yc+|=4qEG<G<qq=IG<5@5{ycqEdr92gSG<G<Ah78q~NDwsSI",3)

#     def __init__(self) -> None:
#         pass

#     def connect(
#         self,
#         host:str="localhost",
#         user:str="root",
#         password:str="",
#         database_name:str="",
#         port:int=3306,
#         taple_name:str=None,
#         )->pandas.DataFrame:
#         """ return a DataFrame from database """
#         """
#         parameters:
#         host : that host or ip_address have database 
#         user : user of database
#         password : password of database standard password is '' 
#         database_name : the name of database 
#         port : port of XAMPP application with MySQL 
#         """
#         self.connection = pymysql.connect(host=host,user=user,port=port,password=password) # database=database_name
#         # self.dataframe = pandas.read_sql_query(f"{self.SQL_SELECT_ALL} {taple_name}",self.connection)

#         # return self.dataframe


    

class Dataframe():

    def __init__(self,dataframe) -> DataFrame:
        global df
        df = self.dataframe = self.df = dataframe
        self._col_name = df.columns.values[0]
        
    def set_col_name(self,col_name:str):
        """ settern of column name """
        self._col_name = col_name

    def get_col_name(self)-> str:
        """ gettern of column name """
        return self._col_name


    def get_column(self):
        """ return list of columns values """
        return df[self._col_name]

    def get_index(self,val):
        """ return the index of this value """
        return df[df[self._col_name]==val].index
        

    def get_row_per_index(self,index)->list:
        """ retutn a List (row) of all Values in this index """
        return df.iloc[index].values
        

    def is_double(self,val:str=None)->bool:
        """ return False if value is already exist if not return True """
        return df[df[self._col_name]==val].empty

    def insert_row_from_end(self,list_of_values:list):
        df.loc[len(df.index)] = list_of_values





# con = Database_connection()
# data =  con.connect(
#     host = "162.55.15.100",    
#     user = str(con.k7),
#     password = str(con.m9n),
#     port = 3306
# )


# print(socket.gethostbyname("https://almamlaka.info"))

# db = Dataframe(data)


# db.set_col_name("numbers")





# print(db.dataframe)#is_double("numbers","ggg")












