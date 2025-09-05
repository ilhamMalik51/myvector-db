from fastapi import FastAPI

from db.vector_db import VectorDB
from schema.request import (
    SearchRequest, InsertDocumentRequest
)

app = FastAPI(title="My Vector DB", openapi_prefix="/api")
vector_db = VectorDB()

@app.get("/")
def get_index():
    return {
        "success": "OK",
        "message": "Welcome to my vector db backend"
    }

@app.post("/search")
async def search_document(request: SearchRequest):
    context_data = vector_db.search(query_vector=request.vector, k=request.k)

    return {"data": context_data}

@app.post("/document")
async def insert_document(request: InsertDocumentRequest):
    vector_db.add(vecs=request.vector, content=request.content)

    return {"success": True}

@app.get("/document")
async def get_documents():
    return {"data": vector_db.get_docs_size()}