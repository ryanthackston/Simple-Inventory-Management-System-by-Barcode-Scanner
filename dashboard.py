# Running on Python 3.9.5

import tkinter as tk           # Tkinter GUI library # Comes with python
from tkinter import messagebox
from PIL import Image, ImageTk # Pillow library # pip istall pillow
from datetime import datetime
import sqlite3
import pandas as pd
from sqlalchemy import create_engine
from inventory_window import inventoryWindowClass
from checkout_window import checkoutWindowClass
import os

root=tk.Tk()

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.root.title("Inventory Management System for IEEE")
        self.root.config(bg="white")

        # Title
        self.icon_title=tk.PhotoImage(file="Images/IEEE-logo-vector.png")
        title=tk.Label(self.root, 
                        text="Inventory Management System",
                        image=self.icon_title,
                        compound=tk.LEFT,
                        font=("times new roman", 40, "bold"), 
                        bg="#010c48", fg="white", anchor="w", padx=20).place(x=0, y=0, relwidth=1, height=70)
        

        # Logout Button - Closes window
        logoutButton=tk.Button(self.root, 
                               text="Logout", 
                               compound=tk.RIGHT, 
                               command = quit,
                               font=("times new roman", 15, "bold"),
                               bg="red",
                               cursor="hand2").place(x=1175, y=10,height=50,width=150)


        # Clock - Displays Time
        self.labelClock=tk.Label(self.root, 
                        text="Welcome \t\t Date: D-M-Y \t\t Time: HH-MM-SS",
                        font=("times new roman", 15, "bold"), 
                        bg="#4d636d", fg="white")
        self.labelClock.place(x=0, y=70, relwidth=1, height=30)

        def update_datetime():
            current_date = datetime.now().strftime("%d-%m-%Y")
            current_time = datetime.now().strftime("%H:%M:%S")
            self.labelClock.config(text=f"Welcome \t\t " + "Date: " + (current_date) + "\t\t Time: " + (current_time))  
            self.labelClock.after(1000, update_datetime)  # Update time every 1000ms (1 second)
        root.after(1000, update_datetime())
        
        # Left Menu
        self.menuLogo= Image.open("Images/finger_kiss.png")
        self.menuLogo=self.menuLogo.resize((200,150))
        self.menuLogo=ImageTk.PhotoImage(self.menuLogo)
        
        leftMenu = tk.Frame(self.root, bd=2, relief=tk.RIDGE, bg="white")
        leftMenu.place(x=0, y=102, width=200, height=515)

        labelMenuLogo = tk.Label(leftMenu, image=self.menuLogo)
        labelMenuLogo.pack(side=tk.TOP, fill=tk.X)

        self.icon_side = tk.PhotoImage(file="Images/shift-right-flat-icon-vector-8068341.png")

        labelMenu=tk.Label(leftMenu, 
                               text="Menu", 
                               font=("times new roman", 20, "bold"),
                               bg="#009688").pack(side=tk.TOP, fill=tk.X )
        buttonSupplier=tk.Button(leftMenu,
                               text="Supplier", 
                               image=self.icon_side,
                               compound=tk.LEFT,
                               padx=9,
                               anchor="w",
                               font=("times new roman", 20, "bold"),
                               bg="white", 
                               bd=3, 
                               cursor="hand2").pack(side=tk.TOP, fill=tk.X )
        buttonCategory=tk.Button(leftMenu,
                               text="Category", 
                               image=self.icon_side,
                               compound=tk.LEFT,
                               padx=9,
                               anchor="w",
                               font=("times new roman", 20, "bold"),
                               bg="white", 
                               bd=3, 
                               cursor="hand2").pack(side=tk.TOP, fill=tk.X )
        buttonProducts=tk.Button(leftMenu,
                               text="Products", 
                               image=self.icon_side,
                               compound=tk.LEFT,
                               padx=9,
                               anchor="w",
                               font=("times new roman", 20, "bold"),
                               bg="white", 
                               bd=3, 
                               cursor="hand2").pack(side=tk.TOP, fill=tk.X )
        buttonSales=tk.Button(leftMenu,
                               text="Sales", 
                               image=self.icon_side,
                               compound=tk.LEFT,
                               padx=9,
                               anchor="w",
                               font=("times new roman", 20, "bold"),
                               bg="white", 
                               bd=3, 
                               cursor="hand2").pack(side=tk.TOP, fill=tk.X )
        buttonAnalytics=tk.Button(leftMenu,
                               text="Analytics", 
                               image=self.icon_side,
                               compound=tk.LEFT,
                               padx=9,
                               anchor="w",
                               font=("times new roman", 20, "bold"),
                               bg="white", 
                               bd=3, 
                               cursor="hand2").pack(side=tk.TOP, fill=tk.X )
        buttonExit=tk.Button(leftMenu,
                               text="Exit", 
                               image=self.icon_side,
                               compound=tk.LEFT,
                               padx=9,
                               anchor="w",
                               font=("times new roman", 20, "bold"),
                               bg="white", 
                               bd=3, 
                               cursor="hand2").pack(side=tk.TOP, fill=tk.X )
        
        #============================================ 

        def checkout():

            self.root = checkoutWindowClass(self.root)


        def admin():
            pass_window=tk.Tk()
            pass_window.geometry("750x400")
            pass_window.title("Enter The Password To Continue")

            def check_password():
                entered_password = password_entry.get()
                if entered_password == "12345":  # Replace "your_password" with your actual password
                    # If the password is correct, open the next window or perform actions
                    messagebox.showinfo("Success", "Password accepted!")
                    print("Password accepted!")

                    self.root=inventoryWindowClass(self.root)  
                    pass_window.destroy()          
                else:
                    messagebox.showerror("Error", "Incorrect password!")
                    print("Password rejected!")

            # Label
            password_label = tk.Label(pass_window, text="Password: ", font=("times new roman", 14, "bold"), bg="#010c48", fg="white", anchor="w", padx=20)
            password_label.place(x=10, y=10, height=30, width=150)
                    
            password_entry = tk.Entry(pass_window, show="*")  # Entry widget to hide entered characters
            password_entry.place(x=170, y=10, height=30, width=150)

            submit_button = tk.Button(pass_window, text="Submit", command=check_password)
            submit_button.place(x=340, y=10, height=30, width=150)

        # Entry
                
        # Button - check_password()

        #============================================

        # Main Menu
        self.buttonCheckout = tk.Button( self.root, 
                                        text="Checkout Items",
                                        command=checkout,
                                        bd=5, relief=tk.RIDGE, 
                                        bg="#00ff00", fg="black", 
                                        font=("goudy old style", 20, "bold"), 
                                        cursor="hand2")
        self.buttonCheckout.place(x=300, y=120, height=150, width=300)

        self.buttonAdmin = tk.Button( self.root, 
                                        text="Admin Only",
                                        command=admin,
                                        bd=5, relief=tk.RIDGE, 
                                        bg="#7851a9", fg="black", 
                                        font=("goudy old style", 20, "bold"), 
                                        cursor="hand2")
        self.buttonAdmin.place(x=650, y=120, height=150, width=300) 


        def export_to_excel():
            # Connect to the database
            connection = sqlite3.connect("IEEE_Shop.db")
            # write the data into excel file
            engine = create_engine("sqlite:///D:\\Simple-Inventory-Management-System-by-Barcode-Scanner\\IEEE_Shop.db")
            # table_names = insp.get_table_names
            # dataframe
            inventory_df = pd.read_sql("SELECT * FROM inventory", engine)
            transactions_df = pd.read_sql("SELECT * FROM transactions", engine)

            with pd.ExcelWriter('IEEE_Shop.xlsx') as writer:
                inventory_df.to_excel(writer, sheet_name = 'inventory ' + datetime.now().strftime("%d-%m-%Y"))
                transactions_df.to_excel(writer, sheet_name = 'transactions '+ datetime.now().strftime("%d-%m-%Y") )

            connection.commit()
            connection.close()    
            """   # SQL query variable
                SQL = "SELECT * FROM " + sheet_name
                print(SQL)

                # Load data from IEEE_Shop.db into dataframe
                dft = pd.read_sql(SQL, connection)

            print(dft.head(5)) """

        self.buttonCSV = tk.Button( self.root, 
                                        text="Convert To\nExcel",
                                        command = export_to_excel,
                                        bd=5, relief=tk.RIDGE, 
                                        bg="#90ee90", fg="black", 
                                        font=("goudy old style", 20, "bold"), 
                                        cursor="hand2")
        self.buttonCSV.place(x=1000, y=120, height=150, width=300) 



        # Footer - Hide footer button is on very bottom and hides the Footer in all windows
        hideFooter = tk.Button(root, command=lambda: labelFooterlock.pack_forget())
        hideFooter.pack(side=tk.BOTTOM, fill=tk.X)
        labelFooterlock=tk.Label(root, 
                        text="IMS-Inventory Management System | Developed By Ryan Thackston\nFor any Technical Issue Contact ryan.r.thackston@gmail.com",
                        font=("times new roman", 15, "bold"), 
                        bg="#4d636d", fg="white")
        labelFooterlock.pack(side=tk.BOTTOM, fill=tk.X) 


"""     def update_content(self):
        try: 
            current_date = datetime.now().strftime("%d-%m-%Y")
            current_time = datetime.now().strftime("%H:%M:%S")
            self.labelClock.config(text=f"Welcome \t\t " + "Date: " + {str(current_date)} + "\t\t Time: " + {str(current_time)})  
            self.labelClock.after(1000, self.update_content)  # Update time every 1000ms (1 second)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :" + {str(ex)}, parent=self.root)
 """
obj=IMS(root)
root.mainloop()