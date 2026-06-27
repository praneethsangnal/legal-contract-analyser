from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from app.ingestion.ingest_document import ingest_document
from app.retrieval.vector_retriever import search as vector_search
from app.retrieval.bm25_retriever import search as bm25_search
from app.retrieval.rrf import reciprocal_rank_fusion
from app.retrieval.reranker import rerank
from app.llm.question_answer import generate_answer
from app.llm.summary import generate_summary
from app.llm.risk_analysis import generate_risk_analysis
from app.config import CONTRACTS_DIR

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "http://localhost:5173",
    "https://legal-contract-analyser.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "Legal Contract Analyzer API Running"
    }


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        CONTRACTS_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

        file_path = CONTRACTS_DIR / file.filename

        with open(file_path, "wb") as pdf_file:
            pdf_file.write(
                await file.read()
            )

        result = ingest_document(file_path)

        return {
            "message": "Document processed successfully",
            "result": result
        }

    except Exception as e:
        return {
            "error": str(e)
        }


@app.post("/ask")
def ask_question(request: QuestionRequest):
    try:
        query = request.question

        vector_results = vector_search(
            query=query,
            n_results=10
        )

        bm25_results = bm25_search(
            query=query,
            n_results=10
        )

        rrf_results = reciprocal_rank_fusion(
            vector_results,
            bm25_results
        )

        reranked_results = rerank(
            query=query,
            results=rrf_results,
            top_k=3
        )

        answer = generate_answer(
            query=query,
            reranked_results=reranked_results
        )

        found = (
            answer.strip() != "I could not find this information in the contract."
        )

        sources = []

        if found:
            for i, result in enumerate(reranked_results):
                sources.append(
                    {
                        "title": f"Evidence {i + 1}",
                        "text": result["text"]
                    }
                )

        return {
            "question": query,
            "answer": answer,
            "found": found,
            "sources": sources
        }

    except Exception as e:
        return {
            "error": str(e)
        }
    

@app.post("/summary")
def contract_summary():
    try:
        summary = generate_summary()

        return {
            "summary": summary
        }

    except Exception as e:
        return {
            "error": str(e)
        }
    
    
@app.post("/risk-analysis")
def risk_analysis():
    try:
        report = generate_risk_analysis()

        return {
            "risk_analysis": report
        }

    except Exception as e:
        return {
            "error": str(e)
        }