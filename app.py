from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from frontend

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

SYSTEM_PROMPT = """
You are an AI assistant specialized in Real World Asset (RWA) Tokenization. You must only answer questions related to RWA tokenization, blockchain, fractional ownership, asset tokenization, and related topics. If a question is not related to this domain, politely refuse to answer and redirect to RWA topics.

Key topics you can discuss:
- What is RWA tokenization?
- How does it work?
- Benefits and risks.
- Examples of RWAs.
- Blockchain in RWAs.
- Fractional ownership.

Do not discuss or provide information on any other topics.
"""

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')

    if not user_message:
        return jsonify({'response': 'Please provide a message.'})

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ],
            max_tokens=150,
            temperature=0.7
        )
        ai_response = response.choices[0].message.content
        if ai_response:
            ai_response = ai_response.strip()
        else:
            ai_response = "Sorry, I couldn't generate a response."

        # Additional check: if response doesn't contain RWA keywords, refuse
        rwa_keywords = ['rwa', 'tokenization', 'blockchain', 'asset', 'fractional', 'ownership']
        if not any(keyword in ai_response.lower() for keyword in rwa_keywords):
            ai_response = "I'm sorry, I can only assist with questions related to RWA Tokenization. Please ask something about real-world asset tokenization!"

        return jsonify({'response': ai_response})
    except Exception as e:
        return jsonify({'response': 'Sorry, an error occurred. Please try again.'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
