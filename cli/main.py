from agents.planner import PlannerAgent
import os
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
def main():
    agent = PlannerAgent()

    while True:
        user_input = input("🧠 You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        response = agent.handle_input(user_input)
        print(f"🤖 Agent: {response}")

if __name__ == "__main__":
    main()
