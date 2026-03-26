import requests
import mysql.connector
import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("App")
tk.Label(root, text="Title").pack()
entry_id = tk.Entry(root)
entry_id.pack()


root.mainloop()
