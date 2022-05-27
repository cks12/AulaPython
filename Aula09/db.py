import sqlite3
from sqlite3 import Error

class utils:
    def __list_to_string__ (self, element: list):
        newString = ""
        for i,e in enumerate(element):
            string = f"{e} , " if i != (len(element) - 1) else f"{e}"
            newString += string
        return newString

    def __item_type__(self, elements: list):
            newElements = []
            for e in elements:
                string = "{item} {type}".format(item = e[0], type = e[1])
                newElements.append(string)
            return newElements

class Database(utils):
    def __init__(self):
        self.conn = None
        super().__init__()

    def create_connection(self,db_file) -> None:
        '''Creates new connection with database'''
        try: 
            self.conn = sqlite3.connect(db_file)
            print(sqlite3.version)

        except Error as err:
            print(err)

    def __create_table__(self, name: str, elements: list) -> None:
        ''' Create table with name and elements ([[item ,type]]) '''
        try:
            cur = self.conn.cursor()
            newArr = self.__item_type__(elements)
            newString = self.__list_to_string__(newArr)
            print(newString)
            cur.execute(f'''CREATE TABLE {name} ({newString})''')
            self.conn.commit()
        except Error as err:
            print(err)

    def __insert_in_table__ (self, name: str, elements:list) -> None:
        try:
            newString = self.__list_to_string__(elements)
            cur = self.conn.cursor()
            cur.execute(f"INSERT INTO {name} VALUES ({newString})")
            self.conn.commit()
        except Error as err:
            print(err)

    def __get_all__ (self, name):
        try:
            cur = self.conn.cursor()
            rows = cur.execute(f"SELECT * FROM {name}")
            for i in rows:
                print(i)
        
        except Error as err:
            print(err)     
    def get_conn (self):
        return self.conn


class orm_db(Database):
    def __init__(self):
        super().__init__()
    def createModal(self, elements: list):
        try:
            arr = []
            for element in elements:
                newArr = [element["name"], element["type"]]
                arr.append(newArr)
        except:
            pass


db = orm_db()
db.create_connection(r"databse.db")

# db.create_table("peoples", [
#     ["name","text"],
#     ["email","text"],
#     ["age","real"],
# ])

# db.insertInTable("peoples", [
#     "'caio Caik Fresneda de souza'",
#     "'caiodesouza12@gmail.com'",
#     "'21'"
# ])

users = db.get_all("peoples")
print(users)