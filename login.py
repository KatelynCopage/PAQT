import sqlite3, time
import os
from flask import Flask , render_template, request, url_for, redirect, render_template, flash
import logging
from colorama import Fore, Back, Style

def get_db_connection():
    connection = sqlite3.connect("db_paqt.db", timeout=100)
    connection.row_factory = sqlite3.Row
    return connection

app = Flask(__name__)
app.config['SECRET_KEY'] = '3cd94627d521fafeadb921052768714ea68c09dcc5e497fa'

@app.route("/", methods=['GET','POST'])
def index():
    logging.basicConfig(level=logging.DEBUG, filename='loginlog.log', format='%(asctime)s %(levelname)s:%(message)s')
    if request.method == 'POST':
        email_var = request.form["email"]
        passwd_var = request.form["password"]

        if not email_var:
            flash('Email is required!')
            #Fore.ORANGE + Back.BLUE + '?: ' + Style.RESET_ALL, end="" + 
            print("Email box: email is required")
        elif not passwd_var:
            flash('Password is required!')
            print("Password box: password is required")

        else:
            connection = get_db_connection()
            print("Established Connection")
            connection.cursor()
            data = connection.execute("SELECT * FROM account WHERE email = :em AND password = :pa", {"em": email_var, "pa":passwd_var}).fetchone()
            #app.logger.info("%s ")
            #result = connection.fetchall()

            connection.commit()
            connection.close()
            
            if data is not None:
                print("You successfully got in!")
                return redirect(url_for('test'))
                print(data[0])
            else:
                flash("Username and Password don't match. Please try again.")
                print("no match: not today peep")   
            return redirect(url_for("index"))

    return render_template("index.html")

@app.route("/test", methods=['GET','POST'])
def test():
    return render_template("test.html")

@app.route("/create_login", methods=['GET','POST'])
def create_login():
    #connection = get_db_connection()
    #c = connection.cursor()

    #c.execute("INSERT INTO account VALUES (?,?,?,?,?,?)", (username, first_name, last_name, email, location, password))

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


'''
@app.route("/signin", methods=['GET','POST'])
def signin():
    if request.method == 'POST':
        email = request.form["email"]
        password = request.form["password"]
        if not email:
            flash('Email is required!')
        elif not password:
            flash('Password is required!')
        else:
            connection = get_db_connection()
            connection.cursor()
            data = connection.execute("SELECT rowid, * FROM account")
            result = connection.fetchall()

            connection.commit()
            connection.close()
            return redirect(url_for("index"), data = data)
    return create_login
    

    ## add code for handling adding the data dto dB
    #link to create account html: missing ???

    c.execute("INSERT INTO account VALUES (?,?,?,?,?,?)", (username, first_name, last_name, email, location, password))

    # do stuff when the form is submitted    
    if request.method == 'POST':
        user = request.form["nm"]
    # redirect to end the POST handling
    # the redirect can be to the same route or somewhere else
        return redirect(url_for("user", account_page=user))
    else:
        return render_template("create_account.html")

    connection.close()
    return render_template("create_account.html")


@app.route("/<account_page>")
def user(account_page):
    return f"The account page will be here after you successfully log in or created an account!"
    '''