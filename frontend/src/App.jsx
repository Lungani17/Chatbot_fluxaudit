import React, { useState } from 'react';
import axios from 'axios'; // 1. Import axios
import Header from './components/Header';
import ChatWindow from './components/ChatWindow';
import InputBar from './components/InputBar';

// --- CONVERSATION STARTERS ---
const conversationStarters = [
  "Hi",
  "What is FluxAudit?",
  "What problem does it solve?",
  "What are its core features?",
  "Who uses it?",
  "Can it make reports?"
];

// --- API URL ---
const CHAT_API_URL = "http://127.0.0.1:5000/chat";

function App() {
  const [messages, setMessages] = useState([
    {
      sender: 'bot',
      text: "Hello! I'm the FluxAudit bot. How can I help you?",
      starters: conversationStarters
    }
  ]);

  const handleSendMessage = async (userMessage) => {
    // 1. Hide starters and add the user's message
    const newMessages = messages.map(msg => ({ ...msg, starters: [] }));
    const newUserMessage = { sender: 'user', text: userMessage };
    setMessages([...newMessages, newUserMessage]);

    try {
      // 2. Send the user's message to the backend
      const response = await axios.post(CHAT_API_URL, {
        message: userMessage
      });

      // 3. Create the bot's response message from the API
      const botResponse = {
        sender: 'bot',
        text: response.data.reply
      };

      // 4. Add the bot's response to the chat
      setMessages(prev => [...prev, botResponse]);

    } catch (error) {
      console.error("Error sending message:", error);
      
      // 5. Add an error message to the chat if the API fails
      const errorResponse = {
        sender: 'bot',
        text: "I'm having trouble connecting to the server. Please try again later."
      };
      setMessages(prev => [...prev, errorResponse]);
    }
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-200">
      <div className="flex flex-col w-full max-w-md h-[700px] bg-white rounded-lg shadow-xl overflow-hidden">
        <Header />
        <ChatWindow
          messages={messages}
          onSendMessage={handleSendMessage}
        />
        <InputBar onSendMessage={handleSendMessage} />
      </div>
    </div>
  );
}

export default App;