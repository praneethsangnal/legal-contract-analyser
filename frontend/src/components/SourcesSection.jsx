function SourcesSection({ sources }) {
  return (
    <section>

      <h2>Sources</h2>

      {
        sources.length === 0
          ? (
              <p>No sources available.</p>
            )
          : (
              <ul>
                {
                  sources.map((source) => (
                    <li key={source.chunk_id}>
                      {source.chunk_id} ({(source.score * 100).toFixed(2)}%)
                    </li>
                  ))
                }
              </ul>
            )
      }

    </section>
  );
}

export default SourcesSection;