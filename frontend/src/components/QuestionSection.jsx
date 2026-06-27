// function QuestionSection({
//   question,
//   setQuestion,
//   handleAsk,
//   uploaded,
// }) {
//   return (
//     <section>

//       <h2>Ask a Question</h2>

//       <input
//         type="text"
//         placeholder="Enter your question..."
//         value={question}
//         onChange={(e) => setQuestion(e.target.value)}
//       />

//       <br />
//       <br />

//       <button
//         onClick={handleAsk}
//         disabled={!uploaded}
//       >
//         Ask
//       </button>

//       <hr />

//     </section>
//   );
// }

// export default QuestionSection;

function QuestionSection({
  question,
  setQuestion,
  handleAsk,
  uploaded,
  isLoading,
}) {
  return (
    <section className="section">

      <div className="section__header">
        <h2 className="section__title">
          <span className="section__title-icon">💬</span>
          Ask a Question
        </h2>
      </div>

      <div className="question-row">
        <input
          className="text-input"
          type="text"
          placeholder={
            uploaded
              ? "Enter your question..."
              : "Upload a contract to ask questions"
          }
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          disabled={!uploaded}
        />

        <button
          className="btn btn-primary"
          onClick={handleAsk}
          disabled={!uploaded || isLoading}
        >
          {isLoading && <span className="spinner" />}
          {isLoading ? "Asking..." : "Ask"}
        </button>
      </div>

    </section>
  );
}

export default QuestionSection;