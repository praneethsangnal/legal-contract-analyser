function QuestionSection({
  question,
  setQuestion,
  handleAsk,
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

      <button onClick={handleAsk}>
        Ask
      </button>

      <hr />

    </section>
  );
}

export default QuestionSection;