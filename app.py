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

@app.route('/db_create')
def create():
    conn = psycopg2.connect("postgresql://sql_lab10_user:S4Ls8GIQDclAbq4RPfzshkPNgIF6NtQf@dpg-cqlddk5umphs738qjoe0-a/sql_lab10")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
''')
    conn.commit()
    conn.close()
    return "DB CREATED"

@app.route('/db_insert')
def insert():
    conn = psycopg2.connect("postgresql://sql_lab10_user:S4Ls8GIQDclAbq4RPfzshkPNgIF6NtQf@dpg-cqlddk5umphs738qjoe0-a/sql_lab10")
    cur = conn.cursor()
    cur.execute('''
    INSERT INTO Basketball (First, Last, City, Name, Number)
    Values
    ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
    ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
    ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
    ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
''')
    conn.commit()
    conn.close()
    return "DB SUCCESFULLY INSERTED"