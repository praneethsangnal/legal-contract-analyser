import { useState } from "react";

function SourcesSection({ sources }) {

  const [expanded, setExpanded] = useState({});

  const toggleEvidence = (index) => {
    setExpanded((prev) => ({
      ...prev,
      [index]: !prev[index],
    }));
  };

  return (
    <section>

      <h2>Evidence</h2>

      {
        sources.map((source, index) => {

          const isExpanded = expanded[index];

          const preview =
            source.text.length > 300
              ? source.text.slice(0, 300) + "..."
              : source.text;

          return (

            <div key={index}>

              <h3>📄 {source.title}</h3>

              <p>
                {isExpanded ? source.text : preview}
              </p>

              {
                source.text.length > 300 && (
                  <button
                    onClick={() => toggleEvidence(index)}
                  >
                    {isExpanded ? "Show Less ▲" : "Show More ▼"}
                  </button>
                )
              }

              <hr />

            </div>

          );

        })
      }

    </section>
  );
}

export default SourcesSection;