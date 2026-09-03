<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Build a RAG API with FastAPI

**Project Link:** [View Project](http://nextwork.ai/projects/ai-devops-api)

**Author:** Aniruddha Sharma  
**Email:** aniruddhakirthisharma@gmail.com

---

---

## Introducing Today's Project!

In this project, I'm going to implement a RAG API by creating a REST endpoint. This will help me understand REST API, and RAG. I'm interested in this because I want to know how to run private models and still access data from external sources.

### Key tools and concepts

The key tools I used include chromaDB, pydantic's BaseModel for validation, and filtering searches by user via a FastAPI endpoint.  Key concepts I learnt include multitenancy, RAG architecture, context injection. 

### Challenges and wins

The project took me 3 months to complete. The most challenging part was refactoring the code such that FastAPI did not contain any business logic.

---

## Performing RAG Manually

In this step, I'm going to manually implement RAG with an ollama model, set up a python virutal environment, install requirements from a requirements.txt file, and download the nomic-embed text model from ollama via `ollama pull`. RAG stands for Retrieval Augmented Generation and is a way to enable local models to access data from external sources.

![Image](http://nextwork.ai/heartfelt_orange_curious_grapefruit/uploads/ai-devops-api_v3j7x5b9)

### Understanding the three parts of RAG

I performed RAG manually by providing information about myself, and then asking a question based on the information provided. The three parts are:
1. Retrieval: Get the relevant text from the database. 
2. Augmentation: Add the relevant text into the prompt.
3. Generation: Generate the answers to the user query from the retrieved text added to the prompt.

### Comparing the two AI models

The key difference I noticed is that nomic embed text converts the query into vector embeddings which is compared against vector embeddings in a database to match the query to the records in the databse using semantic search. Qwen 2.5:0.5b generates responses by predicting the next token and is a conversational model.  

---

## Building a Personal Knowledge Base

In this step, I'm going to first create a document containing information about myself, create a python script that loads, and processes, and stores the information as embeddings, and lastly, run the script to verify the knowledge base exists. Embeddings are numerical representations of text from the information. 

![Image](http://nextwork.ai/heartfelt_orange_curious_grapefruit/uploads/ai-devops-api_g3h7m2r5)

### Creating the profile document

I included information about my interests, skills, and hobbies. This will enable the AI to retrieve the relevant information from the database according to the query. 

### How semantic search finds relevant chunks

When I ask a question, ChromaDB first converts my query into embeddings, and then compares similarity with the query embeddings to the embeddings created during chunking (semantic search). It then retrieves the text which has the least difference in the vector embedding values. 

---

## Creating the RAG API with FastAPI

In this step, I'm going to build an API that has an `/ask` endpoint which will send the query to the ollama model. In the backend, the query is passed on to nomic-embed-text to convert the query to a vector embedding, which will be compared with chromaDB's embeddings. I'll test it using Swagger UI.

![Image](http://nextwork.ai/heartfelt_orange_curious_grapefruit/uploads/ai-devops-api_j5m1r8t2)

### How the /ask endpoint works

When a question comes in, my endpoint first calls the client.query() with query, and n_results as arguments, which converts the query to a vector embedding, and returns the top 3 results according to the semantic search performed by chromaDB. The second step involves augmenting the prompt to include context from step 1 for the model to use while generating answers. The last step is generation, where the ollama.chat() function is used on the context, and the user query to generate the answers.

### Testing with Swagger UI

I tested my API by asking what is my name. The AI answered with Aniruddha Sharma. The context used was the data from the profile.txt.

---

## Extending to a Multi-User AI Directory

In this project extension, I'm adding multi-user support because information can be retrieved for any user and is not restricted to a single user. Multi-tenancy means providing support for multiple users in any piece of software. 

![Image](http://nextwork.ai/heartfelt_orange_curious_grapefruit/uploads/ai-devops-api_d5g9k3n7)

### Adding the POST /documents endpoint

In this project extension, I added a POST endpoint that stores the data in the database with the profile and the user name. Metadata filtering allows the response to be tailored according to the user_name reducing the amount of chunks to process.  

![Image](http://nextwork.ai/heartfelt_orange_curious_grapefruit/uploads/ai-devops-api_r8t2w6y1)

### Verifying multi-user filtering

In this project extension, I tested multi-user queries by adding the user_name in the user_name parameter. The filter works because the semantic search runs using the where parameter in the vector database enabling semantic search by user. 

---

## Wrapping Up

I did this project to learn how a RAG pipeline works, and to refactor code to hide business logic using modularity and granularity. Another skill I want to learn is AI deployment.

---

---
