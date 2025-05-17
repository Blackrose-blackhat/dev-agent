import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class IntentClassifier:
    def __init__(self):
        self.possible_intents = ["summarize", "generate", "store", "recall", "chat", "unknown"]

    def classify(self, user_input: str) -> str:
        prompt = f"""
You are an AI intent classifier for an agent swarm. Given a user input, return ONLY the intent from the list:
{", ".join(self.possible_intents)}.

Input: "{user_input}"
Intent:
"""
        # Initialize the model
        model = genai.GenerativeModel("gemini-1.5-flash")  # Use the correct model name
        # Generate content
        response = model.generate_content(
            prompt,
            generation_config={
                "temperature": 0.0,
                "max_output_tokens": 10
            }
        )
        intent = response.text.strip().lower()

        if intent not in self.possible_intents:
            return "unknown"
        return intent