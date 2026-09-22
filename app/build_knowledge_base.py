import chromadb

from typing import cast
from chromadb.api.types import Embeddable, EmbeddingFunction
from chromadb.utils.embedding_functions.ollama_embedding_function import OllamaEmbeddingFunction

from document import Document
from db_config import client, collection, embedding_func


# Read the file in context manager, split into chunks (split on new lines) 
# and add or create a collection in chromadb

def build_knowledge_base(doc: Document):
    text = doc.profile

    chunks = [line.strip() for line in text.split("\n\n") if line.strip()]

    print(f"{len(chunks)} chunks successfully loaded.")

    collections = collection

    collections.add(
        ids=[f"{doc.user_name}-chunk{i}" for i in range(len(chunks))],
        documents=chunks,
        metadatas=[{"source":"profile string", 
                    "user_name": doc.user_name,
                    "chunk_index":i} for i in range(len(chunks))] 
    )

    print(f"Added {len(chunks)} for user {doc.user_name}")
    print("Knowledge base built successfully!")
    
    return len(chunks)