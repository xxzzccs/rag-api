import chromadb

from chromadb.utils.embedding_functions import OllamaEmbeddingFunction
from chromadb.api.types import Embeddable, EmbeddingFunction
from typing import cast

from app.os_config import ollama_url,db_path

client = chromadb.PersistentClient(path=f"{db_path}")

embedding_func = cast(EmbeddingFunction[Embeddable], OllamaEmbeddingFunction(
    url=f"{ollama_url}",
    model_name="nomic-embed-text:latest"
))

collection = client.get_or_create_collection(
    name="personal_profile",
    embedding_function=embedding_func
)