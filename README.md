# 🔍 Violence Detection System

This is a real-time violence detection project using deep learning, OpenCV, and Telegram API. It analyzes live video feed, detects violent scenes using a trained CNN model, and alerts via Telegram with timestamped snapshots.

---

## 📚 Table of Contents
- [Features](#-features)
- [Technologies Used](#-technologies-used)
- [Installation](#-installation)
- [How to Run the App](#-how-to-run-the-app)
- [Telegram Alerts](#-telegram-alerts)
- [Future Enhancements](#-future-enhancements)
- [Author](#-author)
- [License](#-license)

---

## 🚀 Features
- 📹 Real-time video stream processing from webcam
- 🤖 Violence detection using TensorFlow/Keras CNN model
- 📸 Saves images with timestamps when violence is detected
- 📬 Sends instant Telegram alerts

## 💻 Technologies Used
- TensorFlow & Keras
- OpenCV
- NumPy
- Python
- Telegram Bot API
- datetime
- requests

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/PRAVIN2506/violence_detection.git
cd violence_detection
```
### 2. Install Required Packages
```bash
pip install -r requirements.txt
```
### 3. Add Model File
Place your trained model file named modelnew.h5 inside the root folder of the project.

### 4. Configure Telegram Bot
Open the Python script and replace the following with your actual credentials:

```
bot_token = "YOUR_BOT_TOKEN"
chat_id = "YOUR_CHAT_ID"
```

## 🏃 How to Run the App
#### Run the script to start detection:

```bash
python main.py
```
Press q to quit the camera feed

#### Detected frames are saved with filenames like:
```
violence_detected_YYYY-MM-DD_HH-MM-SS.jpg
```

## 📬 Telegram Alerts
Whenever violence is detected, you’ll receive a message on Telegram:
```
"Violence detected! Immediate action required."
```

## 📌 Future Enhancements
- Improve model performance
- Support external/IP camera input
- Integrate cloud storage for saved snapshots
- Create a monitoring dashboard


## 👤 Author
Developed by Pravin Feel free to star ⭐ the repo, contribute, or share feedback!

## 📄 License
This project is licensed under the MIT License — free to use and modify.


