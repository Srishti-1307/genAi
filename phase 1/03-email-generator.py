import requests
import json
import csv

url = "http://localhost:11434/api/generate"


def read_prompt():
    with open("email-generator.md", "r", encoding="utf-8") as f:
        return f.read() 
    

def generate_email(prompt):
    payload = {
        "model" : "llama3",
        "prompt" : prompt,
        "stream" : False,
        "options" : {
            "temperature" : 0              # removes randomness (model picks most likely next token)
        }
    }

    response = requests.post(url, json=payload)
    return response.json()["response"]


def main():
    base_prompt = read_prompt()
    with open("candidate.csv", newline = "") as f:
        reader = csv.DictReader(f)
        for row in reader:
            candidate_name = row["Name"] 
            candidate_email = row["Email"]
            final_prompt = base_prompt.replace("{{CANDIDATE_NAME}}", candidate_name).replace("{{CANDIDATE_EMAIL}}", candidate_email)
            email_content = generate_email(final_prompt)
            print("=" * 50)
            print(f"To: {candidate_email}")
            print("From: hr@bestpeers.com")
            print()
            print(email_content)
            print("=" * 50)


if __name__ == "__main__":
    main()
