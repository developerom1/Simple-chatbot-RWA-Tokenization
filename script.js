const knowledgeBase = {
    "what is rwa tokenization": "RWA Tokenization is the process of converting real-world assets, such as real estate, art, or commodities, into digital tokens on a blockchain. This allows for fractional ownership, increased liquidity, and easier transfer of assets.",
    "how does rwa tokenization work": "Assets are digitized into tokens representing ownership shares. These tokens are issued on a blockchain, enabling secure, transparent trading and management of the underlying asset.",
    "benefits of rwa tokenization": "Benefits include fractional ownership (allowing more people to invest), improved liquidity (easier buying/selling), reduced intermediaries, and global accessibility.",
    "examples of rwa": "Examples include tokenizing real estate properties, fine art, commodities like gold, or even revenue streams from businesses.",
    "risks of rwa tokenization": "Risks involve regulatory uncertainty, market volatility, smart contract vulnerabilities, and potential lack of legal recognition for tokenized assets.",
    "why tokenize assets": "Tokenization enhances accessibility, reduces costs, increases transparency, and enables new financial products like DeFi integrations.",
    "blockchain in rwa": "Blockchain provides the secure, decentralized ledger for recording ownership and transactions of tokenized assets.",
    "fractional ownership": "Fractional ownership means dividing an asset into smaller, tradable shares via tokens, making high-value assets affordable to more investors."
};

const keywords = ['rwa', 'tokenization', 'real world asset', 'blockchain', 'fractional', 'ownership', 'liquidity', 'asset', 'token'];

function isRelevant(input) {
    const lowerInput = input.toLowerCase();
    return keywords.some(keyword => lowerInput.includes(keyword));
}

function getResponse(input) {
    const lowerInput = input.toLowerCase();
    for (const question in knowledgeBase) {
        if (lowerInput.includes(question)) {
            return knowledgeBase[question];
        }
    }
    // Fuzzy match or default
    return "I'm sorry, I can only assist with questions related to RWA Tokenization. Please ask something about real-world asset tokenization!";
}

function addMessage(message, isUser = false) {
    const chatMessages = document.getElementById('chat-messages');
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message');
    messageDiv.classList.add(isUser ? 'user-message' : 'bot-message');
    messageDiv.innerHTML = `<p>${message}</p>`;
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

document.getElementById('send-button').addEventListener('click', function() {
    const userInput = document.getElementById('user-input').value.trim();
    if (userInput) {
        addMessage(userInput, true);
        document.getElementById('user-input').value = '';
        if (isRelevant(userInput)) {
            const response = getResponse(userInput);
            setTimeout(() => addMessage(response), 500); // Simulate typing delay
        } else {
            setTimeout(() => addMessage("I'm sorry, I can only assist with questions related to RWA Tokenization. Please ask something about real-world asset tokenization!"), 500);
        }
    }
});

document.getElementById('user-input').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        document.getElementById('send-button').click();
    }
});
