function SourcesSection({ sources }) {
  return (
    <section>

      <h2>Evidence</h2>

      {
        sources.map((source, index) => (

          <div key={index}>

            <h3>{source.title}</h3>

            <p>{source.text}</p>

            <hr />

          </div>

        ))
      }

    </section>
  );
}

export default SourcesSection;