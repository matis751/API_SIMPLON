from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from bdd.create_db import host, user, password, db

app = Flask(__name__)

# Configure db
app.config['MYSQL_HOST'] = host
app.config['MYSQL_USER'] = user
app.config['MYSQL_PASSWORD'] = password
app.config['MYSQL_DB'] = 'db_name'

mysql = MySQL(app)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         # Fetch form data
#         userDetails = request.form
#         name = userDetails['name']
#         email = userDetails['email']
#         cur = mysql.connection.cursor()
#         cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)",(name, email))
#         mysql.connection.commit()
#         cur.close()
#         return redirect('/users')
#     return render_template('index.html')

# @app.route('/users')
# def users():
#     cur = mysql.connection.cursor()
#     resultValue = cur.execute("SELECT * FROM users")
#     if resultValue > 0:
#         userDetails = cur.fetchall()
#         return render_template('users.html',userDetails=userDetails)

from flask import Flask
from flask import request
import app.Abr as Abr
import app.Class as Class
from app.main import creat_tree

app = Flask(__name__)
@app.route('/text', methods=['POST', 'GET'])
def create_tree():
    request.data = 'https://en.wikipedia.org/wiki/Tokyo'
    tree = creat_tree(Class.Tree(), request.data)
    r = Abr.Iterative_tree_shearch(tree.root, hash('and'))
    if r is not None:
        return ({r.word_occurence[0] : r.word_occurence[1]})
    else:
        return('Rien trouver')

if __name__ == '__main__':
    app.run(debug=True)