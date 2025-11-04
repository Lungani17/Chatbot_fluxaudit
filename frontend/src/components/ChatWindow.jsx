import React, { useEffect, useRef, useState } from 'react';

function ChatWindow({ messages, onSendMessage }) {
  const messagesEndRef = useRef(null);
  
  // This state is now smarter: it checks the *initial* message
  const [showStarters, setShowStarters] = useState(() => 
    messages.length === 1 && messages[0].starters && messages[0].starters.length > 0
  );

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  const handleStarterClick = (starterText) => {
    onSendMessage(starterText); 
    setShowStarters(false); // Hide starters immediately on click
  };

  useEffect(() => {
    scrollToBottom();
    // If we have more than one message, hide the starters
    if (messages.length > 1 && showStarters) {
      setShowStarters(false);
    }
  }, [messages, showStarters]);

  return (
    <div className="flex-1 p-4 overflow-y-auto bg-gray-100">
      <div className="flex flex-col space-y-4">
        
        {messages.map((message, index) => {
          const isUserMessage = message.sender === 'user';
          return (
            <div 
              key={index} 
              className={`flex ${isUserMessage ? 'justify-end' : 'justify-start'}`}
            >
              <div
                className={`max-w-xs lg:max-w-md px-4 py-2 rounded-lg shadow ${
                  isUserMessage
                    ? 'bg-blue-600 text-white'
                    : 'bg-white text-gray-800'
                }`}
              >
                {message.text}
              </div>
            </div>
          );
        })}
        
        {/* Render Conversation Starters */}
        {showStarters && messages[0]?.starters && (
          <div className="flex flex-wrap gap-2 justify-start pt-2">
            {messages[0].starters.map((starter, index) => (
              <button
                key={index}
                onClick={() => handleStarterClick(starter)}
                className="px-4 py-2 bg-white border border-blue-500 text-blue-500 rounded-full shadow-md hover:bg-blue-50 transition-all text-sm"
              >
                {starter}
              </button>
            ))}
          </div>
        )}
        
        <div ref={messagesEndRef} />
      </div>
    </div>
  );
}

export default ChatWindow;