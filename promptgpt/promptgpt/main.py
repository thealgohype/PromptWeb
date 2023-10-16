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
        optimized_prompt = promptgpt.generate_prompt(user_prompt)
        return jsonify({'optimized_prompt': optimized_prompt})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
