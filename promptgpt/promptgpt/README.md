## PromptGPT.py
import openai

class PromptGPT:
    def __init__(self, user_prompt: str):
        self.user_prompt = user_prompt
        self.optimized_prompt = ""

    def generate_prompt(self) -> str:
        """
        This function generates an optimized prompt using GPT-3 model from OpenAI.
        """
        response = openai.Completion.create(engine="text-davinci-002", prompt=self.user_prompt, max_tokens=60)
        self.optimized_prompt = response.choices[0].text.strip()
        return self.optimized_prompt

## main.py
from flask import Flask, request, jsonify
from PromptGPT import PromptGPT

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    user_prompt = data.get('user_prompt')
    if not user_prompt:
        return jsonify({'error': 'user_prompt is required'}), 400
    try:
        promptgpt = PromptGPT(user_prompt)
        optimized_prompt = promptgpt.generate_prompt()
        return jsonify({'optimized_prompt': optimized_prompt})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

## Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Add current directory files into container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run main.py when the container launches
CMD ["python", "main.py"]

## requirements.txt
flask==1.1.2
openai==0.27.0
docker==5.0.3
react==17.0.2

## README.md
