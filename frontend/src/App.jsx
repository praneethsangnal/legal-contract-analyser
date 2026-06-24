import { useState } from "react";

function App() {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const handleUpload = async () => {
    if (!file) {
      setMessage("Please select a PDF first");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/upload",
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();
      setMessage(data.message);
    } catch (error) {
      console.error(error);
      setMessage("Upload Failed");
    }
  };

  const handleAsk = async () => {
    if (!question.trim()) {
      return;
    }

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/ask",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            question: question,
          }),
        }
      );

      const data = await response.json();
      setAnswer(data.answer);
    } catch (error) {
      console.error(error);
      setAnswer("Failed to get answer");
    }
  };

  return (
    <div>
      <h1>Legal Contract Analyzer</h1>

      <br />

      <input
        type="file"
        accept=".pdf"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br />
      <br />

      <button onClick={handleUpload}>
        Upload
      </button>

      <br />
      <br />

      <p>
        {file ? file.name : "No file selected"}
      </p>

      <br />

      <p>{message}</p>

      <br />
      <hr />
      <br />

      <h2>Ask a Question</h2>

      <input
        type="text"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Enter your question"
      />

      <br />
      <br />

      <button onClick={handleAsk}>
        Ask
      </button>

      <br />
      <br />

      <h2>Answer</h2>

      <p>{answer}</p>
    </div>
  );
}

export default App;