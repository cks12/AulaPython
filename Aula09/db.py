import sqlite3
from sqlite3 import Error
class Database:
    def __init__(self):
        self.conn = None
    def createConnection(self,db_file):
        '''Creates new connection with database'''
        try: 
            self.conn = sqlite3.connect(db_file)
            print(sqlite3.version)

        except Error as err:
            print(err)

    def __list_to_string__ (self, elemnt: list):
        newString = ""
        for e in newElements:
            string = f"{e} "
            newString += string
        return newString

    def __item_type__(self, elements: list):
            newElements = []
            for e in elements:
                string = "{item} {type}".format(item = e[0], type = e[1])
                newElements.append(string)
            return newElements
            
    def create_table(self, name: str, elements: list) -> None:
        ''' Create table with name and elements ([[item ,type]]) '''
        try:
            cur = self.conn.cursor()
            newArr = __item_type__(elements)
            newString = self.__list_to_string__(newArr)
            cur.execute(f'''CREATE TABLE {name} ({newString})''')
            self.conn.commit()
        except Error as err:
            print(err)

    def insertInTable(self, name: str, elements:list):
        try:
            newString = self.__list_to_string__(newArr)
            cur = self.conn.cursor()
            cur.execute(f"INSERT INTO {name} VALUES ({newString})")
            self.conn.commit()
        except Error as err:
            print(err)
    def get_conn (self):
        return self.conn

db = Database()
db.createConnection(r"databse.db")

db.insertInTable("sla",
   [ "caio",
    "caiofresneda@gmail.com",10,]
)