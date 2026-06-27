// import { useState } from "react";

// function SourcesSection({ sources }) {

//   const [expanded, setExpanded] = useState({});

//   const toggleEvidence = (index) => {
//     setExpanded((prev) => ({
//       ...prev,
//       [index]: !prev[index],
//     }));
//   };

//   return (
//     <section>

//       <h2>Evidence</h2>

//       {
//         sources.map((source, index) => {

//           const isExpanded = expanded[index];

//           const preview =
//             source.text.length > 300
//               ? source.text.slice(0, 300) + "..."
//               : source.text;

//           return (

//             <div key={index}>

//               <h3>📄 {source.title}</h3>

//               <p>
//                 {isExpanded ? source.text : preview}
//               </p>

//               {
//                 source.text.length > 300 && (
//                   <button
//                     onClick={() => toggleEvidence(index)}
//                   >
//                     {isExpanded ? "Show Less ▲" : "Show More ▼"}
//                   </button>
//                 )
//               }

//               <hr />

//             </div>

//           );

//         })
//       }

//     </section>
//   );
// }

// export default SourcesSection;


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
    <section className="section">

      <div className="section__header">
        <h2 className="section__title">
          <span className="section__title-icon">🔎</span>
          Evidence
        </h2>
      </div>

      {
        sources.map((source, index) => {

          const isExpanded = expanded[index];

          const preview =
            source.text.length > 300
              ? source.text.slice(0, 300) + "..."
              : source.text;

          return (

            <div className="evidence-card" key={index}>

              <h3 className="evidence-card__title">📄 {source.title}</h3>

              <p className="evidence-card__text">
                {isExpanded ? source.text : preview}
              </p>

              {
                source.text.length > 300 && (
                  <button
                    className="evidence-card__toggle"
                    onClick={() => toggleEvidence(index)}
                  >
                    {isExpanded ? "Show Less ▲" : "Show More ▼"}
                  </button>
                )
              }

            </div>

          );

        })
      }

    </section>
  );
}

export default SourcesSection;