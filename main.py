import tkinter as tk
import os
import webbrowser
import datetime
import requests
import together
from config import weatherapi, ff_apikey, together_ai_api_key
import speech_recognition as sr


root = tk.Tk()
root.title("Smart Voice Assistant")
root.geometry("600x400")


chat_frame = tk.Frame(root)
chat_frame.pack(fill="both", expand=True)


client = together.Together(api_key=os.getenv("TOGETHER_API_KEY", together_ai_api_key))

# Functions 

def get_weather(city):
    try:
        response = requests.get("http://api.weatherapi.com/v1/current.json", params={
            "key": weatherapi,
            "q": city
        })
        data = response.json()
        if "error" in data:
            return f"API error: {data['error']['message']}"
        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        return f"The temperature in {city} is {temp}°C with {condition.lower()}."
    except Exception as e:
        return f"An error occurred: {str(e)}"

#Human like chatting using together ai
def chat(prompt):
    try:
        system_prompt = (
            "You are a helpful AI assistant. Answer only the user's question clearly and concisely."
        )
        response = client.completions.create(
            model="mistralai/Mixtral-8x7B-v0.1",
            prompt=f"{system_prompt}\n\nUser: {prompt}\nAssistant:",
            max_tokens=100,
            temperature=0.3,
            top_p=0.7,
            top_k=50,
            repetition_penalty=1.2
        )
        assistant_reply = response.choices[0].text.strip().split("\n")[0]
        return assistant_reply
    except Exception as e:
        return f"API Error: {e}"

# AI call from Forefront AI 
def ai(prompt):
    apiKey = os.getenv("FOREFRONT_API_KEY", ff_apikey)
    if not apiKey:
        raise ValueError("API Key is missing.")
    
    payload = {
        "model": "mistralai/Mistral-7B-v0.1",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 100,
        "temperature": 0.7,
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {apiKey}",
    }
    try:
        response = requests.post("https://api.forefront.ai/v1/chat/completions", json=payload, headers=headers)
        content = response.json()["choices"][0]["message"]["content"]
        text = f"Forefront AI response for prompt: {prompt}\n\n{content}"
        filename = f"ffai/{prompt.split()[-1]}.txt"
        os.makedirs("ffai", exist_ok=True)
        with open(filename, "w") as f:
            f.write(text)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Function to add the text on our frame
def add_message(text, is_user=False):
    msg_frame = tk.Frame(chat_frame)
    msg_frame.pack(anchor='e' if is_user else 'w', pady=5, padx=10, fill='x')

    label = tk.Label(
        msg_frame,
        text=text,
        font=("Helvetica", 12),
        wraplength=500,
        justify="right" if is_user else "left",
        padx=10,
        pady=5
    )
    label.pack(anchor='e' if is_user else 'w')

# Function to make the voice assistant speak
def say(text):
    os.system(f"say \"{text}\"")
    add_message(text, is_user=False)

# Function to take command from user (HEAR)
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            return r.recognize_google(audio, language="en-in")
        except Exception as e:
            say("I couldn't hear you. Please try again.")
            return None


def handle_voice_assistant():
    query = takeCommand()
    if query:
        add_message(query, is_user=True)

        if "open" in query.lower():
            for name, url in [
                ("youtube", "https://youtube.com"),
                ("wikipedia", "https://wikipedia.com"),
                ("google", "https://google.com"),
                ("amazon", "https://amazon.com")
            ]:
                if name in query.lower():
                    say(f"Opening {name}")
                    webbrowser.open(url)
                    return

        elif "play music" in query.lower():
            os.system("open song.mp3")
            say("Playing music")
        
        elif "the time" in query.lower():
            time = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"The time is {time}")

        elif "app" in query.lower():
            for app, path in [
                ("facetime", "/System/Applications/FaceTime.app"),
                ("spotify", "/Applications/Spotify.app"),
                ("google", "/Applications/Google Chrome.app"),
                ("notes", "/System/Applications/Notes.app")
            ]:
                if app in query.lower():
                    say(f"Opening {app}")
                    os.system(f"open '{path}'")
                    return

        elif "using artificial intelligence" in query.lower():
            ai(query)
            say("AI response has been saved.")

        elif "assistant quit" in query.lower():
            say("Goodbye!")
            root.destroy()

        elif "weather" in query.lower():
            say("Which city?")
            city = takeCommand()
            if city:
                report = get_weather(city)
                say(report)

        elif "chat" in query.lower():
            response = chat(query)
            say(response)

        else:
            say("Sorry, I don't understand that command.")

# Button

speak_btn = tk.Button(root, text="Speak", command=handle_voice_assistant, font=("Helvetica", 14), bg="#90caf9")
speak_btn.pack(pady=10)

root.mainloop()
