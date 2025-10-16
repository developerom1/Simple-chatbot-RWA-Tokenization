# RWA Tokenization AI Chatbot

An AI-powered chatbot with an attractive UI designed to assist users with questions about Real World Asset (RWA) Tokenization. The chatbot operates strictly within this domain and refuses off-topic queries.

## Approach to Context Control

The chatbot uses a system prompt in the AI model to limit responses to RWA Tokenization topics. Additionally, client-side keyword filtering ensures only relevant queries are sent to the backend. If the AI response lacks RWA keywords, a refusal is returned.

## Technical Overview

- **Frontend**: Static web application using HTML, CSS, and JavaScript.
- **Backend**: Python Flask API with OpenAI GPT-3.5-turbo for AI responses.
- **UI**: Responsive chat interface with modern styling (gradients, chat bubbles).
- **Logic**: Frontend validates input, sends to backend API; backend uses AI with system prompt for context control.
- **AI Model**: GPT-3.5-turbo with custom system prompt to enforce domain limits.

## Limitations

- **Scope**: Only answers questions related to RWA Tokenization; off-topic queries are refused.
- **Responses**: AI-generated, but constrained; no conversational memory.
- **Technology**: Requires OpenAI API key; backend needs hosting.
- **Accuracy**: Depends on AI model; may not be 100% accurate or up-to-date.

## Usage Documentation

### How to Use
1. Set up the backend (see below).
2. Open `index.html` in a web browser (or deploy frontend).
3. Type your question about RWA Tokenization.
4. Click "Send" or press Enter.
5. The AI will respond if relevant; otherwise, refuse.

### What to Expect
- Relevant questions get AI-generated answers.
- Off-topic queries get refusals.
- Chat-like experience with typing delay.

## Setup and Deployment

### Backend Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Set OpenAI API key in `.env`: `OPENAI_API_KEY=your_key`
3. Run locally: `python app.py` (runs on http://localhost:5000)

### Frontend Deployment
Deploy static files (`index.html`, `style.css`, `script.js`) to GitHub Pages as before. Update `script.js` fetch URL to deployed backend.

### Backend Deployment (Free)
Use Railway or Heroku:
- **Railway**: Connect GitHub repo, set environment variables, deploy.
- **Heroku**: Create app, push code, set config vars.
Update frontend fetch URL to deployed backend URL.
