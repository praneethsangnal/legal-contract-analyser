// function UploadSection({
//   file,
//   message,
//   handleFileChange,
//   handleUpload,
// }) {
//   return (
//     <section>

//       <h2>Upload Contract</h2>

//       <input
//         type="file"
//         accept=".pdf"
//         onChange={handleFileChange}
//       />

//       <br />
//       <br />

//       <button onClick={handleUpload}>
//         Upload
//       </button>

//       <br />
//       <br />

//       <p>
//         {file ? file.name : "No file selected"}
//       </p>

//       <p>{message}</p>

//       <hr />

//     </section>
//   );
// }

// export default UploadSection;


function UploadSection({
  file,
  message,
  handleFileChange,
  handleUpload,
  isUploading,
}) {
  const isError = message === "Upload Failed";

  return (
    <section className="section">

      <div className="section__header">
        <h2 className="section__title">
          <span className="section__title-icon">📤</span>
          Upload Contract
        </h2>
      </div>

      <div className="upload-box">
        <label className="upload-box__label">
          <span className="upload-box__icon">📄</span>
          <span>
            {file ? file.name : "Click to choose a PDF, or drag it here"}
          </span>
          <span className="upload-box__hint">PDF files only</span>

          <input
            type="file"
            accept=".pdf"
            onChange={handleFileChange}
          />
        </label>
      </div>

      <div className="upload-actions">
        <button
          className="btn btn-primary"
          onClick={handleUpload}
          disabled={isUploading}
        >
          {isUploading && <span className="spinner" />}
          {isUploading ? "Uploading..." : "Upload"}
        </button>
      </div>

      {message && (
        <p
          className={
            "upload-message " +
            (isError ? "upload-message--err" : "upload-message--ok")
          }
        >
          {message}
        </p>
      )}

    </section>
  );
}

export default UploadSection;