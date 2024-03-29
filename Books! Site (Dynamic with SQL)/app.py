
from distutils.util import execute
import sqlite3
from flask import Flask, render_template, g, request
#from player import render

PATH = 'db/books.sqlite'

app = Flask(__name__)

def open_connection():
    connection = getattr(g, '_connection', None)
    if connection == None:
        connection = g._connection = sqlite3.connect(PATH)
    connection.row_factory = sqlite3.Row
    return connection

def execute_sql(sql, values=(), commit=False, single=False):
    connection = open_connection()
    cursor = connection.execute(sql, values)
    if commit == True:
        results = connection. commit()
    else:
        results = cursor.fetchone() if single else cursor.fetchall()

    cursor.close()
    return results

@app.teardown_appcontext
def close_connection(exception):
    connection = getattr(g, '_connection', None)
    if connection is not None:
        connection.close()

@app.route('/')
def home():
    jobs = execute_sql('')
    return render_template('index.html')

@app.route('/contact_page')
def contact():
    return render_template('contact.html')

@app.route('/seedDB')
def seedDB():
        sqlQ = execute_sql('DROP TABLE IF EXISTS Book',commit=True)

        sqlQuery = execute_sql('CREATE TABLE Book (author TEXT,title TEXT, description TEXT)',commit=True)

        sqlQuery2 = execute_sql('INSERT INTO Book (author,title, description) VALUES ("Mary Shelley","Frankenstein", "A horror story written by a romantic.")',commit=True)
        sqlQuery2 = execute_sql('INSERT INTO Book (author,title, description) VALUES ("Henry James","The Turn of the Screw", "Another British horror story.")',commit=True)
        sqlQuery2 = execute_sql('INSERT INTO Book (author,title, description) VALUES ("Max Weber","The Protestant Work Ethic and The Spirit of Capitalism", "A classic early 20th C. sociology text")',commit=True)
        sqlQuery2 = execute_sql('INSERT INTO Book (author,title, description) VALUES ("Robert Putnam","Bowling Alone", "A classic late 20th C. sociology text")',commit=True)


        booksQuery = execute_sql('SELECT rowid, * FROM Book')
        for book in booksQuery:
            print(book['rowid'])
            print(book['author'])

        return '<h1>DB Seeded!</h1>'

@app.route('/erase_DB')
def eraseDB():
        sqlQ = execute_sql('DELETE FROM Book',commit=True)
        return '<h1>DB Erased!</h1>'

@app.route('/all_books')
def all_books():
        books = execute_sql('SELECT * FROM Book')
        return render_template('all_books.html', books=books)

@app.route('/add_book', methods={'GET','POST'})
def addbook():
        if request.method == 'POST':
                author = request.form['author']
                title = request.form['title']
                description = request.form['description']

                returnStatus = execute_sql('INSERT INTO Book (author, title, description ) VALUES (?, ?, ?)',
                (author, title, description),commit=True)

                # return redirect(url_for('home))
                return render_template('add_book.html', book_title=title )
        return render_template('add_book.html', book_title="")
