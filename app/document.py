# from dataclasses import dataclass
from pydantic import BaseModel

class Document(BaseModel):
    profile:str
    user_name:str
    