
import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    if (!input) return;
    const res = await fetch('http://localhost:10000/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: input })
    });
    const data = await res.json();
    setMessages([...messages, { user: input, ai: data.response }]);
    setInput("");
  };

  return (
    <div className="chat-container">
      <h1>Kitenga Chat 🐺</h1>
      <div className="messages">
        {messages.map((msg, i) => (
          <div key={i}>
            <div><strong>You:</strong> {msg.user}</div>
            <div><strong>Kitenga:</strong> {msg.ai}</div>
          </div>
        ))}
      </div>
      <input value={input} onChange={(e) => setInput(e.target.value)} placeholder="Type your message..." />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
}

export default App;
