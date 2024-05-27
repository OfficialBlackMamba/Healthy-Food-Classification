import tkinter as tk
from tkinter import messagebox
import pandas as pd

def save_data(data, filename):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    messagebox.showinfo("Data Saved", "Data saved successfully!")

def packaging_food_entry():
    def save_packaging_food_data():
        name = name_entry.get()
        arrival_time = arrival_time_entry.get()
        expiration_date = expiration_date_entry.get()
        ingredients = ingredients_entry.get("1.0", tk.END)
        is_healthy = is_healthy_var.get()

        data = {
            'Food Name': [name],
            'Arrival Time': [arrival_time],
            'Expiration Date': [expiration_date],
            'Ingredients': [ingredients],
            'Healthy/Unhealthy': [is_healthy]
        }
        save_data(data, "packaging_food_data.xlsx")

    packaging_food_window = tk.Toplevel()
    packaging_food_window.title("Packaging Food Entry")

    tk.Label(packaging_food_window, text="Food Name:").grid(row=0, column=0)
    tk.Label(packaging_food_window, text="Arrival Time:").grid(row=1, column=0)
    tk.Label(packaging_food_window, text="Expiration Date:").grid(row=2, column=0)
    tk.Label(packaging_food_window, text="Ingredients:").grid(row=3, column=0)
    tk.Label(packaging_food_window, text="Healthy/Unhealthy:").grid(row=4, column=0)

    name_entry = tk.Entry(packaging_food_window)
    name_entry.grid(row=0, column=1)

    arrival_time_entry = tk.Entry(packaging_food_window)
    arrival_time_entry.grid(row=1, column=1)

    expiration_date_entry = tk.Entry(packaging_food_window)
    expiration_date_entry.grid(row=2, column=1)

    ingredients_entry = tk.Text(packaging_food_window, height=4, width=30)
    ingredients_entry.grid(row=3, column=1)

    is_healthy_var = tk.BooleanVar()
    is_healthy_checkbox = tk.Checkbutton(packaging_food_window, text="Healthy", variable=is_healthy_var)
    is_healthy_checkbox.grid(row=4, column=1)

    tk.Button(packaging_food_window, text="Save", command=save_packaging_food_data).grid(row=5, columnspan=2)
