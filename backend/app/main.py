from fastapi import FastAPI

app = FastAPI(
    title="Advanced RAG Book Intelligence",
    description="An advanced RAG system for understanding books.",
    version="1.0.0",
)


@app.get("/")
async def root():
    return {
        "message": "Advanced RAG Book Intelligence API"
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy"
    }