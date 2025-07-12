import cv2
import tensorflow as tf
import numpy as np
import serial
import requests
from datetime import datetime

# Load the pre-trained violence detection model
model = tf.keras.models.load_model("modelnew.h5")  # Ensure this path is correct

# Arduino Serial Communication
arduino = serial.Serial(port='COM5', baudrate=9600)  # Replace 'COM5' with your Arduino's port

# Telegram Bot Credentials
bot_token = "7695376200:AAF4tIhzKfeAWc3uE59ZdCIz0bzxKldWG04"
chat_id = "1421223515"

# Function to send Telegram messages
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"    
    payload = {"chat_id": chat_id, "text": message}
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print("Telegram message sent!")
    else:
        print("Failed to send Telegram message:", response.text)

# Function for violence detection
def detect_violence(frame):
    frame_resized = cv2.resize(frame, (128, 128))  # Resize frame to model input shape (128x128)
    frame_array = np.expand_dims(frame_resized, axis=0) / 255.0  # Normalize pixel values to [0, 1]
    prediction = model.predict(frame_array)
    return prediction[0][0] > 0.5  # Threshold for violence detection (True if > 0.5)

# Function to save the image with timestamp
def save_detected_image(frame):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"violence_detected_{timestamp}.jpg"
    cv2.imwrite(filename, frame)
    print(f"Saved image: {filename}")

# Access laptop camera
cap = cv2.VideoCapture(0)  # '0' for default laptop camera

print("Starting violence detection...")
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture video. Exiting...")
        break

    # Detect violence in the current frame
    if detect_violence(frame):
        print("Violence detected!")
        
        # Save the detected frame with timestamp
        save_detected_image(frame)
        
        # Send a signal to Arduino to activate buzzer
        print("Sending signal to Arduino...")
        arduino.write(b'1')  # Send command to activate buzzer
        
        # Send a Telegram alert
        send_telegram_message("Violence detected! Immediate action required.")

    # Display the video feed
    cv2.imshow("Camera Feed", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
