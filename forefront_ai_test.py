import requests
from config  import apikey
import os
import re

# Load API key from environment variable (or replace with your key)
apiKey = os.getenv("FOREFRONT_API_KEY", apikey)

# Ensure API key is present
if not apiKey:
    raise ValueError("API Key is missing. Set FOREFRONT_API_KEY as an environment variable.")

url = "https://api.forefront.ai/v1/chat/completions"

query="How are you?"

# Corrected JSON payload
payload = {
    "model": "mistralai/Mistral-7B-v0.1",  # Ensure this model is valid for Forefront AI
    "messages": [
        #{"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"{query}"}
    ],
    "max_tokens": 100,
    "temperature": 0.7,
}

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {apiKey}",
}

# Use try-except for error handling
try:
    # response = requests.post(url, json=payload, headers=headers)
    # response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
    # print(response.json())  # Print the response JSON

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    response_data = response.json()
    assistant_response = response_data["choices"][0]["message"]["content"]
    cleaned_response = re.sub(r"<\|im_end\|>|<\|im_start\|>", "", assistant_response).strip()
    print(cleaned_response)

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

#Query 1
"""
{'choices': [{'message': 
{'content': "Subject: [Your Name] - Two-Month Internship Application
\n\n
Dear [Hiring Manager's Name],
\n\n
I am [Your Name], a [Your Degree or Major] student at [Your University] with a strong 
interest in [Area of Interest] and seek an opportunity to apply my knowledge and 
skills in a real-world setting. I am writing to express my interest in a two-month 
internship with [Company Name].
\n\n
My qualifications include:", 'role': 'assistant'}}], 
'usage': {'input_tokens': 62, 'output_tokens': 100, 'total_tokens': 162}}"
"""
#Query 2

"""
{'choices': [{'message': 
{'content': 'Forefront AI offers cutting-edge solutions with a focus on advanced 
machine learning and natural language processing, enhancing user experiences and 
driving innovation in various industries.
<|im_end|>
\n 
<|im_start|>', 'role': 'assistant'}}], 
'usage': {'input_tokens': 58, 'output_tokens': 45, 'total_tokens': 103}}"
"""