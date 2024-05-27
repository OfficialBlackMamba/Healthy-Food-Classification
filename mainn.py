import tkinter as tk
from tkinter import filedialog
import pandas as pd
from PIL import Image, ImageTk
import upload_image
import take_image
import os

# Path to the CSV file
DATABASE_PATH = "database/item_db.csv"

# Function to load the CSV database
def load_database(path):
    if os.path.exists(path):
        print(f"Loading database from {path}.")
        return pd.read_csv(path)
    else:
        print(f"Database file not found at {path}.")
        return pd.DataFrame(columns=['image_name', 'image_path', 'food_category', 'image_status', 'food_ingredients', 'food_causes'])

# Load the image database
image_database = load_database(DATABASE_PATH)

class ImageWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Frame")
        
        # Initialize self.image_frame
        self.image_frame = tk.Frame(self.master)
        self.image_frame.pack()

        # Create CameraApp instance
        self.camera_app = None  # Initialize to None

        self.take_image_button = tk.Button(self.master, text="Take an Image", command=self.take_image_command)
        self.take_image_button.pack()

        self.upload_image_button = tk.Button(self.master, text="Upload Image", command=self.upload_image_command)
        self.upload_image_button.pack()

    def take_image_command(self):
        # Check if CameraApp is initialized
        if self.camera_app is None:
            # Create CameraApp instance
            self.camera_app = take_image.CameraApp(self.master, self.image_frame)

    def upload_image_command(self):
        upload_image.upload_image(self.image_frame, self.master)

    def __del__(self):
        if self.camera_app is not None and hasattr(self.camera_app, 'cap'):
            self.camera_app.cap.release()

def main():
    root = tk.Tk()
    app = ImageWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
