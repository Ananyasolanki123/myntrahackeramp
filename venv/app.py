from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = 'sk-proj-HYTTRCunLlKJalXT0smIT3BlbkFJjFdr2TxYPjZbIKeo8Ehe'

@app.route('/generate', methods=['POST'])
def generate_text():
    data = request.get_json()
    prompt = data.get('prompt')
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=100
    )

    return jsonify(response.choices[0].text)

if __name__ == '__main__':
    app.run(debug=True)
