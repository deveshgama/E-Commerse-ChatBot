import { useState } from "react";
import axios from "axios";

export default function Chatbot() {
  const [messages, setMessages] = useState([]);
  const [query, setQuery] = useState("");

  const sendQuery = async () => {
    const res = await axios.get(`http://localhost:5000/api/products?q=${query}`);
    setMessages([...messages, { type: "user", text: query }, { type: "bot", text: res.data.map(p => `${p.name} - $${p.price}`).join('\n') }]);
    setQuery("");
  };

  return (
    <div className="p-4 max-w-md mx-auto">
      <div className="border h-80 overflow-y-auto mb-2 p-2">
        {messages.map((m, i) => <div key={i} className={m.type === "user" ? "text-right" : "text-left"}>{m.text}</div>)}
      </div>
      <input
        className="w-full p-2 border"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && sendQuery()}
        placeholder="Search for a product..."
      />
    </div>
  );
}
