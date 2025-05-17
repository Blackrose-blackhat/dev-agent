from agents.storageAgent import StorageAgent
from agents.task_generator import GeneratorAgent
from agents.task_summarizer import SummarizerAgent
from utils.intent_classifier import IntentClassifier

class PlannerAgent:
    def __init__(self):
        self.summarizer = SummarizerAgent()
        self.generator = GeneratorAgent()
        self.storage = StorageAgent()
        self.classifier = IntentClassifier()

    def handle_input(self, user_input: str) -> str:
        intent = self.classifier.classify(user_input)
        
        if intent == "summarize":
            # existing code...
            pass
        elif intent == "generate":
            # existing code...
            pass
        elif intent == "store":
            key, value = self.extract_storage_data(user_input)
            return self.storage.store(key, value)
        elif intent == "recall":
            key = self.extract_recall_key(user_input)
            return self.storage.recall(key)
        else:
            return "❓ Sorry, I couldn't understand your request."

    def extract_storage_data(self, text: str) -> tuple[str, str]:
        # naive parsing: "store project description: this is my project"
        try:
            _, rest = text.lower().split("store", 1)
            key_value = rest.strip().split(":", 1)
            if len(key_value) == 2:
                key = key_value[0].strip()
                value = key_value[1].strip()
                return key, value
            else:
                return "default", rest.strip()
        except Exception:
            return "default", text

    def extract_recall_key(self, text: str) -> str:
        try:
            _, rest = text.lower().split("recall", 1)
            return rest.strip()
        except Exception:
            return "default"
