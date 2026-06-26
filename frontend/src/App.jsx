import { useState } from "react";

import Header from "./components/Header";
import UploadSection from "./components/UploadSection";
import QuestionSection from "./components/QuestionSection";
import AnswerSection from "./components/AnswerSection";
import SourcesSection from "./components/SourcesSection";

function App() {

  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");

  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const [sources, setSources] = useState([]);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleUpload = async () => {

    if (!file) {
      setMessage("Please select a PDF first.");
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

      setSources(data.sources);

    } catch (error) {

      console.error(error);

      setAnswer("Failed to get answer.");

      setSources([]);

    }

  };

  return (

    <div>

      <Header />

      <UploadSection
        file={file}
        message={message}
        handleFileChange={handleFileChange}
        handleUpload={handleUpload}
      />

      <QuestionSection
        question={question}
        setQuestion={setQuestion}
        handleAsk={handleAsk}
      />

      <AnswerSection
        answer={answer}
      />

      <SourcesSection
        sources={sources}
      />

    </div>

  );

}

export default App;