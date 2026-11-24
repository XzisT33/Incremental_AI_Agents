import requests
from dotenv import load_dotenv
import os

load_dotenv()

ollama_url = os.getenv("OLLAMA_URL")
ollama_model = os.getenv("MODEL_NAME")
model_temperature = float(os.getenv("TEMPERATURE"))
max_output_tokens = int(os.getenv("MAX_OUTPUT_TOKENS"))

url = ollama_url

question = input("Enter your question: ")

payload = {
    "model": ollama_model,
    "messages": [
        {
            "role": "system",
            "content": "You are a professional sales research assistant. Provide concise, factual and structured answers."
        },
        {
            "role": "user",
            "content": question
        }
    ],

    "options": {
        "temperature" : model_temperature,
        "num_predict": max_output_tokens # Output token count
    },

    "stream": False
}


try:
    response = requests.post(
        url, 
        json=payload,
        timeout=60
        )

    response.raise_for_status() # Before sending the whole body to Ollama we first check if the server returned a successful HTTP status

    result = response.json()

    print(result['message']['content'])

except requests.exceptions.Timeout:
    print("LLM timed out.")

except requests.exceptions.HTTPError as e:
    print(f"HTTP error occurred: {e}")

except requests.exceptions.ConnectionError:
    print("Cannot connect to Ollama. Please check whether it is running.")