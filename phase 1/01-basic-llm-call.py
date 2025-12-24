import requests
import json

url = "http://localhost:11434/api/generate"

payload = {
    "model" : "llama3",
    "prompt" : "What is an LLM? Tell me in 1 line",
    "stream" : False
}

response = requests.post(url, json = payload)
data = response.json()
# print(data)
print(data["response"])


'''
response from model is json.. Something looks as below:

{
    "model": "llama3",
    "created_at": "2024-06-01T12:34:56.789Z",
    "response": "...............",
    "done": true,
    "context": [128, 456, 789, ...],
    "total_duration": 1234567890,
    "load_duration": 12345678,
    "prompt_eval_count": 12,
    "prompt_eval_duration": 34567890,
    "eval_count": 28,
    "eval_duration": 987654321
}

'''


# print(data["context"])
# print(data["created_at"])




