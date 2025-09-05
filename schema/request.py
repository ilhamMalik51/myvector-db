from pydantic import BaseModel

class SearchRequest(BaseModel):
    vector: list
    k: int

class InsertDocumentRequest(BaseModel):
    vector: list
    content: str