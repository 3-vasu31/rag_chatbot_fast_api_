from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime

# an enum that restricts the model choice to only 'gemini-1.5-flash'
# this is used to validate the model name in the QueryInput model
class ModelName(str, Enum):
    GOOGLE_MODEL="gemini-1.5-flash"


# Represents the request body for a chat query
class QueryInput(BaseModel):
    question: str
    session_id: str = Field(default=None)
    model: ModelName = Field(default=ModelName.GOOGLE_MODEL)


# Define the structure of the chat response.
class QueryResponse(BaseModel):
    answer: str
    session_id: str
    model: ModelName

# represents metadeta for  an uploaded document.
class DocumentInfo(BaseModel):
    id: int
    filename: str
    upload_timestamp: datetime

# Contains only the file_id that identifies which file to delete.
class DeleteFileRequest(BaseModel):
    file_id: int
