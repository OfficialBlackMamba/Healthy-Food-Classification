import tkinter as tk
from tkinter import filedialog, messagebox, Toplevel
from PIL import Image, ImageTk
import food_check_file
import new_food_file
import expired_food_file
import packaging_food_file
import unpackaging_food_file
import os
import mainn

def open_script():
    os.system('python mainn.py')

def process_image(file_path):
    # Placeholder for image processing logic
    return "Placeholder output: Image processed successfully."

def display_output(output):
    output_window = Toplevel(root)
    output_window.title("Image Identifier Output")

    output_label = tk.Label(output_window, text=output)
    output_label.pack(padx=20, pady=10)

def save_to_excel(data, filename):
    new_food_file.save_to_excel(data, filename)
    
def food_check():
    food_check_file.food_check()

def new_food():
    new_food_window = tk.Toplevel(root)
    new_food_window.title("New Food Entry")

    tk.Button(new_food_window, text="Fruit", command=new_food_file.fruit_entry).pack()
    tk.Button(new_food_window, text="Packaging", command=new_food_file.packaging_entry).pack()
    tk.Button(new_food_window, text="Unpackaging", command=new_food_file.unpackaging_entry).pack()

def expired_food():
    expired_food_file.expired_food_entry()

def packaging_food():
    packaging_food_file.packaging_food_entry()

def unpackaging_food():
     unpackaging_food_file.unpackaging_food_entry()

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        print("Selected file:", file_path)

# Create main window
root = tk.Tk()
root.title("Healthy Food Classification")
root.geometry("800x600")

# Set background color (sparkling golden)
root.configure(bg="#FFD700")

# Customizing the title text
title_font = ("Verdana", 28, "bold")
title_label = tk.Label(root, text="Healthy Food Classification", font=title_font, fg="blue", bg="#FFD700")
title_label.pack(pady=20)

# Create menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create menu items
food_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Food", menu=food_menu)
food_menu.add_command(label="Food Check", command=food_check)
food_menu.add_command(label="New Food", command=new_food)
food_menu.add_command(label="Expired Food", command=expired_food)
food_menu.add_command(label="Packaging Food", command=packaging_food)
food_menu.add_command(label="Unpackaging Food", command=unpackaging_food)

# Load images
fruit_image = Image.open("images/fruit_image.jpg").resize((200, 250))
fruit_photo = ImageTk.PhotoImage(fruit_image)

packaging_image = Image.open("images/packaging_image.jpg").resize((200, 250))
packaging_photo = ImageTk.PhotoImage(packaging_image)

open_button = tk.Button(root, text="Uploading your image here....", command=open_script)
open_button.pack(pady=10)

# Labels for display images.
fruit_label = tk.Label(root, image=fruit_photo, bg="#FFD700")
fruit_label.pack(side=tk.LEFT, padx=20)

packaging_label = tk.Label(root, image=packaging_photo, bg="#FFD700")
packaging_label.pack(side=tk.RIGHT, padx=20)

# Copyright text
copyright_label = tk.Label(root, text="Copyright (c) 2024 Sukhpal Kherera, MCA 2nd Year.", font=("Helvetica", 10), bg="#FFD700", fg="black")
copyright_label.pack(side=tk.BOTTOM, pady=10)

root.mainloop()
