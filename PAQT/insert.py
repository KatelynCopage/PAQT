import sqlite3

connection = sqlite3.connect('db_paqt.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

#cursor
c = connection.cursor()

def select_signin():
    connection = sqlite3.connect('db_paqt.db')
    c = connection.cursor()
    c.execute("SELECT rowid, * FROM account")

    #print data
    result = c.fetchall()

    connection.commit()
    connection.close()


#c.execute("INSERT INTO account VALUES (?,?,?,?,?,?)", (username, first_name, last_name, email, location, password))
def add_one(username, first_name, last_name, email, location, password):
    connection = sqlite3.connect('db_paqt.db')
    c = connection.cursor()

    #link to create account html: missing ???
    c.execute("INSERT INTO account VALUES (?,?,?,?,?,?)", (username, first_name, last_name, email, location, password))

    connection.commit()
    connection.close()


#insert data into one column username
'''
def insert_username(username):
    connection = sqlite3.connect('db_paqt.db')
    c = connection.cursor()

    #link to create account html: missing ???
    c.execute("INSERT INTO account (username) VALUES (?)", (username))

    connection.commit()
    connection.close()
    '''


connection.commit()
connection.close()