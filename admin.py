import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import sqlite3

class adminClass:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("IEEE Execs Only")
        self.root.config(bg="white")

        # Title
        self.icon_title=tk.PhotoImage(file="Images/IEEE-logo-vector.png")
        title=tk.Label(self.root, 
                        text="ADMIN ONLY",
                        image=self.icon_title,
                        compound=tk.LEFT,
                        font=("times new roman", 40, "bold"), 
                        bg="#010c48", fg="white", anchor="w", padx=20).place(x=0, y=0, relwidth=1, height=70)
        
        # Logout Button  
        logoutButton=tk.Button(self.root, 
                               text="Logout", 
                               compound=tk.RIGHT, 
                               font=("times new roman", 15, "bold"),
                               bg="red",
                               cursor="hand2").place(x=1175, y=10,height=50,width=150)
        
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

        # Content
        self.buttonAddItems = tk.Button(self.root, 
                                        text="Add Items To\nThe Database",
                                        bd=5, relief=tk.RIDGE, 
                                        bg="#00ff00", fg="black", 
                                        font=("goudy old style", 20, "bold"), 
                                        cursor="hand2")
        self.buttonAddItems.place(x=300, y=120, height=150, width=300)

        self.buttonCheckIn = tk.Button( self.root, 
                                        text="Check-In\nItems",
                                        bd=5, relief=tk.RIDGE, 
                                        bg="#7851a9", fg="black", 
                                        font=("goudy old style", 20, "bold"), 
                                        cursor="hand2")
        self.buttonCheckIn.place(x=650, y=120, height=150, width=300)  


        # Footer
        labelFooterlock=tk.Label(self.root, 
                        text="IMS-Inventory Management System | Developed By Ryan Thackston\nFor any Technical Issue Contact ryan.r.thackston@gmail.com",
                        font=("times new roman", 15, "bold"), 
                        bg="#4d636d", fg="white").pack(side=tk.BOTTOM, fill=tk.X)

if __name__=="__main__":
    root=tk.Tk()
    obj=adminClass(root)
    root.mainloop()
