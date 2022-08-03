# Citation for the following content display
#    Date:07/22/2022
#      Copied from https://github.com/osu-cs340-ecampus/flask-starter-app#creating-your-directory



from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = 'cs340_diagours'
app.config['MYSQL_PASSWORD'] = '9303' #last 4 of onid
app.config['MYSQL_DB'] = 'cs340_diagours'
app.config['MYSQL_CURSORCLASS'] = "DictCursor"


mysql = MySQL(app)


# Routes
@app.route('/')
def root():
    query = "SELECT * FROM diagnostic;"
    query1 = 'DROP TABLE IF EXISTS diagnostic;';
    query2 = 'CREATE TABLE diagnostic(id INT PRIMARY KEY AUTO_INCREMENT, text VARCHAR(255) NOT NULL);';
    query3 = 'INSERT INTO diagnostic (text) VALUES ("MySQL is working!")';
    query4 = 'SELECT * FROM diagnostic;';
    cur = mysql.connection.cursor()
    cur.execute(query1)
    cur.execute(query2)
    cur.execute(query3)
    cur.execute(query4)
    results = cur.fetchall()

    return results[0]


# Listener
if __name__ == "__main__":

    port = int(os.environ.get('PORT', 27201)) 

    #Start the app on port 27564, it will be different once hosted
    app.run(port=port, debug=True)