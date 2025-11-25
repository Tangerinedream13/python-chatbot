import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chatbot():
    print("Welcome to your AI chatbot! Type 'quit' to exit.\n")

    messages = [
        {"role": "system", "content": "You are a friendly and helpful AI assistant."}
    ]

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["quit", "exit"]:
            print("Chatbot: Goodbye!")
            break

        messages.append({"role": "user", "content": user_input})

        # Generate chatbot response
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        ai_reply = response.choices[0].message.content
        print(f"Chatbot: {ai_reply}")

        messages.append({"role": "assistant", "content": ai_reply})


if __name__ == "__main__":
    chatbot()