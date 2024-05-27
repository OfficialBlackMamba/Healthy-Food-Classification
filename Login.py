import tkinter as tk
from tkinter import messagebox
import pandas as pd
import subprocess

# Function to handle login button click
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "admin":
        messagebox.showinfo("Login Successful", "Welcome to our Product health checker")
        subprocess.Popen(["python", "main.py"])
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.\n\nHint: username and password are both 'admin'")

def register():
    register_window = tk.Toplevel(root)
    register_window.title("Register")

    tk.Label(register_window, text="Name:").grid(row=0, column=0, sticky="e", padx=10, pady=5)
    tk.Label(register_window, text="Username:").grid(row=1, column=0, sticky="e", padx=10, pady=5)
    tk.Label(register_window, text="Password:").grid(row=2, column=0, sticky="e", padx=10, pady=5)
    tk.Label(register_window, text="Date of Birth:").grid(row=3, column=0, sticky="e", padx=10, pady=5)
    tk.Label(register_window, text="City:").grid(row=4, column=0, sticky="e", padx=10, pady=5)

    name_entry = tk.Entry(register_window)
    username_entry = tk.Entry(register_window)
    password_entry = tk.Entry(register_window, show="*")
    dob_entry = tk.Entry(register_window)
    city_entry = tk.Entry(register_window)

    name_entry.grid(row=0, column=1, padx=10, pady=5)
    username_entry.grid(row=1, column=1, padx=10, pady=5)
    password_entry.grid(row=2, column=1, padx=10, pady=5)
    dob_entry.grid(row=3, column=1, padx=10, pady=5)
    city_entry.grid(row=4, column=1, padx=10, pady=5)

    def register_submit():
        name = name_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        dob = dob_entry.get()
        city = city_entry.get()

        data = {'Name': [name], 'Username': [username], 'Password': [password], 'Date of Birth': [dob], 'City': [city]}
        df = pd.DataFrame(data)
        df.to_excel("register_data.xlsx", index=False)

        messagebox.showinfo("Registration Successful", "You have been registered successfully.")
        register_window.destroy()

    # Register submit button
    tk.Button(register_window, text="Register", command=register_submit).grid(row=5, columnspan=2, pady=10)


# Create main window
root = tk.Tk()
root.title("Login")
root.minsize(400, 300)  # Set minimum size

root.configure(bg="#FFD700")  # Shiny yellow color on background

# Create labels and entry fields for login
tk.Label(root, text="Username:", bg="#FFD700").grid(row=0, column=0, sticky="e", padx=10, pady=5)
tk.Label(root, text="Password:", bg="#FFD700").grid(row=1, column=0, sticky="e", padx=10, pady=5)

username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")

username_entry.grid(row=0, column=1, padx=10, pady=5)
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Add Login and Register buttons to the same row without gap
tk.Button(root, text="Login", command=login).grid(row=2, column=0, pady=10)
tk.Button(root, text="Register", command=register).grid(row=2, column=1, pady=10)

# Center all widgets in the main window
for child in root.winfo_children():
    child.grid_configure(padx=10, pady=5)
    
# Copyright text
#copyright_label = tk.Label(root, text="Copyright (c) 2024 Sukhpal Kherera, MCA 2nd Year.", font=("Helvetica", 10), bg="#FFD700", fg="black")
#copyright_label.pack(side=tk.BOTTOM, pady=10)
    

root.mainloop()
