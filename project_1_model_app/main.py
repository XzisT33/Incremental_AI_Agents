import requests

url = "http://localhost:11434/api/chat"

question = input("Enter your question: ")
payload = {
    "model": "qwen2.5:3b",
    "messages": [
        {
            "role": "user",
            "content": question
        }
    ],
    "stream": False
}

response = requests.post(url, json=payload)

result = response.json()

print(result['message']['content'])