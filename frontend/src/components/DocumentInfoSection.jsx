function DocumentInfoSection({ file, documentInfo }) {

  if (!documentInfo) {
    return null;
  }

  return (
    <section>

      <h2>Document Information</h2>

      <p>
        <strong>📄 File Name:</strong> {file?.name}
      </p>

      <p>
        <strong>📑 Pages:</strong> {documentInfo.page_count}
      </p>

      <p>
        <strong>🧩 Chunks Created:</strong> {documentInfo.num_chunks}
      </p>

      <p>
        <strong>📖 Document Type:</strong> {documentInfo.extraction_method}
      </p>

      <p>
        <strong>⏱ Processing Time:</strong> {documentInfo.processing_time} seconds
      </p>

      <hr />

    </section>
  );
}

export default DocumentInfoSection;