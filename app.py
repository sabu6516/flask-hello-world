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
    with conn:
        with conn.cursor() as cur:
            cur.execute('''
            INSERT INTO Basketball (First, Last, City, Name, Number)
            VALUES
            ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
            ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
            ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
            ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2),
            ('Sam', 'Buckler', 'Winchester', 'CS3308', 50);
            ''')
    return "DB SUCCESSFULLY INSERTED"


@app.route('/db_select')
def selecting():
    conn = psycopg2.connect("postgresql://sql_lab10_user:S4Ls8GIQDclAbq4RPfzshkPNgIF6NtQf@dpg-cqlddk5umphs738qjoe0-a/sql_lab10")
    cur = conn.cursor()
    cur.execute('''
    SELECT * FROM Basketball;
''')
    records = cur.fetchall()
    conn.close()
    response = ""
    response += "<table>"
    for player in records:
        response += "<tr>"
        for info in player:
            response += "<td>{}<td>".format(info)
        response += "</tr>"
    response += "</table>"
    return response


@app.route('/db_drop')
def drop():
    conn = psycopg2.connect("postgresql://sql_lab10_user:S4Ls8GIQDclAbq4RPfzshkPNgIF6NtQf@dpg-cqlddk5umphs738qjoe0-a/sql_lab10")
    cur = conn.cursor()
    cur.execute('''
    DROP TABLE Basketball;
''')
    conn.commit()
    conn.close()
    return "Basketball Table Dropped Sucessfully"