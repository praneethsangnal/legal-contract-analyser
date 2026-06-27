// function SummarySection({
//     summary,
//     handleSummary,
//     uploaded
// }) {
//     return (
//         <section>

//             <h2>Contract Summary</h2>

//             <button
//                 onClick={handleSummary}
//                 disabled={!uploaded}
//             >
//                 Generate Summary
//             </button>

//             <br />
//             <br />

//             <p>{summary}</p>

//             <hr />

//         </section>
//     );
// }

// export default SummarySection;

function SummarySection({
    summary,
    handleSummary,
    uploaded,
    isLoading,
}) {
    return (
        <section className="section">

            <div className="section__header">
                <h2 className="section__title">
                    <span className="section__title-icon">📝</span>
                    Contract Summary
                </h2>

                <button
                    className="btn btn-primary"
                    onClick={handleSummary}
                    disabled={!uploaded || isLoading}
                >
                    {isLoading && <span className="spinner" />}
                    {isLoading ? "Generating..." : "Generate Summary"}
                </button>
            </div>

            <div className="section__body">
                {summary ? (
                    <p>{summary}</p>
                ) : (
                    <p className="section__empty">
                        {uploaded
                            ? "No summary yet — click Generate Summary."
                            : "Upload a contract to generate a summary."}
                    </p>
                )}
            </div>

        </section>
    );
}

export default SummarySection;