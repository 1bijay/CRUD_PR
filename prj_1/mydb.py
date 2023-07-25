# connect db -> ../db.sqlite3
# create table(person[pid,fullname,contactadress])
# insert data
# select data
# update data
# search data
# delete data
import sqlite3
import sys
from .person import Person

DB_FILE ="../db.sqlite3"

def create_table():
    conn = None
    sql = '''CREATE TABLE PERSON (
        PID INTEGER PRIMARY KEY,
        name TEXT(50),
        adress TEXT(50)
    )'''
    try:
        # connect with db
        conn = sqlite3.connect(DB_FILE)
        cursor =conn.cursor()
        cursor.execute(sql)
    # insert record

        conn.close()    # connection close
        print(" create table succesfuly")
    except:
        print("Error : ", sys.exc_info()[0])
    finally:
        del sql
        del conn
create_table()

def insertRecord(objPerson):
    conn = None
    sql = ''' INSERT INTO PERSON (pid, name, adress) VALUES(?,?,?)'''
    values=(Person.getPID(),Person.getname(),Person.getadress())
    #connect with db
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(sql,values);  #record insert
        conn.commit()  # save inserted record
        # insert record

        conn.close()  # connection close
        print(" create table succesfuly")
    except:
        print("Error : ", sys.exc_info()[0])
    finally:
        del sql
        del conn
def selectALL():
    conn = None
    sql = '''SELECT * FROM persons'''
    values = (Person.getPID(), Person.getName(), Person.getAdress())
    # connect with db
    persons=[]
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(sql)  # select all
        rows = cursor.fetchall()
        for row in rows:
            persons.append(row)
            print(row)
            cursor.close()
            conn.close()  # connection close
        print(" Display All Record succesfuly")
        return persons
    except:
        print("Error : ", sys.exc_info()[0])
    finally:
        del sql
        del conn
# create
#person = person(1,"raj rai","ktm")
#insertRecord(person)