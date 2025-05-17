import google.generativeai as genai

class SummarizerAgent:
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-2.0-flash")

    def summarize(self, text: str) -> str:
        prompt = f"Summarize this:\n{text}"
        response = self.model.generate_content(prompt)
        return response.text or "No summary available."
