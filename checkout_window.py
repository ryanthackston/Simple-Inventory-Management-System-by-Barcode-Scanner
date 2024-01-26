import tkinter as tk
from tkinter import ttk
#from tkinter import Text, Scrollbar, Canvas, Frame
import sqlite3
from   datetime import datetime

class checkoutWindowClass:

# Main Window
    def __init__(self, root):
        self.root = root
        self.root.geometry("700x550")
        self.root.title("Checkout Window")

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


        # Add Record to the database

        space_row_1 = tk.Label(second_frame, text=' ', font=('Times New Roman', 40))
        space_row_1.grid(row=1, column=4, pady=0)

        space_label = tk.Label(second_frame, text='  ', font=('Times New Roman', 10))
        space_label.grid(row=2, column=4, pady=0)

       # space_entry = tk.Label(second_frame, text='       ', font=('Times New Roman', 10))
        #space_entry.grid(row=4, column=5, pady=0)

        item_barcode_label = tk.Label(second_frame, text='Barcode ')
        item_barcode_label.grid(row=3, column=4, padx=(10,0))

        item_barcode3 = tk.Entry(second_frame, width=20)
        item_barcode3.grid(row=4, column=4, padx=(10,0))

        item_quantity_label = tk.Label(second_frame, text='Quantity ')
        item_quantity_label.grid(row=3, column=4, padx=(275,0) )

        item_quantity = tk.Entry(second_frame, width=20)
        item_quantity.grid(row=4, column=4, padx=(275,0))

        my_tree = ttk.Treeview(second_frame)

        # Define Our Columns
        my_tree['columns'] = ("Name", "Price", "Quantity", "Barcode")

        # Format Our Columns for Treeview List - #0 is a phantom column
        my_tree.column("#0", width=0, stretch=tk.NO)
        my_tree.column("Name", anchor=tk.CENTER, width=120)
        my_tree.column("Price", anchor=tk.CENTER, width = 120)
        my_tree.column("Quantity", anchor=tk.CENTER, width=120)
        my_tree.column("Barcode", anchor=tk.CENTER, width=120)

        # Create Headings
        my_tree.heading("#0", text="")
        my_tree.heading("Name", text="Item Name", anchor=tk.CENTER)
        my_tree.heading("Price", text="Price ($)", anchor=tk.CENTER)
        my_tree.heading("Quantity", text="Quantity", anchor=tk.CENTER)
        my_tree.heading("Barcode", text="Barcode", anchor=tk.CENTER)

        # Add Data
        # my_tree.insert(parent='', index='end', iid=0, text="", values=("Doritos", 2.50, 3, 1432586790))
        space_tree = tk.Label(second_frame, text='     ', font=('Times New Roman', 40))
        space_tree.grid(row=6, column=1, columnspan=2, pady=4)
        my_tree.grid(row=6, column=4, columnspan = 9, pady=20, padx=(30, 0), sticky=tk.E)

        # Match barcode and quantity with items already in inventory
        def checkInventory():
            # Check with try / except
            record_id = item_barcode3.get()
            checkout_amount = item_quantity.get()

            # Label on GUI later
            if (len(item_barcode3.get()) == 0) or (len(item_quantity.get()) == 0):
                print("Barcode and quantity cannot be empty.")
            else:
                try: 
                    connection = sqlite3.connect("IEEE_Shop.db")
                    cursor = connection.cursor()
                    cursor.execute("SELECT * FROM inventory WHERE barcode = ? AND quantity >= ? AND ? > 0 ", (record_id, checkout_amount, checkout_amount))
                    # Returns an empty string if there's nothing there
                    records = cursor.fetchall()
                    connection.commit()
                    connection.close()

                    if len(records) == 0:
                        print("Error: Invalid barcode or quantity.")
                        return []
                    else:
                        print("Successfully checked item in the inventory.")
                        print(records)
                        return records
                    # print(records)

                    

                except sqlite3.Error as e:
                    print("Wrong Barcode or quantity is too high", e)
                    return []

        

        def buyList():
            # records is type List & Tuple - [(Str, Str, Float, Int, Str, Str, Str)]
            listTup = checkInventory()  # Check inventory will return records or []
            rec = listTup[0]
            if len(rec) == 0:
                print ("Error: There's no matching item in inventory")
            else:
                # Add to Treeview
                # barcode, name, price, quantity, category, supplier, last-check-in           

                # Checks if there are already existing my_tree iid entries and deletes the previous one.
                if my_tree.exists(item_barcode3.get()):
                    my_tree.delete(item_barcode3.get())
                else:
                    pass
                # insert entry into Treeview list with identifying id as the barcode entry
                my_tree.insert(parent='', index='end', iid=item_barcode3.get(), text="", values = (rec[1], rec[2], item_quantity.get(), rec[0]) )
                
                # TO DO - Show on GUI
                print("Successfully added entry to checkout list")
                

        addToList = tk.Button(second_frame, text='Add To List', command = buyList)
        addToList.grid(row=4, column=7, pady=4, sticky=tk.W)
        
        def calcTotal():
            price = 0
            for item in my_tree.get_children():
                item_info = my_tree.item(item)
                quantity = item_info['values'][2]
                price += float(item_info['values'][1]) * quantity
            """ for item in my_tree.get_children():
                item_total = my_tree.item(item)
                price = item_total['values'][3]
                is_iid = my_tree.exists(iid)
                print ("iid = ", iid, "Quantity = ", item_total['values'][2])
                print(is_iid) """

            totalLabel = tk.Label(second_frame, text = "Your total is: $" + str(price))
            totalLabel.grid(row=13, column=4, padx = (250,0), pady=4)
            pass

        

        calcTotalButton = tk.Button(second_frame, text='Calculate Total', command=calcTotal)
        calcTotalButton.grid(row=9, column=4,  padx = (150,0), pady=4)
        
        # space_row_9 = tk.Label(second_frame, text='                          ')
        # space_row_9.grid(row=9, column=4, pady=4, padx = 0)

        def checkoutFinal():
            for item in my_tree.get_children():
                item_info = my_tree.item(item)
                iid = item_info['values'][3]
                is_iid = my_tree.exists(iid)
                print ("iid = ", iid, "Quantity = ", item_info['values'][2])
                print(is_iid)

                # subtract from Inventory table by iid and quantity
                connection = sqlite3.connect("IEEE_Shop.db")
                cursor = connection.cursor()
                cursor.execute("SELECT quantity FROM inventory WHERE barcode = ?",(iid,))
                currentQuantity = (cursor.fetchall())[0][0]

                boughtQuantity = item_info['values'][2]
                #Subtract the current quantity from the quantity the user is taking
                updatedQuantity = currentQuantity - boughtQuantity
                #print ("updated quantity is ", updatedQuantity)

                #Update the quantity
                cursor.execute("UPDATE inventory SET quantity = ? WHERE barcode = ?" , (updatedQuantity, iid,))


                cursor.execute("""INSERT INTO transactions(barcode, name, price, quantity, category, supplier, last_check_in)
                                SELECT barcode, name, price, quantity, category, supplier, last_check_in
                                FROM inventory
                                WHERE barcode = ?""", (iid,) )

# BUG IN CODE - NEED TO ORDER BY OTHER THAN BARCODE FOR DIFFERENT TIMES
                cursor.execute("""UPDATE transactions SET
                                quantity = ?,
                                last_check_in = ?
                               
                                WHERE ROWID IN ( SELECT max( ROWID ) FROM transactions ) """, 
                                (boughtQuantity, 
                                (datetime.now().strftime("%d-%m-%Y %H:%M:%S")), ) )
                
#                cursor.execute("""UPDATE transactions
#                                    SET
#                                        name = (SELECT inventory.name FROM inventory),
#                                        price = (SELECT inventory.name FROM inventory)   
#                                        quantity = ?,
#
#                                    WHERE
 #                                       EXISTS (SELECT * FROM inventory WHERE barcode ?)""", (boughtQuantity, iid)
                
                connection.commit()
                connection.close()
                

        checkoutButton = tk.Button(second_frame, text='Checkout', command=checkoutFinal)
        checkoutButton.grid(row=10, column=4, padx = (150,0), pady=4)

if __name__=="__main__":
    root=tk.Tk()
    obj=checkoutWindowClass(root)
    root.mainloop()