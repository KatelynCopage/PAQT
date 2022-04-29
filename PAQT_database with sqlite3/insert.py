#to initialize database and create sqlite3 table
import sqlite3

connection = sqlite3.connect('db_paqt.db')  #database connection

with open('schema.sql') as f:               #read, open, execute the sql file
    connection.executescript(f.read())

#cursor
c = connection.cursor()

def select_signin():
    #make connection to database
    connection = sqlite3.connect('db_paqt.db')
    c = connection.cursor()
    c.execute("SELECT rowid, * FROM account")

    #print data
    result = c.fetchall()

    connection.commit()
    connection.close()

print("Done")

connection.commit()     #save and make changes
connection.close()      #close database connection