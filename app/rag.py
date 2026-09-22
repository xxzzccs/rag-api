import ollama
import chromadb
from typing import cast
from typing import Any

from chromadb.api.types import Embeddable, QueryResult
# from chromadb.utils.embedding_functions import OllamaEmbeddingFunction

from db_config import client, collection

def rag(query:str, user:str=None) -> dict[str, Any]:
   #ChromaDB converts query to vector embedding, and returns the top 3 results matching query (Retrieval)
    query_params = {
       "query_texts": [query],
       "n_results": 2
    }
    if user:
        query_params["where"]={"user_name": user}
    
    results: QueryResult = collection.query(**query_params)
    
    context = "\n\n"
    if "documents" in results:
        context = context.join(results["documents"][0])
    else:
        raise ValueError("Results is missing documents!")

    #Augmenting the prompt with added context
    agent_prompt = f"""Use the following context to answer the question.
                    If the context doesn't contain relevant information, say so. 
                    
                    Context: 
                    {context}
                    
                    Question:
                    {query}
                    """
    
    #Generating the response with the qwen2.5:0.5b model with the augmented prompt
    response = ollama.chat(
        model="qwen2.5:0.5b", 
        messages=[{"role": "user", "content": agent_prompt}]
    )
    
    return {
        "question": query,
        "answer": response["message"]["content"],
        "context_used": results["documents"][0],
        "filtered_by_user": user
    }