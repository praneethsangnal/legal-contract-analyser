// function RiskAnalysisSection({
//     riskAnalysis,
//     handleRiskAnalysis,
//     uploaded
// }) {

//     return (

//         <section>

//             <h2>Risk Analysis</h2>

//             <button
//                 onClick={handleRiskAnalysis}
//                 disabled={!uploaded}
//             >
//                 Analyze Risks
//             </button>

//             <br />
//             <br />

//             <p>{riskAnalysis}</p>

//             <hr />

//         </section>

//     );

// }

// export default RiskAnalysisSection;

function RiskAnalysisSection({
    riskAnalysis,
    handleRiskAnalysis,
    uploaded,
    isLoading,
}) {

    return (

        <section className="section section--risk">

            <div className="section__header">
                <h2 className="section__title">
                    <span className="section__title-icon">⚠️</span>
                    Risk Analysis
                </h2>

                <button
                    className="btn btn-primary"
                    onClick={handleRiskAnalysis}
                    disabled={!uploaded || isLoading}
                >
                    {isLoading && <span className="spinner" />}
                    {isLoading ? "Analyzing..." : "Analyze Risks"}
                </button>
            </div>

            <div className="section__body">
                {riskAnalysis ? (
                    <p>{riskAnalysis}</p>
                ) : (
                    <p className="section__empty">
                        {uploaded
                            ? "No risk analysis yet — click Analyze Risks."
                            : "Upload a contract to analyze its risks."}
                    </p>
                )}
            </div>

        </section>

    );

}

export default RiskAnalysisSection;