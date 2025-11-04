import React, { useState } from 'react';

// We receive the 'onSendMessage' function as a prop from App.jsx
function InputBar({ onSendMessage }) {
  // This state holds the text as the user types
  const [message, setMessage] = useState('');

  // This function runs when the "Send" button is clicked or Enter is pressed
  const handleSubmit = (e) => {
    e.preventDefault(); // Prevents the page from refreshing on form submit
    const trimmedMessage = message.trim();

    if (trimmedMessage) {
      onSendMessage(trimmedMessage); // Send the message up to the App component
      setMessage(''); // Clear the input field after sending
    }
  };

  return (
    <div className="p-4 bg-white border-t border-gray-200">
      <form className="flex space-x-3" onSubmit={handleSubmit}>
        <input
          type="text"
          className="flex-1 px-4 py-2 border border-gray-300 rounded-full focus:outline-none focus:ring-2 focus:ring-blue-500"
          placeholder="Enter your message..."
          value={message}
          onChange={(e) => setMessage(e.target.value)}
        />
        <button
          type="submit"
          className="px-6 py-2 font-semibold text-white bg-blue-600 rounded-full hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
        >
          Send
        </button>
      </form>
    </div>
  );
}

export default InputBar;