import sqlite3, time
from flask import Flask , render_template 
#from django import db

#db.connections.close_all()

def get_db_connection():
    connection = sqlite3.connect("db_paqt.db", timeout=10)
    connection.row_factory = sqlite3.Row
    return connection

app = Flask(__name__)

@app.route("/")

def index():
    connection = get_db_connection()

    data = connection.execute("SELECT * FROM account").fetchall()

    #commmit our command
    connection.commit()    

    #close connection to the db
    connection.close()
    print("\nConnection Closed...")
    return render_template("index.html", data = data)


@app.route("/create_login")
def create_login():
    connection = get_db_connection()
    connection.close()
    return render_template("create-account.html")

#@app.route("/save_login",methods=['GET','POST'])
#def save_login():
    ## add code for handling adding the data dto dB

#    if request.method == 'POST':
#        pass
    # do stuff when the form is submitted

    # redirect to end the POST handling
    # the redirect can be to the same route or somewhere else
#    return redirect(url_for('index'))

