# python-chatbot
A simple OpenAI powered chatbot built in Python

Python Chatbot: Powered by OpenAI API

A simple but expandable Python-based chatbot that uses OpenAI’s API to generate natural, conversational responses. 
This project was inspired by Eli Etherton’s “Intro to OpenAI API for Artificial Intelligence in Python” 
and built as part of a CSCI 339 course project.

This chatbot supports:
	•	Conversational text responses
	•	Memory within a session
	•	A customizable personality
	•	Easy expansion into voice, image, and tool-based features

🚀 Features

✔️ Conversational Chatbot

The bot responds naturally to user input using gpt-4o-mini.

✔️ Session Memory

Maintains the flow of conversation by storing previous messages.

✔️ Custom Personality

Editable system prompt lets you tune the bot’s tone and behavior.



	•	🎤 Voice input (speech-to-text)
	•	🔊 Voice output (text-to-speech)
	•	🖼️ Image generation using OpenAI API
	•	🌦️ Real-time weather & API tools
	•	🖥️ GUI using Tkinter
	•	🌐 Web interface using Flask

python-chatbot/
│
├── chatbot.py         # Main chatbot application
├── .env               # Stores your API key (NOT committed to GitHub)
├── .gitignore         # Ensures .env and other files stay private
└── requirements.txt   # (Optional) Python dependencies

🛠️ Installation & Setup
1. git clone https://github.com/tangerinedream13/python-chatbot.git
cd python-chatbot
2. Install dependencies: pip3 install openai python-dotenv
3. Create a .env
4. Add your API key
5. Run the chatbot

You should see: 
Your chatbot is running! Type 'quit' to exit.

You:

Example: 
You: Hello!
Bot: Hi there! How can I help you today?

You: My name is Maria.
Bot: Nice to meet you, Maria! How can I assist you?

You: What's my name?
Bot: You told me your name is Maria.


📚 Background & Motivation

This project was inspired by:
	•	The 2025 brAIn AI Summit in Asheville, NC
	•	Eli Etherton’s live chatbot demo
	•	The YouTube tutorial “Intro to OpenAI API for Artificial Intelligence in Python”

The goal is to understand fundamental LLM concepts by building a simple, extensible chatbot from scratch.

🧭 Roadmap (Planned Upgrades)
	•	Add voice input using OpenAI Audio Transcription
	•	Add voice output using OpenAI Text-to-Speech
	•	Add image generation capabilities
	•	Integrate external APIs (weather, calculator, etc.)
	•	Add persistent long-term memory
	•	Build a Tkinter-based GUI
	•	Deploy a Flask web version

🤝 Contributions

Pull requests, feature suggestions, and improvements are welcome!





