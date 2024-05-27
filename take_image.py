import tkinter as tk
import cv2
from PIL import Image, ImageTk
import numpy as np
import os

# Path to COCO model files
model_path = r"D:/ProBoy Sukhi/model"  # Update this with the path to your COCO model
weights_path = os.path.join(model_path, "yolov3.weights")
config_path = os.path.join(model_path, "yolov3.cfg")
classes_path = os.path.join(model_path, "coco.names")

# Load COCO model
net = cv2.dnn.readNetFromDarknet(config_path, weights_path)
classes = None
with open(classes_path, 'r') as f:
    classes = f.read().strip().split('\n')
layer_names = net.getLayerNames()
layer_ids = net.getUnconnectedOutLayers().flatten()
output_layers = [layer_names[layer_id - 1] for layer_id in layer_ids]

class CameraApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)
        self.cap = cv2.VideoCapture(0)
        self.current_frame = None
        self.canvas = tk.Canvas(window, width=640, height=480)
        self.canvas.pack()

        self.update()

    def detect_objects(self, frame):
        height, width, _ = frame.shape

        # Detect objects using the COCO model
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(output_layers)

        # Process detections
        class_ids = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:  # Confidence threshold
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        # Apply non-max suppression to remove redundant detections
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

        # Draw bounding boxes and labels
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                color = (255, 0, 0)  # Default color
                # Check if the detected object is healthy or unhealthy
                if label in ['apple', 'banana', 'orange']:  # Adjust this condition based on your criteria
                    label = "Healthy: " + label
                    color = (0, 255, 0)  # Green color for healthy food
                elif label in ['pizza', 'hamburger', 'fries']:  # Adjust this condition based on your criteria
                    label = "Unhealthy: " + label
                    color = (0, 0, 255)  # Red color for unhealthy food
                # Draw the bounding box and label
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                cv2.putText(frame, label, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    def update(self):
        ret, frame = self.cap.read()
        if ret:
            self.detect_objects(frame)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.current_frame = ImageTk.PhotoImage(image=Image.fromarray(frame_rgb))
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.current_frame)
        self.window.after(1, self.update)  # Decreased the delay to 1 millisecond

if __name__ == "__main__":
    root = tk.Tk()
    app = CameraApp(root, "Camera App")
    root.mainloop()
