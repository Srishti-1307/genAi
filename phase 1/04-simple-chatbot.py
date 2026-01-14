# Disclaimer : This is a simple chatbot, Each msg is stateless, No conversation history is maintained!


import requests
import json

url = "http://localhost:11434/api/generate"


def get_reply(prompt):
    payload = {
        "model" : "llama3",
        "prompt" : prompt,
        "stream" : False
    }

    response = requests.post(url, json=payload)
    return response.json()['response']




def chat():
    print("Chatbot: Hello there!\nType 'Bye' to exit")

    while True: 

        user_input = input("You: ")

        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye!")
            break


        chatprompt = f'''
    You are a helpful chat assistant.
    Reply clearly & briefly.

    User : {user_input}
    Assistant : 
    '''
        reply = get_reply(chatprompt)
        print("Chatbot: ",reply.strip())

if __name__ == "__main__":
    chat()