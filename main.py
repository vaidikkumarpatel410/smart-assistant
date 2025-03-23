import speech_recognition as sr
import os
import webbrowser
import datetime
import requests
import random
import together
from config import ff_apikey
from config import together_ai_api_key


client = together.Together(api_key=os.getenv("TOGETHER_API_KEY",together_ai_api_key))

def chat(prompt):
    try:
        system_prompt = (
            "You are a helpful AI assistant. Answer only the user's question clearly and concisely. "
            "Do not generate extra conversation, dialogue, or user responses. Just provide a single, direct answer."
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

        assistant_reply = response.choices[0].text.strip()
        assistant_reply = assistant_reply.split("\n")[0]
        return assistant_reply
    except Exception as e:
        return f"API Error: {e}"



# AI call from Forefront AI
def ai(prompt):
    apiKey = os.getenv("FOREFRONT_API_KEY", ff_apikey)
    if not apiKey:
        raise ValueError("API Key is missing. Set FOREFRONT_API_KEY as an environment variable.")
    
    url = "https://api.forefront.ai/v1/chat/completions"

    query = prompt
    text = f"Forefront AI response for prompt: {prompt} \n *******************************\n\n"

    payload = {
        "model": "mistralai/Mistral-7B-v0.1",  
        "messages": [{"role": "user", "content": query}],
        "max_tokens": 100,
        "temperature": 0.7,
    }
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {apiKey}",
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        response_data = response.json()
        content = response_data["choices"][0]["message"]["content"]
        text += content

        if not os.path.exists("ffai"):
            os.mkdir("ffai")

        filename_part = ''.join(prompt.split('intelligence')[1:]).strip() or f"ai_response_{random.randint(1,99999999)}"
        filename = f"ffai/{filename_part}.txt"
        print("File Created\n")

        with open(filename, "w") as f:
            f.write(text)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Function to make the voice assistant speak
def say(text):
    os.system(f"say \"{text}\"")

# Function to take command from user (HEAR)
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            print(f"Error recognizing speech: {e}")
            say("I couldn't hear you. Please try again.")
            return None  

if __name__ == "__main__":
    say("Hello User")
    while True:
        print("Listening...")

        query = takeCommand()  # Function call to take command from user

        if query is None:  # If speech recognition fails, continue listening
            continue  

        if "open" in query.lower():  # Open websites
            sites = [
                ["youtube", "https://youtube.com"],
                ["wikipedia", "https://wikipedia.com"],
                ["google", "https://google.com"],
                ["amazon", "https://amazon.com"]
            ]
            for site in sites:
                if site[0] in query.lower():
                    say(f"Opening {site[0]} sir...")
                    webbrowser.open(site[1])

        elif "play music" in query.lower():  # Playing music
            musicPath = "song.mp3"
            os.system(f"open \"{musicPath}\"")

        elif "the time" in query.lower():  # Time
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir, the time is {strfTime}")
        
        elif "app" in query.lower():
            apps=[
                ["facetime","/System/Applications/Factime.app/PATH"],
                ["spotify","/Applications/Spotify.app/PATH"],
                ["google","/Applications/Google Chrome.app/PATH"],
                ["notes","/System/Applications/Notes.app/PATH"]
            ]
            for app in apps:
                if app[0] in query.lower():
                    say(f"Opening {app[0]}")
                    os.system(f"open {app[1]}")
        
        elif "using artificial intelligence" in query.lower():  # Function call for AI text response
            ai(prompt=query)
        
        elif "assistant quit" in query.lower():  # Quit command
            say("Goodbye!")
            exit()

        elif "chat" in query.lower():  # Start chat only if "chat" is mentioned (voice chat)
            print("Chatting....")
            response = chat(query)  
            if response:  
                print(f"Assistant: {response}") 
                say(response) 
        else:
            say("I did not understand that. Can you please repeat?")
            continue
