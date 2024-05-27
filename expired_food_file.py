import tkinter as tk
from tkinter import messagebox
import pandas as pd

def save_data(data, filename):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    messagebox.showinfo("Data Saved", "Data saved successfully!")

def expired_food_entry():
    def save_expired_food_data():
        name = name_entry.get()
        food_type = food_type_var.get()
        expiry_date = expiry_date_entry.get()
        days_past_expiry = days_past_expiry_entry.get()

        data = {
            'Food Name': [name],
            'Food Type': [food_type],
            'Expiry Date': [expiry_date],
            'Days Past Expiry': [days_past_expiry]
        }
        save_data(data, "expired_food_data.xlsx")

    expired_food_window = tk.Toplevel()
    expired_food_window.title("Expired Food Entry")

    tk.Label(expired_food_window, text="Food Name:").grid(row=0, column=0)
    tk.Label(expired_food_window, text="Food Type:").grid(row=1, column=0)
    tk.Label(expired_food_window, text="Expiry Date:").grid(row=2, column=0)
    tk.Label(expired_food_window, text="Days Past Expiry:").grid(row=3, column=0)

    name_entry = tk.Entry(expired_food_window)
    name_entry.grid(row=0, column=1)

    food_type_var = tk.StringVar()
    food_type_options = ["Package", "Unpackage", "Fruit"]
    food_type_dropdown = tk.OptionMenu(expired_food_window, food_type_var, *food_type_options)
    food_type_dropdown.grid(row=1, column=1)

    expiry_date_entry = tk.Entry(expired_food_window)
    expiry_date_entry.grid(row=2, column=1)

    days_past_expiry_entry = tk.Entry(expired_food_window)
    days_past_expiry_entry.grid(row=3, column=1)

    tk.Button(expired_food_window, text="Save", command=save_expired_food_data).grid(row=4, columnspan=2)
