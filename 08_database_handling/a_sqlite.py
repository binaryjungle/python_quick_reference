#Beginning of the program
print("Beginning Of the Program")
print("")

import sqlite3

#creates the database if doesn't exists. If database exists, it will connect
db = sqlite3.connect("test.db")
db.row_factory = sqlite3.Row

#execute method is used to pass sql statements
db.execute("drop table if exists students")
db.execute("""
    create table students
    (id int
    ,name text
    ,grade text
    ,location text
    )
    """)
db.execute("insert into students (id, name, grade, location) values (?, ?, ?, ?)",(1, "Sam", "5", "West Street"))
db.execute("insert into students (id, name, grade, location) values (?, ?, ?, ?)",(2, "John", "6", "East Lane"))
#unless commit is executed, sql statements will not be physically reflect
db.commit()

#using cursor to loop through the resultset from the database
cursor = db.execute("select * from students")
for row in cursor:
    print(row) #prints the object related detail
    print(row[:]) #prints the full row
    print(row["name"]) #prints specific column
    print(dict(row)) #returns dictionary with column name and its corresponding value

print("just another way")
#similar to above way, we can execute over cursor as well
cur = db.cursor()
data = cur.execute("select * from students")
for row in data:
    print(dict(row)) #returns dictionary with column name and its corresponding value

#fetchone returns single row at a time
#square brackets are used to get specific column alone
cur.execute("select * from students")
print(cur.fetchone()[1])
db.close()

print("Object Oriented Way")

#creates database class
class database:
    #specify database name and tablename while creating an object 
    def __init__(self,**kwargs):
        self.db_name = kwargs.get("db_name")
        self.tbl_name = kwargs.get("tbl_name", "students")
    
    #this method is to insert rows to table
    def insert(self, row):
        self._db.execute("insert into {} (id, name, grade, location) \
                        values (?, ?, ?, ?)".format(self._tbl_name), \
                        (row["id"],row["name"],row["grade"],row["location"]))
        self._db.commit()
    
    #this method returns rows if key is provided
    def retrieve(self, key):
        cursor = self._db.execute("select * from {} where id = ?".format(self._tbl_name), (key,))
        return dict(cursor.fetchone())
    
    #this method will return all rows
    def disp_rows(self):
        cursor = self._db.execute("select * from {}".format(self._tbl_name))
        for row in cursor:
            print (dict(row))
    
    #below method will be used to make the object iterable (eg: if for loop is required)
    def __iter__(self):
        cursor = self._db.execute("select * from {}".format(self._tbl_name))
        for row in cursor:
            yield(dict(row))
    
    #this method will close the database
    def close(self):
        self._db.close()
        del self._db_name
    
    #will be used by setter and deleter methods
    @property
    def db_name(self): return self._db_name
    
    #sets the database name
    @db_name.setter
    def db_name(self, db_nm):
        self._db_name = db_nm
        self._db = sqlite3.connect(db_nm)
        self._db.row_factory = sqlite3.Row
    
    @db_name.deleter
    def db_name(self): self.close()
    
    @property
    def tbl_name(self): return self._tbl_name
    
    @tbl_name.setter
    def tbl_name(self, tbl_nm):
        self._tbl_name = tbl_nm
    
    @tbl_name.deleter
    def tbl_name(self): self._tbl_name = "students"

db = database(db_name = "non_existing_db", tbl_name = "non_existing_tbl")
db.db_name="test.db"
db.tbl_name="students"
db.disp_rows()
db.insert(dict(id = 3, name = "Alex", grade = "7", location = "South City"))

#below for loop is possible because of __iter__ method
for row in db: print(row)

db.close()

#End of the program
print("")
print("End Of the Program")
