import sqlite3
import random

def initiate_db():
    connection = sqlite3.connect('products.db')
    c = connection.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Products
                 (id INTEGER PRIMARY KEY, title TEXT NOT NULL, description TEXT, price INTEGER NOT NULL)''')
    connection.commit()
    connection.close()

def get_all_products():
    initiate_db()
    conn = sqlite3.connect('products.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Products")
    rows = c.fetchall()
    conn.close()
    return rows

def add_product(title, description, price):
    initiate_db()
    conn = sqlite3.connect('products.db')
    c = conn.cursor()
    c.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", (title, description, price))
    conn.commit()
    conn.close()



add_product('Product1', 'вавававав', 100)
add_product('Product2', 'вавававав', 200)
add_product('Product3', 'вававамсмываеукп', 300)
add_product('Product4', 'пкумсивпапа', 400)
