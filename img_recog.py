import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk
import torch
import torchvision.transforms as transforms

class CameraApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Camera App")

        self.canvas = tk.Canvas(self, width=640, height=480)
        self.canvas.pack()

        self.btn_snapshot = tk.Button(self, text="Take Picture", command=self.take_picture)
        self.btn_snapshot.pack(pady=10)

        self.btn_upload = tk.Button(self, text="Upload Picture", command=self.upload_picture)
        self.btn_upload.pack(pady=5)

        self.status_label = tk.Label(self, text="", fg="green", wraplength=600)
        self.status_label.pack(pady=5)

        self.classification_model = torch.hub.load('pytorch/vision:v0.9.0', 'resnet18', pretrained=True)
        self.classification_model.eval()

        self.detection_model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True, force_reload=True)
        self.detection_model.eval()

        # Define transformations for input images
        self.transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])

    def take_picture(self):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        if ret:
            cv2.imwrite("snapshot.png", cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            self.analyze_image("snapshot.png")
            self.display_picture("snapshot.png")
        cap.release()

    def upload_picture(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if file_path:
            self.analyze_image(file_path)
            self.display_picture(file_path)

    def display_picture(self, file_path):
        img = Image.open(file_path)
        img.thumbnail((640, 480))
        self.photo = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

    def analyze_image(self, file_path):
    # Load and preprocess the image
       image = Image.open(file_path)
       image_resized = self.transform(image).unsqueeze(0) 

       classes = ['Unhealthy', 'Healthy']  # Define your classes here

    # Perform classification inference
       with torch.no_grad():
          outputs = self.classification_model(image_resized)
          _, predicted = torch.max(outputs, 1)
          classification_index = predicted.item()

    # Determine classification result
       if 0 <= classification_index < len(classes):
          classification_result = classes[classification_index]
       else:
          classification_result = "Unknown"

    # Perform object detection inference
       results = self.detection_model([file_path])
       detected_objects = results.xyxy[0].cpu().numpy()

    # Filter out specific food packaging
       specific_food_packaging = ['Haldiram\'s Bhujiya', 'Lahori Jeera (juice)', 'Coca Cola (soft drink)', 'chocolate', 'Lays', 'chips']
       filtered_objects = [obj for obj in detected_objects if results.names[int(obj[5])] in specific_food_packaging]

    # Display object detection result
       if len(filtered_objects) > 0:
          detection_result = "Detected specific food packagings: "
          for obj in filtered_objects:
              label = int(obj[5])
              confidence = obj[4]
              detection_result += f"{results.names[label]} ({confidence:.2f}), "
       else:
            detection_result = "No specific food packagings detected."

    # Display results
       self.show_info(f"Classification: {classification_result}\n{detection_result}")

    def show_info(self, info):
        self.status_label.config(text=info)

if __name__ == "__main__":
    app = CameraApp()
    app.mainloop()
