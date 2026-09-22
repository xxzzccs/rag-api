import os 
from dotenv import load_dotenv

_ = load_dotenv()

#Loading the ollama server url and the path to save db data into environment
ollama_url = os.getenv("OLLAMA_URL")
db_path=os.getenv("DB_PATH")