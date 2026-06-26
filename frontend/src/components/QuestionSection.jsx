function QuestionSection({
  question,
  setQuestion,
  handleAsk,
  uploaded,
}) {
  return (
    <section>

      <h2>Ask a Question</h2>

      <input
        type="text"
        placeholder="Enter your question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />

      <br />
      <br />

      <button
        onClick={handleAsk}
        disabled={!uploaded}
      >
        Ask
      </button>

      <hr />

    </section>
  );
}

export default QuestionSection;