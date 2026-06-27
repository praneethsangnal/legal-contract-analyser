// function AnswerSection({ answer }) {
//   return (
//     <section>

//       <h2>Answer</h2>

//       <p>{answer}</p>

//       <hr />

//     </section>
//   );
// }

// export default AnswerSection;


function AnswerSection({ answer }) {
  return (
    <section className="section">

      <div className="section__header">
        <h2 className="section__title">
          <span className="section__title-icon">✅</span>
          Answer
        </h2>
      </div>

      {answer ? (
        <div className="answer-card">
          <p>{answer}</p>
        </div>
      ) : (
        <p className="section__empty">
          Ask a question above to see the answer here.
        </p>
      )}

    </section>
  );
}

export default AnswerSection;