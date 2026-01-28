import requests
import json

url = "http://localhost:11434/api/generate"



def generate_json(user_text):
    prompt = f"""
You are an information extraction assistant.

Task:
Extract structured information from the text below.

Text:
{user_text}

Constraints:
- Return ONLY valid JSON
- Do not add extra text

Output JSON format:
{{
    "name": "",
    "email": "",
    "intent": ""
}}
"""
    
    payload = {
        "model" : "llama3",
        "prompt" : prompt,
        "stream" : False,
        "options" : {
            "temperature" : 0
        }
    }

    response = requests.post(url, json=payload)
    return response.json()['response']


def main():
    input_text1 = """Hi! My name is Ananya. You can reach me at ananyasingh78@gmail.com. I want to apply for data engineering role"""
    output = generate_json(input_text1)
    print(output)
    print("_________________________________________________________________")
    input_text2 = """Hi! My name is Gaurav Sanghi. You can reach me at gaurav.sanghi@yahoo.com. I love reading books."""
    output2 = generate_json(input_text2)
    print(output2)
    print("_________________________________________________________________")


if __name__ == "__main__":
    main()    
