import sqlite3
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
                   last_check_in TEXT)
                   """ )
    print("Table created successfully")
    conn.commit()
    conn.close()
create_db()

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
                   last_check_in TEXT)
                   """ )
    print("Table created successfully")
    conn.commit()
    conn.close()

create_transactions_table()