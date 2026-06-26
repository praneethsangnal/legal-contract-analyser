function RiskAnalysisSection({
    riskAnalysis,
    handleRiskAnalysis,
    uploaded
}) {

    return (

        <section>

            <h2>Risk Analysis</h2>

            <button
                onClick={handleRiskAnalysis}
                disabled={!uploaded}
            >
                Analyze Risks
            </button>

            <br />
            <br />

            <p>{riskAnalysis}</p>

            <hr />

        </section>

    );

}

export default RiskAnalysisSection;