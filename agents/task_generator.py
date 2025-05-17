import google.generativeai as genai

class GeneratorAgent:
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-2.0-flash")

    def generate(self, instruction: str) -> str:
        prompt = f"Generate based on instruction:\n{instruction}"
        response = self.model.generate_content(prompt)
        return response.text or "No output generated."
