import sqlite3

conn = sqlite3.connect('books.sqlite')

# python db.py //run
cursor = conn.cursor()
sql_query = """ CREATE TABLE book (
id integer PRIMARY KEY,
author text NOT NULL,
language text NOT NULL,
title text NOT NULL
)"""

