import tkinter as tk
from tkinter import ttk
#from tkinter import Text, Scrollbar, Canvas, Frame
import sqlite3
from   datetime import datetime
import time

class checkoutWindowClass:
    # Initializing the checkout window
    def __init__(self, checkout):
        self.checkout = checkout
        # Pixel size of the main window is 700 x 550 pixels
        self.checkout.geometry("700x550")
        # Top title of the window is "Checkout "
        self.checkout.title("Checkout Window")

         # Create a frame around the window (think like a picture frame)
        main_frame = tk.Frame(checkout)
        main_frame.pack(fill=tk.BOTH, expand=1)

        # Create A Canvas for Scrollbar
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
        # All buttons and labels in the window go inside the canvas
        my_canvas.create_window((0,0), window=second_frame, anchor="nw")

        # Adds space to the labels and buttons
        space_row_1 = tk.Label(second_frame, text=' ', font=('Times New Roman', 40))
        space_row_1.grid(row=1, column=4, pady=0)

        # Adds space to the labels and buttons
        space_label = tk.Label(second_frame, text='  ', font=('Times New Roman', 10))
        space_label.grid(row=2, column=4, pady=0)

        # Barcode box Label
        item_barcode_label = tk.Label(second_frame, text='Barcode ')
        item_barcode_label.grid(row=3, column=4, padx=(10,0))

        # Barcode box entry
        item_barcode3 = tk.Entry(second_frame, width=20)
        item_barcode3.grid(row=4, column=4, padx=(10,0))

        # Quantity box label
        item_quantity_label = tk.Label(second_frame, text='Quantity ')
        item_quantity_label.grid(row=3, column=4, padx=(275,0) )

        # Quantity box entry
        item_quantity = tk.Entry(second_frame, width=20)
        item_quantity.grid(row=4, column=4, padx=(275,0))

        # initialize Treeview in the second_frame to act as the cart checkout list.
        my_tree = ttk.Treeview(second_frame)

        # Define Our Columns for the checkout list
        my_tree['columns'] = ("Name", "Price", "Quantity", "Barcode")

        # Format Our Columns for Treeview List - #0 is a phantom column
        my_tree.column("#0", width=0, stretch=tk.NO)
        my_tree.column("Name", anchor=tk.CENTER, width=120)
        my_tree.column("Price", anchor=tk.CENTER, width = 120)
        my_tree.column("Quantity", anchor=tk.CENTER, width=120)
        my_tree.column("Barcode", anchor=tk.CENTER, width=120)

        # Create Headings for the columns, text is actually the name of the columns that is seen.
        my_tree.heading("#0", text="")
        my_tree.heading("Name", text="Item Name", anchor=tk.CENTER)
        my_tree.heading("Price", text="Price ($)", anchor=tk.CENTER)
        my_tree.heading("Quantity", text="Quantity", anchor=tk.CENTER)
        my_tree.heading("Barcode", text="Barcode", anchor=tk.CENTER)

        # Adding space next to Treeview grid to even it out on the window
        space_tree = tk.Label(second_frame, text='     ', font=('Times New Roman', 40))
        space_tree.grid(row=6, column=1, columnspan=2, pady=4)
        my_tree.grid(row=6, column=4, columnspan = 9, pady=20, padx=(30, 0), sticky=tk.E)

        # Function - Match barcode and quantity with items already in inventory, if barcode doesn't match or quantity is too low, return an error
        def checkInventory():
            
            # barcode is the barcode number in the Barcode entry box, the identifying ID for items will be by barcode
            barcode = item_barcode3.get()
            quantity = item_quantity.get()

           # If nothing is input for barcode or quantity, throw an error message, no value become 0
            if (len(barcode) == 0) or (len(quantity) <= 0):
                
                # Erase over any label that was on the bottom row previously
                eraseLabel = tk.Label(second_frame, text = "                                                                                 ")
                eraseLabel.grid(row=13, column=4, padx = (150,0), pady=4)

                # Error message
                errorLabel = tk.Label(second_frame, text = "Barcode and quantity cannot be empty.")
                errorLabel.grid(row=13, column=4, padx = (150,0), pady=4)

            else:
                try: 
                    # Open connection to IEEE_Shop database in the same folder as the workspace
                    connection = sqlite3.connect("IEEE_Shop.db")
                    cursor = connection.cursor()
                    # Check if there is matching barcode and quantity in the inventory table and that quantity is > 0
                    cursor.execute("SELECT * FROM inventory WHERE barcode = ? AND quantity >= ? AND ? > 0 ", (barcode, quantity, quantity))

                    # records - fetches all matching information from the inventory table by barcode and quantity
                    records = cursor.fetchall()
                    # commits the commands to the SQLite Database
                    connection.commit()
                    # Closes the connection to the SQLite database
                    connection.close()

                     # In the inventory databse, if there is no matching barcode or the quantity is 0 and under, pull an error message
                    if len(records) == 0:
                        print("Error: Invalid barcode or quantity.")
                        return []
                    else:
                        # Erase over any label that was on the bottom row previously
                        eraseLabel = tk.Label(second_frame, text = "                                                                                 ")
                        eraseLabel.grid(row=13, column=4, padx = (150,0), pady=4)

                        # Success message
                        successLabel = tk.Label(second_frame, text = "Successfully checked item in the inventory.")
                        successLabel.grid(row=13, column=4, padx = (150,0), pady=4)
                        # print("Successfully checked item in the inventory.")
                        print(records)
                        return records

                except sqlite3.Error as e:

                    # Erase over any label that was on the bottom row previously
                    eraseLabel = tk.Label(second_frame, text = "                                                                                 ")
                    eraseLabel.grid(row=13, column=4, padx = (150,0), pady=4)

                    # Success message
                    errorLabel = tk.Label(second_frame, text = "Wrong Barcode or quantity is too high: " + e)
                    errorLabel.grid(row=13, column=4, padx = (150,0), pady=4)
                    # print("Wrong Barcode or quantity is too high", e)
                    return []

        

        # Function - checks if there is matching items and quantity in inventory and if so, adds to the Treeview checkout list.
        def buyList():

            # listTup is type List & Tuple - [(Str, Str, Float, Int, Str, Str, Str)] - Ex: to call on Float value (the price) listTup[0][2].
            listTup = checkInventory()  # Check inventory will return records or empty list [] if there is no matching records

            # If there is nothing in the list, then nothing came up when checkInventory() function was called and len(listTup) == 0
            if len(listTup) == 0:
                eraseLabel = tk.Label(second_frame, text = "                                                                                 ")
                eraseLabel.grid(row=13, column=4, padx = (150,0), pady=4)

                errorLabel = tk.Label(second_frame, text = "Error: There's no matching item in inventory")
                errorLabel.grid(row=13, column=4, padx = (150,0), pady=4)
            else:
                         
                # Checks if there are already existing my_tree iid entries and deletes the previous one.
                if my_tree.exists(item_barcode3.get()):
                    my_tree.delete(item_barcode3.get())

                # If there is no previous value, skip to inserting the value into the Treeview checkout list
                else:
                    pass

                # Add to Treeview
                # barcode, name, price, quantity, category, supplier, last-check-in 
                # insert entry into Treeview list with identifying id (iid) as the barcode entry
                my_tree.insert(parent='', index='end', iid=str(item_barcode3.get()), text="", values = (listTup[0][1], listTup[0][2], item_quantity.get(), str(listTup[0][0])) )
                
                # Clear the Barcode and Quantity boxes after 'Add To List' button is clicked
                item_barcode3.delete(0, tk.END)
                item_quantity.delete(0, tk.END)
                
        # Button - Add Item to Cart List using buyList() function
        addToList = tk.Button(second_frame, text='Add To List', command = buyList)
        addToList.grid(row=4, column=7, pady=4, sticky=tk.W)

        # Function - Removes selected items in checkout 
        def remove_selected():
            # x = my_tree.selection()
            # for record in x:
            #     my_tree.delete(record)
            list(map(lambda x: my_tree.delete(x), my_tree.selection()))
            # [my_tree.delete(x) for x in my_tree.selection()]

        # Remove Items Button - Removes selected items in checkout - hold CTRL and click items you want removed in any order, the click 'Remove Items' button
        # Button uses remove_selected() function
        removeItems = tk.Button(second_frame, text="Remove Items", command=remove_selected)
        removeItems.grid(row=8, column=4, padx = (150,0), pady=4)

        # Function - Calculates the total in the cart checkout
        def calcTotal():

            # Initialize price at $0
            price = 0

            # Imperatively calculate item prices in for loop
            # For all items in the Treeview checkout list
            for item in my_tree.get_children():
                # Get item info
                item_info = my_tree.item(item)
                # Get item quanity
                quantity = item_info['values'][2]
                # Price is updated to that specific item in the list multiplied by the quantity
                price += float(item_info['values'][1]) * quantity

            # Erase over any label that was on the bottom row previously
            eraseLabel = tk.Label(second_frame, text = "                                                                                 ")
            eraseLabel.grid(row=13, column=4, padx = (150,0), pady=4)

            # Label the price on the bottom of the screen
            totalLabel = tk.Label(second_frame, text = "Your total is: $" + str(price))
            totalLabel.grid(row=13, column=4, padx = (150,0), pady=4)

        # Button for calculating the total price of the item using calcTotal()
        calcTotalButton = tk.Button(second_frame, text='Calculate Total', command=calcTotal)
        calcTotalButton.grid(row=9, column=4,  padx = (150,0), pady=4)

        def checkoutFinal():
            for item in my_tree.get_children():
                
                item_info = my_tree.item(item)

                iid = item
                is_iid = my_tree.exists(iid)
                print ("iid = ", iid, "Quantity = ", item_info['values'][2])
                print(is_iid)

                connection = sqlite3.connect("IEEE_Shop.db")
                cursor = connection.cursor()

                # Select items by Barcode which is being used as the IID  
                cursor.execute("SELECT quantity FROM inventory WHERE barcode = ?",(iid,))
                currentQuantity = (cursor.fetchall())[0][0]

                boughtQuantity = item_info['values'][2]

                # Subtract the current quantity from the quantity the user is taking
                updatedQuantity = currentQuantity - boughtQuantity

                # Update the quantity in inventory after checkout 
                cursor.execute("UPDATE inventory SET quantity = ? WHERE barcode = ?" , (updatedQuantity, iid,))

                # Insert values into the transactions table 
                cursor.execute("""INSERT INTO transactions(barcode, name, price, quantity, category, supplier, timestamp)
                                SELECT barcode, name, price, quantity, category, supplier, timestamp
                                FROM inventory
                                WHERE barcode = ?""", (iid,) )

                # Add a timestamp to each transaction of items
                cursor.execute("""UPDATE transactions SET
                                quantity = ?,
                                timestamp = ?
                               
                                WHERE ROWID IN ( SELECT max( ROWID ) FROM transactions ) """, 
                                (boughtQuantity, 
                                (datetime.now().strftime("%d-%m-%Y %H:%M:%S")), ) )
                
                # commits the commands to the SQLite Database
                connection.commit()

                # Closes the connection to the SQLite database
                connection.close()

                my_tree.delete(item)

            eraseLabel = tk.Label(second_frame, text = "                                                                                 ")
            eraseLabel.grid(row=13, column=4, padx = (150,0), pady=4)

            successLabel = tk.Label(second_frame, text = "Item(s) successfully checked out")
            successLabel.grid(row=13, column=4, padx = (150,0), pady=4)

            time.sleep(3)
            checkout.destroy()


                
        # Button - uses checkoutFinal() function to 
        checkoutButton = tk.Button(second_frame, text='Checkout', command=checkoutFinal)
        checkoutButton.grid(row=10, column=4, padx = (150,0), pady=4)

if __name__=="__main__":
    checkout=tk.Tk()
    obj=checkoutWindowClass(checkout)
    checkout.mainloop()