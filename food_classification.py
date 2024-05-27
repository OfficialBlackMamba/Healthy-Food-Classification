import tkinter as tk
from tkinter import messagebox

def food_check():
    def check_food():
        food = food_entry.get().lower()

        healthy_fruits = ["apple", "mango", "grapes", "banana"]

        if food in healthy_fruits:
            messagebox.showinfo("Food Check Result", f"{food.title()} is healthy!")
        else:
            messagebox.showwarning("Food Check Result", f"{food.title()} is unhealthy!")

    food_check_window = tk.Toplevel()
    food_check_window.title("Food Check")

    # Create label and entry for food input
    tk.Label(food_check_window, text="Enter the food:").pack()
    food_entry = tk.Entry(food_check_window)
    food_entry.pack()

    tk.Button(food_check_window, text="Check Food", command=check_food).pack()
