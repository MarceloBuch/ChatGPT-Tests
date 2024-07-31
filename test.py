import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def request_gpt(prompt):
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['sair', 'tchau']:
            break

        response = request_gpt(user_input)
        print("Chatbot: ", response)