## PromptGPT.py
import openai

class PromptGPT:
    def __init__(self, user_prompt: str):
        self.user_prompt = user_prompt
        self.optimized_prompt = ""

    def generate_prompt(self, user_prompt: str) -> str:
        """
        This function generates an optimized prompt using GPT-3 model from OpenAI.
        """
        self.user_prompt = user_prompt
        response = openai.Completion.create(engine="text-davinci-002", prompt=self.user_prompt, max_tokens=60)
        self.optimized_prompt = response.choices[0].text.strip()
        return self.optimized_prompt
