# RWA Tokenization Chatbot

A simple chatbot with an attractive UI designed to assist users with questions about Real World Asset (RWA) Tokenization. The chatbot operates strictly within this domain and refuses off-topic queries.

**Live Demo**: [https://developerom1.github.io/Simple-chatbot-RWA-Tokenization/](https://developerom1.github.io/Simple-chatbot-RWA-Tokenization/)

## Approach to Context Control

The chatbot maintains strict context by:
- Defining a set of allowed keywords related to RWA Tokenization (e.g., 'rwa', 'tokenization', 'blockchain').
- Checking user input for the presence of at least one keyword before processing.
- If no keywords are found, responding with a polite refusal message.
- Responses are limited to a predefined knowledge base of Q&A pairs, ensuring no drift outside the domain.

## Technical Overview

- **Frontend**: Static web application using HTML, CSS, and JavaScript.
- **Backend**: Python Flask API with static knowledge base for responses.
- **UI**: Responsive chat interface with modern styling (gradients, chat bubbles).
- **Logic**: Frontend validates input, sends to backend API; backend uses keyword matching and static responses.
- **No AI/Model**: Responses are predefined; no dynamic generation.

## Limitations

- **Scope**: Only answers predefined questions related to RWA Tokenization. Cannot handle complex queries, generate new content, or discuss unrelated topics.
- **Responses**: Limited to the knowledge base; no conversational memory or follow-up.
- **Technology**: Frontend-only for static, but backend for API; no persistence or advanced features.
- **Accuracy**: Based on static information; may not reflect the latest developments in RWA.

## Usage Documentation

### How to Use
1. Set up the backend (see below).
2. Open `index.html` in a web browser (or deploy frontend).
3. Type your question about RWA Tokenization.
4. Click "Send" or press Enter.
5. The chatbot will respond if relevant; otherwise, refuse.
