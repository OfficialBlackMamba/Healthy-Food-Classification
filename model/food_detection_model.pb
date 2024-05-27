import cv2
import tensorflow as tf

# Load the TensorFlow model
model = tf.saved_model.load('food_detection_model')

# Load the class labels
class_names = ['class1', 'class2', 'class3']  # replace with your actual class names

def preprocess_image(image):
    image = cv2.resize(image, (224, 224))
    image = image / 255.0
    return image

def detect_food(frame):
    image = preprocess_image(frame)
    input_tensor = tf.convert_to_tensor([image], dtype=tf.float32)
    detections = model(input_tensor)
    return detections

# Capture video from the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    detections = detect_food(frame)
    # Display the results
    label = class_names[np.argmax(detections)]
    cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow('Food Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
