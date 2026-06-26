function SummarySection({
    summary,
    handleSummary,
    uploaded
}) {
    return (
        <section>

            <h2>Contract Summary</h2>

            <button
                onClick={handleSummary}
                disabled={!uploaded}
            >
                Generate Summary
            </button>

            <br />
            <br />

            <p>{summary}</p>

            <hr />

        </section>
    );
}

export default SummarySection;