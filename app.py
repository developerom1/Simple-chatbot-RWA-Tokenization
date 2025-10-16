from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from frontend

knowledgeBase = {
    "what is rwa tokenization": "RWA Tokenization is the process of converting real-world assets, such as real estate, art, or commodities, into digital tokens on a blockchain. This allows for fractional ownership, increased liquidity, and easier transfer of assets.",
    "how does rwa tokenization work": "Assets are digitized into tokens representing ownership shares. These tokens are issued on a blockchain, enabling secure, transparent trading and management of the underlying asset.",
    "benefits of rwa tokenization": "Benefits include fractional ownership (allowing more people to invest), improved liquidity (easier buying/selling), reduced intermediaries, and global accessibility.",
    "examples of rwa": "Examples include tokenizing real estate properties, fine art, commodities like gold, or even revenue streams from businesses.",
    "risks of rwa tokenization": "Risks involve regulatory uncertainty, market volatility, smart contract vulnerabilities, and potential lack of legal recognition for tokenized assets.",
    "why tokenize assets": "Tokenization enhances accessibility, reduces costs, increases transparency, and enables new financial products like DeFi integrations.",
    "blockchain in rwa": "Blockchain provides the secure, decentralized ledger for recording ownership and transactions of tokenized assets.",
    "fractional ownership": "Fractional ownership means dividing an asset into smaller, tradable shares via tokens, making high-value assets affordable to more investors."
}

keywords = ['rwa', 'tokenization', 'real world asset', 'blockchain', 'fractional', 'ownership', 'liquidity', 'asset', 'token']

def isRelevant(input_str):
    lower_input = input_str.lower()
    return any(keyword in lower_input for keyword in keywords)

def getResponse(input_str):
    lower_input = input_str.lower()
    for question in knowledgeBase:
        if question in lower_input:
            return knowledgeBase[question]
    return "I'm sorry, I can only assist with questions related to RWA Tokenization. Please ask something about real-world asset tokenization!"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')

    if not user_message:
        return jsonify({'response': 'Please provide a message.'})

    if isRelevant(user_message):
        response = getResponse(user_message)
    else:
        response = "I'm sorry, I can only assist with questions related to RWA Tokenization. Please ask something about real-world asset tokenization!"

    return jsonify({'response': response})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
