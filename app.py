from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Samuel Buckler in 3308!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://sql_lab10_user:S4Ls8GIQDclAbq4RPfzshkPNgIF6NtQf@dpg-cqlddk5umphs738qjoe0-a/sql_lab10")
    conn.close()
    return "Database Connection Successful!"
