import { useState } from "react";

function App() {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");

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
    </div>
  );
}

export default App;