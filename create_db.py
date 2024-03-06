import sqlite3

# Create Database if there's no database starting with inventory table
def create_db():
    conn=sqlite3.connect(database=r'IEEE_Shop.db')
    cursor=conn.cursor()
    cursor.execute("""CREATE TABLE inventory (
                   barcode TEXT, 
                   name TEXT, 
                   price REAL,
                   quantity INTEGER, 
                   category TEXT, 
                   supplier TEXT, 
                   timestamp TEXT)
                   """ )
    print("Table created successfully")
    conn.commit()
    conn.close()
create_db()

# Create the transactions table in the IEEE_Shop database
def create_transactions_table():
    conn=sqlite3.connect(database='IEEE_Shop.db')
    cursor=conn.cursor()
    cursor.execute("""CREATE TABLE transactions (
                   barcode TEXT, 
                   name TEXT, 
                   price REAL,
                   quantity INTEGER, 
                   category TEXT, 
                   supplier TEXT, 
                   timestamp TEXT)
                   """ )
    print("Table created successfully")
    conn.commit()
    conn.close()

create_transactions_table()