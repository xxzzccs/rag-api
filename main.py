from fastapi import FastAPI

from typing import cast
from typing import Any

from db_config import client, collection

from build_knowledge_base import build_knowledge_base
from document import Document

import rag


app = FastAPI()

@app.get("/ask")
def ask(query:str, user:str=None) -> dict[str, Any]:
    return rag.rag(query, user)

@app.post("/documents")
def create_profile(document:Document):
    chunk_length = build_knowledge_base(document)
    return {
            "message":f"Profile created for user {document.user_name}",
            "user": document.user_name,
            "chunks": chunk_length   
        }