import os
import tkinter as tk
from tkinter import filedialog
import pandas as pd
from PIL import Image, ImageTk

# Path to the CSV file
DATABASE_PATH = "database/item_db.csv"

# Function to load the CSV database
def load_database(path):
    if os.path.exists(path):
        print(f"Loading database from {path}.")
        return pd.read_csv(path)
    else:
        print(f"Database file not found at {path}.")
        return pd.DataFrame(columns=['image_name', 'image_path', 'food_category', 'image_category', 'food_ingredients', 'image_status', 'food_causes'])

# Load the image database
image_database = load_database(DATABASE_PATH)

def upload_image(image_frame, root):
    # Open a file dialog to select an image
    file_path = filedialog.askopenfilename()

    # If a file is selected
    if file_path:
        print(f"Image selected: {file_path}")
        # Display the uploaded image in the Image_Frame
        display_image(image_frame, file_path)
        # Extract the image name without the extension
        image_name = os.path.basename(file_path).split('.')[0]
        print(f"Extracted image name: {image_name}")
        # Check if the image name is in the image_name column of the database
        if image_name in image_database['image_name'].values:
            # Image found in database, display details after a delay
            display_detection_message(image_frame, "Image found in database. Now wait 2 seconds for details.")
            root.after(2000, show_image_details, image_name)
        else:
            # Image not found in the database
            display_detection_message(image_frame, "Image not found in the database.")
            print("Image not found in database.")

def display_image(frame, file_path):
    # Clear the frame first
    for widget in frame.winfo_children():
        widget.destroy()

    # Open the image file using PIL
    pil_image = Image.open(file_path)
    # Resize the image to fit the label frame
    pil_image.thumbnail((300, 300))
    # Convert PIL Image to Tkinter-compatible format
    photo = ImageTk.PhotoImage(pil_image)
    # Display the uploaded image in the image frame
    label = tk.Label(frame, image=photo)
    label.image = photo
    label.pack()

def display_detection_message(frame, message):
    # Display message indicating image detection status
    label = tk.Label(frame, text=message, font=('Courier', 10), fg='red')
    label.pack(pady=10)

def show_image_details(image_name):
    details = image_database[image_database['image_name'] == image_name].iloc[0]
    print(f"Details fetched from database: {details.to_dict()}")

    result_window = tk.Toplevel()
    result_window.title("Image Details")

    details_text = (f"Food Name: {details['image_name']}\n"
                    f"Food Category: {details['food_category']}\n"
                    f"Image Category: {details['image_category']}\n"
                    f"Food Ingredients: {details['food_ingredients']}\n"
                    f"Image Status: {details['image_status']}\n"
                    f"Food Causes: {details['food_causes']}")

    result_label = tk.Label(result_window, text=details_text, font=('Courier', 10))
    result_label.pack(padx=20, pady=20)

# Main entry point of the script
if __name__ == "__main__":
    # Create the Tkinter root window
    root = tk.Tk()
    root.title("Upload Image")

    # Create a frame for uploading image
    upload_frame = tk.Frame(root)
    upload_frame.pack(pady=20)

    # Button to upload image
    upload_button = tk.Button(upload_frame, text="Upload Image", command=lambda: upload_image(image_frame, root))
    upload_button.pack(pady=10)

    # Frame to display the uploaded image
    image_frame = tk.Frame(root)
    image_frame.pack(pady=20)

    # Start the Tkinter event loop
    root.mainloop()
