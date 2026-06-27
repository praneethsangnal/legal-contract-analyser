// function DocumentInfoSection({ file, documentInfo }) {

//   if (!documentInfo) {
//     return null;
//   }

//   return (
//     <section>

//       <h2>Document Information</h2>

//       <p>
//         <strong>📄 File Name:</strong> {file?.name}
//       </p>

//       <p>
//         <strong>📑 Pages:</strong> {documentInfo.page_count}
//       </p>

//       <p>
//         <strong>🧩 Chunks Created:</strong> {documentInfo.num_chunks}
//       </p>

//       <p>
//         <strong>📖 Document Type:</strong> {documentInfo.extraction_method}
//       </p>

//       <p>
//         <strong>⏱ Processing Time:</strong> {documentInfo.processing_time} seconds
//       </p>

//       <hr />

//     </section>
//   );
// }

// export default DocumentInfoSection;


function DocumentInfoSection({ file, documentInfo }) {

  if (!documentInfo) {
    return null;
  }

  return (
    <section className="section">

      <div className="section__header">
        <h2 className="section__title">
          <span className="section__title-icon">📋</span>
          Document Information
        </h2>
      </div>

      <div className="info-grid">

        <div className="info-card info-card--filename">
          <div className="info-card__label">📄 File Name</div>
          <div className="info-card__value">{file?.name}</div>
        </div>

        <div className="info-card">
          <div className="info-card__label">📑 Pages</div>
          <div className="info-card__value">{documentInfo.page_count}</div>
        </div>

        <div className="info-card">
          <div className="info-card__label">🧩 Chunks</div>
          <div className="info-card__value">{documentInfo.num_chunks}</div>
        </div>

        <div className="info-card">
          <div className="info-card__label">📖 Doc Type</div>
          <div className="info-card__value">{documentInfo.extraction_method}</div>
        </div>

        <div className="info-card">
          <div className="info-card__label">⏱ Processing</div>
          <div className="info-card__value">{documentInfo.processing_time}s</div>
        </div>

      </div>

    </section>
  );
}

export default DocumentInfoSection;