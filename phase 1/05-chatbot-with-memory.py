''' convo history : a list with 
[old convo]
user:
assistant:

[new input]
user:


'''

import requests
import json

url = "http://localhost:11434/api/generate"

convo_history = []

def get_reply(prompt):
    payload = {
        "model" : "llama3",
        "prompt" : prompt,
        "stream" : False
    }

    response = requests.post(url, json=payload)
    return response.json()['response']


def build_prompt():
    prompt = "You are a helpful chat assistant, Reply clearly & briefly.\n\n"
    for msg in convo_history:
        prompt += msg + "\n"
    prompt += "Assistant: "
    return prompt



def chat():
    print("Chatbot: Hello there!\nType 'Bye' to exit")

    while True: 
        user_input = input("You: ")

        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye!")
            break

        convo_history.append(f"User: {user_input}")
        final_prompt = build_prompt()
        reply = get_reply(final_prompt)
        convo_history.append(f"Assistant: {reply}")
        print("Chatbot: ",reply.strip())
        



if __name__ == "__main__":
    chat()  