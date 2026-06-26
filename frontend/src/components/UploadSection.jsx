function UploadSection({
  file,
  message,
  handleFileChange,
  handleUpload,
}) {
  return (
    <section>

      <h2>Upload Contract</h2>

      <input
        type="file"
        accept=".pdf"
        onChange={handleFileChange}
      />

      <br />
      <br />

      <button onClick={handleUpload}>
        Upload
      </button>

      <br />
      <br />

      <p>
        {file ? file.name : "No file selected"}
      </p>

      <p>{message}</p>

      <hr />

    </section>
  );
}

export default UploadSection;