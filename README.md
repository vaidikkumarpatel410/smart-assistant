# 🤖 Smart Voice Assistant

📌 Overview

Smart Voice Assistant is a GUI-based voice-controlled Python assistant built using Tkinter. It processes spoken commands, performs tasks like opening apps or websites, fetching weather updates, and chatting via AI models like Together AI and Forefront AI. Optimized for macOS, it offers a sleek chat-style interface where user queries appear on the right and assistant responses on the left.

✨ Features

🎤 Voice Recognition: Converts your speech to text using speech_recognition.
🧠 AI-Powered Chat: Uses Together AI (Mixtral) and Forefront AI for intelligent responses.
🌦️ Weather Updates: Fetches real-time weather using WeatherAPI.
🌐 Web & App Launcher: Opens common websites and system applications via voice.
🔊 System TTS Output: Uses macOS's say command for vocal responses.
💬 Chat UI: Tkinter interface shows a left-right aligned conversation flow.
🎵 Music Playback: Plays a local song file with a voice command.
🧪 AI Output Storage: Saves AI responses to text files.
⚙️ Installation

📋 Prerequisites
Ensure the following are installed:

🐍 Python 3.x
📦 Dependencies from requirements.txt
💾 Recommended: Virtual environment setup
🚀 Setup Instructions
Clone the repository
git clone https://github.com/vaidikkumarpatel410/smart-assistant.git
cd smart-assistant
Create a virtual environment (optional)
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
Install dependencies
pip install -r requirements.txt
🎙️ Usage

Run the assistant:

python main.py
Click the Speak button and issue your command. Responses will be spoken and shown in the GUI.

🔑 Configuration

Add your API keys to a config.py file:
weatherapi = "YOUR_WEATHER_API_KEY"
ff_apikey = "YOUR_FORE_FRONT_API_KEY"
together_ai_api_key = "YOUR_TOGETHER_API_KEY"
Make sure config.py is in your .gitignore.
📂 Project Structure

smart-assistant/
│
├── main.py             # Main GUI application
├── config.py           # API keys (excluded from repo)
├── requirements.txt    # Required packages
├── README.md           # This file
├── ffai/               # Saved AI responses (auto-created)
└── .gitignore          # Hides sensitive files
🙌 Acknowledgments

🧠 Forefront AI
🤝 Together AI
🗣️ SpeechRecognition
🔊 macOS say command for voice output
🌦️ WeatherAPI
