# RWA Tokenization Chatbot

A simple, attractive chatbot designed to assist users with questions about Real World Asset (RWA) Tokenization. The chatbot operates strictly within this domain and refuses off-topic queries.

## Approach to Context Control

The chatbot maintains strict context by:
- Defining a set of allowed keywords related to RWA Tokenization (e.g., 'rwa', 'tokenization', 'blockchain', 'fractional ownership').
- Checking user input for the presence of at least one keyword before processing.
- If no keywords are found, responding with a polite refusal message.
- Responses are limited to a predefined knowledge base of Q&A pairs, ensuring no drift outside the domain.

## Technical Overview

- **Structure**: Static web application using HTML, CSS, and JavaScript.
- **UI**: Responsive chat interface with modern styling (gradients, chat bubbles).
- **Logic**: Client-side JavaScript handles input validation, keyword matching, and response generation.
- **Knowledge Base**: Hardcoded object with common questions and answers on RWA Tokenization.
- **No Training/Model**: No machine learning; responses are exact or fuzzy-matched from the knowledge base.
- **Contextual Constraints**: Enforced via keyword filtering; no external APIs or dynamic content.

## Limitations

- **Scope**: Only answers predefined questions related to RWA Tokenization. Cannot handle complex queries, generate new content, or discuss unrelated topics.
- **Responses**: Limited to the knowledge base; no conversational memory or follow-up.
- **Technology**: Frontend-only; no backend for persistence or advanced features.
- **Accuracy**: Based on static information; may not reflect the latest developments in RWA.

## Usage Documentation

### How to Use
1. Open `index.html` in a web browser.
2. Type your question about RWA Tokenization in the input field.
3. Click "Send" or press Enter.
4. The chatbot will respond if the query is relevant; otherwise, it will politely refuse.

### What to Expect
- Relevant questions (e.g., "What is RWA tokenization?") will receive informative answers.
- Off-topic queries (e.g., "What's the weather?") will be met with a refusal message.
- The interface is user-friendly, with a chat-like experience.

## Deployment

This is a static site, deployable for free on GitHub Pages:
1. Create a GitHub repository.
2. Upload the files: `index.html`, `style.css`, `script.js`, `README.md`.
3. Enable GitHub Pages in repository settings (source: main branch).
4. Access the site at `https://yourusername.github.io/repositoryname/`.

For local testing, open `index.html` in your browser.
