# 🤖 Smart Voice Assistant

## 📌 Overview
This is a Python-based smart voice assistant that can recognize voice commands, process them, and provide responses using AI models. It is designed to run on macOS and utilizes speech recognition, text-to-speech, and natural language processing.

## ✨ Features
- 🎤 **Voice Command Recognition**: Converts spoken input into text.
- 🧠 **AI-Powered Responses**: Uses an AI model to generate relevant answers.
- 🔊 **Text-to-Speech (TTS)**: Reads responses aloud using gTTS.
- ⚡ **Lightweight and Efficient**: Optimized for running on macOS with minimal resources.

## ⚙️ Installation
### 📋 Prerequisites
Ensure you have the following installed on your system:
- 🐍 Python 3.x
- 💾 Virtual Environment (Recommended)
- 📦 Required dependencies listed in `requirements.txt`

🚀 Setup Instructions
1. **Clone the Repository**
   git clone https://github.com/vaidikkumarpatel410/smart-assistant.git
   cd smart-assistant
2. **Create a Virtual Environment (Optional but Recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🎙️ Usage
Run the assistant by executing:
```bash
python main.py
```
Speak into your microphone when prompted, and the assistant will respond accordingly.

## 🛠️ Configuration
- 🔑 **API Keys & Credentials**: If your project uses API keys (e.g., for GPT models), store them securely in a `config.py` file or an `.env` file and ensure it is not included in version control (`.gitignore`).

## 📂 File Structure
```
smart-assistant/
│── main.py                # Main script
│── forefront_ai_test.py   # AI integration test
│── requirements.txt       # Dependencies
│── README.md              # Project documentation
│── .gitignore             # Ignore sensitive files
```


## 🙌 Acknowledgments
- 🎉 Fore Front AI (For AI model)
- 🎉 Together AI (For AI model)
- 🗣️ gTTS (Google Text-to-Speech)
- 🎧 SpeechRecognition Library

