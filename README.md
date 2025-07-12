# 🔍 Violence Detection System

This is a real-time violence detection project using deep learning, OpenCV, and Telegram API for alerting authorities with snapshots.

## 🚀 Features
- Detects violence from a live camera feed
- Sends Telegram alert messages
- Saves detected frames with timestamp

## 💻 Technologies Used
- TensorFlow (Keras)
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
2. Install Required Packages
```bash
pip install -r requirements.txt
```

3. Add Model File
Place your trained model file named modelnew.h5 inside the root folder of the project.

4. Configure Telegram Bot
Open the Python script and replace the following with your actual credentials:

python
```
bot_token = "YOUR_BOT_TOKEN"
chat_id = "YOUR_CHAT_ID"
```

