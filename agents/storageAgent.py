import json
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class StorageAgent:
    def __init__(self, storage_file="storage.json"):
        self.storage_file = storage_file
        if os.path.exists(self.storage_file):
            with open(self.storage_file, "r") as f:
                self.data = json.load(f)
        else:
            self.data = {}

    def _normalize_key(self, key: str) -> str:
        return key.strip().lower() if key else "default"

    def _save(self):
        with open(self.storage_file, "w") as f:
            json.dump(self.data, f, indent=2)

    def store(self, key: str, value: str) -> str:
        normalized_key = self._normalize_key(key)
        self.data[normalized_key] = value
        self._save()
        return "Got it! I've saved that info for you."

    def recall(self, key: str) -> str:
        normalized_key = self._normalize_key(key)
        stored_value = self.data.get(normalized_key)
        if stored_value:
            # Use LLM to reformat before returning
            return self._llm_reformat(stored_value, normalized_key)
        else:
            return f"Sorry, I don't have any information saved under '{normalized_key}'."

    def _llm_reformat(self, text: str, key: str) -> str:
        prompt = f"""
You are a helpful assistant. Rephrase the following stored information naturally as if you are telling a person that what they have stored about what
e.g what is my project about?
answer = your project is about.....

Key: {key}
Information: {text}

Response:
"""
        try:
            # Initialize the model
            model = genai.GenerativeModel("gemini-1.5-flash")
            # Generate content
            response = model.generate_content(
                prompt,
                generation_config={
                    "temperature": 0.7,
                    "max_output_tokens": 150
                }
            )
            return response.text.strip()
        except Exception as e:
            return f"Error reformatting text: {str(e)}"