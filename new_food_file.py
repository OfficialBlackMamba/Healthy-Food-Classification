import tkinter as tk
from tkinter import messagebox
import pandas as pd

def save_data(data, filename):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    messagebox.showinfo("Data Saved", "Data saved successfully!")

def fruit_entry():
    def save_fruit_data():
        name = name_entry.get()
        time_period = time_period_entry.get()
        export_date = export_date_entry.get()
        export_time = export_time_entry.get()

        data = {
            'Name': [name],
            'Time Period': [time_period],
            'Export Date': [export_date],
            'Export Time': [export_time]
        }
        save_data(data, "fruit_data.xlsx")

    fruit_window = tk.Toplevel()
    fruit_window.title("Fruit Entry")

    tk.Label(fruit_window, text="Fruit Name:").grid(row=0, column=0)
    tk.Label(fruit_window, text="Time Period:").grid(row=1, column=0)
    tk.Label(fruit_window, text="Export Date:").grid(row=2, column=0)
    tk.Label(fruit_window, text="Export Time:").grid(row=3, column=0)

    name_entry = tk.Entry(fruit_window)
    time_period_entry = tk.Entry(fruit_window)
    export_date_entry = tk.Entry(fruit_window)
    export_time_entry = tk.Entry(fruit_window)

    name_entry.grid(row=0, column=1)
    time_period_entry.grid(row=1, column=1)
    export_date_entry.grid(row=2, column=1)
    export_time_entry.grid(row=3, column=1)

    tk.Button(fruit_window, text="Save", command=save_fruit_data).grid(row=4, columnspan=2)

def packaging_entry():
    def save_packaging_data():
        food_name = food_name_entry.get()
        manufacturer_name = manufacturer_name_entry.get()
        manufacture_date = manufacture_date_entry.get()
        expiry_date = expiry_date_entry.get()
        ingredients = ingredients_entry.get("1.0", tk.END)

        data = {
            'Food Name': [food_name],
            'Manufacturer Name': [manufacturer_name],
            'Manufacture Date': [manufacture_date],
            'Expiry Date': [expiry_date],
            'Ingredients': [ingredients]
        }
        save_data(data, "packaging_data.xlsx")

    packaging_window = tk.Toplevel()
    packaging_window.title("Packaging Entry")

    tk.Label(packaging_window, text="Food Name:").grid(row=0, column=0)
    tk.Label(packaging_window, text="Manufacturer Name:").grid(row=1, column=0)
    tk.Label(packaging_window, text="Manufacture Date:").grid(row=2, column=0)
    tk.Label(packaging_window, text="Expiry Date:").grid(row=3, column=0)
    tk.Label(packaging_window, text="Ingredients:").grid(row=4, column=0)

    food_name_entry = tk.Entry(packaging_window)
    manufacturer_name_entry = tk.Entry(packaging_window)
    manufacture_date_entry = tk.Entry(packaging_window)
    expiry_date_entry = tk.Entry(packaging_window)
    ingredients_entry = tk.Text(packaging_window, height=4, width=30)

    food_name_entry.grid(row=0, column=1)
    manufacturer_name_entry.grid(row=1, column=1)
    manufacture_date_entry.grid(row=2, column=1)
    expiry_date_entry.grid(row=3, column=1)
    ingredients_entry.grid(row=4, column=1)

    tk.Button(packaging_window, text="Save", command=save_packaging_data).grid(row=5, columnspan=2)

def unpackaging_entry():
    def save_unpackaging_data():
        food_name = food_name_entry.get()
        food_type = food_type_entry.get()
        manufacturer_name = manufacturer_name_entry.get()
        manufacture_date = manufacture_date_entry.get()
        expiry_date = expiry_date_entry.get()
        ingredients = ingredients_entry.get("1.0", tk.END)

        data = {
            'Food Name': [food_name],
            'Food Type': [food_type],
            'Manufacturer Name': [manufacturer_name],
            'Manufacture Date': [manufacture_date],
            'Expiry Date': [expiry_date],
            'Ingredients': [ingredients]
        }
        save_data(data, "unpackaging_data.xlsx")

    unpackaging_window = tk.Toplevel()
    unpackaging_window.title("Unpackaging Entry")

    tk.Label(unpackaging_window, text="Food Name:").grid(row=0, column=0)
    tk.Label(unpackaging_window, text="Food Type:").grid(row=1, column=0)
    tk.Label(unpackaging_window, text="Manufacturer Name:").grid(row=2, column=0)
    tk.Label(unpackaging_window, text="Manufacture Date:").grid(row=3, column=0)
    tk.Label(unpackaging_window, text="Expiry Date:").grid(row=4, column=0)
    tk.Label(unpackaging_window, text="Ingredients:").grid(row=5, column=0)

    food_name_entry = tk.Entry(unpackaging_window)
    food_type_entry = tk.Entry(unpackaging_window)
    manufacturer_name_entry = tk.Entry(unpackaging_window)
    manufacture_date_entry = tk.Entry(unpackaging_window)
    expiry_date_entry = tk.Entry(unpackaging_window)
    ingredients_entry = tk.Text(unpackaging_window, height=4, width=30)

    food_name_entry.grid(row=0, column=1)
    food_type_entry.grid(row=1, column=1)
    manufacturer_name_entry.grid(row=2, column=1)
    manufacture_date_entry.grid(row=3, column=1)
    expiry_date_entry.grid(row=4, column=1)
    ingredients_entry.grid(row=5, column=1)

    tk.Button(unpackaging_window, text="Save", command=save_unpackaging_data).grid(row=6, columnspan=2)
