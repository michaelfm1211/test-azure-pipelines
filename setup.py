import psycopg2 as sql
from psycopg2.extras import DictCursor
from hashlib import sha3_256
from os import environ

conn = sql.connect(environ['DATABASE_URL'])
cur = conn.cursor()

try:
    print("Creating Data Table")
    cur.execute('CREATE TABLE data (key TEXT NOT NULL, value TEXT NOT NULL)')
    conn.commit()
except:
    print('Table Already Exists')
conn.close()

conn = sql.connect(environ['DATABASE_URL'])
cur = conn.cursor()

cur.execute(
    "INSERT INTO data (key, value) VALUES ('value', 'hi')")
conn.commit()

conn.close()
