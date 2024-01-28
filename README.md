A Simple Database Management System to monitor Inoventory via barcode!

To start using, download the file and Unzip in a folder of your choice.

Use a Python source code editor or IDE and set your workspace to the file you unzipped to (my preferred one is Visual Studio Code)

You will need to use
pip install tkinter, sqlite3, pillow, pandas, SQLAlchemy

This code was made using Python 3.9.5 but any version 3.9 and above should work.

First Run create_db.py . You won't be able to run this again if there is a database with the same name in your folder

Next run dashboard.py . 

This is your main program and you can add/modify/delete inventory by clicking on 'Admin Only' and putting in the password. The default password is 12345.

Customers will use 'Checkout Items' when they are buying. They need to scan each item with the barcode scanner and input the quantity. A calculated price is given and when they pay for the items and they can checkout when they are ready to pay for the items.

The timestamp for when items are added or modified are added to the 'inventory' table and the timestamp for every checkout is added to the 'transactions' table.

-----------
I use DB Browser (SQLite) to look at the the database outside of Excel. While there shouldn't be bugs, this should be a helpful tool in looking at the SQLite tables when trying to change or debug the code.
https://sqlitebrowser.org/

-----------

To take off the Footer message with my name and contact, click the gray area underneath.
