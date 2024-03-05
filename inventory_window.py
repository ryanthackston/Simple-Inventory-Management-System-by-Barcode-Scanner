import tkinter as tk
from tkinter import ttk
import sqlite3
from   datetime import datetime

class inventoryWindowClass:

# Main Window 
    def __init__(self, root):
        self.root = root
        self.root.geometry("550x450")
        self.root.title("Inventory Summary")

        ##############################################################################
        # VERTICAL SCROLL BAR - ADJUST WINDOW SIZE WHILE RUNNING TO ACTIVATE SCROLLBAR
        ##############################################################################

        # Create A Main Frame
        main_frame = tk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=1)

        # Create A CAnvas
        my_canvas= tk.Canvas(main_frame)
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        # Add a Scrollbar to the Canvas
        my_scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the Canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        # Create another frame inside the Canvas
        second_frame = tk.Frame(my_canvas)

        # Add That New frame To A Window In The Canvas
        my_canvas.create_window((0,0), window=second_frame, anchor="nw")

        ########################################################
        # Add Record to the database
        ########################################################

        space_row_1 = tk.Label(second_frame, text=' ', font=('Times New Roman', 7))
        space_row_1.grid(row=1, column=4, pady=0)

        item_barcode = tk.Entry(second_frame, width=20)
        item_barcode.grid(row=2, column=1, pady=1, sticky=tk.W)

        item_name = tk.Entry(second_frame, width=20)
        item_name.grid(row=3, column=1, pady=1, sticky=tk.W)

        item_price = tk.Entry(second_frame, width=20)
        item_price.grid(row=4, column=1, pady=1, sticky=tk.W)

        item_quantity = tk.Entry(second_frame, width=20)
        item_quantity.grid(row=5, column=1, pady=1, sticky=tk.W)

        item_category = tk.Entry(second_frame, width=20)
        item_category.grid(row=6, column=1, pady=1, sticky=tk.W) 

        item_supplier = tk.Entry(second_frame, width=20)
        item_supplier.grid(row=7, column=1, pady=1, sticky=tk.W) 

        #item_last_check_in = tk.Entry(second_frame, width=20)
        #item_last_check_in.grid(row=6, column=1, pady=2, sticky=tk.W)                 

        item_barcode_label = tk.Label(second_frame, text='Barcode ')
        item_barcode_label.grid(row=2, column=0, pady=1, sticky=tk.E)
        item_name_label = tk.Label(second_frame, text='Name ')
        item_name_label.grid(row=3, column=0, pady=1, sticky=tk.E)
        item_price_label = tk.Label(second_frame, text ='Price ($) ')
        item_price_label.grid(row=4,column=0, pady=1, sticky=tk.E)
        item_quantity_label = tk.Label(second_frame,  text='Quantity ')
        item_quantity_label.grid(row=5, column=0, pady=1, sticky=tk.E)
        item_category_label = tk.Label(second_frame,  text='Category ')
        item_category_label.grid(row=6, column=0, pady=1, sticky=tk.E)
        item_supplier_label = tk.Label(second_frame,  text='Supplier ')
        item_supplier_label.grid(row=7, column=0, pady=1, sticky=tk.E)        
        item_last_check_in_label = tk.Label(second_frame,  text='Last Check-In ')
        item_last_check_in_label.grid(row=8, column=0, pady=1, sticky=tk.E)

        # Error Label for a duplicate value
        error_label = tk.Label(second_frame,  text='')
        error_label.grid(row=18, column=0, pady=2, sticky=tk.E)


        # Submit - Adds new barcodes to the database
        def submit():
            connection = sqlite3.connect("IEEE_Shop.db")
            cursor = connection.cursor()
            try: 
                cursor.execute( """SELECT COUNT(*) AS occurrence_count 
                                FROM inventory 
                                WHERE barcode = ?""",(item_barcode.get(),))
                result = cursor.fetchone()

                # Handle the result
                occurrence_count = result[0]
                if occurrence_count >= 1:
                    error_label.config(text="Error: Duplicate value found.")
                else:
                    cursor.execute("""INSERT INTO 
                                    inventory(barcode,name,price,quantity,category, supplier, last_check_in)
                                    VALUES (?,?,?,?,?,?,?)""",
                                    (item_barcode.get(), 
                                    item_name.get(), 
                                    item_price.get(), 
                                    item_quantity.get(), 
                                    item_category.get(), 
                                    item_supplier.get(), 
                                    (datetime.now().strftime("%d-%m-%Y %H:%M:%S"))))
                    print("Command executed successfully...")

            except:
                cursor.execute("""INSERT INTO 
                                    inventory(barcode,name,price,quantity,category, supplier, last_check_in)
                                    VALUES (?,?,?,?,?,?,?)""",
                                    (item_barcode.get(), 
                                    item_name.get(), 
                                    item_price.get(), 
                                    item_quantity.get(), 
                                    item_category.get(), 
                                    item_supplier.get(), 
                                    (datetime.now().strftime("%d-%m-%Y %H:%M:%S"))))
                print("Command executed successfully...")


       #     SELECT COUNT(*) as occurrence_count
       #     FROM inventory
       #     WHERE barcode = 'YourValueToCheck';

            # If barcode is same as an item in the database, return an error message.
            connection.commit()
            connection.close()
           # item_name.delete(0, tk.END)
           # item_quantity.delete(0, tk.END)
           # item_price.delete(0, tk.END)

        submit_btn = tk.Button(second_frame, text="Add Record to Database", command=submit)
        submit_btn.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx = 33)

# TO DO - WHEN Adding a Record to Database | Deleting, Updating, restart the window

        # Show Records - Shows all records in the database
        def query():
            connection = sqlite3.connect("IEEE_Shop.db")
            cursor = connection.cursor()
            cursor.execute("SELECT *, oid FROM inventory")
            records = cursor.fetchall()
            print(records)
            print_records = ''
            for record in records:
                print_records += "Barcode: " + str(record[0]) + ", " + "Name: " + str(record[1]) + ", $" + str(record[2]) + ", Quantity: " + str(record[3]) + ", Last Check-In: " + str(record[6]) +"\n"
            query_label = tk.Label(second_frame, text=print_records)
            query_label.grid(row=12, column=0, columnspan=2)
            connection.commit()
            connection.close()

        query_btn = tk.Button(second_frame, text="Show Records", command=query)
        query_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=60)

        # Create a Barcode text box for deleting or editing inventory by barcode.
        global item_barcode2
        item_barcode2 = tk.Entry(second_frame, width=20)
        item_barcode2.grid(row=13, column=1, pady=10, sticky=tk.W) 
        item_barcode2_label = tk.Label(second_frame, text='Select Barcode')
        item_barcode2_label.grid(row=13, column=0, pady=10, sticky=tk.E)

        def update():
            connection = sqlite3.connect("IEEE_Shop.db")
            cursor = connection.cursor()
            record_id = item_barcode2.get()

            cursor.execute(
                """ UPDATE inventory SET
                    name = :name,
                    price = :price, 
                    quantity = :quantity, 
                    category = :category, 
                    supplier = :supplier, 
                    last_check_in = :last_check_in

                    WHERE barcode = :barcode""",
                 {
                    'name': item_name_editor.get(),
                    'price': item_price_editor.get(),
                    'quantity': item_quantity_editor.get(),
                    'category': item_category_editor.get(),
                    'supplier': item_supplier_editor.get(),
                    'last_check_in':(datetime.now().strftime("%d-%m-%Y %H:%M:%S")),

                    'barcode': record_id})
            print("Sucessfully updated inventory")
            
            connection.commit()
            connection.close()
            
        # Edit the Inventory - Open up an editable SQLite inventory sheet
                
        # Create Edit Function to update inventory
        def edit():
            editor = tk.Tk()
            editor.geometry("750x400")
            editor.title("Edit Inventory")

            connection = sqlite3.connect("IEEE_Shop.db")
            cursor = connection.cursor()

            record_id = item_barcode2.get()
            cursor.execute("SELECT * FROM inventory WHERE barcode = " + record_id)
            records = cursor.fetchall()

            # Create global variables for text box names
            global item_name_editor
            global item_price_editor
            global item_quantity_editor
            global item_category_editor
            global item_supplier_editor
            global item_last_check_in_editor

            # Create Text Boxes
            item_barcode_editor = tk.Entry(editor, width=20)
            item_barcode_editor.grid(row=0, column=1, sticky=tk.W)
            item_name_editor = tk.Entry(editor, width=20)
            item_name_editor.grid(row=1, column=1, sticky=tk.W)
            item_price_editor = tk.Entry(editor, width=20)
            item_price_editor.grid(row=2, column=1, sticky=tk.W)
            item_quantity_editor = tk.Entry(editor, width=20)
            item_quantity_editor.grid(row=3, column=1, sticky=tk.W)
            item_category_editor = tk.Entry(editor, width=20)
            item_category_editor.grid(row=4, column=1, sticky=tk.W)
            item_supplier_editor = tk.Entry(editor, width=20)
            item_supplier_editor.grid(row=5, column=1, sticky=tk.W)
            item_last_check_in_editor = tk.Entry(editor, width=20, state=tk.DISABLED)
            item_last_check_in_editor.grid(row=6, column=1, sticky=tk.W)                                    

            # Create Text Box Labels  
            item_barcode_label = tk.Label(editor, text='Barcode ')
            item_barcode_label.grid(row=0, column=0, sticky=tk.E)
            item_name_label = tk.Label(editor, text='Name ')
            item_name_label.grid(row=1, column=0, sticky=tk.E)
            item_price_label = tk.Label(editor, text ='Price ($) ')
            item_price_label.grid(row=2,column=0, sticky=tk.E) 
            item_quantity_label = tk.Label(editor,  text='Quantity ')
            item_quantity_label.grid(row=3, column=0, sticky=tk.E)
            item_category_label = tk.Label(editor, text ='Category ')
            item_category_label.grid(row=4,column=0, sticky=tk.E)
            item_supplier_label = tk.Label(editor, text ='Supplier ')
            item_supplier_label.grid(row=5,column=0, sticky=tk.E)
            item_last_check_in_label = tk.Label(editor, text ='Last Check-In ')
            item_last_check_in_label.grid(row=6,column=0, sticky=tk.E)

            # Loop through results
            for record in records:
                item_barcode_editor.insert(0, record[0])
                item_name_editor.insert(0, record[1])
                item_price_editor.insert(0, record[2])
                item_quantity_editor.insert(0, record[3])
                item_category_editor.insert(0, record[4])
                item_supplier_editor.insert(0, record[5])
                item_last_check_in_editor.insert(0, record[6])

            # Create a Save button to save edited record
            edit_btn = tk.Button(editor, text="Save Record", command=update)
            edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=80)
            connection.commit()
            connection.close()

        edit_btn = tk.Button(second_frame, text="Edit Inventory By Barcode", command=edit)
        edit_btn.grid(row=14, column=0, columnspan=2, pady=10, padx=10, ipadx=30)

        # edit_btn = tk.Button(self.second_frame, text="Edit Inventory", command=edit)
        # edit_btn.grid(row=12, column=0, columnspan=2, pady=2)

        # Delete Inventory by Barcode

        def delete():
            barcode_var = item_barcode2.get()
            # Input validation
            if not barcode_var:
                print("Barcode cannot be empty.")
                return
            try: 
                connection = sqlite3.connect('IEEE_Shop.db')
                cursor = connection.cursor()
                cursor.execute('DELETE FROM inventory WHERE barcode=?',(barcode_var, ))
                print("Sucessfully deleted " + str(barcode_var) )
                connection.commit()
                connection.close()

            except sqlite3.Error as e:
                print("Error deleting record:", e)

        delete_btn = tk.Button(second_frame, text="Delete by Barcode", command=delete)
        delete_btn.grid(row=15, column=0, columnspan=2, pady=10, padx=10, ipadx=48)
    

if __name__=="__main__":
    root=tk.Tk()
    obj=inventoryWindowClass(root)
    root.mainloop()