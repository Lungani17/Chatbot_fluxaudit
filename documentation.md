# Chatbot Documentation

## Introduction

This document provides a comprehensive overview of the FluxAudit chatbot, a conversational AI designed to answer questions about the FluxAudit platform. The chatbot is built with a Python backend and a React frontend, providing a seamless user experience.

## Backend

The backend is a Python application built with the Flask web framework. It provides a simple API for the frontend to interact with the chatbot.

### Flask Application (`app.py`)

The `app.py` file contains the Flask application. It defines a single API endpoint:

-   **`/chat`** (POST): This endpoint receives a JSON payload with a "message" key and returns a JSON response with the chatbot's reply.

### Chatbot Logic (`flux_bot.py`)

The core chatbot logic resides in the `flux_bot.py` file. It uses a knowledge base and the `fuzzywuzzy` library to find the most relevant response to a user's message.

### Knowledge Base

The knowledge base is a Python dictionary in `flux_bot.py` that contains a collection of topics, keywords, and responses. When a user sends a message, the chatbot uses fuzzy string matching to compare the user's message to the keywords in the knowledge base and find the best match.

## Frontend

The frontend is a single-page application built with React and Vite. It provides a user-friendly interface for interacting with the chatbot.

### `App.jsx`

This is the main component of the application. It manages the state of the chat messages and handles sending and receiving messages from the backend.

### Components

The UI is broken down into several smaller components:

-   **`Header.jsx`**: Displays the header of the chat window.
-   **`ChatWindow.jsx`**: Displays the chat messages.
-   **`InputBar.jsx`**: Provides a text input for the user to type their message and a send button.

### API Interaction

The frontend uses the `axios` library to make POST requests to the backend's `/chat` endpoint. When a user sends a message, the frontend sends the message to the backend and displays the chatbot's response in the chat window.

## How to Run

To run the chatbot, you will need to start both the backend and frontend servers.

### Backend

1.  Navigate to the `backend` directory:
    ```bash
    cd backend
    ```
2.  Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
3.  Start the Flask development server:
    ```bash
    flask run
    ```
    The backend server will be running at `http://127.0.0.1:5000`.

### Frontend

1.  Navigate to the `frontend` directory:
    ```bash
    cd frontend
    ```
2.  Install the required Node.js packages:
    ```bash
    npm install
    ```
3.  Start the Vite development server:
    ```bash
    npm run dev
    ```
    The frontend server will be running at `http://localhost:5173`.
