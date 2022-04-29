import sqlite3, time
from flask import Flask , render_template, request, url_for, redirect, flash
from os import environ
from flask_sqlalchemy import SQLAlchemy
import logging
from flask_ngrok import run_with_ngrok

#create connection to database
def get_db_connection():
    connection = sqlite3.connect("db_paqt.db", timeout=100)
    connection.row_factory = sqlite3.Row
    return connection

#initialize FLASH application
app = Flask(__name__)
#secret key
app.config['SECRET_KEY'] = '3cd94627d521fafeadb921052768714ea68c09dcc5e497fa'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_paqt.db'
#ignore modification on database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#run_with_ngrok(app)
#db = SQLAlchemy(app)

#route webpage
@app.route("/", methods=['GET','POST'])
def index():
    
    if request.method == 'POST':        #direct to index.html to request
        email_var = request.form["email"]       
        passwd_var = request.form["password"]

        if not email_var:           #no data input
            flash('Email is required!', 'alert-email')      #flash(print text to screen, CSS styling category)
            print("Email box: email is required")
        elif not passwd_var:        #no data input
            flash('Password is required!', 'alert-pass')    #flash(print text to screen, CSS styling category)
            print("Password box: password is required")

        else:
            #appears to be true, make connection to database
            connection = get_db_connection()
            print("Established Connection")
            connection.cursor()
            
            #insecure code
            #data = connection.execute("SELECT * FROM account WHERE email = '%s' AND password = '%s'" % (email_var, passwd_var)).fetchone()

            #secure code for fetching data in the database
            data = connection.execute("SELECT * FROM account WHERE email = :em AND password = :pa", {"em": email_var, "pa":passwd_var}).fetchone()

                #grabs data from the database
            #result = cursor.fetchall()
            

            connection.commit()     #make and save changes to database 
            connection.close()      #close database connection

            print(email_var)
            print(passwd_var)

            if data is not None:        #if data is true
                print("You successfully got in!")
                return redirect(url_for('test'))    #redirect it to the test page or basically got in

            else:                       #if data does not match --> ERROR
                flash("Username and Password don't match. Please try again.", "alert-error")        #flash(print text to screen, CSS styling category)
                print("no match: not today peep")   
            return redirect(url_for("index"))       #reload the login page

    return render_template("index.html")

#route test webpage
@app.route("/test", methods=['GET','POST'])         #route for test page
def test():
    return render_template("test.html")

#route create_login webpage
@app.route("/create_login", methods=['GET','POST'])
def create_login():

    # do stuff when the form is submitted    
    if request.method == 'POST':
        username = request.form["username"]
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        email = request.form["email"]
        password = request.form["password"]

        if not username:
            flash('Username is required!')
        elif not firstname:
            flash('First Name is required!')
        elif not lastname:
            flash('Last Name is required!')
        elif not email:
            flash('Email is required!')
        elif not password:
            flash('Password is required!')
        else:
            connection = get_db_connection()
            connection.execute("INSERT INTO account (username, firstname, lastname, email, password) VALUES (?, ?, ?, ? ,?)")
            connection.commit()
            connection.close()
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
            return redirect(url_for("create-account"))
    #connection.close()
    return render_template("create-account.html")


if __name__== '__main__':
    app.run()
