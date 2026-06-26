import { useState } from "react";

import Header from "./components/Header";
import UploadSection from "./components/UploadSection";
import SummarySection from "./components/SummarySection";
import RiskAnalysisSection from "./components/RiskAnalysisSection";
import QuestionSection from "./components/QuestionSection";
import AnswerSection from "./components/AnswerSection";
import SourcesSection from "./components/SourcesSection";

function App() {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [sources, setSources] = useState([]);
  const [summary, setSummary] = useState("");
  const [riskAnalysis, setRiskAnalysis] = useState("");
  const [contractUploaded, setContractUploaded] = useState(false);
  const [found, setFound] = useState(false);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
    setContractUploaded(false);
    setMessage("");
    setSummary("");
    setRiskAnalysis("");
    setQuestion("");
    setAnswer("");
    setSources([]);
    setFound(false);
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
      setContractUploaded(true);
      setSummary("");
      setRiskAnalysis("");
      setQuestion("");
      setAnswer("");
      setSources([]);
      setFound(false);
    } catch (error) {
      console.error(error);
      setMessage("Upload Failed");
      setContractUploaded(false);
    }
  };

  const handleSummary = async () => {
    if (!contractUploaded) {
      return;
    }

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/summary",
        {
          method: "POST"
        }
      );

      const data = await response.json();
      setSummary(data.summary);
    } catch (error) {
      console.error(error);
      setSummary("Failed to generate summary.");
    }
  };

  const handleRiskAnalysis = async () => {
    if (!contractUploaded) {
      return;
    }

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/risk-analysis",
        {
          method: "POST"
        }
      );

      const data = await response.json();
      setRiskAnalysis(data.risk_analysis);
    } catch (error) {
      console.error(error);
      setRiskAnalysis("Failed to generate risk analysis.");
    }
  };

  const handleAsk = async () => {
    if (!contractUploaded) {
      return;
    }

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
      setFound(data.found);
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

      <SummarySection
        summary={summary}
        handleSummary={handleSummary}
        uploaded={contractUploaded}
      />

      <RiskAnalysisSection
        riskAnalysis={riskAnalysis}
        handleRiskAnalysis={handleRiskAnalysis}
        uploaded={contractUploaded}
      />

      <QuestionSection
        question={question}
        setQuestion={setQuestion}
        handleAsk={handleAsk}
        uploaded={contractUploaded}
      />

      <AnswerSection
        answer={answer}
      />

      {found && sources.length > 0 && (
        <SourcesSection
          sources={sources}
        />
      )}
    </div>
  );
}

export default App;