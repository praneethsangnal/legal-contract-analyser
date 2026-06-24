from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel

from ingestion.ingest_document import ingest_document
from retrieval.vector_retriever import search as vector_search
from retrieval.bm25_retriever import search as bm25_search
from retrieval.rrf import reciprocal_rank_fusion
from retrieval.reranker import rerank
from llm.groq_client import generate_answer

from config import CONTRACTS_DIR


app = FastAPI()


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

        sources = [
            {
                "chunk_id": result["id"],
                "score": float(result["score"])
            }
            for result in reranked_results
        ]

        return {
            "question": query,
            "answer": answer,
            "sources": sources
        }

    except Exception as e:
        return {
            "error": str(e)
        }
    